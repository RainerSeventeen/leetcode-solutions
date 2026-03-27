---
id: 2946
title: Matrix Similarity After Cyclic Shifts
difficulty: Easy
tags: [array, math, matrix, simulation]
created: 2026-03-27
---

# 2946. 循环移位后的矩阵相似检查

## 题目链接
https://leetcode.cn/problems/matrix-similarity-after-cyclic-shifts/

## 题目描述
<p>给你一个<strong>下标从 0 开始</strong>且大小为 <code>m x n</code> 的整数矩阵 <code>mat</code> 和一个整数 <code>k</code> 。请你将矩阵中的<strong> 奇数</strong> 行循环 <strong>右</strong> 移 <code>k</code> 次，<strong>偶数</strong> 行循环 <strong>左</strong> 移 <code>k</code> 次。</p>

<p>如果初始矩阵和最终矩阵完全相同，则返回 <code>true</code> ，否则返回 <code>false</code> 。</p>

<p><strong class="example">示例 1：</strong></p>

<pre>
<strong>输入：</strong>mat = [[1,2,1,2],[5,5,5,5],[6,3,6,3]], k = 2
<strong>输出：</strong>true
<strong>解释：</strong>
<img alt="" src="https://assets.leetcode.com/uploads/2023/10/29/similarmatrix.png" style="width: 500px; height: 117px;" />

初始矩阵如图一所示。
图二表示对奇数行右移一次且对偶数行左移一次后的矩阵状态。
图三是经过两次循环移位后的最终矩阵状态，与初始矩阵相同。
因此，返回 true 。
</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<strong>输入：</strong>mat = [[2,2],[2,2]], k = 3
<strong>输出：</strong>true
<strong>解释：</strong>由于矩阵中的所有值都相等，即使进行循环移位，矩阵仍然保持不变。因此，返回 true 。
</pre>

<p><strong class="example">示例 3：</strong></p>

<pre>
<strong>输入：</strong>mat = [[1,2]], k = 1
<strong>输出：</strong>false
<strong>解释：</strong>循环移位一次后，mat = [[2,1]]，与初始矩阵不相等。因此，返回 false 。
</pre>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= mat.length &lt;= 25</code></li>
	<li><code>1 &lt;= mat[i].length &lt;= 25</code></li>
	<li><code>1 &lt;= mat[i][j] &lt;= 25</code></li>
	<li><code>1 &lt;= k &lt;= 50</code></li>
</ul>


## 解题思路

- 只需要逐行判断是否仍然相同。由于矩阵下标从 0 开始，偶数行向左循环移 `k` 次，奇数行向右循环移 `k` 次。
- 先把 `k` 对列数取模，然后对每一行按目标方向生成移位后的新行，与原行直接比较；任意一行不相同就返回 `false`。
- 如果所有行都匹配，说明矩阵经过操作后没有变化，返回 `true`。

- 时间复杂度: $O(mn)$，其中 `m` 是行数，`n` 是列数

- 空间复杂度: $O(n)$

## 相关专题
- [常用数据结构](../../topics/common-data-structures.md)

## 代码
```python
class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        n = len(mat)
        N = len(mat[0])
        k = k % N
        new_line = [0] * N

        def move(is_right, line):
            m = 1 if is_right else -1
            nonlocal new_line
            for i in range(N):
                nxt_idx = (i + N + m * k) % N
                new_line[nxt_idx] = line[i]
            return new_line

        ans = True
        for i in range(n):
            if i & 1 == 0:
                ans = (mat[i] == move(-1, mat[i]))
            else:
                ans = (mat[i] == move(1, mat[i]))
            if not ans:
                return False
        return True
```
