---
id: 2906
title: Construct Product Matrix
difficulty: Medium
tags: [array, matrix, prefix-sum]
created: 2026-03-24
---

# 2906. 构造乘积矩阵

## 题目链接
https://leetcode.cn/problems/construct-product-matrix/

## 题目描述
<p>给你一个下标从 <strong>0</strong> 开始、大小为 <code>n * m</code> 的二维整数矩阵 <code><font face="monospace">grid</font></code><font face="monospace"> ，定义一个下标从 <strong>0</strong> 开始、大小为 <code>n * m</code> 的的二维矩阵</font> <code>p</code>。如果满足以下条件，则称 <code>p</code> 为 <code>grid</code> 的 <strong>乘积矩阵</strong> ：</p>

<ul>
	<li>对于每个元素 <code>p[i][j]</code> ，它的值等于除了 <code>grid[i][j]</code> 外所有元素的乘积。乘积对 <code>12345</code> 取余数。</li>
</ul>

<p>返回 <code>grid</code> 的乘积矩阵。</p>

<p><strong class="example">示例 1：</strong></p>

<pre>
<strong>输入：</strong>grid = [[1,2],[3,4]]
<strong>输出：</strong>[[24,12],[8,6]]
<strong>解释：</strong>p[0][0] = grid[0][1] * grid[1][0] * grid[1][1] = 2 * 3 * 4 = 24
p[0][1] = grid[0][0] * grid[1][0] * grid[1][1] = 1 * 3 * 4 = 12
p[1][0] = grid[0][0] * grid[0][1] * grid[1][1] = 1 * 2 * 4 = 8
p[1][1] = grid[0][0] * grid[0][1] * grid[1][0] = 1 * 2 * 3 = 6
所以答案是 [[24,12],[8,6]] 。</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<strong>输入：</strong>grid = [[12345],[2],[1]]
<strong>输出：</strong>[[2],[0],[0]]
<strong>解释：</strong>p[0][0] = grid[0][1] * grid[0][2] = 2 * 1 = 2
p[0][1] = grid[0][0] * grid[0][2] = 12345 * 1 = 12345. 12345 % 12345 = 0 ，所以 p[0][1] = 0
p[0][2] = grid[0][0] * grid[0][1] = 12345 * 2 = 24690. 24690 % 12345 = 0 ，所以 p[0][2] = 0
所以答案是 [[2],[0],[0]] 。</pre>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n == grid.length&nbsp;&lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= m == grid[i].length&nbsp;&lt;= 10<sup>5</sup></code></li>
	<li><code>2 &lt;= n * m &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= grid[i][j] &lt;= 10<sup>9</sup></code></li>
</ul>


## 解题思路

- 先把二维矩阵按行展开成一个一维遍历顺序，再分别做一遍前缀乘积和一遍后缀乘积。
- 第一次遍历时，用 `ans[i][j]` 记录当前格子左侧所有元素的乘积；第二次遍历时，再把当前格子右侧所有元素的乘积乘进去。
- 由于模数是 `12345`，不能直接用除法逆元，因此只能用前后缀拆分来计算每个位置的答案。
- 时间复杂度: $O(nm)$，其中 `n` 和 `m` 分别是矩阵的行数和列数。

- 空间复杂度: $O(1)$，不计返回结果所需的输出矩阵。

## 相关专题
- [动态规划](../../topics/dynamic-programming.md)

## 代码
```python
class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        MOD = 12345
        n = len(grid)
        m = len(grid[0])
        ans = [[1] * m for _ in range(n)]
        curr, pre = 1, 1
        for i in range(n):
            for j in range(m):
                curr *= pre
                curr = curr % MOD
                ans[i][j] = curr
                pre = grid[i][j]
        curr, pre = 1, 1
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                curr *= pre
                curr = curr % MOD
                ans[i][j] = curr * ans[i][j] % MOD
                pre = grid[i][j]
        return ans
```
