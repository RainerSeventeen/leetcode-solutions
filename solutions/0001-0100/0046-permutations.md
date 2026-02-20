---
id: 46
title: 全排列
difficulty: Medium
tags: [array, backtracking]
created: 2026-02-20
---

# 46. 全排列

## 题目链接
https://leetcode.cn/problems/permutations/

## 题目描述
暂无（需要从LeetCode获取）

## 解题思路
回溯生成全排列。用 `used[i]` 标记 `nums[i]` 是否已放入当前排列 `curr`：

- 每一层递归选择一个尚未使用的元素加入 `curr`，并把 `used[i]=True`；
- 当 `len(curr) == n`，得到一个完整排列，拷贝加入结果；
- 回溯时撤销选择：弹出 `curr` 末尾并恢复 `used[i]=False`。

`used` 保证每个元素在一条路径中只出现一次，递归树恰好覆盖全部 `n!` 种排列。

- 时间复杂度: $O(n \cdot n!)$
- 空间复杂度: $O(n)$

## 代码
```python
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        used = [False] * n
        ret = []
        curr = []

        def backtrace():
            if len(curr) == n:
                ret.append(curr.copy())
                return

            for i in range(n):
                if used[i]:
                    continue
                used[i] = True
                curr.append(nums[i])
                backtrace()
                curr.pop()
                used[i] = False

        backtrace()
        print(ret)
        return ret
```
