---
id: 39
title: 组合总和
difficulty: Medium
tags: [array, backtracking]
created: 2026-02-20
---

# 39. 组合总和

## 题目链接
https://leetcode.cn/problems/combination-sum/

## 题目描述
暂无（需要从LeetCode获取）

## 解题思路
回溯枚举“选哪些数”来凑出 `target`。由于同一个数可以重复使用，递归时可以继续从当前下标 `idx` 选择。

实现要点：

- 先对 `candidates` 排序，便于剪枝；
- `backtrace(idx, path, left)` 表示：从 `candidates[idx:]` 中选数，当前已选为 `path`，还剩 `left` 需要凑；
- 枚举 `i in [idx, n)`：把 `candidates[i]` 放入 `path`，递归到 `backtrace(i, ..., left - candidates[i])`（注意仍传 `i`，允许重复选）；
- 若 `left == 0` 记录一组解；若 `candidates[i] > left`，后续更大，直接 `break` 剪枝。

递归深度最多为 $T = \lfloor target / \min(candidates) \rfloor$，每层最多有 `n` 个分支（粗略上界）。

- 时间复杂度: $O(n^{T})$
- 空间复杂度: $O(T)$

## 代码
```python
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ret = []
        n = len(candidates)
        def backtrace(idx, path, left):
            if left == 0:
               ret.append(path.copy())
               return

            for i in range(idx, n):
                if candidates[i] > left:
                path.append(candidates[i])
                    break
                backtrace(i, path, left - candidates[i])
                path.pop()
        backtrace(0, [], target)
        return ret
```
