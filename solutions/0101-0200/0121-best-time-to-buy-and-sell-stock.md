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
一次遍历维护“历史最低价”和“当前能获得的最大利润”。

遍历价格 `price`：

- 维护 `min_price` 为到当前天为止出现过的最低价格（买入成本）
- 以今天卖出时的利润为 `price - min_price`，用它更新答案 `ans`
- 然后更新 `min_price = min(min_price, price)`（注意更新顺序不影响正确性，只要同一天不能先卖后买即可）

不变量：

- `min_price` 始终来自当前索引之前（含当前）的最小值，因此 `price - min_price` 表示“在今天卖出且买在今天之前或今天”的最大可能利润。

边界：

- 价格单调下降时利润为 0（不交易）。

- 时间复杂度: $O(n)$
- 空间复杂度: $O(1)$

## 代码
```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_p = float('inf')
        ret = 0
        for p in prices:
            ret = max(p - min_p, ret)
            min_p = min(p, min_p)

        return ret
```
