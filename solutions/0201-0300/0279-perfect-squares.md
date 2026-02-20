---
id: 279
title: Perfect Squares
difficulty: Medium
tags: [breadth-first-search, math, dynamic-programming]
created: 2026-02-20
---

# 279. 完全平方数

## 题目链接
https://leetcode.cn/problems/perfect-squares/

## 题目描述
<p>给你一个整数 <code>n</code> ，返回 <em>和为 <code>n</code> 的完全平方数的最少数量</em> 。</p>

<p><strong>完全平方数</strong> 是一个整数，其值等于另一个整数的平方；换句话说，其值等于一个整数自乘的积。例如，<code>1</code>、<code>4</code>、<code>9</code> 和 <code>16</code> 都是完全平方数，而 <code>3</code> 和 <code>11</code> 不是。</p>

<p><strong>示例&nbsp;1：</strong></p>

<pre>
<strong>输入：</strong>n = <code>12</code>
<strong>输出：</strong>3 
<strong>解释：</strong><code>12 = 4 + 4 + 4</code></pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>n = <code>13</code>
<strong>输出：</strong>2
<strong>解释：</strong><code>13 = 4 + 9</code></pre>
&nbsp;

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 10<sup>4</sup></code></li>
</ul>

## 解题思路
完全背包式的动态规划（最少个数）。

设 `dp[i]` 表示“凑出和为 `i` 的最少完全平方数个数”。初始化：

- `dp[0] = 0`
- 其他 `dp[i]` 初始化为正无穷（表示不可达/尚未更新）

转移：

对每个 `i = 1..n`，枚举最后一个平方数为 `j*j`（满足 `j*j <= i`）：

- `dp[i] = min(dp[i], dp[i - j*j] + 1)`

含义是：如果能用最少 `dp[i - j*j]` 个平方数凑出 `i - j*j`，再加上一个 `j*j` 就能得到 `i`。

边界：

- `n = 0` 时答案为 0（题目一般 `n >= 1`，但状态定义支持该边界）。

- 时间复杂度: $O(n\sqrt{n})$
- 空间复杂度: $O(n)$

## 代码
```python
class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float('inf')] * (n + 1) # 1 ~ n
        dp[0] = 0
        for i in range(1, n + 1):
            for sq in range(int(sqrt(i)) + 1):
                dp[i] = min(dp[i], dp[i - sq * sq] + 1)
        return dp[n]
```
