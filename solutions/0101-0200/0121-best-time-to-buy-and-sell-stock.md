---
id: 121
title: Best Time to Buy and Sell Stock
difficulty: Easy
tags: [array, dynamic-programming]
created: 2026-02-20
---

# 121. 买卖股票的最佳时机

## 题目链接
https://leetcode.cn/problems/best-time-to-buy-and-sell-stock/

## 题目描述
<p>给定一个数组 <code>prices</code> ，它的第 <code>i</code> 个元素 <code>prices[i]</code> 表示一支给定股票第 <code>i</code> 天的价格。</p>

<p>你只能选择 <strong>某一天</strong> 买入这只股票，并选择在 <strong>未来的某一个不同的日子</strong> 卖出该股票。设计一个算法来计算你所能获取的最大利润。</p>

<p>返回你可以从这笔交易中获取的最大利润。如果你不能获取任何利润，返回 <code>0</code> 。</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>[7,1,5,3,6,4]
<strong>输出：</strong>5
<strong>解释：</strong>在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格；同时，你不能在买入前卖出股票。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>prices = [7,6,4,3,1]
<strong>输出：</strong>0
<strong>解释：</strong>在这种情况下, 没有交易完成, 所以最大利润为 0。
</pre>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 <= prices.length <= 10<sup>5</sup></code></li>
	<li><code>0 <= prices[i] <= 10<sup>4</sup></code></li>
</ul>


## 解题思路

遍历价格数组时维护两个状态：

- `hold`：当前持有股票时的最大现金。
- `cash`：当前不持有股票时的最大现金。

本题只允许一次交易，所以 `hold` 只能来自“今天买入”：`hold = max(hold, -price)`；
`cash = max(cash, hold + price)` 表示今天卖出或不操作。

- 时间复杂度: `O(n)`
- 空间复杂度: `O(1)`

## 代码
```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        hold = -prices[0]
        cash = 0
        for p in prices[1:]:
            cash = max(cash, hold + p)
            hold = max(hold, -p)
        return cash
```
