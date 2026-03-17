---
id: 1727
title: Largest Submatrix With Rearrangements
difficulty: Medium
tags: [greedy, array, matrix, sorting]
created: 2026-03-17
---

# 1727. 重新排列后的最大子矩阵

## 题目链接
https://leetcode.cn/problems/largest-submatrix-with-rearrangements/

## 题目描述
<p>给你一个二进制矩阵 <code>matrix</code> ，它的大小为 <code>m x n</code> ，你可以将 <code>matrix</code> 中的 <strong>列</strong> 按任意顺序重新排列。</p>

<p>请你返回最优方案下将 <code>matrix</code> 重新排列后，全是 <code>1</code> 的子矩阵面积。</p>

<p><strong>示例 1：</strong></p>

<p><strong><img alt="" src="https://assets.leetcode.cn/aliyun-lc-upload/uploads/2021/01/17/screenshot-2020-12-30-at-40536-pm.png" style="width: 300px; height: 144px;" /></strong></p>

<pre>
<b>输入：</b>matrix = [[0,0,1],[1,1,1],[1,0,1]]
<b>输出：</b>4
<b>解释：</b>你可以按照上图方式重新排列矩阵的每一列。
最大的全 1 子矩阵是上图中加粗的部分，面积为 4 。
</pre>

<p><strong>示例 2：</strong></p>

<p><img alt="" src="https://assets.leetcode.cn/aliyun-lc-upload/uploads/2021/01/17/screenshot-2020-12-30-at-40852-pm.png" style="width: 500px; height: 62px;" /></p>

<pre>
<b>输入：</b>matrix = [[1,0,1,0,1]]
<b>输出：</b>3
<b>解释：</b>你可以按照上图方式重新排列矩阵的每一列。
最大的全 1 子矩阵是上图中加粗的部分，面积为 3 。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<b>输入：</b>matrix = [[1,1,0],[1,0,1]]
<b>输出：</b>2
<b>解释：</b>由于你只能整列整列重新排布，所以没有比面积为 2 更大的全 1 子矩形。</pre>

<p><strong>示例 4：</strong></p>

<pre>
<b>输入：</b>matrix = [[0,0],[0,0]]
<b>输出：</b>0
<b>解释：</b>由于矩阵中没有 1 ，没有任何全 1 的子矩阵，所以面积为 0 。</pre>

<p><strong>提示：</strong></p>

<ul>
	<li><code>m == matrix.length</code></li>
	<li><code>n == matrix[i].length</code></li>
	<li><code>1 <= m * n <= 10<sup>5</sup></code></li>
	<li><code>matrix[i][j]</code> 要么是 <code>0</code> ，要么是 <code>1</code> 。</li>
</ul>


## 解题思路

先按行计算每一列以当前行为底的连续 `1` 高度：若 `matrix[i][j]=1`，高度加一，否则清零。  
对于固定的一行，这些高度代表可选列高。因为列可以任意重排，所以把该行高度数组排序后，枚举每个高度作为子矩阵最小高，宽度就是其右侧列数，面积为 `height * width`，取最大值。  
遍历所有行即可得到答案。

- 时间复杂度: $O(m \cdot n \log n)$，其中 `m` 为行数、`n` 为列数。每一行做一次长度为 `n` 的排序。

- 空间复杂度: $O(n)$，用于维护每列当前连续 `1` 的高度数组。

## 相关专题
- [贪心与思维](../../topics/greedy-and-thinking.md)

## 代码
```python
class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        # 层级遍历，排序算最大值，层内贪心
        n = len(matrix) # 层数
        m = len(matrix[0])
        lvl = [0] * m
        ans = 0
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 1:
                    lvl[j] += 1
                else:
                    lvl[j] = 0

            slvl = sorted(lvl)
            # print(i, slvl)
            j, pre = 0, -1
            for j in range(m):
                if slvl[j] == pre:
                    continue
                # print(pre, slvl[j], j)
                ans = max(ans, slvl[j] * (m - j))
                pre = slvl[j]
        return ans
```
