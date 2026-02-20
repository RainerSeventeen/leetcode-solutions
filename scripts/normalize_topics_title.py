#!/usr/bin/env python3
from __future__ import annotations

import argparse
import difflib
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TOPICS_DIR = ROOT / "topics"

# 匹配 H2-H6 的标题行，可选地带有已有数字前缀（如 "1 " 或 "1.2 " 或 "1.2." ）
HEADING_RE = re.compile(r"^(#{2,6})( +)(\d+(?:\.\d+)*\.? +)?(.*)")


def _iter_lines(text: str) -> list[str]:
    """保留行尾换行符地分割文本。"""
    return text.splitlines(keepends=True)


def strip_numbers(lines: list[str]) -> list[str]:
    """移除 H2-H6 标题中的数字前缀，跳过代码块内的行。"""
    result: list[str] = []
    in_fence = False

    for line in lines:
        raw = line.rstrip("\n")
        eol = "\n" if line.endswith("\n") else ""

        if raw.startswith("```"):
            in_fence = not in_fence

        if in_fence or not raw.startswith("##"):
            result.append(line)
            continue

        m = HEADING_RE.match(raw)
        if m:
            hashes, space, _num, title = m.groups()
            result.append(f"{hashes}{space}{title}{eol}")
        else:
            result.append(line)

    return result


def add_numbers(lines: list[str]) -> list[str]:
    """为 H2-H6 标题添加层级数字前缀，跳过代码块内的行。"""
    # counters[0]=H2, counters[1]=H3, counters[2]=H4, counters[3]=H5, counters[4]=H6
    counters = [0, 0, 0, 0, 0]
    result: list[str] = []
    in_fence = False

    for line in lines:
        raw = line.rstrip("\n")
        eol = "\n" if line.endswith("\n") else ""

        if raw.startswith("```"):
            in_fence = not in_fence

        if in_fence or not raw.startswith("##"):
            result.append(line)
            continue

        m = HEADING_RE.match(raw)
        if not m:
            result.append(line)
            continue

        hashes, space, _num, title = m.groups()
        level = len(hashes)          # 2..6
        idx = level - 2              # 0..4

        counters[idx] += 1
        for i in range(idx + 1, len(counters)):
            counters[i] = 0

        num = ".".join(str(counters[i]) for i in range(idx + 1))
        result.append(f"{hashes}{space}{num} {title}{eol}")

    return result


def process_text(text: str, *, strip_only: bool) -> str:
    lines = _iter_lines(text)
    lines = strip_numbers(lines)
    if not strip_only:
        lines = add_numbers(lines)
    return "".join(lines)


def process_file(path: Path, *, strip_only: bool, dry_run: bool) -> bool:
    """处理单个文件，返回文件是否发生了变化。"""
    original = path.read_text(encoding="utf-8")
    result = process_text(original, strip_only=strip_only)

    if result == original:
        return False

    if dry_run:
        rel = path.relative_to(ROOT).as_posix()
        diff = difflib.unified_diff(
            original.splitlines(keepends=True),
            result.splitlines(keepends=True),
            fromfile=f"a/{rel}",
            tofile=f"b/{rel}",
        )
        sys.stdout.writelines(diff)
        return True

    path.write_text(result, encoding="utf-8")
    return True


def main() -> int:
    parser = argparse.ArgumentParser(
        description="为 topics/*.md 的 H2-H6 标题格式化层级数字前缀。",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例：
  # 为所有 topics/*.md 添加数字前缀（默认行为）
  python scripts/number_title.py

  # 只移除数字前缀，不重新添加
  python scripts/number_title.py --strip

  # 预览变更，不写入文件
  python scripts/number_title.py --dry-run
""",
    )
    parser.add_argument(
        "--strip",
        action="store_true",
        help="仅移除数字前缀，不重新添加",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="预览 diff，不写入文件",
    )
    args = parser.parse_args()

    paths = sorted(TOPICS_DIR.glob("*.md"))

    if not paths:
        print("没有找到要处理的文件", file=sys.stderr)
        return 1

    changed = 0
    for path in paths:
        was_changed = process_file(path, strip_only=args.strip, dry_run=args.dry_run)
        if was_changed:
            changed += 1
            if not args.dry_run:
                rel = path.relative_to(ROOT).as_posix()
                print(f"已更新：{rel}")

    action = "会被更新" if args.dry_run else "已更新"
    print(f"\n共 {changed} 个文件{action}。")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
