#!/usr/bin/env python3
"""
校验 solutions/competition_problems 下的竞赛题是否已被分配正式题号。

规则:
  - 扫描 solutions/competition_problems/*.md
  - 按文件名中的 slug 查询 LeetCode GraphQL questionFrontendId
  - 若 frontendId < 10000，判定为“已转正但未迁移”，校验失败
  - API 异常或查询失败，校验失败（避免漏检）

用法:
  python scripts/ci/check_competition_promotions.py
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[2]
SOLUTIONS_DIR = ROOT / "solutions"
COMPETITION_DIR = SOLUTIONS_DIR / "competition_problems"
GRAPHQL_URL = "https://leetcode.cn/graphql/"
FILE_RE = re.compile(r"^(\d+)-([a-z0-9-]+)$")

SCRIPT_DIR = Path(__file__).resolve().parents[1]
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

from path_rules import build_range_dir, format_problem_id  # noqa: E402

QUESTION_QUERY = """
query questionData($titleSlug: String!) {
  question(titleSlug: $titleSlug) {
    questionId
    questionFrontendId
    titleSlug
  }
}
"""


def _graphql_query(slug: str) -> dict:
    payload = json.dumps(
        {
            "query": QUESTION_QUERY,
            "variables": {"titleSlug": slug},
        }
    ).encode("utf-8")
    req = Request(
        GRAPHQL_URL,
        data=payload,
        headers={
            "User-Agent": "Mozilla/5.0 (compatible; leetcode-ci-check/1.0)",
            "Referer": "https://leetcode.cn/",
            "Content-Type": "application/json",
        },
        method="POST",
    )
    with urlopen(req, timeout=20) as resp:
        raw = resp.read().decode("utf-8")
    data = json.loads(raw)
    if data.get("errors"):
        raise RuntimeError(f"GraphQL errors: {data['errors']}")
    question = data.get("data", {}).get("question")
    if not question:
        raise RuntimeError("question not found")
    return question


def main() -> int:
    if not COMPETITION_DIR.exists():
        print("competition_problems directory does not exist; skip")
        return 0

    files = sorted(COMPETITION_DIR.glob("*.md"))
    if not files:
        print("No competition problems found")
        return 0

    errors: list[str] = []
    for path in files:
        rel = path.relative_to(ROOT).as_posix()
        m = FILE_RE.match(path.stem)
        if not m:
            errors.append(f"{rel}: invalid filename format, expected <id>-<slug>.md")
            continue
        original_id = int(m.group(1))
        slug = m.group(2)
        try:
            question = _graphql_query(slug)
            frontend_raw = question.get("questionFrontendId") or question.get("questionId")
            if frontend_raw is None:
                raise RuntimeError("missing questionFrontendId/questionId")
            frontend_id = int(frontend_raw)
        except (ValueError, RuntimeError, HTTPError, URLError, TimeoutError, json.JSONDecodeError) as exc:
            errors.append(f"{rel}: API check failed for slug `{slug}`: {exc}")
            continue

        if frontend_id < 10000:
            latest_slug = question.get("titleSlug") or slug
            expected_range = build_range_dir(frontend_id)
            expected_rel = (
                f"solutions/{expected_range}/{format_problem_id(frontend_id)}-{latest_slug}.md"
            )
            errors.append(
                f"{rel}: detected promoted problem (frontendId={frontend_id}); "
                f"suggest migrate: {rel} -> {expected_rel}"
            )
    if errors:
        print("\n".join(errors))
        return 1

    print("All checks passed for competition promotions")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
