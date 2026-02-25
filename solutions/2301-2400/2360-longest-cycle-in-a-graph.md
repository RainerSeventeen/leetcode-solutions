---
id: 2360
title: Longest Cycle in a Graph
difficulty: Hard
tags: [depth-first-search, breadth-first-search, graph, topological-sort]
created: 2026-02-25
---

# 2360. 图中的最长环

## 题目链接
https://leetcode.cn/problems/longest-cycle-in-a-graph/

## 题目描述
<p>给你一个 <code>n</code>&nbsp;个节点的 <b>有向图</b>&nbsp;，节点编号为&nbsp;<code>0</code>&nbsp;到&nbsp;<code>n - 1</code>&nbsp;，其中每个节点&nbsp;<strong>至多</strong>&nbsp;有一条出边。</p>

<p>图用一个大小为 <code>n</code>&nbsp;下标从<strong>&nbsp;0</strong>&nbsp;开始的数组&nbsp;<code>edges</code>&nbsp;表示，节点 <code>i</code>&nbsp;到节点&nbsp;<code>edges[i]</code>&nbsp;之间有一条有向边。如果节点&nbsp;<code>i</code>&nbsp;没有出边，那么&nbsp;<code>edges[i] == -1</code>&nbsp;。</p>

<p>请你返回图中的 <strong>最长</strong>&nbsp;环，如果没有任何环，请返回 <code>-1</code>&nbsp;。</p>

<p>一个环指的是起点和终点是 <strong>同一个</strong>&nbsp;节点的路径。</p>

<p><strong>示例 1：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2022/06/08/graph4drawio-5.png" style="width: 335px; height: 191px;" /></p>

<pre>
<b>输入：</b>edges = [3,3,4,2,3]
<b>输出去：</b>3
<b>解释：</b>图中的最长环是：2 -&gt; 4 -&gt; 3 -&gt; 2 。
这个环的长度为 3 ，所以返回 3 。
</pre>

<p><strong>示例 2：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2022/06/07/graph4drawio-1.png" style="width: 171px; height: 161px;" /></p>

<pre>
<b>输入：</b>edges = [2,-1,3,1]
<b>输出：</b>-1
<b>解释：</b>图中没有任何环。
</pre>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == edges.length</code></li>
	<li><code>2 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>-1 &lt;= edges[i] &lt; n</code></li>
	<li><code>edges[i] != i</code></li>
</ul>


## 解题思路
每个点最多只有一条出边，可以按起点逐条“沿链走”。`visited[x]` 记录节点第一次被全局访问的时间戳。对每个起点，先记下本轮起始时间 `starttime`，沿着出边前进直到走到 `-1` 或走到已访问节点：
- 走到 `-1` 说明本轮无环；
- 走到已访问节点且其时间戳不小于 `starttime`，说明该节点在本轮路径中，形成一个环，长度为 `currtime - visited[curr]`。
遍历所有起点即可得到最长环。

- 时间复杂度: $O(n)$，其中 `n` 代表节点数
- 空间复杂度: $O(n)$，其中 `n` 代表节点数

## 相关专题
- [图论算法](../../topics/graph-algorithms.md)

## 代码
```python
class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        n = len(edges) # 节点数量
        ret = -1
        visited = [-1] * (n)
        currtime = 0
        for start in range(n):
            starttime = currtime
            curr = start
            while curr != -1 and visited[curr] == -1:
                visited[curr] = currtime
                currtime += 1
                curr = edges[curr]
            if curr == -1:
                continue # 没有环
            if visited[curr] >= starttime:
                ret = max(ret, currtime - visited[curr])
        return ret
```
