---
id: 169
title: Majority Element
difficulty: Easy
tags: [array, hash-table, divide-and-conquer, counting, sorting]
created: 2026-02-20
---

# 169. 多数元素

## 题目链接
https://leetcode.cn/problems/majority-element/

## 题目描述
<p>给定一个大小为 <code>n</code><em> </em>的数组&nbsp;<code>nums</code> ，返回其中的多数元素。多数元素是指在数组中出现次数 <strong>大于</strong>&nbsp;<code>⌊ n/2 ⌋</code>&nbsp;的元素。</p>

<p>你可以假设数组是非空的，并且给定的数组总是存在多数元素。</p>

<p><strong>示例&nbsp;1：</strong></p>

<pre>
<strong>输入：</strong>nums = [3,2,3]
<strong>输出：</strong>3</pre>

<p><strong>示例&nbsp;2：</strong></p>

<pre>
<strong>输入：</strong>nums = [2,2,1,1,1,2,2]
<strong>输出：</strong>2
</pre>

<strong>提示：</strong>

<ul>
	<li><code>n == nums.length</code></li>
	<li><code>1 &lt;= n &lt;= 5 * 10<sup>4</sup></code></li>
	<li><code>-10<sup>9</sup> &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
	<li>输入保证数组中一定有一个多数元素。</li>
</ul>

<p><strong>进阶：</strong>尝试设计时间复杂度为 O(n)、空间复杂度为 O(1) 的算法解决此问题。</p>


## 解题思路

使用投票法，只要是候选人他的票数一定超过一半，很巧妙的方法求众数

或者也可以使用排序算法（应该都能想到把）

- 时间复杂度: $O(n)$
- 空间复杂度: $O(1)$
## 代码
```python
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        can = None
        count = 0
        for n in nums:
            if count == 0:
                can = n # 换人和改票数一定要绑定
                count = 1
            elif n == can:
                count += 1
            else:
                count -= 1
        return can
```
