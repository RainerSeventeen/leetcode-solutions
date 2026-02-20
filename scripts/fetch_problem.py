#!/usr/bin/env python3
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
    question_id = question.get("questionId") or str(problem_id)
    english_title = question.get("title") or ""
    body_title = question.get("translatedTitle") or english_title
    difficulty = question.get("difficulty") or ""
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
    parser.add_argument("problem_id", type=int, help="LeetCode frontend problem id, e.g. 1584")
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Overwrite markdown file if it already exists",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if args.problem_id <= 0:
        print("Error: problem_id must be a positive integer", file=sys.stderr)
        return 1
    if requests is None:
        print("Error: missing dependency 'requests'. Install it with: pip install requests", file=sys.stderr)
        return 1

    headers = build_headers()

    try:
        title_slug = fetch_title_slug(args.problem_id, headers)
        question = fetch_problem_details(title_slug, headers)
        if question.get("isPaidOnly"):
            raise RuntimeError(f"Problem {args.problem_id} is premium-only on LeetCode CN")
        markdown = to_markdown(question, args.problem_id, title_slug)
        output_path = write_markdown_file(
            args.problem_id,
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
