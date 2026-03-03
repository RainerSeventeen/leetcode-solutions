#!/usr/bin/env python3
"""
校验 topics/*.md 的规则。

检查项:
  - 每个 `#### 模板题目` 列表条数上限（可选，默认关闭）
  - 题目重复出现检测（同一题号在 topics 中出现 >= 2 次）
  - 题目条目命名格式符合规范
  - 题解笔记路径实际存在
  - 与 `0x3f_problems_list/index.json` 的专题分类对齐：
    - 0x3f 要求的分类标题必须在对应 topics 文件中存在（允许新增，不允许缺失）
    - 对于 topics 中出现且被 0x3f 收录的题目，分类归档位置需与 0x3f 一致

前置依赖:
  - `0x3f_problems_list/index.json` 必须存在

用法:
  python scripts/ci/check_topics.py
"""
from __future__ import annotations

import json
import re
from collections import defaultdict
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
TOPICS_DIR = ROOT / "topics"
ZERO3F_INDEX_PATH = ROOT / "0x3f_problems_list" / "index.json"

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
HEADING_RE = re.compile(r"^(#{2,6})\s+(.+?)\s*$")
PROBLEM_ID_INPUT_RE = re.compile(r"^\d{1,4}$")


def normalize_problem_id(problem_id: str) -> str:
    pid = problem_id.strip()
    if not PROBLEM_ID_INPUT_RE.match(pid):
        raise ValueError(f"invalid problem id: {problem_id!r}")
    return pid.zfill(4)


def load_index(index_path: Path | None = None) -> dict[str, Any]:
    path = index_path or ZERO3F_INDEX_PATH
    if not path.exists():
        rel = path.relative_to(ROOT).as_posix()
        raise ValueError(f"missing {rel}")
    try:
        raw = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        rel = path.relative_to(ROOT).as_posix()
        raise ValueError(f"invalid json in {rel}: {exc}") from exc
    if not isinstance(raw, dict):
        raise ValueError("0x3f index must be a JSON object")
    topics = raw.get("topics")
    if not isinstance(topics, dict):
        raise ValueError("0x3f index missing `topics` object")
    return raw


def _get_topic_meta(index: dict[str, Any], topic_file: str) -> dict[str, Any]:
    topics = index.get("topics")
    if not isinstance(topics, dict):
        raise ValueError("0x3f index schema error: `topics` is not an object")
    topic_meta = topics.get(topic_file)
    if not isinstance(topic_meta, dict):
        raise ValueError(f"0x3f index missing topic: {topic_file}")
    return topic_meta


def get_required_titles(index: dict[str, Any], topic_file: str) -> list[str]:
    topic_meta = _get_topic_meta(index, topic_file)
    required = topic_meta.get("required_titles")
    if not isinstance(required, list):
        raise ValueError(f"0x3f index invalid required_titles for topic: {topic_file}")
    if not all(isinstance(x, str) for x in required):
        raise ValueError(f"0x3f index required_titles must be string array: {topic_file}")
    return required


def get_problem_chains_in_topic(
    index: dict[str, Any], topic_file: str, problem_id: str
) -> list[list[str]]:
    topic_meta = _get_topic_meta(index, topic_file)
    problems = topic_meta.get("problems")
    if not isinstance(problems, dict):
        raise ValueError(f"0x3f index invalid problems map for topic: {topic_file}")
    pid = normalize_problem_id(problem_id)
    chains = problems.get(pid, [])
    if not isinstance(chains, list):
        raise ValueError(f"0x3f index invalid chains for {topic_file}#{pid}")
    cleaned: list[list[str]] = []
    for chain in chains:
        if not isinstance(chain, list) or not all(isinstance(x, str) for x in chain):
            raise ValueError(f"0x3f index invalid chain data for {topic_file}#{pid}")
        cleaned.append(chain)
    return cleaned


def find_problem_locations(index: dict[str, Any], problem_id: str) -> list[tuple[str, list[str]]]:
    pid = normalize_problem_id(problem_id)
    topics = index.get("topics")
    if not isinstance(topics, dict):
        raise ValueError("0x3f index schema error: `topics` is not an object")

    locations: list[tuple[str, list[str]]] = []
    for topic_file, topic_meta in sorted(topics.items()):
        if not isinstance(topic_meta, dict):
            continue
        problems = topic_meta.get("problems")
        if not isinstance(problems, dict):
            continue
        chains = problems.get(pid)
        if not isinstance(chains, list):
            continue
        for chain in chains:
            if isinstance(chain, list) and all(isinstance(x, str) for x in chain):
                locations.append((topic_file, chain))
    return locations


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


def _normalize_heading(title: str) -> str:
    text = title.strip()
    text = re.sub(r"^[零一二三四五六七八九十]+、\s*", "", text)
    text = re.sub(r"^§\d+(?:\.\d+)*\s*", "", text)
    text = re.sub(r"^\d+(?:\.\d+)*\s+", "", text)
    return re.sub(r"\s+", " ", text).strip()


def _collect_topics_structure(path: Path) -> tuple[set[str], list[tuple[str, int, list[str]]]]:
    headings: dict[int, str] = {}
    heading_set: set[str] = set()
    entries: list[tuple[str, int, list[str]]] = []

    for lineno, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        hm = HEADING_RE.match(line)
        if hm:
            level = len(hm.group(1))
            title = _normalize_heading(hm.group(2))
            headings[level] = title
            for key in list(headings):
                if key > level:
                    del headings[key]
            if title:
                heading_set.add(title)
            continue

        match = PROBLEM_ID_RE.match(line)
        if not match:
            continue
        problem_id = match.group(1)
        chain = [headings[k] for k in sorted(headings) if k >= 2 and headings[k]]
        entries.append((problem_id, lineno, chain))

    return heading_set, entries


def _contains_subchain(full_chain: list[str], sub_chain: list[str]) -> bool:
    if not sub_chain or len(full_chain) < len(sub_chain):
        return False
    n = len(sub_chain)
    return any(full_chain[i : i + n] == sub_chain for i in range(len(full_chain) - n + 1))


def _format_chain(chain: list[str]) -> str:
    return " / ".join(chain) if chain else "(root)"


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


def check_zero3f_alignment(path: Path, index: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    rel = path.relative_to(ROOT).as_posix()

    topic_titles, topic_entries = _collect_topics_structure(path)
    try:
        required_titles = get_required_titles(index, path.name)
    except ValueError as exc:
        errors.append(f"{rel}: {exc}")
        return errors

    missing_titles = sorted(set(required_titles) - topic_titles)
    if missing_titles:
        joined = "、".join(missing_titles)
        errors.append(f"{rel}: 缺少 0x3f 对应分类标题（可新增但不可缺失）: {joined}")

    for problem_id, lineno, topic_chain in topic_entries:
        try:
            ref_chains = get_problem_chains_in_topic(index, path.name, problem_id)
        except ValueError as exc:
            errors.append(f"{rel}: {exc}")
            continue
        if not ref_chains:
            continue
        if any(_contains_subchain(topic_chain, ref_chain) for ref_chain in ref_chains):
            continue
        expected = " 或 ".join(_format_chain(c) for c in ref_chains)
        errors.append(
            f"{rel}:{lineno}: 题号 {problem_id} 分类位置与 0x3f 不一致，"
            f"当前在 {_format_chain(topic_chain)}，0x3f 在 {expected}"
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
    try:
        zero3f_index = load_index()
    except ValueError as exc:
        print(f"topics: {exc}")
        return 1

    all_errors: list[str] = []
    for topic_path in sorted(TOPICS_DIR.glob("*.md")):
        all_errors.extend(check_topic_template_limits(topic_path))
        all_errors.extend(check_entry_format_and_paths(topic_path))
        all_errors.extend(check_zero3f_alignment(topic_path, zero3f_index))
    all_errors.extend(check_duplicate_problem_ids())

    if all_errors:
        print("\n".join(all_errors))
        return 1

    print("All checks passed for topics/*.md")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
