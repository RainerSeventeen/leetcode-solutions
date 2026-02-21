---
id: 209
title: Minimum Size Subarray Sum
difficulty: Medium
tags: [array, binary-search, prefix-sum, sliding-window]
created: 2026-02-21
---

# 209. 长度最小的子数组

## 题目链接
https://leetcode.cn/problems/minimum-size-subarray-sum/

## 题目描述
<p>给定一个含有&nbsp;<code>n</code><strong>&nbsp;</strong>个正整数的数组和一个正整数 <code>target</code><strong> 。</strong></p>

<p>找出该数组中满足其总和大于等于<strong> </strong><code>target</code><strong> </strong>的长度最小的 <strong><span data-keyword="subarray-nonempty">子数组</span></strong>&nbsp;<code>[nums<sub>l</sub>, nums<sub>l+1</sub>, ..., nums<sub>r-1</sub>, nums<sub>r</sub>]</code> ，并返回其长度<strong>。</strong>如果不存在符合条件的子数组，返回 <code>0</code> 。</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>target = 7, nums = [2,3,1,2,4,3]
<strong>输出：</strong>2
<strong>解释：</strong>子数组&nbsp;<code>[4,3]</code>&nbsp;是该条件下的长度最小的子数组。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>target = 4, nums = [1,4,4]
<strong>输出：</strong>1
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>target = 11, nums = [1,1,1,1,1,1,1,1]
<strong>输出：</strong>0
</pre>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= target &lt;= 10<sup>9</sup></code></li>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>4</sup></code></li>
</ul>

<p><strong>进阶：</strong></p>

<ul>
	<li>如果你已经实现<em> </em><code>O(n)</code> 时间复杂度的解法, 请尝试设计一个 <code>O(n log(n))</code> 时间复杂度的解法。</li>
</ul>


## 解题思路

同样用滑动窗口，右指针不断加入元素并维护当前窗口和 `sum`。
当 `sum >= target` 时，持续收缩左边界并更新最短长度，直到不满足条件。
遍历后若最短长度未更新则返回 0，否则返回记录值。
- 时间复杂度: $O(n)$
- 空间复杂度: $O(1)$

## 代码
```cpp
#include<climits>
class Solution {
public:

    int minSubArrayLen(int target, vector<int>& nums) {
        int i = 0;
        int sum = 0; // 累加器
        int result = INT_MAX;        
        for (int j = 0; j < nums.size(); j++){
            sum += nums[j];
                while (sum >= target){
                    int now = (j - i + 1);
                    result = result < now ? result : now;
                    sum -= nums[i++];
                }

        }
        if (result == INT_MAX)
            return 0;
        return result;
    }
};
```
