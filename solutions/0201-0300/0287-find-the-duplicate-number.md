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

<p>给定一个包含&nbsp;<code>n + 1</code> 个整数的数组&nbsp;<code>nums</code> ，其数字都在&nbsp;<code>[1, n]</code>&nbsp;范围内（包括 <code>1</code> 和 <code>n</code>），可知至少存在一个重复的整数。</p>

<p>假设 <code>nums</code> 只有 <strong>一个重复的整数</strong> ，返回&nbsp;<strong>这个重复的数</strong> 。</p>

<p>你设计的解决方案必须 <strong>不修改</strong> 数组 <code>nums</code> 且只用常量级 <code>O(1)</code> 的额外空间。</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,3,4,2,2]
<strong>输出：</strong>2
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [3,1,3,4,2]
<strong>输出：</strong>3
</pre>

<p><strong>示例 3 :</strong></p>

<pre>
<strong>输入：</strong>nums = [3,3,3,3,3]
<strong>输出：</strong>3
</pre>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>nums.length == n + 1</code></li>
	<li><code>1 &lt;= nums[i] &lt;= n</code></li>
	<li><code>nums</code> 中 <strong>只有一个整数</strong> 出现 <strong>两次或多次</strong> ，其余整数均只出现 <strong>一次</strong></li>
</ul>

<p><b>进阶：</b></p>

<ul>
	<li>如何证明 <code>nums</code> 中至少存在一个重复的数字?</li>
	<li>你可以设计一个线性级时间复杂度 <code>O(n)</code> 的解决方案吗？</li>
</ul>

## 解题思路
题目满足：数组长度为 `n + 1`，元素值在 `[1, n]`，因此必然存在重复数；并且通常要求不修改数组、额外空间尽量为 `O(1)`。

关键转化：把下标当作节点，把 `i -> nums[i]` 看作“下一跳”，就得到一个从 `0` 出发的函数图（每个节点出度为 1）。由于值域只有 `[1, n]`，从 `0` 出发不断跳转一定会进入某个环；而“环的入口”对应的值，正是重复的那个数（有两个不同下标指向同一个值，导致入环）。

用 Floyd 判圈（龟兔赛跑）分两步：

1. **找相遇点**：`slow = nums[0]` 每次走一步，`fast = nums[nums[0]]` 每次走两步；若存在环一定会在环内相遇。
2. **找入环点（重复数）**：将 `slow` 置为 `0`，`slow` 与 `fast` 同步每次走一步，再次相遇的位置就是入环点，对应重复的数。

边界情况：数组最小长度为 2 也成立；重复数可能出现多次，但入环点仍是同一个重复值。

- 时间复杂度: $O(n)$
- 空间复杂度: $O(1)$

## 相关专题
- [二分算法](../../topics/binary-search.md)

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
