---
id: 188
title: Best Time to Buy and Sell Stock IV
difficulty: Hard
tags: [array, dynamic-programming]
created: 2026-02-21
---

# 188. 买卖股票的最佳时机 IV

## 题目链接
https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-iv/

## 题目描述
<p>给你一个整数数组&nbsp;<code>prices</code> 和一个整数 <code>k</code> ，其中 <code>prices[i]</code> 是某支给定的股票在第 <code>i</code><em> </em>天的价格。</p>

<p>设计一个算法来计算你所能获取的最大利润。你最多可以完成 <code>k</code> 笔交易。也就是说，你最多可以买 <code>k</code> 次，卖 <code>k</code> 次。</p>

<p><strong>注意：</strong>你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。</p>

<p><strong class="example">示例 1：</strong></p>

<pre>
<strong>输入：</strong>k = 2, prices = [2,4,1]
<strong>输出：</strong>2
<strong>解释：</strong>在第 1 天 (股票价格 = 2) 的时候买入，在第 2 天 (股票价格 = 4) 的时候卖出，这笔交易所能获得利润 = 4-2 = 2 。</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<strong>输入：</strong>k = 2, prices = [3,2,6,5,0,3]
<strong>输出：</strong>7
<strong>解释：</strong>在第 2 天 (股票价格 = 2) 的时候买入，在第 3 天 (股票价格 = 6) 的时候卖出, 这笔交易所能获得利润 = 6-2 = 4 。
     随后，在第 5 天 (股票价格 = 0) 的时候买入，在第 6 天 (股票价格 = 3) 的时候卖出, 这笔交易所能获得利润 = 3-0 = 3 。</pre>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= k &lt;= 100</code></li>
	<li><code>1 &lt;= prices.length &lt;= 1000</code></li>
	<li><code>0 &lt;= prices[i] &lt;= 1000</code></li>
</ul>


## 解题思路

- 把一次交易拆成“买入状态 + 卖出状态”，共 `2k+1` 个状态，奇数为持有、偶数为不持有。
- 每天按交易次数更新对应买卖状态，取“延续昨天”与“今天买/卖”两种选择的最大值。

- 时间复杂度: $O(n \times k)$

- 空间复杂度: $O(n \times k)$

## 代码
```cpp
class Solution {
public:
    int maxProfit(int k, vector<int>& prices) {
        // 0无 1第一次持有 2第一次卖出 3第二次持有 4第二次卖出...
        // 奇数持有， 偶数卖出
        vector<vector<int>> dp(prices.size(), vector<int> (2 * k + 1, 0));
        // 初始化
        for (int j = 1; j <= k; j++) {
            dp[0][2 * j - 1] = - prices[0]; 
        }
        for (int i = 1; i < prices.size(); i++) {
            for (int j = 1; j <= k; j++) {
                dp[i][2 * j - 1] = max(dp[i - 1][2 * j - 1], dp[i - 1][2 * j - 2] - prices[i]);
                dp[i][2 * j] = max(dp[i - 1][2 * j], dp[i - 1][2 * j - 1] + prices[i]);
            }
        }
        return dp[prices.size() - 1][2 * k];

    }
};
```
