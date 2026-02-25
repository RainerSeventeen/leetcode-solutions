#!/usr/bin/env python3
"""
校验 solutions/ 下所有题解 Markdown 文件的格式合规性。

检查项:
  - 文件路径与命名规范（solutions/0001-0100/0001-xxx.md）
  - Front matter 必填字段（id / title / difficulty / tags / created）
  - Front matter id 与文件名及 H1 标题的一致性
  - difficulty 取值（Easy / Medium / Hard）
  - created 日期格式（YYYY-MM-DD）
  - 必需章节（## 题目链接 / ## 题目描述 / ## 解题思路 / ## 相关专题 / ## 代码）
  - 复杂度占位符 O() 是否已填写
  - 时间复杂度 / 空间复杂度 格式（$O(...)$），可附变量释义
  - 重复 id 检测
  - ## 相关专题 段落存在、含有回链接、回链接命名规范

用法:
  python scripts/ci/check_solutions.py

返回码:
  0  全部通过
  1  存在格式错误（错误信息打印到 stdout）
"""
from __future__ import annotations

import re
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SOLUTIONS_DIR = ROOT / "solutions"
FILE_RE = re.compile(r"solutions/\d{4}-\d{4}/(\d{4})-[a-z0-9-]+\.md$")
FRONT_MATTER_RE = re.compile(r"^---\n(.*?)\n---\n", re.S)
REQUIRED_SECTIONS = (
    "## 题目链接",
    "## 题目描述",
    "## 解题思路",
    "## 代码",
)
ALLOWED_DIFFICULTY = {"Easy", "Medium", "Hard"}
COMPLEXITY_LINE_RE = re.compile(r"^\$O\([^$\n]+\)\$(?:\s*.*)?$")

# 回链接行格式：- [显示名](../../topics/xxx.md)
BACKLINK_LINE_RE = re.compile(
    r"^- \[([^\]]+)\]\(\.\./\.\./topics/([^)]+\.md)\)\s*$"
)

# topic 文件名 → 规范显示名（与 README 章节名去括号后一致）
TOPIC_NAME_MAP: dict[str, str] = {
    "sliding-window-and-two-pointers.md": "滑动窗口与双指针",
    "binary-search.md":                   "二分算法",
    "monotonic-stack.md":                 "单调栈",
    "grid-graph.md":                      "网格图",
    "bit-operations.md":                  "位运算",
    "graph-algorithms.md":                "图论算法",
    "dynamic-programming.md":             "动态规划",
    "common-data-structures.md":          "常用数据结构",
    "math-algorithms.md":                 "数学算法",
    "greedy-and-thinking.md":             "贪心与思维",
    "linked-list-tree-backtracking.md":   "链表、树与回溯",
    "string-algorithms.md":               "字符串",
}


def parse_front_matter(text: str) -> dict[str, str]:
    match = FRONT_MATTER_RE.match(text)
    if not match:
        return {}
    front_matter: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        front_matter[key.strip()] = value.strip()
    return front_matter


def parse_h1_problem_id(text: str) -> str | None:
    for line in text.splitlines():
        stripped = line.strip()
        if not stripped:
            continue
        if stripped.startswith("# "):
            match = re.match(r"^#\s+(\d+)\b", stripped)
            if not match:
                return None
            return str(int(match.group(1)))
    return None


def check_complexity_line(content: str, label: str) -> str | None:
    match = re.search(rf"(?m)^- {re.escape(label)}[：:]\s*(.*)$", content)
    if not match:
        return f"missing `{label}` line, expected `- {label}: $O(xxx)$`"
    value = match.group(1).strip()
    if not COMPLEXITY_LINE_RE.match(value):
        return f"invalid `{label}` format `{value}`, expected `$O(xxx)$` with optional trailing text"
    return None


def check_backlinks(content: str, rel: str) -> list[str]:
    """
    检查 ## 相关专题 段落：
    1. 段落是否存在
    2. 段落内是否有至少一条回链接
    3. 每条回链接的显示名是否符合规范（与 README 中的短名一致）
    """
    errors: list[str] = []
    lines = content.splitlines()

    # 定位 ## 相关专题 段落
    start: int | None = None
    end: int = len(lines)
    for i, line in enumerate(lines):
        if line.rstrip() == "## 相关专题":
            start = i
        elif start is not None and re.match(r"^##\s", line) and i > start:
            end = i
            break

    if start is None:
        errors.append(f"{rel}: missing section `## 相关专题`")
        return errors

    # 收集段落内所有回链接行
    backlinks: list[tuple[str, str]] = []  # [(display_name, topic_filename), ...]
    for line in lines[start + 1 : end]:
        m = BACKLINK_LINE_RE.match(line)
        if m:
            backlinks.append((m.group(1), m.group(2)))

    if not backlinks:
        errors.append(f"{rel}: `## 相关专题` has no backlinks")
        return errors

    # 检查每条回链接的命名是否规范
    for display_name, topic_filename in backlinks:
        expected = TOPIC_NAME_MAP.get(topic_filename)
        if expected is None:
            errors.append(
                f"{rel}: unknown topic file `{topic_filename}` in `## 相关专题`"
            )
        elif display_name != expected:
            errors.append(
                f"{rel}: backlink name `{display_name}` should be `{expected}`"
                f" (for `{topic_filename}`)"
            )

    return errors


def check_file(path: Path) -> list[str]:
    errors: list[str] = []
    rel = path.relative_to(ROOT).as_posix()
    content = path.read_text(encoding="utf-8")

    file_match = FILE_RE.fullmatch(rel)
    if not file_match:
        return [f"{rel}: invalid path/name format, expected solutions/0001-0100/0001-xxx.md"]

    file_id = str(int(file_match.group(1)))
    front_matter = parse_front_matter(content)

    for key in ("id", "title", "difficulty", "tags", "created"):
        if key not in front_matter or not front_matter[key]:
            errors.append(f"{rel}: missing front matter key `{key}`")

    if "id" in front_matter and front_matter["id"] != file_id:
        errors.append(
            f"{rel}: front matter id `{front_matter['id']}` does not match file id `{file_id}`"
        )

    h1_id = parse_h1_problem_id(content)
    if h1_id is None:
        errors.append(f"{rel}: invalid or missing H1 problem number, expected `# <id> ...`")
    elif h1_id != file_id:
        errors.append(f"{rel}: H1 id `{h1_id}` does not match file id `{file_id}`")

    if "difficulty" in front_matter and front_matter["difficulty"] not in ALLOWED_DIFFICULTY:
        errors.append(
            f"{rel}: invalid difficulty `{front_matter['difficulty']}`, allowed: Easy/Medium/Hard"
        )

    if "created" in front_matter:
        try:
            date.fromisoformat(front_matter["created"])
        except ValueError:
            errors.append(
                f"{rel}: invalid created date `{front_matter['created']}`, expected YYYY-MM-DD"
            )

    for section in REQUIRED_SECTIONS:
        if section not in content:
            errors.append(f"{rel}: missing section `{section}`")

    if "O()" in content:
        errors.append(f"{rel}: placeholder `O()` still exists")

    time_complexity_error = check_complexity_line(content, "时间复杂度")
    if time_complexity_error:
        errors.append(f"{rel}: {time_complexity_error}")

    space_complexity_error = check_complexity_line(content, "空间复杂度")
    if space_complexity_error:
        errors.append(f"{rel}: {space_complexity_error}")

    errors.extend(check_backlinks(content, rel))

    return errors


def main() -> int:
    if not SOLUTIONS_DIR.exists():
        print("solutions directory does not exist")
        return 1

    all_errors: list[str] = []
    seen_ids: set[str] = set()

    for file_path in sorted(SOLUTIONS_DIR.rglob("*.md")):
        file_errors = check_file(file_path)
        all_errors.extend(file_errors)

        rel = file_path.relative_to(ROOT).as_posix()
        content = file_path.read_text(encoding="utf-8")
        front_matter = parse_front_matter(content)
        file_id = front_matter.get("id")
        if file_id:
            if file_id in seen_ids:
                all_errors.append(f"{rel}: duplicate id `{file_id}`")
            else:
                seen_ids.add(file_id)

    if all_errors:
        print("\n".join(all_errors))
        return 1

    print("All checks passed for solutions/*.md")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
