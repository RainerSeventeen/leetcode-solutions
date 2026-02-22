---
id: 1
title: Two Sum
difficulty: Easy
tags: [array, hash-table]
created: 2026-02-20
---

# 1. 两数之和

## 题目链接
https://leetcode.cn/problems/two-sum/

## 题目描述
<p>给定一个整数数组 <code>nums</code>&nbsp;和一个整数目标值 <code>target</code>，请你在该数组中找出 <strong>和为目标值 </strong><em><code>target</code></em>&nbsp; 的那&nbsp;<strong>两个</strong>&nbsp;整数，并返回它们的数组下标。</p>

<p>你可以假设每种输入只会对应一个答案，并且你不能使用两次相同的元素。</p>

<p>你可以按任意顺序返回答案。</p>

<p><strong class="example">示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [2,7,11,15], target = 9
<strong>输出：</strong>[0,1]
<strong>解释：</strong>因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。
</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [3,2,4], target = 6
<strong>输出：</strong>[1,2]
</pre>

<p><strong class="example">示例 3：</strong></p>

<pre>
<strong>输入：</strong>nums = [3,3], target = 6
<strong>输出：</strong>[0,1]
</pre>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 &lt;= nums.length &lt;= 10<sup>4</sup></code></li>
	<li><code>-10<sup>9</sup> &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
	<li><code>-10<sup>9</sup> &lt;= target &lt;= 10<sup>9</sup></code></li>
	<li><strong>只会存在一个有效答案</strong></li>
</ul>

<p><strong>进阶：</strong>你可以想出一个时间复杂度小于 <code>O(n<sup>2</sup>)</code> 的算法吗？</p>



## 解题思路

用哈希表记录「已经遍历过的数值 -> 下标」。遍历到 `nums[i]` 时先查找补数 `target - nums[i]`：

- 若补数已在表中，直接返回两者下标；
- 否则把 `nums[i]` 写入表中继续。

之所以先查再写，是为了保证不会把同一个元素用两次（当前元素尚未入表）。

- 时间复杂度: $O(n)$
- 空间复杂度: $O(n)$

## 相关专题
- [常用数据结构](../../topics/common-data-structures.md)

## 代码
```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s = dict()
        n = len(nums)
        ret = [] * n
        for i in range(n):
            if target - nums[i] not in s:
                s[nums[i]] = i
            else:
                return [i, s[target - nums[i]]]
```
