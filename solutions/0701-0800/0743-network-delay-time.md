---
id: 743
title: Network Delay Time
difficulty: Medium
tags: [depth-first-search, breadth-first-search, graph, shortest-path, heap-priority-queue]
created: 2026-02-25
---

# 743. 网络延迟时间

## 题目链接
https://leetcode.cn/problems/network-delay-time/

## 题目描述
<p>有 <code>n</code> 个网络节点，标记为&nbsp;<code>1</code>&nbsp;到 <code>n</code>。</p>

<p>给你一个列表&nbsp;<code>times</code>，表示信号经过 <strong>有向</strong> 边的传递时间。&nbsp;<code>times[i] = (u<sub>i</sub>, v<sub>i</sub>, w<sub>i</sub>)</code>，其中&nbsp;<code>u<sub>i</sub></code>&nbsp;是源节点，<code>v<sub>i</sub></code>&nbsp;是目标节点， <code>w<sub>i</sub></code>&nbsp;是一个信号从源节点传递到目标节点的时间。</p>

<p>现在，从某个节点&nbsp;<code>K</code>&nbsp;发出一个信号。需要多久才能使所有节点都收到信号？如果不能使所有节点收到信号，返回&nbsp;<code>-1</code> 。</p>

<p><strong>示例 1：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2019/05/23/931_example_1.png" style="height: 220px; width: 200px;" /></p>

<pre>
<strong>输入：</strong>times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
<strong>输出：</strong>2
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>times = [[1,2,1]], n = 2, k = 1
<strong>输出：</strong>1
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>times = [[1,2,1]], n = 2, k = 2
<strong>输出：</strong>-1
</pre>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= k &lt;= n &lt;= 100</code></li>
	<li><code>1 &lt;= times.length &lt;= 6000</code></li>
	<li><code>times[i].length == 3</code></li>
	<li><code>1 &lt;= u<sub>i</sub>, v<sub>i</sub> &lt;= n</code></li>
	<li><code>u<sub>i</sub> != v<sub>i</sub></code></li>
	<li><code>0 &lt;= w<sub>i</sub> &lt;= 100</code></li>
	<li>所有 <code>(u<sub>i</sub>, v<sub>i</sub>)</code> 对都 <strong>互不相同</strong>（即，不含重复边）</li>
</ul>


## 解题思路
使用 Dijkstra 求源点 `k` 到所有点的最短路。先把边构造成邻接表，然后用最小堆每次取当前距离最小的点，若该距离不是最新最短路则跳过；否则尝试松弛其出边。最终若存在不可达点返回 `-1`，否则返回最远最短路。

- 时间复杂度: $O((n+m)\log n)$，其中 `n` 代表节点数，`m` 代表边数
- 空间复杂度: $O(n+m)$，其中 `n` 代表节点数，`m` 代表边数

## 相关专题
- [图论算法](../../topics/graph-algorithms.md)

## 代码
```python
import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # 优化算法，使用 heapq 以及 邻接表
        # 1. 构造邻接表
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u - 1].append((v - 1, w))

        # 2. Dijkstra
        dist = [float('inf')] * n
        dist[k - 1] = 0

        heap = [(0, k - 1)]  # (当前距离, 节点)

        while heap:
            d, u = heapq.heappop(heap)

            if d > dist[u]:
                continue  # 这是堆优化 Dijkstra 的关键剪枝

            for v, w in graph[u]:
                if dist[v] > d + w:
                    dist[v] = d + w
                    heapq.heappush(heap, (dist[v], v))

        ans = max(dist)
        return -1 if ans == float('inf') else ans
```

```python
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # 构造邻接表, 0 base
        INF = float('inf')
        edges = [[INF] * n for _ in range(n)]
        for u, v, w in times: # u -> v
            edges[u - 1][v - 1] = w

        def dijkstra(graph, start):
            visited = [False] * n
            dist = [INF] * n
            dist[start] = 0

            for _ in range(n):
                # 拿最近的下一个点
                u = -1
                for i in range(n):
                    if not visited[i] and (u == -1 or dist[i] < dist[u]):
                        u = i
                if u == -1:
                    break # 全都不可到达

                visited[u] = True # 标记访问
                for v in range(n):  # 更新所有的未访问的节点的距离
                    if not visited[v] and graph[u][v] != INF: # 可以到达且没有访问过
                        dist[v] = min(dist[v], dist[u] + graph[u][v])

            return dist
        ret = max(dijkstra(edges, k - 1)) # 注意 1 base 转化
        return -1 if ret == INF else ret
```
