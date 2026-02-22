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

<p>整数数组的一个 <strong>排列</strong>&nbsp; 就是将其所有成员以序列或线性顺序排列。</p>

<ul>
	<li>例如，<code>arr = [1,2,3]</code> ，以下这些都可以视作 <code>arr</code> 的排列：<code>[1,2,3]</code>、<code>[1,3,2]</code>、<code>[3,1,2]</code>、<code>[2,3,1]</code> 。</li>
</ul>

<p>整数数组的 <strong>下一个排列</strong> 是指其整数的下一个字典序更大的排列。更正式地，如果数组的所有排列根据其字典顺序从小到大排列在一个容器中，那么数组的 <strong>下一个排列</strong> 就是在这个有序容器中排在它后面的那个排列。如果不存在下一个更大的排列，那么这个数组必须重排为字典序最小的排列（即，其元素按升序排列）。</p>

<ul>
	<li>例如，<code>arr = [1,2,3]</code> 的下一个排列是 <code>[1,3,2]</code> 。</li>
	<li>类似地，<code>arr = [2,3,1]</code> 的下一个排列是 <code>[3,1,2]</code> 。</li>
	<li>而 <code>arr = [3,2,1]</code> 的下一个排列是 <code>[1,2,3]</code> ，因为 <code>[3,2,1]</code> 不存在一个字典序更大的排列。</li>
</ul>

<p>给你一个整数数组 <code>nums</code> ，找出 <code>nums</code> 的下一个排列。</p>

<p>必须<strong><a href="https://baike.baidu.com/item/%E5%8E%9F%E5%9C%B0%E7%AE%97%E6%B3%95" target="_blank"> 原地 </a></strong>修改，只允许使用额外常数空间。</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,2,3]
<strong>输出：</strong>[1,3,2]
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [3,2,1]
<strong>输出：</strong>[1,2,3]
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,1,5]
<strong>输出：</strong>[1,5,1]
</pre>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 100</code></li>
	<li><code>0 &lt;= nums[i] &lt;= 100</code></li>
</ul>

## 解题思路
从右往左找“下一字典序”的关键断点。

1) 从右往左找到第一个满足 `nums[i] < nums[i+1]` 的位置 `i`（pivot）。若不存在，说明整个序列非增，下一排列就是把全数组反转得到最小序列。

2) 若找到 pivot：在右侧后缀（必为非增序）中，从右往左找到第一个 `> nums[i]` 的元素 `nums[j]`，交换 `nums[i]` 与 `nums[j]`。

3) 将 `i+1..end` 这段后缀反转，使其变为最小的升序，从而得到“刚好比原序列大一点”的排列。

- 时间复杂度: $O(n)$
- 空间复杂度: $O(1)$

## 相关专题
- [贪心与思维](../../topics/greedy-and-thinking.md)

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
