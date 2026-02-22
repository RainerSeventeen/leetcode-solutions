---
id: 63
title: Unique Paths II
difficulty: Medium
tags: [array, dynamic-programming, matrix]
created: 2026-02-21
---

# 63. 不同路径 II

## 题目链接
https://leetcode.cn/problems/unique-paths-ii/

## 题目描述
<p>给定一个&nbsp;<code>m x n</code>&nbsp;的整数数组&nbsp;<code>grid</code>。一个机器人初始位于 <strong>左上角</strong>（即 <code>grid[0][0]</code>）。机器人尝试移动到 <strong>右下角</strong>（即 <code>grid[m - 1][n - 1]</code>）。机器人每次只能向下或者向右移动一步。</p>

<p>网格中的障碍物和空位置分别用 <code>1</code> 和 <code>0</code> 来表示。机器人的移动路径中不能包含 <strong>任何</strong>&nbsp;有障碍物的方格。</p>

<p>返回机器人能够到达右下角的不同路径数量。</p>

<p>测试用例保证答案小于等于 <code>2 * 10<sup>9</sup></code>。</p>

<p><strong>示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/11/04/robot1.jpg" />
<pre>
<strong>输入：</strong>obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
<strong>输出：</strong>2
<strong>解释：</strong>3x3 网格的正中间有一个障碍物。
从左上角到右下角一共有 <code>2</code> 条不同的路径：
1. 向右 -&gt; 向右 -&gt; 向下 -&gt; 向下
2. 向下 -&gt; 向下 -&gt; 向右 -&gt; 向右
</pre>

<p><strong>示例 2：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/11/04/robot2.jpg" />
<pre>
<strong>输入：</strong>obstacleGrid = [[0,1],[0,0]]
<strong>输出：</strong>1
</pre>

<p><strong>提示：</strong></p>

<ul>
	<li><code>m ==&nbsp;obstacleGrid.length</code></li>
	<li><code>n ==&nbsp;obstacleGrid[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 100</code></li>
	<li><code>obstacleGrid[i][j]</code> 为 <code>0</code> 或 <code>1</code></li>
</ul>


## 解题思路

- 直接原地复用网格作为 DP 表，障碍位置记为 0，非障碍位置累加上方和左方路径数。
- 起点先置为 1，遍历时跳过起点并处理边界，终点值即总路径数。

- 时间复杂度: $O(m \times n)$

- 空间复杂度: $O(1)$

## 相关专题
- [动态规划](../../topics/dynamic-programming.md)

## 代码
```cpp
class Solution {
public:
    int uniquePathsWithObstacles(vector<vector<int>>& obstacleGrid) {
        // 直接把原来数组当作dp数组
        if (obstacleGrid[0][0] == 1) return 0;
        obstacleGrid[0][0] = 1;
        int m = obstacleGrid.size();
        int n = obstacleGrid[0].size();
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (i == 0 && j == 0) continue;
                if (obstacleGrid[i][j] == 1) {
                    obstacleGrid[i][j] = 0;
                    continue; // 石头不处理
                }
                if (i - 1 >= 0)
                    obstacleGrid[i][j] += obstacleGrid[i - 1][j];
                if (j - 1 >= 0) 
                    obstacleGrid[i][j] += obstacleGrid[i][j - 1];
            }
        }
        return obstacleGrid[m - 1][n - 1];
    }
};
```
