---
id: 64
title: Minimum Path Sum
difficulty: Medium
tags: [array, dynamic-programming, matrix]
created: 2026-02-20
---

# 64. Minimum Path Sum

## 题目链接
https://leetcode.cn/problems/minimum-path-sum/

## 题目描述
<p>给定一个包含非负整数的 <code><em>m</em>&nbsp;x&nbsp;<em>n</em></code>&nbsp;网格&nbsp;<code>grid</code> ，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。</p>

<p><strong>说明：</strong>每次只能向下或者向右移动一步。</p>

<p><strong class="example">示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/11/05/minpath.jpg" style="width: 242px; height: 242px;" />
<pre>
<strong>输入：</strong>grid = [[1,3,1],[1,5,1],[4,2,1]]
<strong>输出：</strong>7
<strong>解释：</strong>因为路径 1→3→1→1→1 的总和最小。
</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<strong>输入：</strong>grid = [[1,2,3],[4,5,6]]
<strong>输出：</strong>12
</pre>

<p><strong>提示：</strong></p>

<ul>
	<li><code>m == grid.length</code></li>
	<li><code>n == grid[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 200</code></li>
	<li><code>0 &lt;= grid[i][j] &lt;= 200</code></li>
</ul>



## 解题思路

动态规划求最小路径和。

设 `dp[i][j]` 表示走到 `(i, j)` 的最小路径和，则：

- 只能从上或左过来：`dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])`

初始化/边界：

- `dp[0][0] = grid[0][0]`
- 第一行只能从左累加：`dp[0][j] = dp[0][j-1] + grid[0][j]`
- 第一列只能从上累加：`dp[i][0] = dp[i-1][0] + grid[i][0]`

空间压缩：

用一维 `dp[j]` 表示当前行到达列 `j` 的最小和：

- 更新前的 `dp[j]` 是上一行的 `dp[i-1][j]`
- 更新后的 `dp[j-1]` 是本行左侧的 `dp[i][j-1]`
- 所以对一般位置：`dp[j] = grid[i][j] + min(dp[j], dp[j-1])`

- 时间复杂度: $O(mn)$
- 空间复杂度: $O(n)$

其中 $n$ 取列数（使用一维 dp 压缩列）。

## 代码
```python
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [float('inf')] * n
        dp[0] = grid[0][0]
        # 初始化第一行
        for j in range(1, n):
            dp[j] = dp[j - 1] + grid[0][j]
        # 从第二行开始
        for i in range(1, m):
            dp[0] += grid[i][0]  # 第一列只能从上面来
            for j in range(1, n):
                dp[j] = min(dp[j], dp[j - 1]) + grid[i][j]
        return dp[-1]
```
