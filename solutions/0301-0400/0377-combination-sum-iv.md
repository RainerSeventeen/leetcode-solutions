---
id: 377
title: Combination Sum IV
difficulty: Medium
tags: [array, dynamic-programming]
created: 2026-02-21
---

# 377. 组合总和 Ⅳ

## 题目链接
https://leetcode.cn/problems/combination-sum-iv/

## 题目描述
<p>给你一个由 <strong>不同</strong> 整数组成的数组 <code>nums</code> ，和一个目标整数 <code>target</code> 。请你从 <code>nums</code> 中找出并返回总和为 <code>target</code> 的元素排列的个数。</p>

<p>题目数据保证答案符合 32 位整数范围。</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,2,3], target = 4
<strong>输出：</strong>7
<strong>解释：</strong>
所有可能的组合为：
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)
请注意，顺序不同的序列被视作不同的组合。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [9], target = 3
<strong>输出：</strong>0
</pre>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 200</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 1000</code></li>
	<li><code>nums</code> 中的所有元素 <strong>互不相同</strong></li>
	<li><code>1 &lt;= target &lt;= 1000</code></li>
</ul>

<p><strong>进阶：</strong>如果给定的数组中含有负数会发生什么？问题会产生何种变化？如果允许负数出现，需要向题目中添加哪些限制条件？</p>


## 解题思路

- 用完全背包做排列计数，`dp[j]` 表示和为 `j` 的方案数。
- 外层遍历目标和、内层遍历数字，保证不同顺序会被当作不同方案统计。

- 时间复杂度: $O(target \times n)$

- 空间复杂度: $O(target)$

## 代码
```cpp
class Solution {
public:
    int combinationSum4(vector<int>& nums, int target) {
        // 完全背包
        vector<unsigned int> dp(target + 1, 0);
        dp[0] = 1;
        for (int j = 1; j <= target; j++) {
            for (int i = 0; i < nums.size(); i++) {
                if (nums[i] <= j)
                    dp[j] += dp[j - nums[i]];
            }
        }
        return dp[target];
    }
};
```
