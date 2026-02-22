---
id: 35
title: Search Insert Position
difficulty: Easy
tags: [array, binary-search]
created: 2026-02-21
---

# 35. 搜索插入位置

## 题目链接
https://leetcode.cn/problems/search-insert-position/

## 题目描述
<p>给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。</p>

<p>请必须使用时间复杂度为 <code>O(log n)</code> 的算法。</p>

<p><strong>示例 1:</strong></p>

<pre>
<strong>输入:</strong> nums = [1,3,5,6], target = 5
<strong>输出:</strong> 2
</pre>

<p><strong>示例&nbsp;2:</strong></p>

<pre>
<strong>输入:</strong> nums = [1,3,5,6], target = 2
<strong>输出:</strong> 1
</pre>

<p><strong>示例 3:</strong></p>

<pre>
<strong>输入:</strong> nums = [1,3,5,6], target = 7
<strong>输出:</strong> 4
</pre>

<p><strong>提示:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>4</sup></code></li>
	<li><code>-10<sup>4</sup> &lt;= nums[i] &lt;= 10<sup>4</sup></code></li>
	<li><code>nums</code> 为&nbsp;<strong>无重复元素&nbsp;</strong>的&nbsp;<strong>升序&nbsp;</strong>排列数组</li>
	<li><code>-10<sup>4</sup> &lt;= target &lt;= 10<sup>4</sup></code></li>
</ul>


## 解题思路

数组有序且要求对数复杂度，直接使用二分查找。  
若命中目标值直接返回下标；若未命中，循环结束时 `right` 停在最后一个小于 `target` 的位置。  
因此插入位置就是 `right + 1`（等价于 `left`）。  
- 时间复杂度: $O(\log n)$
- 空间复杂度: $O(1)$

## 相关专题
- [二分算法](../../topics/binary-search.md)

## 代码
```cpp
class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        int left = 0;
        int right = nums.size() -1 ;
        while(left <= right){
        int middle = left + ((right - left) >> 1);
            if (nums[middle] < target)
                left = middle + 1;
            else if (nums[middle] > target)
                right = middle - 1;
            else 
                return middle;
        }
        return right + 1 ;
    }
};
```
