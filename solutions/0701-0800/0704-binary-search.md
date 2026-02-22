---
id: 704
title: Binary Search
difficulty: Easy
tags: [array, binary-search]
created: 2026-02-21
---

# 704. 二分查找

## 题目链接
https://leetcode.cn/problems/binary-search/

## 题目描述
<p>给定一个&nbsp;<code>n</code>&nbsp;个元素有序的（升序）整型数组&nbsp;<code>nums</code> 和一个目标值&nbsp;<code>target</code> &nbsp;，写一个函数搜索&nbsp;<code>nums</code>&nbsp;中的 <code>target</code>，如果&nbsp;<code>target</code> 存在返回下标，否则返回 <code>-1</code>。</p>

<p>你必须编写一个具有 <code>O(log n)</code> 时间复杂度的算法。</p>

<p><br />
<strong>示例 1:</strong></p>

<pre>
<strong>输入:</strong> <code>nums</code> = [-1,0,3,5,9,12], <code>target</code> = 9
<strong>输出:</strong> 4
<strong>解释:</strong> 9 出现在 <code>nums</code> 中并且下标为 4
</pre>

<p><strong>示例&nbsp;2:</strong></p>

<pre>
<strong>输入:</strong> <code>nums</code> = [-1,0,3,5,9,12], <code>target</code> = 2
<strong>输出:</strong> -1
<strong>解释:</strong> 2 不存在 <code>nums</code> 中因此返回 -1
</pre>

<p><strong>提示：</strong></p>

<ol>
	<li>你可以假设 <code>nums</code>&nbsp;中的所有元素是不重复的。</li>
	<li><code>n</code>&nbsp;将在&nbsp;<code>[1, 10000]</code>之间。</li>
	<li><code>nums</code>&nbsp;的每个元素都将在&nbsp;<code>[-9999, 9999]</code>之间。</li>
</ol>


## 解题思路

在有序数组上维护闭区间 `[left, right]`，每轮取中点与目标值比较。
若中点值更小就收缩左边界，否则收缩右边界；相等时直接返回下标。
区间为空仍未命中则返回 `-1`。
- 时间复杂度: $O(\log n)$
- 空间复杂度: $O(1)$

## 相关专题
- [二分算法](../../topics/binary-search.md)

## 代码
```cpp
class Solution {
public:
    int search(vector<int>& nums, int target) {
        int left = 0;
        int right = nums.size() - 1;
        int middle = 0;
        int ret = 0;

        while(left <= right){
            middle = left + (right - left) / 2;
            if (nums[middle] < target){
                left = middle + 1;
            } else if (nums[middle] > target){
                right = middle - 1;
            } else {
                return middle;
            }
        }
        return -1;
    }
};
```
