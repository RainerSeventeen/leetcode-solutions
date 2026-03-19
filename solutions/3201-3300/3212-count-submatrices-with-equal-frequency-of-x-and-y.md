---
id: 3212
title: Count Submatrices With Equal Frequency of X and Y
difficulty: Medium
tags: [array, matrix, prefix-sum]
created: 2026-03-19
---

# 3212. 统计 X 和 Y 频数相等的子矩阵数量

## 题目链接
https://leetcode.cn/problems/count-submatrices-with-equal-frequency-of-x-and-y/

## 题目描述
<p>给你一个二维字符矩阵 <code>grid</code>，其中 <code>grid[i][j]</code> 可能是 <code>'X'</code>、<code>'Y'</code> 或 <code>'.'</code>，返回满足以下条件的<span data-keyword="submatrix">子矩阵</span>数量：</p>

<ul>
	<li>包含 <code>grid[0][0]</code></li>
	<li><code>'X'</code> 和 <code>'Y'</code> 的频数相等。</li>
	<li>至少包含一个 <code>'X'</code>。</li>
</ul>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">grid = [["X","Y","."],["Y",".","."]]</span></p>

<p><strong>输出：</strong> <span class="example-io">3</span></p>

<p><strong>解释：</strong></p>

<p><strong><img alt="" src="https://assets.leetcode.com/uploads/2024/06/07/examplems.png" style="padding: 10px; background: rgb(255, 255, 255); border-radius: 0.5rem; width: 175px; height: 350px;" /></strong></p>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">grid = [["X","X"],["X","Y"]]</span></p>

<p><strong>输出：</strong> <span class="example-io">0</span></p>

<p><strong>解释：</strong></p>

<p>不存在满足 <code>'X'</code> 和 <code>'Y'</code> 频数相等的子矩阵。</p>
</div>

<p><strong class="example">示例 3：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">grid = [[".","."],[".","."]]</span></p>

<p><strong>输出：</strong> <span class="example-io">0</span></p>

<p><strong>解释：</strong></p>

<p>不存在满足至少包含一个 <code>'X'</code> 的子矩阵。</p>
</div>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= grid.length, grid[i].length &lt;= 1000</code></li>
	<li><code>grid[i][j]</code> 可能是 <code>'X'</code>、<code>'Y'</code> 或 <code>'.'</code>.</li>
</ul>


## 解题思路

按行扫描子矩阵的右下角。对每一列维护从第 0 行到当前行的 `X` / `Y` 累计出现次数，这样当前格子对应的前缀子矩阵 `grid[0..i][0..j]` 的 `X` 和 `Y` 总数，就可以在扫描当前行时用两个变量 `s0`、`s1` 线性累加出来。

如果某个前缀子矩阵里 `X` 和 `Y` 数量相等，且 `X` 数量不为 0，就把答案加一。因为必须包含 `grid[0][0]`，所以只需要统计所有从左上角开始的前缀子矩阵即可。

- 时间复杂度: $O(nm)$

- 空间复杂度: $O(m)$

## 相关专题

- [常用数据结构](../../topics/common-data-structures.md)

## 代码
```python
class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        # 一维优化 前缀和，也可以说是 dp
        ans = 0
        n = len(grid)
        m = len(grid[0])
        col = [[0] * 2 for _ in range(m)] # 每一个列的数量
        for i in range(n):
            s0, s1 = 0, 0 # 从左到右累加当前行
            for j in range(m):
                ch = grid[i][j] # i 循环内 包含当前值
                if ch == 'X':
                    col[j][0] += 1
                elif ch == 'Y':
                    col[j][1] += 1
                s0 += col[j][0]
                s1 += col[j][1]
                if s0 == s1 and s0 != 0:
                    ans += 1
        return ans
```
