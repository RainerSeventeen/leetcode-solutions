---
id: 101014
title: First Unique Even Element
difficulty: Easy
tags: []
created: 2026-03-15
---

# 101014. 找到第一个唯一偶数

## 题目链接
https://leetcode.cn/problems/first-unique-even-element/

## 题目描述
<p>给你一个整数数组 <code>nums</code>。</p>

<p>请你返回一个整数，表示 <code>nums</code> 中出现 <strong>恰好</strong> 一次的第一个 <strong>偶数</strong>（以数组下标最早为准）。如果不存在这样的整数，返回 -1。</p>

<p>如果一个整数 <code>x</code> 能被 2 整除，那么它就被认为是 <strong>偶数</strong>。</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">nums = [3,4,2,5,4,6]</span></p>

<p><strong>输出：</strong> <span class="example-io">2</span></p>

<p><strong>解释：</strong></p>

<p>2 和 6 都是偶数，并且它们都恰好出现一次。因为 2 在数组中出现得更早，所以答案是 2。</p>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">nums = [4,4]</span></p>

<p><strong>输出：</strong> <span class="example-io">-1</span></p>

<p><strong>解释：</strong></p>

<p>没有恰好出现一次的偶数，所以返回 -1。</p>
</div>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 100</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 100</code></li>
</ul>


## 解题思路

- 先用 `Counter` 记录每个数字在 `nums` 中出现的次数，再按照原数组顺序遍历，遇到次数为 1 的偶数立即返回。
- 只需一次频次统计和一遍遍历即可满足题意。
- 时间复杂度: $O(n)$
- 空间复杂度: $O(n)$

## 代码
```python
class Solution:
    def firstUniqueEven(self, nums: list[int]) -> int:
        seen = Counter(nums)
        for n in nums:
            if n % 2 == 0:
                if seen[n] == 1:
                    return n
        return -1
```
