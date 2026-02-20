---
id: 287
title: 寻找重复数
difficulty: Medium
tags: [bit-manipulation, array, two-pointers, binary-search]
created: 2026-02-20
---

# 287. 寻找重复数

## 题目链接
https://leetcode.cn/problems/find-the-duplicate-number/

## 题目描述
暂无（需要从LeetCode获取）

## 解题思路
题目满足：数组长度为 `n + 1`，元素值在 `[1, n]`，因此必然存在重复数；并且通常要求不修改数组、额外空间尽量为 `O(1)`。

关键转化：把下标当作节点，把 `i -> nums[i]` 看作“下一跳”，就得到一个从 `0` 出发的函数图（每个节点出度为 1）。由于值域只有 `[1, n]`，从 `0` 出发不断跳转一定会进入某个环；而“环的入口”对应的值，正是重复的那个数（有两个不同下标指向同一个值，导致入环）。

用 Floyd 判圈（龟兔赛跑）分两步：

1. **找相遇点**：`slow = nums[0]` 每次走一步，`fast = nums[nums[0]]` 每次走两步；若存在环一定会在环内相遇。
2. **找入环点（重复数）**：将 `slow` 置为 `0`，`slow` 与 `fast` 同步每次走一步，再次相遇的位置就是入环点，对应重复的数。

边界情况：数组最小长度为 2 也成立；重复数可能出现多次，但入环点仍是同一个重复值。

- 时间复杂度: $O(n)$
- 空间复杂度: $O(1)$

## 代码
```python
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Floyid 环算法
        slow = nums[0]
        fast = nums[nums[0]]

        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        # 找到相遇点，回去找入环点 
        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow
```
