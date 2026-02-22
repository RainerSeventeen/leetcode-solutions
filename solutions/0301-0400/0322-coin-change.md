---
id: 322
title: Coin Change
difficulty: Medium
tags: [breadth-first-search, array, dynamic-programming]
created: 2026-02-20
---

# 322. 零钱兑换

## 题目链接
https://leetcode.cn/problems/coin-change/

## 题目描述

<p>给你一个整数数组 <code>coins</code> ，表示不同面额的硬币；以及一个整数 <code>amount</code> ，表示总金额。</p>

<p>计算并返回可以凑成总金额所需的 <strong>最少的硬币个数</strong> 。如果没有任何一种硬币组合能组成总金额，返回&nbsp;<code>-1</code> 。</p>

<p>你可以认为每种硬币的数量是无限的。</p>

<p><strong>示例&nbsp;1：</strong></p>

<pre>
<strong>输入：</strong>coins = <code>[1, 2, 5]</code>, amount = <code>11</code>
<strong>输出：</strong><code>3</code> 
<strong>解释：</strong>11 = 5 + 5 + 1</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>coins = <code>[2]</code>, amount = <code>3</code>
<strong>输出：</strong>-1</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>coins = [1], amount = 0
<strong>输出：</strong>0
</pre>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= coins.length &lt;= 12</code></li>
	<li><code>1 &lt;= coins[i] &lt;= 2<sup>31</sup> - 1</code></li>
	<li><code>0 &lt;= amount &lt;= 10<sup>4</sup></code></li>
</ul>

## 解题思路

完全背包 DP。`dp[j]` 表示凑出金额 `j` 所需的最少硬币数，初始化为正无穷（不可达），`dp[0] = 0`。

外层枚举硬币，内层正序遍历金额（完全背包允许重复使用）。状态转移：`dp[j] = min(dp[j], dp[j - c] + 1)`。最终 `dp[amount]` 若仍为正无穷则返回 -1。

- 时间复杂度: $O(amount \cdot n)$
- 空间复杂度: $O(amount)$

其中 `n` 为硬币种类数。

## 相关专题
- [动态规划](../../topics/dynamic-programming.md)

## 代码
```python
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0 # 初始化为0
        # 完全背包，先物品后背包，正序遍历
        for c in coins:
            for j in range(c, amount + 1):
                dp[j] = min(dp[j], dp[j - c] + 1)
        return dp[amount] if dp[amount] != float('inf') else -1
```
