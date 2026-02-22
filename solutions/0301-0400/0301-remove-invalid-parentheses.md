---
id: 301
title: 删除无效的括号
difficulty: Medium
tags: [breadth-first-search, string, backtracking]
created: 2026-02-20
---

# 301. 删除无效的括号

## 题目链接
https://leetcode.cn/problems/remove-invalid-parentheses/

## 题目描述

<p>给你一个由若干括号和字母组成的字符串 <code>s</code> ，删除最小数量的无效括号，使得输入的字符串有效。</p>

<p>返回所有可能的结果。答案可以按 <strong>任意顺序</strong> 返回。</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>s = "()())()"
<strong>输出：</strong>["(())()","()()()"]
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>s = "(a)())()"
<strong>输出：</strong>["(a())()","(a)()()"]
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>s = ")("
<strong>输出：</strong>[""]
</pre>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 <= s.length <= 25</code></li>
	<li><code>s</code> 由小写英文字母以及括号 <code>'('</code> 和 <code>')'</code> 组成</li>
	<li><code>s</code> 中至多含 <code>20</code> 个括号</li>
</ul>

## 解题思路
目标是删除最少数量的括号，使结果字符串括号匹配，并返回所有可能结果（去重）。

第一步先计算“必须删除”的左右括号数量：

- 扫描字符串，遇到 `'('` 先计入 `lrem`；
- 遇到 `')'`：
  - 如果当前没有可匹配的左括号（`lrem == 0`），这个右括号必删，`rrem += 1`；
  - 否则用一个左括号去匹配它，`lrem -= 1`。

这样得到的 `(lrem, rrem)` 是**最少删除数**，后续只在这个预算内做回溯，保证不会产生“多删”的解。

第二步回溯枚举删除位置（DFS）：

- 从 `start` 开始遍历 `cur`，只对 `'('` / `')'` 尝试“删除一个”，形成新串 `nxt` 递归。
- 剪枝 1：如果 `lrem < 0` 或 `rrem < 0`，说明删超了，直接返回。
- 剪枝 2（去重）：同一层递归中若出现连续相同字符，只删除第一个（`i > start and cur[i] == cur[i-1]`），避免生成重复答案。
- 当 `lrem == 0` 且 `rrem == 0` 时，才做一次线性校验 `is_valid`：
  - 用 `balance` 统计当前前缀的括号平衡，任何时刻 `balance < 0` 都说明右括号过多，非法；
  - 最终 `balance == 0` 才合法。

边界情况：字符串里夹杂的非括号字符始终保留，不参与删除。

- 时间复杂度: $O(2^n)$
- 空间复杂度: $O(n)$

## 代码
```python
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        lrem = rrem = 0
        for c in s:
            if c == '(':
                lrem += 1
            elif c == ')':
                if lrem == 0:
                    rrem += 1   # 左边没了，只能删右边
                else:
                    lrem -= 1   # 预计匹配，左边少删一个
        
        def is_valid(s):
            balance = 0
            for c in s:
                if c == '(':
                    balance += 1
                elif c == ')':
                    balance -= 1
                if balance < 0:
                    return False
            return (balance == 0)

        def dfs(start: int, lrem: int, rrem: int, cur: str):
            # 只要超删就剪枝
            if lrem < 0 or rrem < 0:
                return
            # 删够了才检查合法性
            if lrem == 0 and rrem == 0 and is_valid(cur):
                ret.append(cur)
                return

            for i in range(start, len(cur)):
                # 只对括号尝试删除
                if cur[i] not in '()':
                    continue
                # 去重：同一层如果连续相同字符，只删第一个
                if i > start and cur[i] == cur[i - 1]:
                    continue

                nxt = cur[:i] + cur[i + 1:]
                if cur[i] == '(':
                    dfs(i, lrem - 1, rrem, nxt)
                else:  # cur[i] == ')'
                    dfs(i, lrem, rrem - 1, nxt)


        ret = []
        dfs(0, lrem, rrem, s)
        return ret
```
