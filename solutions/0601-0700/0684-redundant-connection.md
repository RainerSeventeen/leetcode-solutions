---
id: 684
title: Redundant Connection
difficulty: Medium
tags: [depth-first-search, breadth-first-search, union-find, graph]
created: 2026-02-20
---

# 684. 冗余连接

## 题目链接
https://leetcode.cn/problems/redundant-connection/

## 题目描述
<p>树可以看成是一个连通且 <strong>无环&nbsp;</strong>的&nbsp;<strong>无向&nbsp;</strong>图。</p>

<p>给定一个图，该图从一棵&nbsp;<code>n</code> 个节点 (节点值&nbsp;<code>1～n</code>) 的树中添加一条边后获得。添加的边的两个不同顶点编号在 <code>1</code> 到 <code>n</code>&nbsp;中间，且这条附加的边不属于树中已存在的边。图的信息记录于长度为 <code>n</code> 的二维数组 <code>edges</code>&nbsp;，<code>edges[i] = [a<sub>i</sub>, b<sub>i</sub>]</code>&nbsp;表示图中在 <code>ai</code> 和 <code>bi</code> 之间存在一条边。</p>

<p>请找出一条可以删去的边，删除后可使得剩余部分是一个有着 <code>n</code> 个节点的树。如果有多个答案，则返回数组&nbsp;<code>edges</code>&nbsp;中最后出现的那个。</p>

<p><strong>示例 1：</strong></p>

<p><img alt="" src="https://pic.leetcode.cn/1626676174-hOEVUL-image.png" style="width: 152px; " /></p>

<pre>
<strong>输入:</strong> edges = [[1,2], [1,3], [2,3]]
<strong>输出:</strong> [2,3]
</pre>

<p><strong>示例 2：</strong></p>

<p><img alt="" src="https://pic.leetcode.cn/1626676179-kGxcmu-image.png" style="width: 250px; " /></p>

<pre>
<strong>输入:</strong> edges = [[1,2], [2,3], [3,4], [1,4], [1,5]]
<strong>输出:</strong> [1,4]
</pre>

<p><strong>提示:</strong></p>

<ul>
	<li><code>n == edges.length</code></li>
	<li><code>3 &lt;= n &lt;= 1000</code></li>
	<li><code>edges[i].length == 2</code></li>
	<li><code>1 &lt;= ai&nbsp;&lt; bi&nbsp;&lt;= edges.length</code></li>
	<li><code>ai != bi</code></li>
	<li><code>edges</code> 中无重复元素</li>
	<li>给定的图是连通的&nbsp;</li>
</ul>


## 解题思路

这题等价于在一棵树上额外加了一条边，要求找出这条导致成环的边。并查集非常适合处理“两个点是否已经连通”的判断：如果当前边的两个端点已经在同一个集合，再连这条边就会形成环，这条边就是答案。

做法是顺序遍历 `edges`。每次先判断两端点是否同根：同根则直接返回当前边；不同根则执行合并。题目要求“若有多个答案，返回数组中最后出现的那条”，而输入保证是树加一条边，按顺序第一次检测到的成环边就是需要返回的边。

- 时间复杂度: $O(n \cdot \alpha(n))$，其中 $n$ 是边数，$\alpha$ 是阿克曼函数的反函数，增长极慢，近似常数。
- 空间复杂度: $O(n)$，用于并查集父节点与集合大小数组。

## 代码
```python
from typing import List


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = list(range(n + 1))
        size = [1] * (n + 1)

        def find(x: int) -> int:
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(a: int, b: int) -> bool:
            ra = find(a)
            rb = find(b)
            if ra == rb:
                return False
            if size[ra] < size[rb]:
                ra, rb = rb, ra
            parent[rb] = ra
            size[ra] += size[rb]
            return True

        for a, b in edges:
            if not union(a, b):
                return [a, b]
        return []
```
