---
id: 240
title: 搜索二维矩阵 II
difficulty: Medium
tags: [array, binary-search, divide-and-conquer, matrix]
created: 2026-02-20
---

# 240. 搜索二维矩阵 II

## 题目链接
https://leetcode.cn/problems/search-a-2d-matrix-ii/

## 题目描述

<p>编写一个高效的算法来搜索&nbsp;<code><em>m</em>&nbsp;x&nbsp;<em>n</em></code>&nbsp;矩阵 <code>matrix</code> 中的一个目标值 <code>target</code> 。该矩阵具有以下特性：</p>

<ul>
	<li>每行的元素从左到右升序排列。</li>
	<li>每列的元素从上到下升序排列。</li>
</ul>

<p><b>示例 1：</b></p>
<img alt="" src="https://assets.leetcode.cn/aliyun-lc-upload/uploads/2020/11/25/searchgrid2.jpg" />
<pre>
<b>输入：</b>matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5
<b>输出：</b>true
</pre>

<p><b>示例 2：</b></p>
<img alt="" src="https://assets.leetcode.cn/aliyun-lc-upload/uploads/2020/11/25/searchgrid.jpg" />
<pre>
<b>输入：</b>matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 20
<b>输出：</b>false
</pre>

<p><strong>提示：</strong></p>

<ul>
	<li><code>m == matrix.length</code></li>
	<li><code>n == matrix[i].length</code></li>
	<li><code>1 &lt;= n, m &lt;= 300</code></li>
	<li><code>-10<sup>9</sup>&nbsp;&lt;= matrix[i][j] &lt;= 10<sup>9</sup></code></li>
	<li>每行的所有元素从左到右升序排列</li>
	<li>每列的所有元素从上到下升序排列</li>
	<li><code>-10<sup>9</sup>&nbsp;&lt;= target &lt;= 10<sup>9</sup></code></li>
</ul>

## 解题思路
利用矩阵“行、列均递增”的性质，从右上角（或左下角）开始走。

以右上角 `(0, n-1)` 为例：

- 当前值 `x = matrix[i][j]`
- 若 `x == target`：找到
- 若 `x > target`：由于这一列从上到下递增，`x` 已经太大，`target` 不可能在当前列的更下方，因此 `j -= 1`（左移删掉一整列）
- 若 `x < target`：由于这一行从左到右递增，`x` 太小，`target` 不可能在当前行的更左侧，因此 `i += 1`（下移删掉一整行）

不变量：

- 每一步都能排除一整行或一整列，并且不会错过 `target`（基于单调性）。

边界：

- 空矩阵直接返回 `False`。

- 时间复杂度: $O(m+n)$
- 空间复杂度: $O(1)$

## 代码
```python
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        i, j = m -1, 0
        while i >= 0 and j < n:
            if matrix[i][j] > target:
                i -= 1
            elif matrix[i][j] < target:
                j += 1
            else:
                return True
        else:
            return False
```
