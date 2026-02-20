---
id: 70
title: Climbing Stairs
difficulty: Easy
tags: [memoization, math, dynamic-programming]
created: 2026-02-20
---

# 70. 爬楼梯

## 题目链接
https://leetcode.cn/problems/climbing-stairs/

## 题目描述
<p>假设你正在爬楼梯。需要 <code>n</code>&nbsp;阶你才能到达楼顶。</p>

<p>每次你可以爬 <code>1</code> 或 <code>2</code> 个台阶。你有多少种不同的方法可以爬到楼顶呢？</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>n = 2
<strong>输出：</strong>2
<strong>解释：</strong>有两种方法可以爬到楼顶。
1. 1 阶 + 1 阶
2. 2 阶</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>n = 3
<strong>输出：</strong>3
<strong>解释：</strong>有三种方法可以爬到楼顶。
1. 1 阶 + 1 阶 + 1 阶
2. 1 阶 + 2 阶
3. 2 阶 + 1 阶
</pre>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 45</code></li>
</ul>


## 解题思路

设 `dp[i]` 为到达第 `i` 阶的方法数，则最后一步只能从 `i-1` 或 `i-2` 走来：

`dp[i] = dp[i - 1] + dp[i - 2]`

初始值是 `dp[1] = 1, dp[2] = 2`。由于状态只依赖前两项，可用两个变量滚动维护。

- 时间复杂度: `O(n)`
- 空间复杂度: `O(1)`

## 代码
```python
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        prev2, prev1 = 1, 2
        for _ in range(3, n + 1):
            prev2, prev1 = prev1, prev1 + prev2
        return prev1
```
