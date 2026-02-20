---
id: 128
title: Longest Consecutive Sequence
difficulty: Medium
tags: [union-find, array, hash-table]
created: 2026-02-20
---

# 128. 最长连续序列

## 题目链接
https://leetcode.cn/problems/longest-consecutive-sequence/

## 题目描述

<p>给定一个未排序的整数数组 <code>nums</code> ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。</p>

<p>请你设计并实现时间复杂度为&nbsp;<code>O(n)</code><em> </em>的算法解决此问题。</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [100,4,200,1,3,2]
<strong>输出：</strong>4
<strong>解释：</strong>最长数字连续序列是 [1, 2, 3, 4]。它的长度为 4。</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [0,3,7,2,5,8,4,6,0,1]
<strong>输出：</strong>9
</pre>

<p><strong class="example">示例 3：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,0,1,2]
<b>输出：</b>3
</pre>

<p><strong>提示：</strong></p>

<ul>
	<li><code>0 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>-10<sup>9</sup> &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
</ul>

## 解题思路

哈希集合 + 只从序列起点开始计数。

将数组存入 `set`，遍历集合中每个数 `n`：若 `n-1` 不在集合中，说明 `n` 是某段连续序列的起点，从 `n` 向后依次查找直到断开，记录长度。每个数最多被访问一次，整体 $O(n)$。

- 时间复杂度: $O(n)$
- 空间复杂度: $O(n)$

## 代码
```python
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        ret = 0
        for n in s:
            if n - 1 not in s:
                curr = n
                while curr in s:
                    curr += 1
                ret = max(ret, curr - n)
        return ret
```
