---
id: 1536
title: Minimum Swaps to Arrange a Binary Grid
difficulty: Medium
tags: [greedy, array, matrix]
created: 2026-03-02
---

# 1536. 排布二进制网格的最少交换次数

## 题目链接
https://leetcode.cn/problems/minimum-swaps-to-arrange-a-binary-grid/

## 题目描述
<p>给你一个&nbsp;<code>n&nbsp;x n</code>&nbsp;的二进制网格&nbsp;<code>grid</code>，每一次操作中，你可以选择网格的&nbsp;<strong>相邻两行</strong>&nbsp;进行交换。</p>

<p>一个符合要求的网格需要满足主对角线以上的格子全部都是 <strong>0</strong>&nbsp;。</p>

<p>请你返回使网格满足要求的最少操作次数，如果无法使网格符合要求，请你返回 <strong>-1</strong>&nbsp;。</p>

<p>主对角线指的是从&nbsp;<code>(1, 1)</code>&nbsp;到&nbsp;<code>(n, n)</code>&nbsp;的这些格子。</p>

<p><strong>示例 1：</strong></p>

<p><img alt="" src="https://assets.leetcode.cn/aliyun-lc-upload/uploads/2020/08/02/fw.jpg" style="height: 141px; width: 750px;"></p>

<pre><strong>输入：</strong>grid = [[0,0,1],[1,1,0],[1,0,0]]
<strong>输出：</strong>3
</pre>

<p><strong>示例 2：</strong></p>

<p><img alt="" src="https://assets.leetcode.cn/aliyun-lc-upload/uploads/2020/08/02/e2.jpg" style="height: 270px; width: 270px;"></p>

<pre><strong>输入：</strong>grid = [[0,1,1,0],[0,1,1,0],[0,1,1,0],[0,1,1,0]]
<strong>输出：</strong>-1
<strong>解释：</strong>所有行都是一样的，交换相邻行无法使网格符合要求。
</pre>

<p><strong>示例 3：</strong></p>

<p><img alt="" src="https://assets.leetcode.cn/aliyun-lc-upload/uploads/2020/08/02/e3.jpg" style="height: 210px; width: 210px;"></p>

<pre><strong>输入：</strong>grid = [[1,0,0],[1,1,0],[1,1,1]]
<strong>输出：</strong>0
</pre>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == grid.length</code></li>
	<li><code>n == grid[i].length</code></li>
	<li><code>1 &lt;= n&nbsp;&lt;= 200</code></li>
	<li><code>grid[i][j]</code>&nbsp;要么是&nbsp;<code>0</code>&nbsp;要么是&nbsp;<code>1</code>&nbsp;。</li>
</ul>


## 解题思路

- 对于第 `i` 行（0-indexed），主对角线上方都为 0 等价于该行最右侧的 `1` 的位置 `right[i] <= i`。
- 先预处理每一行最右侧 `1` 的下标（若整行全 0 则记为 `-1`）。
- 然后从上到下贪心处理第 `i` 行：在区间 `[i, n-1]` 找第一个满足 `right[j] <= i` 的行，把它通过相邻交换“冒泡”到 `i`，代价是 `j-i`。这是当前步最小代价选择，整体最优。
- 若某一步找不到可用行，则无解，返回 `-1`。

- 时间复杂度: $O(n^2)$。预处理最右侧 `1` 是 $O(n^2)$，贪心查找与移动在最坏情况下也是 $O(n^2)$。

- 空间复杂度: $O(n)$，用于保存每行最右侧 `1` 的位置。

## 相关专题
- [贪心与思维](../../topics/greedy-and-thinking.md)

## 代码
```python
class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        # 统计最右边的1的位置，然后执行排序
        n = len(grid)
        right = [-1] * n # 最右边的1的位置，初始就是没有，设为 -1
        for i in range(n):
            for j in range(n - 1, -1, -1):
                if grid[i][j] == 1:
                    right[i] = j
                    break
        # 条件: nums[i] <= i
        # 贪心: 从小到大，优先选择满足条件的最小的那个（代价最小）
        ret = 0
        for i in range(n - 1):
            # 目标 nums[i] <= i
            for j in range(i, n):
                if right[j] <= i:
                    ret += j - i # 从 j 移动到 i
                    tmp = right[j]
                    right[i + 1: j + 1] = right[i: j]
                    right[i] = tmp
                    break # i 处理完毕
            else:
                return -1 # 找不到符合条件的
        return ret
```
