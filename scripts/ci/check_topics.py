#!/usr/bin/env python3
"""
校验 topics/*.md 的规则。

检查项:
  - 每个 `#### 模板题目` 列表条数上限（可选，默认关闭）
  - 题目重复出现检测（同一题号在 topics 中出现 >= 2 次）
  - 题目条目命名格式符合规范
  - 题解笔记路径实际存在

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

# 匹配以题号开头的条目行（用于识别候选行）
PROBLEM_ID_RE = re.compile(r"^\s*-\s*(\d{4})\s+-")

# 完整条目格式：- 0000 - 题目名 ｜ [LeetCode 链接](...) ｜ [题解笔记](...)
# 分隔符为全角竖线 ｜ (U+FF5C)
# group 1: 题目名, group 2: LeetCode URL, group 3: 笔记相对路径
ENTRY_FULL_RE = re.compile(
    r"^\s*-\s+\d{4}\s+-\s+(.+?)\s+｜\s+"
    r"\[LeetCode 链接\]\((https://leetcode\.cn/problems/[^)]+/)\)\s+｜\s+"
    r"\[题解笔记\]\(([^)]+)\)\s*$"
)

# 题解文件 H1 标题：# 53. 最大子数组和
H1_TITLE_RE = re.compile(r"^#\s+\d+\.\s+(.+)$")


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


def _h1_title(note_path: Path) -> str | None:
    """从题解文件中提取 H1 中文标题，格式为 '# 53. 最大子数组和'。"""
    for line in note_path.read_text(encoding="utf-8").splitlines():
        m = H1_TITLE_RE.match(line)
        if m:
            return m.group(1).strip()
    return None


def check_entry_format_and_paths(path: Path) -> list[str]:
    errors: list[str] = []
    rel = path.relative_to(ROOT).as_posix()
    for lineno, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        if not PROBLEM_ID_RE.match(line):
            continue
        m = ENTRY_FULL_RE.match(line)
        if not m:
            errors.append(f"{rel}:{lineno}: 条目格式不符合规范: {line.strip()!r}")
            continue

        entry_name, entry_url, note_rel = m.group(1), m.group(2), m.group(3)
        note_path = (path.parent / note_rel).resolve()

        if not note_path.exists():
            errors.append(f"{rel}:{lineno}: 题解笔记路径不存在: {note_rel!r}")
            continue  # 文件不存在时跳过后续检查

        # LeetCode URL：由笔记文件名的 slug 部分构造
        slug = re.sub(r"^\d{4}-", "", note_path.stem)
        expected_url = f"https://leetcode.cn/problems/{slug}/"
        if entry_url != expected_url:
            errors.append(
                f"{rel}:{lineno}: LeetCode 链接与题解 slug 不符: "
                f"{entry_url!r} ≠ {expected_url!r}"
            )

        # 题目中文名：与笔记 H1 标题比对
        h1_name = _h1_title(note_path)
        if h1_name is None:
            errors.append(f"{rel}:{lineno}: 题解文件缺少 H1 标题: {note_rel!r}")
        elif entry_name != h1_name:
            errors.append(
                f"{rel}:{lineno}: 题目名称与题解 H1 不符: "
                f"{entry_name!r} ≠ {h1_name!r}"
            )

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
        all_errors.extend(check_entry_format_and_paths(topic_path))
    all_errors.extend(check_duplicate_problem_ids())

    if all_errors:
        print("\n".join(all_errors))
        return 1

    print("All checks passed for topics/*.md")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
