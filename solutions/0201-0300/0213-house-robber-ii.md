---
id: 213
title: House Robber II
difficulty: Medium
tags: [array, dynamic-programming]
created: 2026-02-21
---

# 213. 打家劫舍 II

## 题目链接
https://leetcode.cn/problems/house-robber-ii/

## 题目描述
<p>你是一个专业的小偷，计划偷窃沿街的房屋，每间房内都藏有一定的现金。这个地方所有的房屋都 <strong>围成一圈</strong> ，这意味着第一个房屋和最后一个房屋是紧挨着的。同时，相邻的房屋装有相互连通的防盗系统，<strong>如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警</strong> 。</p>

<p>给定一个代表每个房屋存放金额的非负整数数组，计算你 <strong>在不触动警报装置的情况下</strong> ，今晚能够偷窃到的最高金额。</p>

<p><strong>示例&nbsp;1：</strong></p>

<pre>
<strong>输入：</strong>nums = [2,3,2]
<strong>输出：</strong>3
<strong>解释：</strong>你不能先偷窃 1 号房屋（金额 = 2），然后偷窃 3 号房屋（金额 = 2）, 因为他们是相邻的。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,2,3,1]
<strong>输出：</strong>4
<strong>解释：</strong>你可以先偷窃 1 号房屋（金额 = 1），然后偷窃 3 号房屋（金额 = 3）。
&nbsp;    偷窃到的最高金额 = 1 + 3 = 4 。</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,2,3]
<strong>输出：</strong>3
</pre>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 100</code></li>
	<li><code>0 &lt;= nums[i] &lt;= 1000</code></li>
</ul>


## 解题思路

- 因为首尾相邻，拆成两段线性打家劫舍：`[0, n-2]` 和 `[1, n-1]`，分别求最大值。
- 线性子问题用一维 DP，转移为 `dp[i]=max(dp[i-1], dp[i-2]+nums[i])`。

- 时间复杂度: $O(n)$

- 空间复杂度: $O(n)$

## 代码
```cpp
class Solution {
public:
    int rob(vector<int>& nums) {
        int length = nums.size();
        if (nums.size() == 1) return nums[0];
        int result1 = _rob(nums, 0, length - 1);
        int result2 = _rob(nums, 1, length);
        return max(result1, result2);
    }
    
    int _rob(vector<int>& nums, int start, int stop) {
        // 从 start 到 stop 中取最大值, 左闭右开
        int length = stop - start;
        if (length == 0) return 0;
        vector<int> dp(length, 0);
        dp[0] = nums[start];
        if (length == 1) return dp[0];
        dp[1] =  max(nums[start], nums[start + 1]);
        if (length == 2) return dp[1];

        for (int i = 2; i < length; i++) {
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[start + i]);
        }
        return dp[length - 1];
    }
};
```
