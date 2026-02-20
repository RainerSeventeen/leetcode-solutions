---
id: 31
title: 下一个排列
difficulty: Medium
tags: [array, two-pointers]
created: 2026-02-20
---

# 31. 下一个排列

## 题目链接
https://leetcode.cn/problems/next-permutation/

## 题目描述
暂无（需要从LeetCode获取）

## 解题思路
从右往左找“下一字典序”的关键断点。

1) 从右往左找到第一个满足 `nums[i] < nums[i+1]` 的位置 `i`（pivot）。若不存在，说明整个序列非增，下一排列就是把全数组反转得到最小序列。

2) 若找到 pivot：在右侧后缀（必为非增序）中，从右往左找到第一个 `> nums[i]` 的元素 `nums[j]`，交换 `nums[i]` 与 `nums[j]`。

3) 将 `i+1..end` 这段后缀反转，使其变为最小的升序，从而得到“刚好比原序列大一点”的排列。

- 时间复杂度: $O(n)$
- 空间复杂度: $O(1)$

## 代码
```python
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        n = len(nums)
        pre = -1
        i = n - 1
        def reverse_nums(nums, a, b):
            while a < b:
                nums[a], nums[b] = nums[b], nums[a]
                a += 1
                b -= 1
        while i >= 0:
            if nums[i] < pre:
                break
            pre = nums[i]
            i -= 1
        else:
            reverse_nums(nums, 0, n - 1)    # 重新排列最小值
            return
        # 找到第一个 比 nums[i] 大的交换一下
        for j in range(n - 1, i, -1):
            if nums[i] < nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
                break
        reverse_nums(nums, i + 1, n - 1)
```
