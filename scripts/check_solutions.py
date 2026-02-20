#!/usr/bin/env python3
from __future__ import annotations

import re
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
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
