---
id: 136
title: Single Number
difficulty: Medium
tags: [bit-manipulation, array]
created: 2026-02-20
---

# 136. 只出现一次的数字

## 题目链接
https://leetcode.cn/problems/single-number/

## 题目描述

<p>给你一个 <strong>非空</strong> 整数数组 <code>nums</code> ，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。</p>

<p>你必须设计并实现线性时间复杂度的算法来解决此问题，且该算法只使用常量额外空间。</p>

<div class="original__bRMd">
<div>

<p><strong class="example">示例 1 ：</strong></p>

<div class="example-block">
<p><strong>输入：</strong>nums = [2,2,1]</p>

<p><strong>输出：</strong>1</p>
</div>

<p><strong class="example">示例 2 ：</strong></p>

<div class="example-block">
<p><strong>输入：</strong>nums = [4,1,2,1,2]</p>

<p><strong>输出：</strong>4</p>
</div>

<p><strong class="example">示例 3 ：</strong></p>

<div class="example-block">
<p><strong>输入：</strong>nums = [1]</p>

<p><strong>输出：</strong>1</p>
</div>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 3 * 10<sup>4</sup></code></li>
	<li><code>-3 * 10<sup>4</sup> &lt;= nums[i] &lt;= 3 * 10<sup>4</sup></code></li>
	<li>除了某个元素只出现一次以外，其余每个元素均出现两次。</li>
</ul>
</div>
</div>

## 解题思路

利用异或（XOR）的性质：`a ^ a = 0`，`a ^ 0 = a`，且满足交换律和结合律。将数组所有元素异或，成对出现的数两两抵消为 0，最终结果即为只出现一次的数。

- 时间复杂度: $O(n)$
- 空间复杂度: $O(1)$

## 相关专题
- [位运算](../../topics/bit-operations.md)

## 代码
```python
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return reduce(lambda x, y: x ^ y, nums)
```
