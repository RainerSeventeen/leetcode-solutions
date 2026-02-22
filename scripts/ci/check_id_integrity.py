#!/usr/bin/env python3
"""
检查 solutions/**/*.md 中每道题的 ID 与 LeetCode API 返回值是否一致。

对每个文件：
  - 提取文件名 ID、front matter ID、titleSlug、H1 中文标题
  - 查 GraphQL 获取 questionFrontendId、translatedTitle
  - 验证：文件名 ID == front matter ID == API 前端 ID，且目录 range 正确
  - 验证：H1 中文标题 == API translatedTitle（仅 API 模式）

输出:
  artifacts/id_integrity_report.jsonl  每行一条 JSON 记录
  终端打印 MISMATCH 汇总

用法:
  python scripts/check_id_integrity.py
  python scripts/check_id_integrity.py --slug-only   # 只做本地校验，不请求 API
  python scripts/check_id_integrity.py --delay 0.8
"""
from __future__ import annotations

import argparse
import json
import pathlib
import re
import sys
import time

try:
    import requests
except ModuleNotFoundError:
    print("Error: pip install requests", file=sys.stderr)
    sys.exit(1)

ROOT = pathlib.Path(__file__).parents[2]
SOLUTIONS_DIR = ROOT / "solutions"
ARTIFACTS_DIR = ROOT / "artifacts"
OUTPUT_FILE = ARTIFACTS_DIR / "id_integrity_report.jsonl"

GRAPHQL_URL = "https://leetcode.cn/graphql/"

QUESTION_QUERY = """
query questionData($titleSlug: String!) {
  question(titleSlug: $titleSlug) {
    questionId
    questionFrontendId
    translatedTitle
  }
}
"""

FILE_RE = re.compile(r"^(\d{4})-(.+)$")
FRONT_MATTER_RE = re.compile(r"^---\s*\n(.*?)\n---", re.DOTALL)
ID_RE = re.compile(r"^id:\s*(.+)$", re.MULTILINE)
H1_RE = re.compile(r"^#\s+\d+[.。]?\s+(.+)$", re.MULTILINE)


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def build_headers() -> dict[str, str]:
    return {
        "User-Agent": "Mozilla/5.0 (compatible; leetcode-fetcher/1.0)",
        "Referer": "https://leetcode.cn/",
        "Content-Type": "application/json",
    }


def build_range_dir(problem_id: int) -> str:
    start = ((problem_id - 1) // 100) * 100 + 1
    end = start + 99
    return f"{start:04d}-{end:04d}"


def fetch_question_data(headers: dict, slug: str, delay: float) -> tuple[str, str] | None:
    """查 GraphQL 获取 (questionFrontendId, translatedTitle)，失败返回 None。"""
    BACKOFF = [5, 15, 30, 90, 180]
    for attempt, wait in enumerate([0] + BACKOFF):
        if wait:
            print(f"  [限流] 等待 {wait}s ...", flush=True)
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
                raise RuntimeError(f"GraphQL errors: {payload['errors']}")
            question = payload["data"]["question"]
            if not question:
                return None
            # 优先用 frontendId，fallback questionId
            fid = question.get("questionFrontendId") or question.get("questionId")
            translated_title = (question.get("translatedTitle") or "").strip()
            return (str(fid), translated_title) if fid else None
        except Exception as exc:
            if attempt == len(BACKOFF):
                print(f"  拉取失败: {exc}", file=sys.stderr)
                return None
    return None


def parse_file(md_path: pathlib.Path) -> tuple[str, str, str, str] | None:
    """
    返回 (file_id, slug, fm_id, h1_title) 或 None（解析失败）。
    file_id:   文件名数字部分，去前导零后的字符串（如 "3838"）
    h1_title:  H1 标题中的中文名（如 "两数之和"），未找到时为空字符串
    """
    stem = md_path.stem  # e.g. "4216-weighted-word-mapping"
    m = FILE_RE.match(stem)
    if not m:
        return None
    file_id = str(int(m.group(1)))  # 去前导零
    slug = m.group(2)

    text = md_path.read_text(encoding="utf-8")
    fm_match = FRONT_MATTER_RE.match(text)
    if not fm_match:
        return (file_id, slug, "", "")
    fm_block = fm_match.group(1)
    id_match = ID_RE.search(fm_block)
    fm_id = id_match.group(1).strip() if id_match else ""

    h1_match = H1_RE.search(text)
    h1_title = h1_match.group(1).strip() if h1_match else ""

    return (file_id, slug, fm_id, h1_title)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--slug-only", action="store_true", help="只做本地文件名/front matter 校验，不请求 API")
    parser.add_argument("--delay", type=float, default=0.5, help="每次 API 请求间隔秒数（默认 0.5）")
    parser.add_argument("--output", type=pathlib.Path, default=OUTPUT_FILE, help="报告输出路径")
    args = parser.parse_args()

    md_files = sorted(SOLUTIONS_DIR.rglob("*.md"))
    total = len(md_files)
    print(f"[信息] 扫描 {total} 个文件 ...\n")

    headers = build_headers()
    ARTIFACTS_DIR.mkdir(exist_ok=True)

    results: list[dict] = []
    mismatch_count = 0

    for i, md_path in enumerate(md_files, 1):
        rel = str(md_path.relative_to(ROOT))
        if not md_path.exists():
            print(f"  [{i:3d}/{total}] ⚠  文件已删除，跳过: {rel}")
            results.append({"file": rel, "status": "DELETED", "issues": ["文件在扫描后被删除"]})
            continue
        parsed = parse_file(md_path)
        if not parsed:
            print(f"  [{i:3d}/{total}] ⚠  解析失败: {rel}")
            results.append({"file": rel, "status": "PARSE_ERROR", "issues": ["无法解析文件名或 front matter"]})
            continue

        file_id, slug, fm_id, h1_title = parsed
        issues: list[str] = []

        # 本地校验
        if fm_id != file_id:
            issues.append(f"front matter id `{fm_id}` ≠ 文件名 id `{file_id}`")

        record: dict = {
            "file": rel,
            "file_id": file_id,
            "fm_id": fm_id,
            "slug": slug,
            "h1_title": h1_title,
        }

        if args.slug_only:
            status = "MISMATCH" if issues else "OK"
            record["status"] = status
            record["issues"] = issues
            if issues:
                mismatch_count += 1
                print(f"  [{i:3d}/{total}] ✗  {rel}  →  {', '.join(issues)}")
            else:
                print(f"  [{i:3d}/{total}] ✓  {rel}")
            results.append(record)
            continue

        # API 校验
        api_data = fetch_question_data(headers, slug, args.delay)
        if api_data is None:
            record["api_id"] = "FETCH_FAILED"
            record["status"] = "API_ERROR"
            record["issues"] = issues + ["API 拉取失败"]
            print(f"  [{i:3d}/{total}] ✗  {rel}  →  API 拉取失败")
            results.append(record)
            mismatch_count += 1
            time.sleep(args.delay)
            continue

        api_id, api_translated_title = api_data
        record["api_id"] = api_id
        record["api_translated_title"] = api_translated_title

        if api_id != file_id:
            issues.append(f"API frontendId `{api_id}` ≠ 文件名 id `{file_id}`")

        if api_translated_title and h1_title and h1_title != api_translated_title:
            issues.append(f"H1 中文名 `{h1_title}` ≠ API translatedTitle `{api_translated_title}`")

        # 验证目录 range
        try:
            expected_range = build_range_dir(int(api_id))
            expected_path = f"solutions/{expected_range}/{int(api_id):04d}-{slug}.md"
            record["expected_path"] = expected_path
            actual_range = md_path.parent.name
            if actual_range != expected_range:
                issues.append(f"目录应为 `{expected_range}`，实为 `{actual_range}`")
        except (ValueError, TypeError):
            pass

        status = "MISMATCH" if issues else "OK"
        record["status"] = status
        record["issues"] = issues

        if issues:
            mismatch_count += 1
            print(f"  [{i:3d}/{total}] ✗  {rel}")
            for iss in issues:
                print(f"            → {iss}")
        else:
            print(f"  [{i:3d}/{total}] ✓  {rel}")

        results.append(record)
        time.sleep(args.delay)

    # 写报告
    args.output.write_text(
        "\n".join(json.dumps(r, ensure_ascii=False) for r in results) + "\n",
        encoding="utf-8",
    )

    ok_count = sum(1 for r in results if r["status"] == "OK")
    print(f"\n[完成] OK: {ok_count} / MISMATCH 或错误: {mismatch_count} / 共 {total}")
    print(f"[报告] → {args.output.relative_to(ROOT)}")
    return 1 if mismatch_count else 0


if __name__ == "__main__":
    raise SystemExit(main())
