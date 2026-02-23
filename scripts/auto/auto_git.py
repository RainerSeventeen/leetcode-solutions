#!/usr/bin/env python3
from __future__ import annotations

import argparse
import logging
import re
import subprocess
import sys
from datetime import date
from pathlib import Path


MESSAGE_PATTERN = re.compile(
    r"^docs: LeetCode \(([0-9]{4})(,[0-9]{4})*\), [0-9]{4}-[0-9]{2}-[0-9]{2}$"
)
SOLUTION_FILE_PATTERN = re.compile(r"^(\d{4})-[^.]+\.md$")


def run_git(args: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["git", *args],
        text=True,
        capture_output=True,
        check=False,
    )


def parse_status_files(status_output: str) -> list[tuple[str, str]]:
    files: list[tuple[str, str]] = []
    seen: set[str] = set()
    for raw_line in status_output.splitlines():
        if len(raw_line) < 3:
            continue
        code = raw_line[:2]
        path_part = raw_line[3:]
        if " -> " in path_part:
            path = path_part.split(" -> ", 1)[1]
        else:
            path = path_part
        path = path.strip()
        if not path or path in seen:
            continue
        seen.add(path)
        files.append((code, path))
    return files


def extract_solution_ids(paths: list[str]) -> list[str]:
    ids: list[str] = []
    seen: set[str] = set()
    for path_text in paths:
        path = Path(path_text)
        if not path_text.startswith("solutions/"):
            continue
        m = SOLUTION_FILE_PATTERN.match(path.name)
        if not m:
            continue
        pid = m.group(1)
        if pid in seen:
            continue
        seen.add(pid)
        ids.append(pid)
    return ids


def collect(log: logging.Logger) -> tuple[str, list[str]] | None:
    """检查工作区，返回 (commit_message, files_to_stage)，无需提交则返回 None。"""
    status = run_git(["status", "--porcelain=1", "--untracked-files=all"])
    if status.returncode != 0:
        log.error("git status failed: %s", status.stderr.strip())
        sys.exit(status.returncode)

    status_files = parse_status_files(status.stdout)
    if not status_files:
        log.info("no working tree changes found; skip")
        return None

    files_to_stage: list[str] = []
    solution_files: list[str] = []
    for code, path in status_files:
        is_new = code == "??" or "A" in code
        is_modified = "M" in code
        if path.startswith("solutions/") and (is_new or is_modified):
            files_to_stage.append(path)
            solution_files.append(path)
            continue
        if path.startswith("topics/") and is_modified:
            files_to_stage.append(path)

    if not files_to_stage:
        log.info("no eligible files (new/modified solutions/* or modified topics/*); skip")
        return None

    problem_ids = extract_solution_ids(solution_files)
    if not problem_ids:
        log.warning(
            "eligible files found but no solution with 4-digit id; skip: %s",
            ", ".join(files_to_stage),
        )
        return None

    commit_date = date.today().isoformat()
    ids_joined = ",".join(sorted(problem_ids))
    message = f"docs: LeetCode ({ids_joined}), {commit_date}"
    if not MESSAGE_PATTERN.fullmatch(message):
        log.error("commit message failed validation: %s", message)
        sys.exit(1)

    return message, files_to_stage


def main() -> int:
    parser = argparse.ArgumentParser(description="Auto git commit for LeetCode solutions")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--log-file", default=None)
    args = parser.parse_args()

    repo_root = Path(__file__).resolve().parent.parent.parent
    log_file = (
        Path(args.log_file) if args.log_file else repo_root / "scripts/auto/log/leetcode.log"
    )
    log_file.parent.mkdir(parents=True, exist_ok=True)

    logging.basicConfig(
        level=logging.DEBUG,
        format="[%(asctime)s] [%(levelname)s] %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        handlers=[logging.FileHandler(log_file)],
    )
    log = logging.getLogger(__name__)

    log.info("run started (dry-run=%s)", args.dry_run)

    result = collect(log)
    if result is None:
        return 0

    message, files_to_stage = result
    log.info("commit message: %s", message)
    for f in files_to_stage:
        log.info("  stage: %s", f)

    if args.dry_run:
        log.info("dry-run mode; skip git add/commit/push")
        return 0

    add = run_git(["add", "--", *files_to_stage])
    if add.returncode != 0:
        log.error("git add failed: %s", add.stderr.strip())
        return add.returncode

    diff = run_git(["diff", "--cached", "--quiet"])
    if diff.returncode == 0:
        log.info("no staged changes after git add; skip commit")
        return 0

    commit = run_git(["commit", "-m", message])
    if commit.returncode != 0:
        log.error("git commit failed: %s", commit.stderr.strip())
        return commit.returncode
    log.info("commit completed: %s", commit.stdout.strip())

    push = run_git(["push"])
    if push.returncode != 0:
        log.error("git push failed: %s", push.stderr.strip())
        return push.returncode
    log.info("push completed")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
