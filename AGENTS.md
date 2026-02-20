# Repository Guidelines

## Project Structure

- `solutions/`: LeetCode solutions as Markdown, grouped by id range (e.g. `solutions/0001-0100/`).
- `scripts/`: Python helpers for generating and validating solution files.
- `topics/`: Topic notes/knowledge base (Markdown), e.g. `topics/dp.md`.
- `.github/workflows/`: CI workflows (currently validates solution Markdown on push/PR).

## Build, Test, and Development Commands

- Create a local Python env (optional): `python3 -m venv .venv && source .venv/bin/activate`
- Install deps for fetching problems: `python -m pip install requests`
- Generate a solution template: `python3 scripts/fetch_problem.py 1584`
  - Writes to `solutions/<range>/<id>-<title-slug>.md` (use `--overwrite` to replace).
- Validate all solution Markdown: `python3 scripts/check_solutions.py`
  - This is what CI runs in `.github/workflows/solutions-check.yml`.

## Coding Style & Naming Conventions

- Python: 4-space indentation, type hints encouraged; keep scripts small and CLI-friendly.
- Solutions (Markdown) must match this pattern:
  - Path: `solutions/0001-0100/0001-some-title-slug.md`
  - Front matter keys: `id`, `title`, `difficulty` (`Easy|Medium|Hard`), `tags`, `created` (`YYYY-MM-DD`)
  - Required sections: `## 题目链接`, `## 题目描述`, `## 解题思路`, `## 代码`
- Avoid placeholders before merging (e.g. `O()` or empty ` ```python ``` ` blocks).

## Testing Guidelines

- There is no unit test suite; the repo’s “tests” are content checks.
- Run `python3 scripts/check_solutions.py` before pushing, especially after adding/editing `solutions/*.md`.

## Commit & Pull Request Guidelines

- Prefer Conventional Commit-style subjects (observed: `feat: ...`).
- PRs should:
  - Describe what was added/changed (problem id(s), topic notes, script changes).
  - Include any generated/updated solution files and keep CI green.

## Security & Configuration Tips

- `scripts/fetch_problem.py` makes network requests to `leetcode.cn`; don’t add credentials/cookies to the repo.
