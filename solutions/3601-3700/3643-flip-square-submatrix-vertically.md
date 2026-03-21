---
id: 3643
title: Flip Square Submatrix Vertically
difficulty: Easy
tags: [array, two-pointers, matrix]
created: 2026-03-21
---

# 3643. 垂直翻转子矩阵

## 题目链接
https://leetcode.cn/problems/flip-square-submatrix-vertically/

## 题目描述
<p>给你一个 <code>m x n</code> 的整数矩阵 <code>grid</code>，以及三个整数 <code>x</code>、<code>y</code> 和 <code>k</code>。</p>

<p>整数 <code>x</code> 和 <code>y</code> 表示一个&nbsp;<strong>正方形子矩阵&nbsp;</strong>的左上角下标，整数 <code>k</code> 表示该正方形子矩阵的边长。</p>

<p>你的任务是垂直翻转子矩阵的行顺序。</p>

<p>返回更新后的矩阵。</p>

<p><strong class="example">示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2025/07/20/gridexmdrawio.png" style="width: 300px; height: 116px;" />
<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">grid = </span>[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]<span class="example-io">, x = 1, y = 0, k = 3</span></p>

<p><strong>输出：</strong> <span class="example-io">[[1,2,3,4],[13,14,15,8],[9,10,11,12],[5,6,7,16]]</span></p>

<p><strong>解释：</strong></p>

<p>上图展示了矩阵在变换前后的样子。</p>
</div>

<p><strong class="example">示例 2：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2025/07/20/gridexm2drawio.png" style="width: 350px; height: 68px;" />
<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">grid = [[3,4,2,3],[2,3,4,2]], x = 0, y = 2, k = 2</span></p>

<p><strong>输出：</strong> <span class="example-io">[[3,4,4,2],[2,3,2,3]]</span></p>

<p><strong>解释：</strong></p>

<p>上图展示了矩阵在变换前后的样子。</p>
</div>

<p><strong>提示：</strong></p>

<ul>
	<li><code>m == grid.length</code></li>
	<li><code>n == grid[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 50</code></li>
	<li><code>1 &lt;= grid[i][j] &lt;= 100</code></li>
	<li><code>0 &lt;= x &lt; m</code></li>
	<li><code>0 &lt;= y &lt; n</code></li>
	<li><code>1 &lt;= k &lt;= min(m - x, n - y)</code></li>
</ul>


## 解题思路

- 只需要对正方形子矩阵内的行做上下对称交换。
- 用 `up` 和 `down` 分别指向当前要交换的上、下两行，逐次把这两行在 `[y, y + k)` 区间内的元素交换。
- 这样就完成了子矩阵的垂直翻转，并且直接在原数组上修改，不需要额外空间。

- 时间复杂度: $O(k^2)$
- 空间复杂度: $O(1)$

## 相关专题
- [滑动窗口与双指针](../../topics/sliding-window-and-two-pointers.md)

## 代码
```python
class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        up, down = x, x + k - 1
        while up < down:
            for j in range(y, y + k):
                grid[up][j], grid[down][j] = grid[down][j], grid[up][j]
            up += 1
            down -= 1
        return grid
```
