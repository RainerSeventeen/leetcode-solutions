---
id: 1878
title: Get Biggest Three Rhombus Sums in a Grid
difficulty: Medium
tags: [array, math, matrix, prefix-sum, sorting, heap-priority-queue]
created: 2026-03-16
---

# 1878. 矩阵中最大的三个菱形和

## 题目链接
https://leetcode.cn/problems/get-biggest-three-rhombus-sums-in-a-grid/

## 题目描述
<p>给你一个 <code>m x n</code> 的整数矩阵 <code>grid</code> 。</p>

<p><strong>菱形和</strong> 指的是 <code>grid</code> 中一个正菱形 <strong>边界</strong> 上的元素之和。本题中的菱形必须为正方形旋转45度，且四个角都在一个格子当中。下图是四个可行的菱形，每个菱形和应该包含的格子都用了相应颜色标注在图中。</p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/04/23/pc73-q4-desc-2.png" style="width: 385px; height: 385px;" />

<p>注意，菱形可以是一个面积为 0 的区域，如上图中右下角的紫色菱形所示。</p>

<p>请你按照 <strong>降序</strong> 返回 <code>grid</code> 中三个最大的 <strong>互不相同的菱形和</strong> 。如果不同的和少于三个，则将它们全部返回。</p>

<p><strong>示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/04/23/pc73-q4-ex1.png" style="width: 360px; height: 361px;" />
<pre>
<b>输入：</b>grid = [[3,4,5,1,3],[3,3,4,2,3],[20,30,200,40,10],[1,5,5,4,1],[4,3,2,2,5]]
<b>输出：</b>[228,216,211]
<b>解释：</b>最大的三个菱形和如上图所示。
- 蓝色：20 + 3 + 200 + 5 = 228
- 红色：200 + 2 + 10 + 4 = 216
- 绿色：5 + 200 + 4 + 2 = 211
</pre>

<p><strong>示例 2：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/04/23/pc73-q4-ex2.png" style="width: 217px; height: 217px;" />
<pre>
<b>输入：</b>grid = [[1,2,3],[4,5,6],[7,8,9]]
<b>输出：</b>[20,9,8]
<b>解释：</b>最大的三个菱形和如上图所示。
- 蓝色：4 + 2 + 6 + 8 = 20
- 红色：9 （右下角红色的面积为 0 的菱形）
- 绿色：8 （下方中央面积为 0 的菱形）
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<b>输入：</b>grid = [[7,7,7]]
<b>输出：</b>[7]
<b>解释：</b>所有三个可能的菱形和都相同，所以返回 [7] 。
</pre>

<p><strong>提示：</strong></p>

<ul>
	<li><code>m == grid.length</code></li>
	<li><code>n == grid[i].length</code></li>
	<li><code>1 <= m, n <= 100</code></li>
	<li><code>1 <= grid[i][j] <= 10<sup>5</sup></code></li>
</ul>


## 解题思路

- 先分别在 `\` 和 `/` 两个方向构建前缀和矩阵，使得任意边界的对角线和可以常数时间得到，再枚举每个格子作为菱形中心及所有合法半径，将四边和加入结果集合并取最大三个不同值。
- 时间复杂度: $O(n \cdot m \cdot \min(n, m))$
- 空间复杂度: $O(n \cdot m)$

## 相关专题
- [常用数据结构](../../topics/common-data-structures.md)

## 代码
```python
class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        n, m = len(grid), len(grid[0])

        # \ 方向前缀和
        diag1 = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(n):
            for j in range(m):
                diag1[i + 1][j + 1] = diag1[i][j] + grid[i][j]

        # / 方向前缀和
        diag2 = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(n):
            for j in range(m - 1, -1, -1):
                diag2[i + 1][j] = diag2[i][j + 1] + grid[i][j]

        vals = set()

        # 取 \ 方向上从 (x1,y1) 到 (x2,y2) 的和，要求 x2-x1 == y2-y1
        def sum_diag1(x1, y1, x2, y2):
            return diag1[x2 + 1][y2 + 1] - diag1[x1][y1]

        # 取 / 方向上从 (x1,y1) 到 (x2,y2) 的和，要求 x2-x1 == y1-y2
        def sum_diag2(x1, y1, x2, y2):
            return diag2[x2 + 1][y2] - diag2[x1][y1 + 1]

        for i in range(n):
            for j in range(m):
                vals.add(grid[i][j])   # 半径 0

                max_r = min(i, n - 1 - i, j, m - 1 - j)
                for r in range(1, max_r + 1):
                    top = (i - r, j)
                    right = (i, j + r)
                    bottom = (i + r, j)
                    left = (i, j - r)

                    s1 = sum_diag1(top[0], top[1], right[0], right[1])       # top -> right
                    s2 = sum_diag2(right[0], right[1], bottom[0], bottom[1]) # right -> bottom
                    s3 = sum_diag1(left[0], left[1], bottom[0], bottom[1])   # left -> bottom
                    s4 = sum_diag2(top[0], top[1], left[0], left[1])         # top -> left

                    # 四个顶点各被算了两次，减去一次
                    total = s1 + s2 + s3 + s4 - grid[top[0]][top[1]] - grid[right[0]][right[1]] - grid[bottom[0]][bottom[1]] - grid[left[0]][left[1]]
                    vals.add(total)

        return sorted(vals, reverse=True)[:3]
```
