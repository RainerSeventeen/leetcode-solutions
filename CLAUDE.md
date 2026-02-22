# Repository Guidelines

## Project Structure

详见：`.ai_docs/structure.md`

## Build, Test, and Development Commands

详见：`.ai_docs/scripts.md`（各脚本用法）和 `.ai_docs/workflows.md`（典型工作流）

## Coding Style & Naming Conventions

详见：`.ai_docs/rules.md`

## Testing Guidelines

详见：`.ai_docs/format.md`（solutions / topics 格式规范与 CI 校验规则）

## Commit & Pull Request Guidelines

- Prefer Conventional Commit-style subjects (observed: `feat: ...`).
- PRs should summarize what changed and keep CI green.

## Security & Configuration Tips

- `.env` 存放 `LC_SESSION` / `LC_CSRF`，不提交到版本库。
