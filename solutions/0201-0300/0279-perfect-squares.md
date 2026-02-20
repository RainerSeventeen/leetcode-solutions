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

这是完全背包的最小值版本。令 `dp[j]` 表示凑出和为 `j` 的最少完全平方数个数。

- 初始：`dp[0] = 0`，其余设为正无穷。
- 物品：所有平方数 `1, 4, 9, ... <= n`。
- 转移：`dp[j] = min(dp[j], dp[j - sq] + 1)`（正序遍历容量表示可重复选取）。

- 时间复杂度: `O(n * sqrt(n))`
- 空间复杂度: `O(n)`

## 代码
```python
class Solution:
    def numSquares(self, n: int) -> int:
        inf = 10**9
        dp = [inf] * (n + 1)
        dp[0] = 0
        i = 1
        while i * i <= n:
            sq = i * i
            for j in range(sq, n + 1):
                dp[j] = min(dp[j], dp[j - sq] + 1)
            i += 1
        return dp[n]
```
