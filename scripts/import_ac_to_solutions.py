#!/usr/bin/env python3
"""
将 artifacts/ac_with_code.jsonl 中的题目批量导入到 solutions/ 目录。

对每条记录：
  - 若对应题目已在 solutions/ 中存在 → 跳过
  - 否则 → 从力扣 API 拉取题目详情，创建 Markdown 文件并填入 AC 代码

用法:
  python scripts/import_ac_to_solutions.py
  python scripts/import_ac_to_solutions.py --dry-run   # 只统计，不写文件
  python scripts/import_ac_to_solutions.py --delay 0.8
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import pathlib
import re
import sys
import time

try:
    import env  # noqa: F401 — side-effect: loads .env into os.environ
except ImportError:
    pass

try:
    import requests
except ModuleNotFoundError:
    print("Error: pip install requests", file=sys.stderr)
    sys.exit(1)

GRAPHQL_URL = "https://leetcode.cn/graphql/"
ROOT = pathlib.Path(__file__).parent.parent
SOLUTIONS_DIR = ROOT / "solutions"
INPUT_FILE = ROOT / "artifacts" / "ac_with_code.jsonl"

QUESTION_QUERY = """
query questionData($titleSlug: String!) {
  question(titleSlug: $titleSlug) {
    questionId
    title
    translatedTitle
    difficulty
    topicTags {
      name
    }
    translatedContent
    content
  }
}
"""

# 力扣 lang 字段 → Markdown 代码块语言标签
LANG_MAP: dict[str, str] = {
    "python3": "python",
    "python": "python",
    "golang": "go",
    "cpp": "cpp",
    "c": "c",
    "java": "java",
    "javascript": "javascript",
    "typescript": "typescript",
    "rust": "rust",
    "kotlin": "kotlin",
    "swift": "swift",
    "ruby": "ruby",
    "scala": "scala",
    "php": "php",
    "csharp": "csharp",
    "mysql": "sql",
    "mssql": "sql",
    "oraclesql": "sql",
}


# ---------------------------------------------------------------------------
# 复用 fetch_problem.py 的工具函数
# ---------------------------------------------------------------------------

def normalize_tag(tag: str) -> str:
    normalized = re.sub(r"[^a-z0-9]+", "-", tag.strip().lower())
    return normalized.strip("-")


def strip_empty_paragraphs(content: str) -> str:
    return re.sub(
        r"<p>\s*(?:&nbsp;|\u00a0|\s)*\s*</p>",
        "",
        content,
        flags=re.IGNORECASE,
    )


def collapse_blank_lines(text: str) -> str:
    normalized = text.replace("\r\n", "\n").replace("\r", "\n")
    return re.sub(r"\n\s*\n(?:\s*\n)+", "\n\n", normalized)


def build_headers() -> dict[str, str]:
    import os
    headers = {
        "User-Agent": "Mozilla/5.0 (compatible; leetcode-fetcher/1.0)",
        "Referer": "https://leetcode.cn/",
        "Content-Type": "application/json",
    }
    session = os.environ.get("LC_SESSION")
    csrf = os.environ.get("LC_CSRF")
    if session and csrf:
        headers["Cookie"] = f"LEETCODE_SESSION={session}; csrftoken={csrf}"
        headers["x-csrftoken"] = csrf
    return headers


def build_range_dir(problem_id: int) -> str:
    start = ((problem_id - 1) // 100) * 100 + 1
    end = start + 99
    return f"{start:04d}-{end:04d}"


# ---------------------------------------------------------------------------
# API
# ---------------------------------------------------------------------------

def fetch_question(headers: dict, slug: str) -> dict | None:
    BACKOFF = [5, 15, 30, 60]
    for attempt, wait in enumerate([0] + BACKOFF):
        if wait:
            print(f"\n  [限流] 等待 {wait}s 后重试 ...", flush=True)
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
            return payload["data"]["question"]
        except Exception as exc:
            if attempt == len(BACKOFF):
                print(f"  拉取失败: {exc}")
                return None
    return None


# ---------------------------------------------------------------------------
# Markdown 生成
# ---------------------------------------------------------------------------

def build_markdown(slug: str, entry: dict, question: dict) -> str:
    problem_id = int(question.get("questionId") or 0)
    en_title = question.get("title") or ""
    zh_title = question.get("translatedTitle") or en_title
    difficulty = question.get("difficulty") or ""

    topic_tags = []
    for tag in question.get("topicTags", []):
        name = tag.get("name", "")
        normalized = normalize_tag(name)
        if normalized:
            topic_tags.append(normalized)
    tags_str = ", ".join(topic_tags)

    content = question.get("translatedContent") or question.get("content") or ""
    content = strip_empty_paragraphs(content)
    content = collapse_blank_lines(content)

    lang_key = entry.get("lang", "")
    lang_tag = LANG_MAP.get(lang_key, lang_key)
    code = (entry.get("code") or "").rstrip()

    today = dt.date.today().isoformat()

    return f"""---
id: {problem_id}
title: {en_title}
difficulty: {difficulty}
tags: [{tags_str}]
created: {today}
---

# {problem_id}. {zh_title}

## 题目链接
https://leetcode.cn/problems/{slug}/

## 题目描述
{content}

## 解题思路

- 时间复杂度: $O()$

- 空间复杂度: $O()$

## 代码
```{lang_tag}
{code}
```
"""


# ---------------------------------------------------------------------------
# 主逻辑
# ---------------------------------------------------------------------------

def build_existing_slugs() -> set[str]:
    """扫描 solutions/ 返回所有已有题目的 slug 集合。"""
    existing: set[str] = set()
    for md_file in SOLUTIONS_DIR.rglob("*.md"):
        stem = md_file.stem  # e.g. "0001-two-sum"
        parts = stem.split("-", 1)
        if len(parts) == 2:
            existing.add(parts[1])  # "two-sum"
    return existing


def main() -> int:
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("--dry-run", action="store_true", help="只统计，不写文件")
    parser.add_argument("--delay", type=float, default=0.5, help="每次请求间隔秒数（默认 0.5）")
    args = parser.parse_args()

    if not INPUT_FILE.exists():
        print(f"[错误] 找不到输入文件: {INPUT_FILE}", file=sys.stderr)
        return 1

    headers = build_headers()
    existing_slugs = build_existing_slugs()
    print(f"[信息] solutions/ 中已有 {len(existing_slugs)} 道题")

    lines = [l.strip() for l in INPUT_FILE.read_text(encoding="utf-8").splitlines() if l.strip()]
    print(f"[信息] ac_with_code.jsonl 共 {len(lines)} 条\n")

    created = skipped = failed = 0
    created_paths: list[str] = []

    PATHS_FILE = ROOT / "artifacts" / "imported_paths.txt"

    for i, line in enumerate(lines, 1):
        try:
            entry = json.loads(line)
        except json.JSONDecodeError as e:
            print(f"[警告] 第 {i} 行 JSON 解析失败: {e}，跳过")
            continue

        slug = entry.get("titleSlug", "")
        if not slug:
            print(f"[警告] 第 {i} 行缺少 titleSlug，跳过")
            continue

        if slug in existing_slugs:
            skipped += 1
            continue

        title = entry.get("title", slug)
        print(f"  [{i:3d}] {slug}  ({title})", end=" ", flush=True)

        if args.dry_run:
            print("(dry-run)")
            existing_slugs.add(slug)  # 防止同题重复计数
            created += 1
            continue

        question = fetch_question(headers, slug)
        if not question:
            print("✗ 拉取失败")
            failed += 1
            time.sleep(args.delay)
            continue

        problem_id = int(question.get("questionId") or 0)
        if not problem_id:
            print("✗ 无效的 questionId")
            failed += 1
            time.sleep(args.delay)
            continue

        markdown = build_markdown(slug, entry, question)

        range_dir = build_range_dir(problem_id)
        out_dir = SOLUTIONS_DIR / range_dir
        out_dir.mkdir(parents=True, exist_ok=True)
        out_path = out_dir / f"{problem_id:04d}-{slug}.md"

        out_path.write_text(markdown, encoding="utf-8")
        existing_slugs.add(slug)
        created += 1
        rel = str(out_path.relative_to(ROOT))
        created_paths.append(rel)
        print(f"✓  → {rel}")

        time.sleep(args.delay)

    if not args.dry_run and created_paths:
        PATHS_FILE.write_text("\n".join(created_paths) + "\n", encoding="utf-8")
        print(f"\n[路径列表] → {PATHS_FILE.relative_to(ROOT)}")

    print(f"\n[完成] 新建 {created} / 跳过 {skipped} / 失败 {failed}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
