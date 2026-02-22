#!/usr/bin/env python3
"""
校验 solutions/ 下所有题解 Markdown 文件的格式合规性，以及 topics/*.md 的模板题目数量限制。

检查项:
  - 文件路径与命名规范（solutions/0001-0100/0001-xxx.md）
  - Front matter 必填字段（id / title / difficulty / tags / created）
  - Front matter id 与文件名及 H1 标题的一致性
  - difficulty 取值（Easy / Medium / Hard）
  - created 日期格式（YYYY-MM-DD）
  - 必需章节（## 题目链接 / ## 题目描述 / ## 解题思路 / ## 代码）
  - 复杂度占位符 O() 是否已填写
  - 时间复杂度 / 空间复杂度 格式（$O(...)$）
  - topics/*.md 中每个"模板题目"列表条数上限（≤ 20）
  - 重复 id 检测

用法:
  python scripts/check_solutions.py

返回码:
  0  全部通过
  1  存在格式错误（错误信息打印到 stdout）
"""
from __future__ import annotations

import re
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOLUTIONS_DIR = ROOT / "solutions"
TOPICS_DIR = ROOT / "topics"
FILE_RE = re.compile(r"solutions/\d{4}-\d{4}/(\d{4})-[a-z0-9-]+\.md$")
FRONT_MATTER_RE = re.compile(r"^---\n(.*?)\n---\n", re.S)
REQUIRED_SECTIONS = (
    "## 题目链接",
    "## 题目描述",
    "## 解题思路",
    "## 代码",
)
ALLOWED_DIFFICULTY = {"Easy", "Medium", "Hard"}
COMPLEXITY_VALUE_RE = re.compile(r"^\$O\([^$\n]+\)\$")
MAX_TEMPLATE_ITEMS = -1


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
    if not COMPLEXITY_VALUE_RE.match(value):
        return f"invalid `{label}` format `{value}`, expected `$O(xxx)$`"
    return None


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

    return errors


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

    if TOPICS_DIR.exists():
        for topic_path in sorted(TOPICS_DIR.glob("*.md")):
            all_errors.extend(check_topic_template_limits(topic_path))

    if all_errors:
        print("\n".join(all_errors))
        return 1

    print("All checks passed for solutions/*.md and topics/*.md")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
