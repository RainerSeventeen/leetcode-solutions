---
id: 48
title: 旋转图像
difficulty: Medium
tags: [array, math, matrix]
created: 2026-02-20
---

# 48. 旋转图像

## 题目链接
https://leetcode.cn/problems/rotate-image/

## 题目描述

<p>给定一个 <em>n&nbsp;</em>×&nbsp;<em>n</em> 的二维矩阵&nbsp;<code>matrix</code> 表示一个图像。请你将图像顺时针旋转 90 度。</p>

<p>你必须在<strong><a href="https://baike.baidu.com/item/%E5%8E%9F%E5%9C%B0%E7%AE%97%E6%B3%95" target="_blank"> 原地</a></strong> 旋转图像，这意味着你需要直接修改输入的二维矩阵。<strong>请不要 </strong>使用另一个矩阵来旋转图像。</p>

<p><strong>示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/08/28/mat1.jpg" style="height: 188px; width: 500px;" />
<pre>
<strong>输入：</strong>matrix = [[1,2,3],[4,5,6],[7,8,9]]
<strong>输出：</strong>[[7,4,1],[8,5,2],[9,6,3]]
</pre>

<p><strong>示例 2：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/08/28/mat2.jpg" style="height: 201px; width: 500px;" />
<pre>
<strong>输入：</strong>matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
<strong>输出：</strong>[[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
</pre>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == matrix.length == matrix[i].length</code></li>
	<li><code>1 &lt;= n &lt;= 20</code></li>
	<li><code>-1000 &lt;= matrix[i][j] &lt;= 1000</code></li>
</ul>

## 解题思路
要求原地旋转 90°，可以按“分层 + 四点循环置换”做。

把矩阵看成若干层（外圈到内圈）。对每一层的每个位置 `(i, j)`，它会与另外三个位置形成一个 4 环：

`(i, j) -> (n-1-j, i) -> (n-1-i, n-1-j) -> (j, n-1-i) -> (i, j)`

按这个顺序做四点交换即可完成旋转。循环边界的写法（代码中 `i <= n/2-1`、`j <= (n-1)/2`）确保每个 4 环只处理一次，且奇偶 `n` 都覆盖到位。

- 时间复杂度: $O(n^2)$
- 空间复杂度: $O(1)$

## 相关专题
- [网格图](../../topics/grid-graph.md)

## 代码
```cpp
class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        int n = matrix.size();
        for (int i = 0; i <= n / 2 - 1; i++) {
            for (int j = 0; j <= (n - 1) / 2; j++) {
                // 四点变换
                int tmp = matrix[i][j];
                matrix[i][j] = matrix[n - j - 1][i];
                matrix[n - j - 1][i] = matrix[n - i -1][n - j -1];
                matrix[n - i -1][n - j -1] = matrix[j][n - i -1];
                matrix[j][n - i -1] = tmp;
            }
        }
    }
};
```
