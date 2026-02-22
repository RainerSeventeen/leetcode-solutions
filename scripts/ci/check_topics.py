#!/usr/bin/env python3
"""
校验 topics/*.md 的规则。

检查项:
  - 每个 `#### 模板题目` 列表条数上限（可选，默认关闭）
  - 题目重复出现检测（同一题号在 topics 中出现 >= 2 次）

用法:
  python scripts/ci/check_topics.py
"""
from __future__ import annotations

import re
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
TOPICS_DIR = ROOT / "topics"
MAX_TEMPLATE_ITEMS = -1
PROBLEM_ID_RE = re.compile(r"(?m)^\s*-\s*(\d{4})\s+-")


def check_topic_template_limits(path: Path) -> list[str]:
    if MAX_TEMPLATE_ITEMS < 0:
        return []
    errors: list[str] = []
    rel = path.relative_to(ROOT).as_posix()
    lines = path.read_text(encoding="utf-8").splitlines()

    i = 0
    while i < len(lines):
        line = lines[i].strip()
        if line.startswith("#### ") and "模板题目" in line:
            count = 0
            j = i + 1
            while j < len(lines):
                stripped = lines[j].strip()
                if stripped.startswith("#"):
                    break
                if stripped.startswith("- "):
                    count += 1
                j += 1
            if count > MAX_TEMPLATE_ITEMS:
                errors.append(
                    f"{rel}:{i + 1}: `#### 模板题目` has {count} links, max allowed is {MAX_TEMPLATE_ITEMS}"
                )
            i = j
            continue
        i += 1
    return errors


def collect_problem_occurrences() -> dict[str, list[str]]:
    occurrences: dict[str, list[str]] = defaultdict(list)
    for topic_path in sorted(TOPICS_DIR.glob("*.md")):
        rel = topic_path.relative_to(ROOT).as_posix()
        for lineno, line in enumerate(topic_path.read_text(encoding="utf-8").splitlines(), start=1):
            match = PROBLEM_ID_RE.match(line)
            if not match:
                continue
            problem_id = match.group(1)
            occurrences[problem_id].append(f"{rel}:{lineno}")
    return occurrences


def check_duplicate_problem_ids() -> list[str]:
    errors: list[str] = []
    occurrences = collect_problem_occurrences()
    duplicates = {pid: refs for pid, refs in occurrences.items() if len(refs) >= 2}
    if not duplicates:
        return errors

    duplicate_ids = ", ".join(sorted(duplicates))
    errors.append(f"topics: duplicate problem ids found: {duplicate_ids}")
    for pid in sorted(duplicates):
        refs = ", ".join(duplicates[pid])
        errors.append(f"topics: problem `{pid}` appears at {refs}")
    return errors


def main() -> int:
    if not TOPICS_DIR.exists():
        print("topics directory does not exist")
        return 1

    all_errors: list[str] = []
    for topic_path in sorted(TOPICS_DIR.glob("*.md")):
        all_errors.extend(check_topic_template_limits(topic_path))
    all_errors.extend(check_duplicate_problem_ids())

    if all_errors:
        print("\n".join(all_errors))
        return 1

    print("All checks passed for topics/*.md")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
