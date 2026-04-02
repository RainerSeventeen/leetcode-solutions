---
id: 3418
title: Maximum Amount of Money Robot Can Earn
difficulty: Medium
tags: [array, dynamic-programming, matrix]
created: 2026-04-02
---

# 3418. 机器人可以获得的最大金币数

## 题目链接
https://leetcode.cn/problems/maximum-amount-of-money-robot-can-earn/

## 题目描述
<p>给你一个 <code>m x n</code> 的网格。一个机器人从网格的左上角 <code>(0, 0)</code> 出发，目标是到达网格的右下角 <code>(m - 1, n - 1)</code>。在任意时刻，机器人只能向右或向下移动。</p>

<p>网格中的每个单元格包含一个值 <code>coins[i][j]</code>：</p>

<ul>
	<li>如果 <code>coins[i][j] &gt;= 0</code>，机器人可以获得该单元格的金币。</li>
	<li>如果 <code>coins[i][j] &lt; 0</code>，机器人会遇到一个强盗，强盗会抢走该单元格数值的&nbsp;<strong>绝对值</strong> 的金币。</li>
</ul>

<p>机器人有一项特殊能力，可以在行程中&nbsp;<strong>最多感化&nbsp;</strong>2个单元格的强盗，从而防止这些单元格的金币被抢走。</p>

<p><strong>注意：</strong>机器人的总金币数可以是负数。</p>

<p>返回机器人在路径上可以获得的&nbsp;<strong>最大金币数&nbsp;</strong>。</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">coins = [[0,1,-1],[1,-2,3],[2,-3,4]]</span></p>

<p><strong>输出：</strong> <span class="example-io">8</span></p>

<p><strong>解释：</strong></p>

<p>一个获得最多金币的最优路径如下：</p>

<ol>
	<li>从 <code>(0, 0)</code> 出发，初始金币为 <code>0</code>（总金币 = <code>0</code>）。</li>
	<li>移动到 <code>(0, 1)</code>，获得 <code>1</code> 枚金币（总金币 = <code>0 + 1 = 1</code>）。</li>
	<li>移动到 <code>(1, 1)</code>，遇到强盗抢走 <code>2</code> 枚金币。机器人在此处使用一次感化能力，避免被抢（总金币 = <code>1</code>）。</li>
	<li>移动到 <code>(1, 2)</code>，获得 <code>3</code> 枚金币（总金币 = <code>1 + 3 = 4</code>）。</li>
	<li>移动到 <code>(2, 2)</code>，获得 <code>4</code> 枚金币（总金币 = <code>4 + 4 = 8</code>）。</li>
</ol>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">coins = [[10,10,10],[10,10,10]]</span></p>

<p><strong>输出：</strong> <span class="example-io">40</span></p>

<p><strong>解释：</strong></p>

<p>一个获得最多金币的最优路径如下：</p>

<ol>
	<li>从 <code>(0, 0)</code> 出发，初始金币为 <code>10</code>（总金币 = <code>10</code>）。</li>
	<li>移动到 <code>(0, 1)</code>，获得 <code>10</code> 枚金币（总金币 = <code>10 + 10 = 20</code>）。</li>
	<li>移动到 <code>(0, 2)</code>，再获得 <code>10</code> 枚金币（总金币 = <code>20 + 10 = 30</code>）。</li>
	<li>移动到 <code>(1, 2)</code>，获得 <code>10</code> 枚金币（总金币 = <code>30 + 10 = 40</code>）。</li>
</ol>
</div>

<p><strong>提示：</strong></p>

<ul>
	<li><code>m == coins.length</code></li>
	<li><code>n == coins[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 500</code></li>
	<li><code>-1000 &lt;= coins[i][j] &lt;= 1000</code></li>
</ul>


## 解题思路

用三维动态规划统计到达每个格子时，已经感化了 `0/1/2` 个强盗时的最大金币数。设 `dp[i][j][k]` 表示走到 `(i, j)` 且已用掉 `k` 次感化能力的最大收益。转移时只会从上方或左方来，所以先继承两侧状态中的较大值，再根据当前格子是否为负数决定是否要消耗一次感化能力。最终答案就是右下角三个状态里的最大值。

- 时间复杂度: $O(mn)$

- 空间复杂度: $O(mn)$

## 相关专题
- [动态规划](../../topics/dynamic-programming.md)

## 代码
```python
class Solution:
    def maximumAmount(self, coins: List[List[int]]) -> int:
        # 可以选择两个 负数变成正数, 向右下移动
        # 维护一个： 三个子数组的dp
        n = len(coins)
        m = len(coins[0])
        dp = [[[-inf] * 3 for _ in range(m)] for _ in range(n)]

        def dp_forward(curr_coin, curr_dp, pre1, pre2):
            if not pre2:
                pre2 = [-inf] * 3
            curr_dp[2] = max(pre1[2], pre2[2]) + curr_coin
            curr_dp[1] = max(pre1[1], pre2[1]) + curr_coin
            curr_dp[0] = max(pre1[0], pre2[0]) + curr_coin
            if curr_coin < 0:
                curr_dp[1] = max(curr_dp[1], pre1[2], pre2[2]) # 用一次感化
                curr_dp[0] = max(curr_dp[0], pre1[1], pre2[1]) # 用一次感化
            
        # 初始化
        dp[0][0] = [coins[0][0]] * 3
        if coins[0][0] < 0:
            # 第一格子有强盗，可以感化
            dp[0][0][1] = 0
            dp[0][0][0] = 0
        for j in range(1, m):
            dp_forward(coins[0][j], dp[0][j], dp[0][j - 1], None)
            # print(0, j, dp[0][j])

        # 上到下，左到右
        for i in range(1, n):
            dp_forward(coins[i][0], dp[i][0], dp[i - 1][0], None)
            for j in range(1, m):
                dp_forward(coins[i][j], dp[i][j], dp[i][j - 1], dp[i - 1][j])
                # print(i, j, dp[i][j])

        return max(dp[n - 1][m - 1])
```
