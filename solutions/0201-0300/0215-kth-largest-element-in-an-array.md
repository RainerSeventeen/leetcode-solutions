---
id: 215
title: Kth Largest Element in an Array
difficulty: Medium
tags: [array, divide-and-conquer, quickselect, sorting, heap-priority-queue]
created: 2026-02-20
---

# 215. 数组中的第K个最大元素

## 题目链接
https://leetcode.cn/problems/kth-largest-element-in-an-array/

## 题目描述
<p>给定整数数组 <code>nums</code> 和整数 <code>k</code>，请返回数组中第 <code><strong>k</strong></code> 个最大的元素。</p>

<p>请注意，你需要找的是数组排序后的第 <code>k</code> 个最大的元素，而不是第 <code>k</code> 个不同的元素。</p>

<p>你必须设计并实现时间复杂度为 <code>O(n)</code> 的算法解决此问题。</p>

<p><strong>示例 1:</strong></p>

<pre>
<strong>输入:</strong> <code>[3,2,1,5,6,4],</code> k = 2
<strong>输出:</strong> 5
</pre>

<p><strong>示例&nbsp;2:</strong></p>

<pre>
<strong>输入:</strong> <code>[3,2,3,1,2,4,5,5,6], </code>k = 4
<strong>输出:</strong> 4</pre>

<p><strong>提示： </strong></p>

<ul>
	<li><code>1 &lt;= k &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>-10<sup>4</sup>&nbsp;&lt;= nums[i] &lt;= 10<sup>4</sup></code></li>
</ul>


## 解题思路

使用最小堆进行操作

**注意：应该学会优先级队列的底层操作逻辑（堆，一种基于完全二叉树的数据结构）**

- 时间复杂度: $O(n \log k)$
- 空间复杂度: $O(k)$
## 相关专题
- [常用数据结构](../../topics/common-data-structures.md)

## 代码
```python
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # 最小堆，使用 heapq 实现，默认就是最小堆
        heap = []
        for x in nums:
            heapq.heappush(heap, x)
            if len(heap) > k:
                heapq.heappop(heap)
        return heap[0]
```
