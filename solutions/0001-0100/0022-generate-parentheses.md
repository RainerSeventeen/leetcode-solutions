---
id: 22
title: 括号生成
difficulty: Medium
tags: [string, dynamic-programming, backtracking]
created: 2026-02-20
---

# 22. 括号生成

## 题目链接
https://leetcode.cn/problems/generate-parentheses/

## 题目描述
暂无（需要从LeetCode获取）

## 解题思路
回溯生成所有合法括号串。用 `left/right` 表示还剩多少个 `'('`/`')'` 可以放入（或等价地表示已用数量），并维护路径 `path`。

关键约束（不变量）：任何前缀中，右括号数量不能超过左括号数量。用“剩余量”表达就是：任意时刻必须满足 `left <= right`，否则当前前缀必然非法，直接剪枝。

递归选择：

- 若 `left > 0`，可以放 `'('`；
- 若 `right > 0` 且 `left <= right - 1`（等价于放完后仍满足 `left <= right`），可以放 `')'`；
- 当 `left == 0 and right == 0`，得到一个完整解。

一共会生成第 `n` 个卡特兰数 `C_n` 个结果，每个结果长度为 `2n`。

- 时间复杂度: $O(C_n \cdot n)$
- 空间复杂度: $O(n)$

## 代码
```python
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        path = []

        def backtrace(left, right):
            if left == 0 and right == 0:
                res.append("".join(path))
                return

            if left > right:    # 右括号数 > 左括号
                return

            if left > 0:
                path.append('(')
                backtrace(left - 1, right)
                path.pop()

            if right > 0:
                path.append(')')
                backtrace(left, right - 1)
                path.pop()

        backtrace(n, n)
        return res
```
