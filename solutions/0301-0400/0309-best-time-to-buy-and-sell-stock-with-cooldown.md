---
id: 309
title: 买卖股票的最佳时机含冷冻期
difficulty: Medium
tags: [array, dynamic-programming]
created: 2026-02-20
---

# 309. 买卖股票的最佳时机含冷冻期

## 题目链接
https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-with-cooldown/

## 题目描述
暂无（需要从LeetCode获取）

## 解题思路
冷冻期的限制是：**卖出后的下一天不能买入**。用状态机 DP 把“当天结束时”的状态分清楚，就能 `O(1)` 空间滚动。

定义 3 个状态（都表示处理到当天价格后，能获得的最大利润）：

- `hold`：手里持有股票（可能是之前买入）。
- `frozen`：当天刚卖出股票，因此明天处于冷冻期。
- `free`：手里没有股票，且不在冷冻期（可以买）。

设当天价格为 `p`，状态转移：

- `new_frozen = hold + p`：把之前持有的卖掉，进入冷冻期。
- `new_free = max(free, frozen)`：今天不持股；要么本来就自由，要么昨天卖出冷冻期结束变自由。
- `new_hold = max(hold, free - p)`：今天持股；要么继续持有，要么从自由状态买入（不能从 `frozen` 买）。

初始化：第 0 天 `free = 0`，`hold = -prices[0]`（买入），`frozen = 0`。答案是最后不持股的最大值：`max(free, frozen)`。

边界情况：只有 1 天价格时，无法完成一次买卖，结果为 0。

- 时间复杂度: $O(n)$
- 空间复杂度: $O(1)$

## 代码
```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        free, hold, frozen = 0, -prices[0], 0
        for p in prices[1:]:
            new_frozen = hold + p
            new_free = max(free, frozen)
            new_hold = max(hold, free - p)
            free, hold, frozen = new_free, new_hold, new_frozen
        return max(free, frozen)
```
