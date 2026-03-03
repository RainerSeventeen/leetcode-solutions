#!/usr/bin/env python3
"""
按题号查询 0x3f 静态索引中的归档位置。

用法:
  python scripts/query_0x3f_index.py 70
  python scripts/query_0x3f_index.py 0070
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CI_DIR = ROOT / "scripts" / "ci"
if str(CI_DIR) not in sys.path:
    sys.path.insert(0, str(CI_DIR))

from check_topics import find_problem_locations, load_index, normalize_problem_id


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("problem_id", help="题号，支持 1~4 位数字（会自动补零）")
    args = parser.parse_args()

    try:
        pid = normalize_problem_id(args.problem_id)
        index = load_index()
        locations = find_problem_locations(index, pid)
    except ValueError as exc:
        print(exc)
        return 1

    if not locations:
        print(f"{pid}: not found")
        return 0

    print(f"{pid}:")
    for topic_file, chain in locations:
        chain_text = " / ".join(chain) if chain else "(root)"
        print(f"- {topic_file}: {chain_text}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
