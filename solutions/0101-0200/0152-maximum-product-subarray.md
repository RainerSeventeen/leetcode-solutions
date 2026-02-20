---
id: 152
title: Maximum Product Subarray
difficulty: Medium
tags: [array, dynamic-programming]
created: 2026-02-20
---

# 152. 乘积最大子数组

## 题目链接
https://leetcode.cn/problems/maximum-product-subarray/

## 题目描述
<p>给你一个整数数组 <code>nums</code>&nbsp;，请你找出数组中乘积最大的非空连续 <span data-keyword="subarray-nonempty">子数组</span>（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。</p>

<p>测试用例的答案是一个&nbsp;<strong>32-位</strong> 整数。</p>

<p><strong>请注意</strong>，一个只包含一个元素的数组的乘积是这个元素的值。</p>

<p><strong class="example">示例 1:</strong></p>

<pre>
<strong>输入:</strong> nums = [2,3,-2,4]
<strong>输出:</strong> <code>6</code>
<strong>解释:</strong>&nbsp;子数组 [2,3] 有最大乘积 6。
</pre>

<p><strong class="example">示例 2:</strong></p>

<pre>
<strong>输入:</strong> nums = [-2,0,-1]
<strong>输出:</strong> 0
<strong>解释:</strong>&nbsp;结果不能为 2, 因为 [-2,-1] 不是子数组。</pre>

<p><strong>提示:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 2 * 10<sup>4</sup></code></li>
	<li><code>-10 &lt;= nums[i] &lt;= 10</code></li>
	<li><code>nums</code> 的任何子数组的乘积都 <strong>保证</strong>&nbsp;是一个 <strong>32-位</strong> 整数</li>
</ul>


## 解题思路

注意要同时维护最大值和最小值，因为负数可以乘以负数来逆袭

这里用的是 `O(1)` 复杂度的，但是实际上一般是写完 `O(n)` 再优化为滚动数组的

- 时间复杂度: $O(n)$
- 空间复杂度: $O(1)$
## 代码
```python
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        lastmin = nums[0]
        lastmax = nums[0]
        ret = nums[0]

        for i in range(1, len(nums)):
            x = nums[i]
            tmp_min = min(x, lastmax * x, lastmin * x)
            lastmax = max(x, lastmax * x, lastmin * x)
            lastmin = tmp_min
            ret = max(ret, lastmax)

        return ret
```
