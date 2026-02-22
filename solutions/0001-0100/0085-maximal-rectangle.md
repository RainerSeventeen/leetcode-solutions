---
id: 85
title: Maximal Rectangle
difficulty: Hard
tags: [stack, array, dynamic-programming, matrix, monotonic-stack]
created: 2026-02-20
---

# 85. 最大矩形

## 题目链接
https://leetcode.cn/problems/maximal-rectangle/

## 题目描述
<p>给定一个仅包含&nbsp;<code>0</code> 和 <code>1</code> 、大小为 <code>rows x cols</code> 的二维二进制矩阵，找出只包含 <code>1</code> 的最大矩形，并返回其面积。</p>

<p><strong>示例 1：</strong></p>
<img alt="" src="https://pic.leetcode.cn/1722912576-boIxpm-image.png" style="width: 402px; height: 322px;" />
<pre>
<strong>输入：</strong>matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
<strong>输出：</strong>6
<strong>解释：</strong>最大矩形如上图所示。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>matrix = [["0"]]
<strong>输出：</strong>0
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>matrix = [["1"]]
<strong>输出：</strong>1
</pre>

<p><strong>提示：</strong></p>

<ul>
	<li><code>rows == matrix.length</code></li>
	<li><code>cols == matrix[0].length</code></li>
	<li><code>1 &lt;= rows, cols &lt;= 200</code></li>
	<li><code>matrix[i][j]</code> 为 <code>'0'</code> 或 <code>'1'</code></li>
</ul>



## 解题思路

把每一行当作直方图底边，转化为“最大矩形（84 题）”的多次求解。

核心观察：

- 若把第 `i` 行作为矩形的底，那么每一列向上连续的 `1` 的个数就是该列在直方图中的高度 `height[j]`
- 当扫描到新的一行时：
  - 若 `matrix[i][j] == '1'`：`height[j] += 1`
  - 否则：`height[j] = 0`（被 0 截断）

对每一行的 `height[]`，用单调递增栈求“直方图最大矩形面积”：

- 栈中存放下标，保证对应高度单调递增
- 当遇到一个高度 `h` 小于栈顶高度时，说明以栈顶为“最矮柱”的最大扩展右边界已经确定，可以不断弹栈计算面积
- 宽度由“当前下标 i 作为右边界”与“弹栈后新的栈顶作为左边界”确定
- 末尾可追加一个高度 0 的哨兵，强制把栈清空，避免漏算

不变量：

- 栈内下标对应的高度严格递增（或非递减，取决于实现）；因此弹栈时能一次确定被弹元素的左右边界。

边界：

- 矩阵为空直接返回 0。

- 时间复杂度: $O(mn)$
- 空间复杂度: $O(n)$

说明：每行更新高度 $O(n)$，并用单调栈均摊 $O(n)$ 求一次直方图最大矩形。

## 代码
```python
class Solution:
    @staticmethod
    def largestRectangleArea(heights: List[int]) -> int:
        hs = [0] + heights + [0]   # 不修改入参
        stk = [0]
        ret = 0
        for i in range(1, len(hs)):
            while hs[i] < hs[stk[-1]]:
                mid = stk.pop()
                left = stk[-1]
                ret = max(ret, hs[mid] * (i - left - 1))
            stk.append(i)
        return ret

    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        R, C = len(matrix), len(matrix[0])
        heights = [0] * C
        ret = 0

        # 从最小的高度开始逐步上升，一旦中断就归零
        for r in range(R):
            for c in range(C):
                heights[c] = heights[c] + 1 if matrix[r][c] == '1' else 0
            ret = max(ret, self.largestRectangleArea(heights),)
        return ret
```
