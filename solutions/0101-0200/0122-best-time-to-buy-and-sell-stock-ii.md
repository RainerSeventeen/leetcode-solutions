---
id: 122
title: Best Time to Buy and Sell Stock II
difficulty: Medium
tags: [greedy, array, dynamic-programming]
created: 2026-02-21
---

# 122. 买卖股票的最佳时机 II

## 题目链接
https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-ii/

## 题目描述
<p>给你一个整数数组 <code>prices</code> ，其中&nbsp;<code>prices[i]</code> 表示某支股票第 <code>i</code> 天的价格。</p>

<p>在每一天，你可以决定是否购买和/或出售股票。你在任何时候&nbsp;<strong>最多</strong>&nbsp;只能持有 <strong>一股</strong> 股票。然而，你可以在 <strong>同一天</strong> 多次买卖该股票，但要确保你持有的股票不超过一股。</p>

<p>返回 <em>你能获得的 <strong>最大</strong> 利润</em>&nbsp;。</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>prices = [7,1,5,3,6,4]
<strong>输出：</strong>7
<strong>解释：</strong>在第 2 天（股票价格 = 1）的时候买入，在第 3 天（股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5 - 1 = 4。
随后，在第 4 天（股票价格 = 3）的时候买入，在第 5 天（股票价格 = 6）的时候卖出, 这笔交易所能获得利润 = 6 - 3 = 3。
最大总利润为 4 + 3 = 7 。</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>prices = [1,2,3,4,5]
<strong>输出：</strong>4
<strong>解释：</strong>在第 1 天（股票价格 = 1）的时候买入，在第 5 天 （股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5 - 1 = 4。
最大总利润为 4 。</pre>

<p><strong>示例&nbsp;3：</strong></p>

<pre>
<strong>输入：</strong>prices = [7,6,4,3,1]
<strong>输出：</strong>0
<strong>解释：</strong>在这种情况下, 交易无法获得正利润，所以不参与交易可以获得最大利润，最大利润为 0。</pre>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= prices.length &lt;= 3 * 10<sup>4</sup></code></li>
	<li><code>0 &lt;= prices[i] &lt;= 10<sup>4</sup></code></li>
</ul>


## 解题思路

- 设 `dp[i][0]` 为第 `i` 天不持股利润，`dp[i][1]` 为持股利润。
- 每天在“沿用昨天状态”和“今天买/卖”之间取最大，允许进行多次交易。

- 时间复杂度: $O(n)$

- 空间复杂度: $O(n)$

## 代码
```cpp
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        // dp
        vector<vector<int>> dp(prices.size(), vector<int>(2,0));
        dp[0][1] = -prices[0]; // 表示买入
        for (int i = 1; i < prices.size(); i++) {
            // 没有持有的状态
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i]);
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i]); 
        }
        return dp[prices.size() -1][0];
    }
};
```
