---
id: 3070
title: Count Submatrices with Top-Left Element and Sum Less Than k
difficulty: Medium
tags: [array, matrix, prefix-sum]
created: 2026-03-18
---

# 3070. 元素和小于等于 k 的子矩阵的数目

## 题目链接
https://leetcode.cn/problems/count-submatrices-with-top-left-element-and-sum-less-than-k/

## 题目描述
<p>给你一个下标从 <strong>0</strong> 开始的整数矩阵 <code>grid</code> 和一个整数 <code>k</code>。</p>

<p>返回包含 <code>grid</code> 左上角元素、元素和小于或等于 <code>k</code> 的 <strong><span data-keyword="submatrix">子矩阵</span></strong>的数目。</p>

<p><strong class="example">示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2024/01/01/example1.png" style="padding: 10px; background: #fff; border-radius: .5rem;" />
<pre>
<strong>输入：</strong>grid = [[7,6,3],[6,6,1]], k = 18
<strong>输出：</strong>4
<strong>解释：</strong>如上图所示，只有 4 个子矩阵满足：包含 grid 的左上角元素，并且元素和小于或等于 18 。</pre>

<p><strong class="example">示例 2：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2024/01/01/example21.png" style="padding: 10px; background: #fff; border-radius: .5rem;" />
<pre>
<strong>输入：</strong>grid = [[7,2,9],[1,5,0],[2,6,6]], k = 20
<strong>输出：</strong>6
<strong>解释：</strong>如上图所示，只有 6 个子矩阵满足：包含 grid 的左上角元素，并且元素和小于或等于 20 。
</pre>

<p><strong>提示：</strong></p>

<ul>
	<li><code>m == grid.length </code></li>
	<li><code>n == grid[i].length</code></li>
	<li><code>1 &lt;= n, m &lt;= 1000 </code></li>
	<li><code>0 &lt;= grid[i][j] &lt;= 1000</code></li>
	<li><code>1 &lt;= k &lt;= 10<sup>9</sup></code></li>
</ul>


## 解题思路

- 先用二维前缀和预处理出任意左上角子矩阵的和，这样每个位置 `(i, j)` 的答案都能直接在 `O(1)` 时间内得到。
- 由于题目只要求统计左上角为 `(0, 0)` 的子矩阵，所以只需要枚举右下角位置，判断对应前缀和是否不超过 `k` 即可。
- 这里 `n` 表示行数，`m` 表示列数。

- 时间复杂度: $O(nm)$

- 空间复杂度: $O(nm)$

## 相关专题
- [常用数据结构](../../topics/common-data-structures.md)

## 代码
```python
class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        # 矩阵前缀和
        n = len(grid)
        m = len(grid[0])
        presum = [[0] * (m + 1) for _ in range(n + 1)]
        
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                presum[i][j] = presum[i - 1][j] + presum[i][j - 1] - presum[i - 1][j - 1] + grid[i - 1][j - 1]

        ans = 0
        for i in range(n):
            for j in range(m):
                s = presum[i + 1][j + 1]
                if s > k:
                    continue
                ans += 1
                # print(i, j, s)
        
        return ans
```
