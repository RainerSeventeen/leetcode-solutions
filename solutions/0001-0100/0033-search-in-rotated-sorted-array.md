---
id: 33
title: 搜索旋转排序数组
difficulty: Medium
tags: [array, binary-search]
created: 2026-02-20
---

# 33. 搜索旋转排序数组

## 题目链接
https://leetcode.cn/problems/search-in-rotated-sorted-array/

## 题目描述

<p>整数数组 <code>nums</code> 按升序排列，数组中的值 <strong>互不相同</strong> 。</p>

<p>在传递给函数之前，<code>nums</code> 在预先未知的某个下标 <code>k</code>（<code>0 &lt;= k &lt; nums.length</code>）上进行了 <strong>向左旋转</strong>，使数组变为 <code>[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]</code>（下标 <strong>从 0 开始</strong> 计数）。例如， <code>[0,1,2,4,5,6,7]</code> 下标&nbsp;<code>3</code>&nbsp;上向左旋转后可能变为&nbsp;<code>[4,5,6,7,0,1,2]</code> 。</p>

<p>给你 <strong>旋转后</strong> 的数组 <code>nums</code> 和一个整数 <code>target</code> ，如果 <code>nums</code> 中存在这个目标值 <code>target</code> ，则返回它的下标，否则返回&nbsp;<code>-1</code>&nbsp;。</p>

<p>你必须设计一个时间复杂度为 <code>O(log n)</code> 的算法解决此问题。</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [4,5,6,7,0,1,2], target = 0
<strong>输出：</strong>4
</pre>

<p><strong>示例&nbsp;2：</strong></p>

<pre>
<strong>输入：</strong>nums = [4,5,6,7,0,1,2], target = 3
<strong>输出：</strong>-1</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>nums = [1], target = 0
<strong>输出：</strong>-1
</pre>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 5000</code></li>
	<li><code>-10<sup>4</sup> &lt;= nums[i] &lt;= 10<sup>4</sup></code></li>
	<li><code>nums</code> 中的每个值都 <strong>独一无二</strong></li>
	<li>题目数据保证 <code>nums</code> 在预先未知的某个下标上进行了旋转</li>
	<li><code>-10<sup>4</sup> &lt;= target &lt;= 10<sup>4</sup></code></li>
</ul>

## 解题思路
拆成“两次二分”：

1) 先二分找到旋转点（最小值下标 `pivot`）。由于数组是“前半段都 > nums[-1]，后半段都 <= nums[-1]”，这个布尔条件对下标单调，因此可以用二分找第一个满足 `nums[mid] <= nums[-1]` 的位置。

2) 再根据 `target` 与 `nums[-1]` 的大小关系决定去哪个有序区间做普通二分：  
- `target <= nums[-1]` 则在 `[pivot, n)` 搜索；  
- 否则在 `[0, pivot)` 搜索。

每一步都是对单调区间做二分，整体仍是对数复杂度。

- 时间复杂度: $O(\log n)$
- 空间复杂度: $O(1)$

## 代码
```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        last = nums[-1]

        def find_split():    
            l, r = 0, n
            while l < r:
                mid = (l + r) // 2
                if nums[mid] <= last:
                    r = mid
                else:
                    l = mid + 1
            return l

        pivot = find_split()

        def bin_search(l, r):  # 等值二分查找
            while l < r:
                mid = (l + r) // 2
                if nums[mid] == target:
                    return mid
                if nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid
            return -1

        if target <= last:
            return bin_search(pivot, n)
        else:
            return bin_search(0, pivot)
```
