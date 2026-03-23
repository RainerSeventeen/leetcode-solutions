---
id: 1594
title: Maximum Non Negative Product in a Matrix
difficulty: Medium
tags: [array, dynamic-programming, matrix]
created: 2026-03-23
---

# 1594. 矩阵的最大非负积

## 题目链接
https://leetcode.cn/problems/maximum-non-negative-product-in-a-matrix/

## 题目描述
<p>给你一个大小为 <code>m x n</code> 的矩阵 <code>grid</code> 。最初，你位于左上角 <code>(0, 0)</code> ，每一步，你可以在矩阵中 <strong>向右</strong> 或 <strong>向下</strong> 移动。</p>

<p>在从左上角 <code>(0, 0)</code> 开始到右下角 <code>(m - 1, n - 1)</code> 结束的所有路径中，找出具有 <strong>最大非负积</strong> 的路径。路径的积是沿路径访问的单元格中所有整数的乘积。</p>

<p>返回 <strong>最大非负积 </strong>对<strong><em> </em><code>10<sup>9</sup>&nbsp;+ 7</code></strong> <strong>取余</strong> 的结果。如果最大积为 <strong>负数</strong> ，则返回<em> </em><code>-1</code> 。</p>

<p><strong>注意，</strong>取余是在得到最大积之后执行的。</p>

<p><strong>示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/12/23/product1.jpg" style="width: 244px; height: 245px;" />
<pre>
<strong>输入：</strong>grid = [[-1,-2,-3],[-2,-3,-3],[-3,-3,-2]]
<strong>输出：</strong>-1
<strong>解释：</strong>从 (0, 0) 到 (2, 2) 的路径中无法得到非负积，所以返回 -1 。</pre>

<p><strong>示例 2：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/12/23/product2.jpg" style="width: 244px; height: 245px;" />
<pre>
<strong>输入：</strong>grid = [[1,-2,1],[1,-2,1],[3,-4,1]]
<strong>输出：</strong>8
<strong>解释：</strong>最大非负积对应的路径如图所示 (1 * 1 * -2 * -4 * 1 = 8)
</pre>

<p><strong>示例 3：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/12/23/product3.jpg" style="width: 164px; height: 165px;" />
<pre>
<strong>输入：</strong>grid = [[1,3],[0,-4]]
<strong>输出：</strong>0
<strong>解释：</strong>最大非负积对应的路径如图所示 (1 * 0 * -4 = 0)
</pre>

<p><strong>提示：</strong></p>

<ul>
	<li><code>m == grid.length</code></li>
	<li><code>n == grid[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 15</code></li>
	<li><code>-4 &lt;= grid[i][j] &lt;= 4</code></li>
</ul>


## 解题思路

用动态规划维护每个位置能得到的最小乘积和最大乘积。因为当前格子可能是负数，上一位置的最小值乘上负数后会变成更大的正数，所以必须同时保存两种极值。

一维优化时，`dp[j]` 表示当前行到列 `j` 的最小值和最大值。先按第一行初始化，再逐行更新第一列和其余位置，转移时分别从上方和左方的极值中取乘积的最小值和最大值。最后看右下角最大值是否为负，若非负则对 `10^9 + 7` 取模返回。

- 时间复杂度: $O(mn)$

- 空间复杂度: $O(n)$

## 相关专题
- [动态规划](../../topics/dynamic-programming.md)

## 代码
```python
class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        # 一维优化
        n = len(grid)
        m = len(grid[0])
        dp = [[0] * 2 for _ in range(m)]
        dp[0][0], dp[0][1] = grid[0][0], grid[0][0]
        # 手动更新第一行
        for j in range(1, m):
            dp[j][0] = min(dp[j - 1][0] * grid[0][j], dp[j - 1][1] * grid[0][j])
            dp[j][1] = max(dp[j - 1][0] * grid[0][j], dp[j - 1][1] * grid[0][j])
        for i in range(1, n):
            # 第一列
            old_min, old_max = dp[0][0], dp[0][1]
            dp[0][0] = min(old_min * grid[i][0], old_max * grid[i][0])
            dp[0][1] = max(old_min * grid[i][0], old_max * grid[i][0])
            for j in range(1, m):
                a = dp[j][0] * grid[i][j]
                b = dp[j - 1][0] * grid[i][j]
                c = dp[j][1] * grid[i][j]
                d = dp[j - 1][1] * grid[i][j]

                dp[j][0] = min(a, b, c, d)
                dp[j][1] = max(a, b, c, d)
        if dp[m - 1][1] < 0:
            return -1
        else:
            return dp[m - 1][1] % 1_000_000_007
```
