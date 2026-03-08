#!/usr/bin/env python3
"""
迁移 solutions/competition_problems 下已分配正式题号的题目。

规则:
  - 仅处理 API 返回 questionFrontendId < 10000 的题目。
  - 迁移目标文件名使用 API 最新 titleSlug。
  - 同步更新 front matter id 与 H1 标题题号。
  - 目标路径已存在时跳过并报冲突，不自动合并。

用法:
  python scripts/migrate_competition_problems.py
  python scripts/migrate_competition_problems.py --dry-run
"""
from __future__ import annotations

import argparse
import json
import pathlib
import re
import sys
import time

from path_rules import build_solution_subdir, format_problem_id

try:
    import requests
except ModuleNotFoundError:
    print("Error: pip install requests", file=sys.stderr)
    sys.exit(1)

ROOT = pathlib.Path(__file__).resolve().parent.parent
COMP_DIR = ROOT / "solutions" / "competition_problems"
MIGRATED_PATHS_FILE = ROOT / "artifacts" / "migrated_competition_paths.txt"
GRAPHQL_URL = "https://leetcode.cn/graphql/"
FILE_RE = re.compile(r"^(\d+)-([a-z0-9-]+)\.md$")
FM_ID_RE = re.compile(r"(?m)^id:\s*(.+)\s*$")
H1_RE = re.compile(r"(?m)^#\s+\d+[.。]?\s*(.+?)\s*$")

QUESTION_QUERY = """
query questionData($titleSlug: String!) {
  question(titleSlug: $titleSlug) {
    questionId
    questionFrontendId
    title
    translatedTitle
    titleSlug
  }
}
"""


def build_headers() -> dict[str, str]:
    return {
        "User-Agent": "Mozilla/5.0 (compatible; leetcode-fetcher/1.0)",
        "Referer": "https://leetcode.cn/",
        "Content-Type": "application/json",
    }


def fetch_question(headers: dict[str, str], slug: str) -> dict | None:
    backoff = [3, 8, 15, 30]
    for attempt, wait in enumerate([0] + backoff):
        if wait:
            print(f"  [重试] {slug}: 等待 {wait}s 后重试 ({attempt}/{len(backoff)})")
            time.sleep(wait)
        try:
            resp = requests.post(
                GRAPHQL_URL,
                headers=headers,
                json={"query": QUESTION_QUERY, "variables": {"titleSlug": slug}},
                timeout=15,
            )
            resp.raise_for_status()
            payload = resp.json()
            if payload.get("errors"):
                raise RuntimeError(json.dumps(payload["errors"], ensure_ascii=False))
            return payload.get("data", {}).get("question")
        except (RuntimeError, requests.RequestException, ValueError, json.JSONDecodeError):
            if attempt == len(backoff):
                return None
    return None


def update_markdown_ids(content: str, new_id: int, title_for_h1: str) -> str:
    updated = FM_ID_RE.sub(f"id: {new_id}", content, count=1)
    if updated == content:
        raise ValueError("front matter missing `id`")

    h1_line = f"# {new_id}. {title_for_h1}"
    updated_h1 = H1_RE.sub(h1_line, updated, count=1)
    if updated_h1 == updated:
        raise ValueError("missing valid H1 line")
    return updated_h1


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dry-run", action="store_true", help="只预览迁移，不写文件")
    parser.add_argument("--delay", type=float, default=0.3, help="请求间隔秒数")
    args = parser.parse_args()

    if not COMP_DIR.exists():
        print(f"[信息] 目录不存在: {COMP_DIR.relative_to(ROOT)}")
        return 0

    headers = build_headers()
    migrated_paths: list[str] = []
    failed = 0
    conflict = 0
    checked = 0

    for path in sorted(COMP_DIR.glob("*.md")):
        rel = path.relative_to(ROOT).as_posix()
        m = FILE_RE.fullmatch(path.name)
        if not m:
            print(f"[跳过] {rel}: 文件名不合法")
            continue

        checked += 1
        current_id = int(m.group(1))
        slug = m.group(2)
        print(f"[检查] {rel}", flush=True)

        try:
            question = fetch_question(headers, slug)
        except RuntimeError as exc:
            print(f"  ✗ 致命错误: {exc}")
            return 1
        if not question:
            print(f"  ✗ API 查询失败: {slug}")
            failed += 1
            time.sleep(args.delay)
            continue

        frontend_id_raw = question.get("questionFrontendId") or question.get("questionId")
        try:
            frontend_id = int(frontend_id_raw)
        except (TypeError, ValueError):
            print(f"  ✗ 无效 frontendId: {frontend_id_raw}")
            failed += 1
            time.sleep(args.delay)
            continue

        if frontend_id >= 10000:
            print(f"  - 未转正（frontendId={frontend_id}），保持不动")
            time.sleep(args.delay)
            continue

        latest_slug = str(question.get("titleSlug") or slug).strip() or slug
        title_for_h1 = (
            str(question.get("translatedTitle") or "").strip()
            or str(question.get("title") or "").strip()
            or slug
        )
        target_subdir = build_solution_subdir(frontend_id)
        target_dir = ROOT / "solutions" / target_subdir
        target_dir.mkdir(parents=True, exist_ok=True)
        target_path = target_dir / f"{format_problem_id(frontend_id)}-{latest_slug}.md"
        target_rel = target_path.relative_to(ROOT).as_posix()

        if target_path.exists() and target_path.resolve() != path.resolve():
            print(f"  ⚠ 冲突，目标已存在: {target_rel}")
            conflict += 1
            time.sleep(args.delay)
            continue

        try:
            content = path.read_text(encoding="utf-8")
            new_content = update_markdown_ids(content, frontend_id, title_for_h1)
        except Exception as exc:
            print(f"  ✗ 内容更新失败: {exc}")
            failed += 1
            time.sleep(args.delay)
            continue

        print(f"  ✓ 迁移: {rel} -> {target_rel} (id: {current_id} -> {frontend_id})")
        migrated_paths.append(target_rel)

        if not args.dry_run:
            target_path.write_text(new_content, encoding="utf-8")
            if target_path.resolve() != path.resolve():
                path.unlink()

        time.sleep(args.delay)

    if not args.dry_run:
        MIGRATED_PATHS_FILE.parent.mkdir(parents=True, exist_ok=True)
        output = "\n".join(migrated_paths)
        if output:
            output += "\n"
        MIGRATED_PATHS_FILE.write_text(output, encoding="utf-8")
        print(f"\n[输出] 已写入 {MIGRATED_PATHS_FILE.relative_to(ROOT)}")

    print(
        f"\n[完成] checked={checked}, migrated={len(migrated_paths)}, conflict={conflict}, failed={failed}"
    )
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
