#!/usr/bin/env python3
"""
从力扣中文站拉取指定题目，并在 solutions/ 下生成 Markdown 模板文件。

用法:
  python scripts/fetch_problem.py <problem_id>
  python scripts/fetch_problem.py <problem_id> --overwrite
  python scripts/fetch_problem.py --slug <titleSlug>

参数:
  problem_id    力扣前端题目 ID（如 1584）；与 --slug 二选一
  --slug        直接指定 titleSlug，跳过 problems/all 查询（适用于竞赛题）
  --overwrite   文件已存在时强制覆盖（默认报错退出）

输出: solutions/<范围目录>/<id>-<slug>.md
  按题号模式：id 为传入的 problem_id
  按 slug 模式：id 为 GraphQL 返回的 questionId
"""
from __future__ import annotations

import argparse
import datetime as dt
import pathlib
import re
import sys
from typing import Any

try:
    import requests
except ModuleNotFoundError:
    requests = None

PROBLEMS_ALL_URL = "https://leetcode.cn/api/problems/all/"
GRAPHQL_URL = "https://leetcode.cn/graphql/"
REQUEST_TIMEOUT = 15
PREMIUM_DESCRIPTION = "该题为 LeetCode 会员题（Premium），无法自动获取完整题目描述。"


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
    return {
        "User-Agent": "Mozilla/5.0 (compatible; leetcode-fetcher/1.0)",
        "Referer": "https://leetcode.cn/",
        "Content-Type": "application/json",
    }


def fetch_title_slug(problem_id: int, headers: dict[str, str]) -> str:
    try:
        response = requests.get(PROBLEMS_ALL_URL, headers=headers, timeout=REQUEST_TIMEOUT)
        response.raise_for_status()
        payload = response.json()
    except requests.RequestException as exc:
        raise RuntimeError(f"Failed to fetch problem list: {exc}") from exc
    except ValueError as exc:
        raise RuntimeError("Failed to parse problem list response as JSON") from exc

    for item in payload.get("stat_status_pairs", []):
        stat = item.get("stat", {})
        frontend_id = stat.get("frontend_question_id")
        if str(frontend_id) == str(problem_id):
            slug = stat.get("question__title_slug")
            if not slug:
                raise RuntimeError(f"Found problem {problem_id}, but titleSlug is missing")
            return slug

    raise RuntimeError(f"Problem id {problem_id} not found in LeetCode problem list")


def fetch_problem_details(title_slug: str, headers: dict[str, str]) -> dict[str, Any]:
    query = """
    query questionData($titleSlug: String!) {
      question(titleSlug: $titleSlug) {
        questionId
        questionFrontendId
        title
        translatedTitle
        difficulty
        isPaidOnly
        content
        translatedContent
        topicTags {
          name
        }
      }
    }
    """
    body = {"query": query, "variables": {"titleSlug": title_slug}}

    try:
        response = requests.post(
            GRAPHQL_URL,
            headers=headers,
            json=body,
            timeout=REQUEST_TIMEOUT,
        )
        response.raise_for_status()
        payload = response.json()
    except requests.RequestException as exc:
        raise RuntimeError(f"Failed to fetch problem detail via GraphQL: {exc}") from exc
    except ValueError as exc:
        raise RuntimeError("Failed to parse GraphQL response as JSON") from exc

    if payload.get("errors"):
        raise RuntimeError(f"GraphQL returned errors: {payload['errors']}")

    question = payload.get("data", {}).get("question")
    if not question:
        raise RuntimeError("GraphQL response does not include question data")

    return question


def build_range_dir(problem_id: int) -> str:
    start = ((problem_id - 1) // 100) * 100 + 1
    end = start + 99
    return f"{start:04d}-{end:04d}"


def to_markdown(question: dict[str, Any], problem_id: int, title_slug: str) -> str:
    question_id = question.get("questionFrontendId") or question.get("questionId") or str(problem_id)
    english_title = question.get("title") or ""
    body_title = question.get("translatedTitle") or english_title
    difficulty = question.get("difficulty") or ""
    if question.get("isPaidOnly"):
        content = PREMIUM_DESCRIPTION
    else:
        content = question.get("translatedContent") or question.get("content") or ""
        content = strip_empty_paragraphs(content)
        content = collapse_blank_lines(content)
    topic_tags = []
    for tag in question.get("topicTags", []):
        tag_name = tag.get("name")
        if not tag_name:
            continue
        normalized = normalize_tag(tag_name)
        if normalized:
            topic_tags.append(normalized)
    created = dt.date.today().isoformat()
    tags_literal = ", ".join(topic_tags)

    return f"""---
id: {question_id}
title: {english_title}
difficulty: {difficulty}
tags: [{tags_literal}]
created: {created}
---

# {question_id}. {body_title}

## 题目链接
https://leetcode.cn/problems/{title_slug}/

## 题目描述
{content}

## 解题思路

- 时间复杂度: $O()$

- 空间复杂度: $O()$

## 代码
```python

```
"""


def write_markdown_file(
    problem_id: int,
    title_slug: str,
    markdown: str,
    overwrite: bool,
) -> pathlib.Path:
    range_dir = build_range_dir(problem_id)
    output_dir = pathlib.Path("solutions") / range_dir
    output_dir.mkdir(parents=True, exist_ok=True)

    output_path = output_dir / f"{problem_id:04d}-{title_slug}.md"
    if output_path.exists() and not overwrite:
        raise RuntimeError(
            f"File already exists: {output_path}. Use --overwrite to replace it."
        )
    output_path.write_text(markdown, encoding="utf-8")
    return output_path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Fetch a LeetCode problem and generate a markdown template."
    )
    parser.add_argument(
        "problem_id",
        type=int,
        nargs="?",
        default=None,
        help="LeetCode frontend problem id, e.g. 1584（与 --slug 二选一）",
    )
    parser.add_argument(
        "--slug",
        type=str,
        default=None,
        help="直接指定 titleSlug，跳过 problems/all 查询（适用于竞赛题）",
    )
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Overwrite markdown file if it already exists",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if requests is None:
        print("Error: missing dependency 'requests'. Install it with: pip install requests", file=sys.stderr)
        return 1

    if not args.slug and args.problem_id is None:
        print("Error: 必须提供 problem_id 或 --slug", file=sys.stderr)
        return 1
    if args.problem_id is not None and args.problem_id <= 0:
        print("Error: problem_id must be a positive integer", file=sys.stderr)
        return 1

    headers = build_headers()

    try:
        if args.slug:
            title_slug = args.slug
            problem_id_for_file = None
        else:
            title_slug = fetch_title_slug(args.problem_id, headers)
            problem_id_for_file = args.problem_id

        question = fetch_problem_details(title_slug, headers)

        if problem_id_for_file is None:
            problem_id_for_file = int(question.get("questionFrontendId") or question.get("questionId") or 0)
            if not problem_id_for_file:
                raise RuntimeError("GraphQL 未返回有效 questionFrontendId/questionId")

        markdown = to_markdown(question, problem_id_for_file, title_slug)
        output_path = write_markdown_file(
            problem_id_for_file,
            title_slug,
            markdown,
            overwrite=args.overwrite,
        )
    except RuntimeError as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1

    print(f"Generated: {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
