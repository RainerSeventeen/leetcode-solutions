---
id: 34
title: 在排序数组中查找元素的第一个和最后一个位置
difficulty: Medium
tags: [array, binary-search]
created: 2026-02-20
---

# 34. 在排序数组中查找元素的第一个和最后一个位置

## 题目链接
https://leetcode.cn/problems/find-first-and-last-position-of-element-in-sorted-array/

## 题目描述
暂无（需要从LeetCode获取）

## 解题思路
这道题目很好，涉及到了二分查找的本质，我们可以从中抽象出二分查找的通用模板

二分查找边界的本质：一个结构，对某一个 `bool` 表达式的值呈现单调性，我们通过对半取区间来找到第一个发生变化的区间

做法上等价于实现两次“边界二分”：

- `lower_bound`：找到第一个 `nums[i] >= target` 的位置 `L`；
- `upper_bound`：找到第一个 `nums[i] > target` 的位置 `R`。

若 `L == n` 或 `nums[L] != target`，说明不存在目标值，返回 `[-1, -1]`；否则答案为 `[L, R-1]`。代码里统一使用半开区间 `[l, r)`，可以避免很多 `+1/-1` 的边界错误。

- 时间复杂度: $O(\log n)$
- 空间复杂度: $O(1)$

## 代码
```python
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # 二分查找, 一个是 [0, l) <= target, 另一个是 [l, n) > target
        n = len(nums)
        def lower():  # 找到第一个 nums[i] >= target
            l, r = 0, n
            while l < r: # [l, r)
                mid = (l + r) >> 1
                if nums[mid] >= target:
                    r = mid
                else:
                    l = mid + 1
            return l
        
        def upper(): # 找到第一个 nums[i] > target
            l, r = 0, n
            while l < r: # [l, r)
                mid = (l + r) >> 1
                if nums[mid] > target:
                    r = mid
                else:
                    l = mid + 1
            return l
        l = lower()
        u = upper()

        if l == n or nums[l] != target:
            return(-1, -1)
        else:
            return(l, u - 1)
```
