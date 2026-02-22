#!/usr/bin/env python3
"""
CI 总入口：串行执行 solutions 与 topics 校验。

用法:
  python scripts/ci/ci.py
"""
from __future__ import annotations

import sys
from pathlib import Path


def _prepare_import_path() -> None:
    current_dir = Path(__file__).resolve().parent
    if str(current_dir) not in sys.path:
        sys.path.insert(0, str(current_dir))


def main() -> int:
    _prepare_import_path()

    import check_solutions
    import check_topics

    exit_code = 0

    print("[ci] running solutions checks...")
    solutions_rc = check_solutions.main()
    if solutions_rc != 0:
        exit_code = 1

    print("[ci] running topics checks...")
    topics_rc = check_topics.main()
    if topics_rc != 0:
        exit_code = 1

    if exit_code == 0:
        print("[ci] all checks passed")
    else:
        print("[ci] checks failed")
    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
