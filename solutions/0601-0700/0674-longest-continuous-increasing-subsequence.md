---
id: 674
title: Longest Continuous Increasing Subsequence
difficulty: Easy
tags: [array]
created: 2026-02-21
---

# 674. 最长连续递增序列

## 题目链接
https://leetcode.cn/problems/longest-continuous-increasing-subsequence/

## 题目描述
<p>给定一个未经排序的整数数组，找到最长且<strong> 连续递增的子序列</strong>，并返回该序列的长度。</p>

<p><strong>连续递增的子序列</strong> 可以由两个下标 <code>l</code> 和 <code>r</code>（<code>l < r</code>）确定，如果对于每个 <code>l <= i < r</code>，都有 <code>nums[i] < nums[i + 1]</code> ，那么子序列 <code>[nums[l], nums[l + 1], ..., nums[r - 1], nums[r]]</code> 就是连续递增子序列。</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,3,5,4,7]
<strong>输出：</strong>3
<strong>解释：</strong>最长连续递增序列是 [1,3,5], 长度为3。
尽管 [1,3,5,7] 也是升序的子序列, 但它不是连续的，因为 5 和 7 在原数组里被 4 隔开。 
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [2,2,2,2,2]
<strong>输出：</strong>1
<strong>解释：</strong>最长连续递增序列是 [2], 长度为1。
</pre>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 <= nums.length <= 10<sup>4</sup></code></li>
	<li><code>-10<sup>9</sup> <= nums[i] <= 10<sup>9</sup></code></li>
</ul>


## 解题思路

- 定义 `dp[i]` 为以 `nums[i]` 结尾的连续递增子数组长度，初始都为 1。
- 若 `nums[i] > nums[i-1]` 则 `dp[i]=dp[i-1]+1`，遍历时维护全局最大值。

- 时间复杂度: $O(n)$

- 空间复杂度: $O(n)$

## 代码
```cpp
class Solution {
public:
    int findLengthOfLCIS(vector<int>& nums) {
        vector<int> dp(nums.size(), 1);
        int ret = 1;
        for (int i = 1; i < nums.size(); i++) {
            if (nums[i] > nums[i - 1]) {
                dp[i] = dp[i - 1] + 1;
            }
            ret = max(ret,  dp[i]);
        }
        return ret;
    }
};
```
