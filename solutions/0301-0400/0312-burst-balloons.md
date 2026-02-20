---
id: 312
title: 戳气球
difficulty: Medium
tags: [array, dynamic-programming]
created: 2026-02-20
---

# 312. 戳气球

## 题目链接
https://leetcode.cn/problems/burst-balloons/

## 题目描述
暂无（需要从LeetCode获取）

## 解题思路
这是典型的 **区间 DP**：直接按“先戳哪个”会导致左右边界不断变化，很难定义状态；反过来按“最后戳哪个”就能固定边界。

做两个关键处理：

- 在原数组两端各补一个虚拟气球 `1`，得到 `a = [1] + nums + [1]`，这样每次戳 `k` 的收益统一为 `a[l] * a[k] * a[r]`。
- 定义 `dp[l][r]` 表示**开区间** `(l, r)` 内的气球全部戳完，能获得的最大金币数（`l` 和 `r` 位置的气球不戳，作为边界）。

状态转移：假设 `(l, r)` 中最后一个被戳的是 `k`（`l < k < r`），那么在戳 `k` 之前，`(l, k)` 与 `(k, r)` 两个子区间都已被完全戳完：

`dp[l][r] = max(dp[l][k] + dp[k][r] + a[l] * a[k] * a[r])`

计算顺序：区间长度从小到大（代码里用 `l` 逆序、`r` 正序保证子问题已算好）。

边界：当 `r <= l + 1`（开区间里没有气球）时，`dp[l][r] = 0`。

- 时间复杂度: $O(n^3)$
- 空间复杂度: $O(n^2)$

## 代码
```python
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        a = [1] + nums + [1]
        m = len(a)
        dp = [[0] * m for _ in range(m)]

        # dp[l][r] 表示开区间 (l, r) 全部戳完的最大金币
        for l in range(m - 1, -1, -1):
            for r in range(l + 2, m):   # 至少留一个 k：l < k < r
                best = 0
                for k in range(l + 1, r):
                    best = max(best, dp[l][k] + dp[k][r] + a[l] * a[k] * a[r])
                dp[l][r] = best

        return dp[0][m - 1]
```
