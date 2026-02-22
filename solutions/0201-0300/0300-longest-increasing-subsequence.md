---
id: 300
title: Longest Increasing Subsequence
difficulty: Medium
tags: [array, binary-search, dynamic-programming]
created: 2026-02-20
---

# 300. 最长递增子序列

## 题目链接
https://leetcode.cn/problems/longest-increasing-subsequence/

## 题目描述
<p>给你一个整数数组 <code>nums</code> ，找到其中最长严格递增子序列的长度。</p>

<p><strong>子序列&nbsp;</strong>是由数组派生而来的序列，删除（或不删除）数组中的元素而不改变其余元素的顺序。例如，<code>[3,6,2,7]</code> 是数组 <code>[0,3,1,6,2,2,7]</code> 的<span data-keyword="subsequence-array">子序列</span>。</p>
&nbsp;

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [10,9,2,5,3,7,101,18]
<strong>输出：</strong>4
<strong>解释：</strong>最长递增子序列是 [2,3,7,101]，因此长度为 4 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [0,1,0,3,2,3]
<strong>输出：</strong>4
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>nums = [7,7,7,7,7,7,7]
<strong>输出：</strong>1
</pre>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 2500</code></li>
	<li><code>-10<sup>4</sup> &lt;= nums[i] &lt;= 10<sup>4</sup></code></li>
</ul>

<p><b>进阶：</b></p>

<ul>
	<li>你能将算法的时间复杂度降低到&nbsp;<code>O(n log(n))</code> 吗?</li>
</ul>

## 解题思路
经典解法有两种：`O(n^2)` 的 DP 与 `O(n log n)` 的“贪心 + 二分”。下面对应代码使用的是后者。

维护一个数组 `tails`，含义是：

- `tails[i]` 表示“长度为 `i + 1` 的严格递增子序列，其末尾元素可能的最小值”。
- `tails` 始终保持递增。

遍历每个数 `x`：

- 在 `tails` 中二分查找第一个 `>= x` 的位置 `idx`（用 `bisect_left`）。
  - 如果 `idx == len(tails)`，说明 `x` 比所有末尾都大，可以把最长长度延长 1：`tails.append(x)`。
  - 否则用更小的末尾去“替换台阶”：`tails[idx] = x`。这不会改变已有最长长度，但会让对应长度的末尾更小，从而给后续元素留出更大增长空间（贪心点）。

因为题目是**严格递增**，对相等元素必须放在同一长度上做替换，所以使用 `bisect_left` 而不是 `bisect_right`。

边界情况：

- 全部相等：`tails` 只会被反复替换，最终长度为 1。
- 存在负数/乱序不影响，算法只依赖比较大小。

- 时间复杂度: $O(n \log n)$
- 空间复杂度: $O(n)$

## 相关专题
- [动态规划](../../topics/dynamic-programming.md)

## 代码
```python
from bisect import bisect_left
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        tails = [] # 这是一个有序数组
        for n in nums:
            idx = bisect_left(tails, n) # 找到 <= x 的下标位置
            if idx == len(tails): # 是结尾，直接加入
                tails.append(n)
            else:
                tails[idx] = n
        return len(tails)
```
