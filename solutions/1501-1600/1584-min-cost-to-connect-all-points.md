---
id: 1584
title: Min Cost to Connect All Points
difficulty: Medium
tags: [union-find, graph, array, minimum-spanning-tree]
created: 2026-02-21
---

# 1584. 连接所有点的最小费用

## 题目链接
https://leetcode.cn/problems/min-cost-to-connect-all-points/

## 题目描述
<p>给你一个<code>points</code>&nbsp;数组，表示 2D 平面上的一些点，其中&nbsp;<code>points[i] = [x<sub>i</sub>, y<sub>i</sub>]</code>&nbsp;。</p>

<p>连接点&nbsp;<code>[x<sub>i</sub>, y<sub>i</sub>]</code> 和点&nbsp;<code>[x<sub>j</sub>, y<sub>j</sub>]</code>&nbsp;的费用为它们之间的 <strong>曼哈顿距离</strong>&nbsp;：<code>|x<sub>i</sub> - x<sub>j</sub>| + |y<sub>i</sub> - y<sub>j</sub>|</code>&nbsp;，其中&nbsp;<code>|val|</code>&nbsp;表示&nbsp;<code>val</code>&nbsp;的绝对值。</p>

<p>请你返回将所有点连接的最小总费用。只有任意两点之间 <strong>有且仅有</strong>&nbsp;一条简单路径时，才认为所有点都已连接。</p>

<p><strong>示例 1：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2020/08/26/d.png" style="height:268px; width:214px; background:#e5e5e5" /></p>

<pre>
<strong>输入：</strong>points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
<strong>输出：</strong>20
<strong>解释：
</strong><img alt="" src="https://assets.leetcode.com/uploads/2020/08/26/c.png" style="height:268px; width:214px; background:#e5e5e5" />
我们可以按照上图所示连接所有点得到最小总费用，总费用为 20 。
注意到任意两个点之间只有唯一一条路径互相到达。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>points = [[3,12],[-2,5],[-4,1]]
<strong>输出：</strong>18
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>points = [[0,0],[1,1],[1,0],[-1,1]]
<strong>输出：</strong>4
</pre>

<p><strong>示例 4：</strong></p>

<pre>
<strong>输入：</strong>points = [[-1000000,-1000000],[1000000,1000000]]
<strong>输出：</strong>4000000
</pre>

<p><strong>示例 5：</strong></p>

<pre>
<strong>输入：</strong>points = [[0,0]]
<strong>输出：</strong>0
</pre>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= points.length &lt;= 1000</code></li>
	<li><code>-10<sup>6</sup>&nbsp;&lt;= x<sub>i</sub>, y<sub>i</sub> &lt;= 10<sup>6</sup></code></li>
	<li>所有点&nbsp;<code>(x<sub>i</sub>, y<sub>i</sub>)</code>&nbsp;两两不同。</li>
</ul>


## 解题思路

这份代码是朴素 Prim：`dis[i]` 表示当前生成树到点 `i` 的最小连边代价。
每轮选一个未访问且 `dis` 最小的点加入生成树，并累加该代价到答案。
再用新点去更新其余未访问点的曼哈顿距离，重复 `n` 轮得到最小生成树。
- 时间复杂度: $O(n^2)$
- 空间复杂度: $O(n)$

## 相关专题
- [图论算法](../../topics/graph-algorithms.md)

## 代码
```python
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        INF = 10**7

        # dis[i]: 当前生成树集合 S 到点 i 的最小连接边权
        dis = [INF] * n
        dis[0] = 0

        visited = [False] * n
        ret = 0

        for _ in range(n):
            # 1) 选出未访问点里 dis 最小的那个点 u
            u = -1
            best = INF
            for i in range(n):
                if not visited[i] and dis[i] < best:
                    best = dis[i]
                    u = i

            visited[u] = True
            ret += best

            # 2) 用新加入的点 u 去更新其他未访问点的 dis
            x, y = points[u]
            for v in range(n):
                if visited[v]:
                    continue
                nx, ny = points[v]
                w = abs(x - nx) + abs(y - ny)
                if w < dis[v]:
                    dis[v] = w

        return ret
```
