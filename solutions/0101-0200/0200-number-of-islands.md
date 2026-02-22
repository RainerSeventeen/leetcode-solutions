---
id: 200
title: Number of Islands
difficulty: Medium
tags: [depth-first-search, breadth-first-search, union-find, array, matrix]
created: 2026-02-20
---

# 200. 岛屿数量

## 题目链接
https://leetcode.cn/problems/number-of-islands/

## 题目描述
<p>给你一个由&nbsp;<code>'1'</code>（陆地）和 <code>'0'</code>（水）组成的的二维网格，请你计算网格中岛屿的数量。</p>

<p>岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。</p>

<p>此外，你可以假设该网格的四条边均被水包围。</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>grid = [
&nbsp; ['1','1','1','1','0'],
&nbsp; ['1','1','0','1','0'],
&nbsp; ['1','1','0','0','0'],
&nbsp; ['0','0','0','0','0']
]
<strong>输出：</strong>1
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>grid = [
&nbsp; ['1','1','0','0','0'],
&nbsp; ['1','1','0','0','0'],
&nbsp; ['0','0','1','0','0'],
&nbsp; ['0','0','0','1','1']
]
<strong>输出：</strong>3
</pre>

<p><strong>提示：</strong></p>

<ul>
	<li><code>m == grid.length</code></li>
	<li><code>n == grid[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 300</code></li>
	<li><code>grid[i][j]</code> 的值为 <code>'0'</code> 或 <code>'1'</code></li>
</ul>


## 解题思路

经典 DFS 遍历网格题目。

遍历每个格子，遇到 `'1'` 时岛屿计数 +1，同时用 DFS 将与其相连的所有陆地格子标记为 `'0'`（沉岛），避免重复计数。

关键点：直接修改原始 grid 避免额外的 visited 数组。

- 时间复杂度: $O(mn)$
- 空间复杂度: $O(mn)$（递归栈最深 $mn$ 层）
## 代码
```python
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        m = len(grid)
        n = len(grid[0])

        def dfs(x, y):
            if not (0 <= x < m and 0 <= y < n):
                return
            if grid[x][y] == '0':
                return

            grid[x][y] = '0'  # 标记访问过
            for dx, dy in direction:
                dfs(x + dx, y + dy)

        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    count += 1
                    dfs(i, j)

        return count
```
