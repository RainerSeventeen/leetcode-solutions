---
id: 1582
title: Special Positions in a Binary Matrix
difficulty: Easy
tags: [array, matrix]
created: 2026-03-04
---

# 1582. 二进制矩阵中的特殊位置

## 题目链接
https://leetcode.cn/problems/special-positions-in-a-binary-matrix/

## 题目描述
<p>给定一个 <code>m x n</code> 的二进制矩阵 <code>mat</code>，返回矩阵 <code>mat</code> 中特殊位置的数量。</p>

<p>如果位置 <code>(i, j)</code> 满足 <code>mat[i][j] == 1</code> 并且行 <code>i</code> 与列 <code>j</code> 中的所有其他元素都是 <code>0</code>（行和列的下标从 <strong>0 </strong>开始计数），那么它被称为<strong> 特殊 </strong>位置。</p>

<p><strong class="example">示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/12/23/special1.jpg" style="width: 244px; height: 245px;" />
<pre>
<strong>输入：</strong>mat = [[1,0,0],[0,0,1],[1,0,0]]
<strong>输出：</strong>1
<strong>解释：</strong>位置 (1, 2) 是一个特殊位置，因为 mat[1][2] == 1 且第 1 行和第 2 列的其他所有元素都是 0。
</pre>

<p><strong class="example">示例 2：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/12/24/special-grid.jpg" style="width: 244px; height: 245px;" />
<pre>
<strong>输入：</strong>mat = [[1,0,0],[0,1,0],[0,0,1]]
<strong>输出：</strong>3
<strong>解释：</strong>位置 (0, 0)，(1, 1) 和 (2, 2) 都是特殊位置。
</pre>

<p><strong>提示：</strong></p>

<ul>
	<li><code>m == mat.length</code></li>
	<li><code>n == mat[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 100</code></li>
	<li><code>mat[i][j]</code> 是 <code>0</code> 或 <code>1</code>。</li>
</ul>


## 解题思路

先分别统计每一行和每一列中 `1` 的个数：

- `rows_sum[i]` 表示第 `i` 行的 `1` 的数量；
- `cols_sum[j]` 表示第 `j` 列的 `1` 的数量。

再遍历矩阵中的每个位置 `(i, j)`，当且仅当：

- `mat[i][j] == 1`
- `rows_sum[i] == 1`
- `cols_sum[j] == 1`

该位置就是特殊位置，计入答案即可。

- 时间复杂度: $O(mn)$，其中 $m$ 为行数，$n$ 为列数。

- 空间复杂度: $O(m+n)$，用于存储行列计数数组。

## 相关专题
- [常用数据结构](../../topics/common-data-structures.md)

## 代码
```python
class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        rows_sum = [sum(row) for row in mat]
        cols_sum = [sum(col) for col in zip(*mat)] # 按列取值
        ans = 0
        for i, row in enumerate(mat):
            for j, x in enumerate(row):
                if x == 1 and rows_sum[i] == 1 and cols_sum[j] == 1:
                    ans += 1

        return ans
```
