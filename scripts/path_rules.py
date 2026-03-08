#!/usr/bin/env python3
from __future__ import annotations

COMPETITION_ID_THRESHOLD = 10000
COMPETITION_DIRNAME = "competition_problems"


def is_competition_problem(problem_id: int) -> bool:
    return problem_id > COMPETITION_ID_THRESHOLD


def format_problem_id(problem_id: int) -> str:
    if problem_id < COMPETITION_ID_THRESHOLD:
        return f"{problem_id:04d}"
    return str(problem_id)


def build_range_dir(problem_id: int) -> str:
    start = ((problem_id - 1) // 100) * 100 + 1
    end = start + 99
    return f"{start:04d}-{end:04d}"


def build_solution_subdir(problem_id: int) -> str:
    if is_competition_problem(problem_id):
        return COMPETITION_DIRNAME
    return build_range_dir(problem_id)
