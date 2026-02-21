#!/usr/bin/env python3
from __future__ import annotations

import re
import subprocess
import sys
from datetime import date
from pathlib import Path


MESSAGE_PATTERN = re.compile(
    r"^docs: addd note for LeetCode \(([0-9]{4})(,[0-9]{4})*\), [0-9]{4}-[0-9]{2}-[0-9]{2}$"
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


def main() -> int:
    status = run_git(["status", "--porcelain=1", "--untracked-files=all"])
    if status.returncode != 0:
        sys.stderr.write(status.stderr)
        return status.returncode

    status_files = parse_status_files(status.stdout)
    if not status_files:
        sys.stderr.write("No working tree changes found.\n")
        return 2

    files_to_stage: list[str] = []
    new_solution_files: list[str] = []
    for code, path in status_files:
        is_new = code == "??" or "A" in code
        if path.startswith("solutions/") and is_new:
            files_to_stage.append(path)
            new_solution_files.append(path)
            continue
        if path.startswith("topics/"):
            files_to_stage.append(path)

    if not files_to_stage:
        sys.stderr.write(
            "No eligible files found. Only new solutions/* and changed topics/* are allowed.\n"
        )
        return 2

    problem_ids = extract_solution_ids(new_solution_files)
    if not problem_ids:
        sys.stderr.write(
            "Eligible files found, but no new solution files with 4-digit problem id.\n"
        )
        for path in files_to_stage:
            sys.stderr.write(f"- {path}\n")
        return 3

    commit_date = date.today().isoformat()
    ids_joined = ",".join(problem_ids)
    message = f"docs: addd note for LeetCode ({ids_joined}), {commit_date}"
    if not MESSAGE_PATTERN.fullmatch(message):
        sys.stderr.write(f"Commit message failed regex validation: {message}\n")
        return 1

    # Output contract for bash caller:
    # line 1: commit message
    # line 2..N: files to stage
    print(message)
    for path in files_to_stage:
        print(path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
