---
id: 1019
title: Squares of a Sorted Array
difficulty: Easy
tags: [array, two-pointers, sorting]
created: 2026-02-21
---

# 1019. 有序数组的平方

## 题目链接
https://leetcode.cn/problems/squares-of-a-sorted-array/

## 题目描述
<p>给你一个按 <strong>非递减顺序</strong> 排序的整数数组 <code>nums</code>，返回 <strong>每个数字的平方</strong> 组成的新数组，要求也按 <strong>非递减顺序</strong> 排序。</p>

<ul>
</ul>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [-4,-1,0,3,10]
<strong>输出：</strong>[0,1,9,16,100]
<strong>解释：</strong>平方后，数组变为 [16,1,0,9,100]
排序后，数组变为 [0,1,9,16,100]</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [-7,-3,2,3,11]
<strong>输出：</strong>[4,9,9,49,121]
</pre>

<p><strong>提示：</strong></p>

<ul>
	<li><code><span>1 &lt;= nums.length &lt;= </span>10<sup>4</sup></code></li>
	<li><code>-10<sup>4</sup> &lt;= nums[i] &lt;= 10<sup>4</sup></code></li>
	<li><code>nums</code> 已按 <strong>非递减顺序</strong> 排序</li>
</ul>

<p><strong>进阶：</strong></p>

<ul>
	<li>请你设计时间复杂度为 <code>O(n)</code> 的算法解决本问题</li>
</ul>


## 解题思路

有序数组两端绝对值最大，平方后也最大，因此用双指针从两端向中间比较。
每次把较大平方值放到结果数组末尾，并向前移动结果写入位置。
这样可在线性时间内直接得到非递减结果。
- 时间复杂度: $O(n)$
- 空间复杂度: $O(n)$

## 代码
```cpp
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> sortedSquares(vector<int>& nums) {
        int len = nums.size();
        vector<int> ret(len); // 直接分配好空间
        int left = 0;
        int right = len - 1;
        int index = len - 1;

        while (left <= right) {
            int left2 = nums[left] * nums[left];
            int right2 = nums[right] * nums[right];
            if (left2 < right2) {
                ret[index--] = right2;
                right--;
            } else {
                ret[index--] = left2;
                left++;
            }
        }
        return ret;
    }
};
```
