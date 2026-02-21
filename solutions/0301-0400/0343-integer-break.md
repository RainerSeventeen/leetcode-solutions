---
id: 343
title: Integer Break
difficulty: Medium
tags: [math, dynamic-programming]
created: 2026-02-21
---

# 343. 整数拆分

## 题目链接
https://leetcode.cn/problems/integer-break/

## 题目描述
<p>给定一个正整数&nbsp;<code>n</code>&nbsp;，将其拆分为 <code>k</code> 个 <strong>正整数</strong> 的和（&nbsp;<code>k &gt;= 2</code>&nbsp;），并使这些整数的乘积最大化。</p>

<p>返回 <em>你可以获得的最大乘积</em>&nbsp;。</p>

<p><strong>示例 1:</strong></p>

<pre>
<strong>输入: </strong>n = 2
<strong>输出: </strong>1
<strong>解释: </strong>2 = 1 + 1, 1 × 1 = 1。</pre>

<p><strong>示例&nbsp;2:</strong></p>

<pre>
<strong>输入: </strong>n = 10
<strong>输出: </strong>36
<strong>解释: </strong>10 = 3 + 3 + 4, 3 ×&nbsp;3 ×&nbsp;4 = 36。</pre>

<p><strong>提示:</strong></p>

<ul>
	<li><code>2 &lt;= n &lt;= 58</code></li>
</ul>


## 解题思路

- 设 `dp[i]` 为整数 `i` 拆分后的最大乘积，初始 `dp[2]=1`。
- 枚举第一段 `j`，比较“只拆一次 `j*(i-j)`”和“继续拆 `j*dp[i-j]`”两种情况。

- 时间复杂度: $O(n^2)$

- 空间复杂度: $O(n)$

## 代码
```cpp
class Solution {
public:
    int integerBreak(int n) {
        // 动态规划
        // dp 代表 i 个数值的最大乘
        vector<int> dp(n + 1 ,0);
        dp[2] = 1;

        for (int i = 3; i <= n; i++) {
            // 计算整个dp
            for (int j = 1; j <= i / 2; j++) {
                // 单个数值的遍历
                dp[i] = max(dp[i], j * (i - j));
                dp[i] = max(dp[i], j * dp[i - j]);
            }
        }
        return dp[n];
    }
};
```
