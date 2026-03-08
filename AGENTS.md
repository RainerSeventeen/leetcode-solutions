# Repository Guidelines

## Project Structure

详见：`.ai_docs/structure.md`

## Coding Style & Naming Conventions

详见：`.ai_docs/rules.md`

## Testing Guidelines

详见：`.ai_docs/format.md`（solutions / topics 格式规范与 CI 校验规则）
以及：`.ai_docs/scripts.md`（脚本说明与推荐执行方式）

## Commit & Pull Request Guidelines

- Prefer Conventional Commit-style subjects (observed: `feat: ...`).
- PRs should summarize what changed and keep CI green.

## Security & Configuration Tips

- `.env` 存放 `LC_SESSION` / `LC_CSRF`，不提交到版本库。

## Automation Notes

- 常规校验入口：`python scripts/ci/ci.py`
- 竞赛题转正检查：`python scripts/ci/check_competition_promotions.py`
- 题号完整性检查：`python scripts/ci/check_id_integrity.py`
