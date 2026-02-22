---
id: 62
title: Unique Paths
difficulty: Medium
tags: [math, dynamic-programming, combinatorics]
created: 2026-02-20
---

# 62. 不同路径

## 题目链接
https://leetcode.cn/problems/unique-paths/

## 题目描述
<p>一个机器人位于一个 <code>m x n</code><em>&nbsp;</em>网格的左上角 （起始点在下图中标记为 “Start” ）。</p>

<p>机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为 “Finish” ）。</p>

<p>问总共有多少条不同的路径？</p>

<p><strong>示例 1：</strong></p>
<img src="https://pic.leetcode.cn/1697422740-adxmsI-image.png" style="width: 400px; height: 183px;" />
<pre>
<strong>输入：</strong>m = 3, n = 7
<strong>输出：</strong>28</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>m = 3, n = 2
<strong>输出：</strong>3
<strong>解释：</strong>
从左上角开始，总共有 3 条路径可以到达右下角。
1. 向右 -&gt; 向下 -&gt; 向下
2. 向下 -&gt; 向下 -&gt; 向右
3. 向下 -&gt; 向右 -&gt; 向下
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>m = 7, n = 3
<strong>输出：</strong>28
</pre>

<p><strong>示例 4：</strong></p>

<pre>
<strong>输入：</strong>m = 3, n = 3
<strong>输出：</strong>6</pre>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= m, n &lt;= 100</code></li>
	<li>题目数据保证答案小于等于 <code>2 * 10<sup>9</sup></code></li>
</ul>



## 解题思路

典型动态规划。

设 `dp[i][j]` 表示从左上角走到格子 `(i, j)` 的不同路径数。由于机器人只能向右/向下走，所以到达 `(i, j)` 只能来自：

- 上方 `(i-1, j)`
- 左方 `(i, j-1)`

因此转移：`dp[i][j] = dp[i-1][j] + dp[i][j-1]`。

初始化/边界：

- 第一行只能一直向右走：`dp[0][j] = 1`
- 第一列只能一直向下走：`dp[i][0] = 1`

空间优化：

第 `i` 行只依赖第 `i-1` 行和本行左侧，可以用一维数组 `dp[j]` 表示当前列的路径数：

- 更新时 `dp[j]`（旧值）相当于 `dp[i-1][j]`，`dp[j-1]`（新值）相当于 `dp[i][j-1]`
- 所以 `dp[j] += dp[j-1]`

- 时间复杂度: $O(mn)$
- 空间复杂度: $O(n)$

其中 $n$ 取列数。

## 代码
```python
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1] * (n + 1) # 第一列全是 1
        dp[0] = 1
        for i in range(1, m):
            dp[0] = 0 # 最上面一个不允许从上来
            for j in range(1, n + 1):
                    dp[j] += dp [j - 1]
        return dp[n]
```
