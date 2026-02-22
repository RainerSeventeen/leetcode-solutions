---
id: 685
title: Redundant Connection II
difficulty: Hard
tags: [depth-first-search, breadth-first-search, union-find, graph]
created: 2026-02-21
---

# 685. 冗余连接 II

## 题目链接
https://leetcode.cn/problems/redundant-connection-ii/

## 题目描述
<p>在本问题中，有根树指满足以下条件的 <strong>有向</strong> 图。该树只有一个根节点，所有其他节点都是该根节点的后继。该树除了根节点之外的每一个节点都有且只有一个父节点，而根节点没有父节点。</p>

<p>输入一个有向图，该图由一个有着 <code>n</code> 个节点（节点值不重复，从 <code>1</code> 到 <code>n</code>）的树及一条附加的有向边构成。附加的边包含在 <code>1</code> 到 <code>n</code> 中的两个不同顶点间，这条附加的边不属于树中已存在的边。</p>

<p>结果图是一个以边组成的二维数组&nbsp;<code>edges</code> 。 每个元素是一对 <code>[u<sub>i</sub>, v<sub>i</sub>]</code>，用以表示 <strong>有向 </strong>图中连接顶点 <code>u<sub>i</sub></code> 和顶点 <code>v<sub>i</sub></code> 的边，其中 <code>u<sub>i</sub></code> 是 <code>v<sub>i</sub></code> 的一个父节点。</p>

<p>返回一条能删除的边，使得剩下的图是有 <code>n</code> 个节点的有根树。若有多个答案，返回最后出现在给定二维数组的答案。</p>

<p><strong class="example">示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/12/20/graph1.jpg" style="width: 222px; height: 222px;" />
<pre>
<strong>输入：</strong>edges = [[1,2],[1,3],[2,3]]
<strong>输出：</strong>[2,3]
</pre>

<p><strong class="example">示例 2：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/12/20/graph2.jpg" style="width: 222px; height: 382px;" />
<pre>
<strong>输入：</strong>edges = [[1,2],[2,3],[3,4],[4,1],[1,5]]
<strong>输出：</strong>[4,1]
</pre>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == edges.length</code></li>
	<li><code>3 &lt;= n &lt;= 1000</code></li>
	<li><code>edges[i].length == 2</code></li>
	<li><code>1 &lt;= u<sub>i</sub>, v<sub>i</sub> &lt;= n</code></li>
</ul>


## 解题思路

先扫描一次找是否存在入度为 2 的节点，记录两条候选父边 `cand1/cand2`。
用并查集校验：优先尝试删除后出现的候选边，若仍非法则删除先出现的边。
若不存在入度为 2，则直接并查集扫描，第一条导致成环的边就是答案。
- 时间复杂度: $O(n \alpha(n))$
- 空间复杂度: $O(n)$

## 相关专题
- [图论算法](../../topics/graph-algorithms.md)

## 代码
```python
from typing import List

class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)

        # 1) 找入度为 2 的节点对应的两条边：cand1(先出现的父边), cand2(后出现的父边)
        parent = [-1] * (n + 1)
        cand1 = None
        cand2 = None
        for a, b in edges:
            if parent[b] == -1:
                parent[b] = a
            else:
                # b 已经有父亲了：parent[b] -> b 是第一条；a -> b 是第二条
                cand1 = [parent[b], b]
                cand2 = [a, b]
                break

        # 并查集工具：每次 check 都要重置一套
        def check(skip_edge: List[int]) -> bool:
            fa = list(range(n + 1))

            def find(x: int) -> int:
                while fa[x] != x:
                    fa[x] = fa[fa[x]]
                    x = fa[x]
                return x

            def union(x: int, y: int) -> bool:
                rx, ry = find(x), find(y)
                if rx == ry:
                    return False
                fa[ry] = rx
                return True

            for x, y in edges:
                if skip_edge is not None and x == skip_edge[0] and y == skip_edge[1]:
                    continue
                if not union(x, y):  # 成环
                    return False
            return True

        # 2) 如果存在入度 2：优先删后出现的那条；若删它不成树，再删先出现的
        if cand1 is not None:
            if check(cand2):
                return cand2
            else:
                return cand1

        # 3) 不存在入度 2：直接找成环的那条边（并查集一次扫描）
        fa = list(range(n + 1))

        def find(x: int) -> int:
            while fa[x] != x:
                fa[x] = fa[fa[x]]
                x = fa[x]
            return x

        def union(x: int, y: int) -> bool:
            rx, ry = find(x), find(y)
            if rx == ry:
                return False
            fa[ry] = rx
            return True

        for a, b in edges:
            if not union(a, b):
                return [a, b]

        return []
```
