---
id: 33
title: 搜索旋转排序数组
difficulty: Medium
tags: [array, binary-search]
created: 2026-02-20
---

# 33. 搜索旋转排序数组

## 题目链接
https://leetcode.cn/problems/search-in-rotated-sorted-array/

## 题目描述
暂无（需要从LeetCode获取）

## 解题思路
拆成“两次二分”：

1) 先二分找到旋转点（最小值下标 `pivot`）。由于数组是“前半段都 > nums[-1]，后半段都 <= nums[-1]”，这个布尔条件对下标单调，因此可以用二分找第一个满足 `nums[mid] <= nums[-1]` 的位置。

2) 再根据 `target` 与 `nums[-1]` 的大小关系决定去哪个有序区间做普通二分：  
- `target <= nums[-1]` 则在 `[pivot, n)` 搜索；  
- 否则在 `[0, pivot)` 搜索。

每一步都是对单调区间做二分，整体仍是对数复杂度。

- 时间复杂度: $O(\log n)$
- 空间复杂度: $O(1)$

## 代码
```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        last = nums[-1]

        def find_split():    
            l, r = 0, n
            while l < r:
                mid = (l + r) // 2
                if nums[mid] <= last:
                    r = mid
                else:
                    l = mid + 1
            return l

        pivot = find_split()

        def bin_search(l, r):  # 等值二分查找
            while l < r:
                mid = (l + r) // 2
                if nums[mid] == target:
                    return mid
                if nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid
            return -1

        if target <= last:
            return bin_search(pivot, n)
        else:
            return bin_search(0, pivot)
```
