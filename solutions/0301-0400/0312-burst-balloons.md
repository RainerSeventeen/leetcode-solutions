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

<p>有 <code>n</code> 个气球，编号为<code>0</code> 到 <code>n - 1</code>，每个气球上都标有一个数字，这些数字存在数组&nbsp;<code>nums</code>&nbsp;中。</p>

<p>现在要求你戳破所有的气球。戳破第 <code>i</code> 个气球，你可以获得&nbsp;<code>nums[i - 1] * nums[i] * nums[i + 1]</code> 枚硬币。&nbsp;这里的 <code>i - 1</code> 和 <code>i + 1</code> 代表和&nbsp;<code>i</code>&nbsp;相邻的两个气球的序号。如果 <code>i - 1</code>或 <code>i + 1</code> 超出了数组的边界，那么就当它是一个数字为 <code>1</code> 的气球。</p>

<p>求所能获得硬币的最大数量。</p>

<strong>示例 1：</strong>

<pre>
<strong>输入：</strong>nums = [3,1,5,8]
<strong>输出：</strong>167
<strong>解释：</strong>
nums = [3,1,5,8] --&gt; [3,5,8] --&gt; [3,8] --&gt; [8] --&gt; []
coins =  3*1*5    +   3*5*8   +  1*3*8  + 1*8*1 = 167</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,5]
<strong>输出：</strong>10
</pre>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == nums.length</code></li>
	<li><code>1 &lt;= n &lt;= 300</code></li>
	<li><code>0 &lt;= nums[i] &lt;= 100</code></li>
</ul>

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
