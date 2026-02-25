---
name: solution-quality-ranker
description: Use when the user provides one or more imported `solutions/...md` files and asks to dedupe same-method AC submissions, rank solutions from best to worst, rewrite code-block order, fill idea/complexity from best solution, and report non-optimality.
---

# Solution Quality Ranker

## Environment

- Use `.venv/bin/python` for Python scripts.
- If `.venv/bin/python` is missing, stop and report that virtual environment is required.

## Input

- One or more `solutions/...md` paths from the current run.
- Operate only on given paths; do not scan or modify unrelated solution files.

## Hard Rules

- Do not create new solution files.
- Keep output style concise and consistent with existing solution files.
- Never leave placeholders such as `O()` in complexity fields.
- Preserve all genuinely distinct methods; remove only redundant same-method variants.

## Workflow

1. Parse code variants
   - For each file, parse all code blocks under `## 代码`.
   - Group submissions by method; treat debug-only/comment-only differences as same method.

2. Dedupe + rank
   - Remove redundant same-method variants.
   - Rank remaining methods from best to worst, primarily by asymptotic complexity and secondarily by implementation quality/readability.
   - Rewrite `## 代码` block order to best-to-worst (best must be first).

3. Best-solution documentation
   - Use the top-ranked block as best solution.
   - Fill `## 解题思路` with a concise, code-consistent explanation in Chinese.
   - Fill concrete complexity lines:
     - `时间复杂度：$O(xxx)$`
     - `空间复杂度：$O(xxx)$`

4. Optimality checks
   - Determine whether the best submission reaches problem-level optimality (usually asymptotic optimality for known mainstream approaches).
   - If latest submission is not the best one, mark `latest-not-best`.
   - If all AC submissions for the problem are still suboptimal, mark `all AC non-optimal`.

## Final Output

Report per processed file:
- Whether blocks were reordered.
- Kept variants count and filtered same-method count.
- Whether latest submission is not best.
- Whether all AC submissions are non-optimal.
- Complexity filled (`time`, `space`).

