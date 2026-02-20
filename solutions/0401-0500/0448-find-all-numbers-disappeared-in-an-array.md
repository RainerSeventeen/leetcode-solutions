---
id: 448
title: Find All Numbers Disappeared in an Array
difficulty: Medium
tags: [array, hash-table]
created: 2026-02-20
---

# 448. 找到所有数组中消失的数字

## 题目链接
https://leetcode.cn/problems/find-all-numbers-disappeared-in-an-array/

## 题目描述

<p>给你一个含 <code>n</code> 个整数的数组 <code>nums</code> ，其中 <code>nums[i]</code> 在区间 <code>[1, n]</code> 内。请你找出所有在 <code>[1, n]</code> 范围内但没有出现在 <code>nums</code> 中的数字，并以数组的形式返回结果。</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [4,3,2,7,8,2,3,1]
<strong>输出：</strong>[5,6]
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,1]
<strong>输出：</strong>[2]
</pre>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == nums.length</code></li>
	<li><code>1 <= n <= 10<sup>5</sup></code></li>
	<li><code>1 <= nums[i] <= n</code></li>
</ul>

<p><strong>进阶：</strong>你能在不使用额外空间且时间复杂度为<em> </em><code>O(n)</code><em> </em>的情况下解决这个问题吗? 你可以假定返回的数组不算在额外空间内。</p>

## 解题思路

原地标记法（$O(1)$ 额外空间）。

利用数组值在 `[1, n]` 范围内的性质，将每个数 `num` 对应的索引 `num - 1` 处的值加 `n`（用取模 `(num-1) % n` 读取原始索引，防止重复加后越界）。遍历结束后，值仍 `<= n` 的位置 `i` 说明数字 `i+1` 从未出现过，即为消失的数字。

- 时间复杂度: $O(n)$
- 空间复杂度: $O(1)$

不计输出数组。

## 代码
```python
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for num in nums:
            idx = (num - 1) % n   # -1 再取模，保证 0..n-1
            nums[idx] += n

        return [i + 1 for i, x in enumerate(nums) if x <= n]
```
