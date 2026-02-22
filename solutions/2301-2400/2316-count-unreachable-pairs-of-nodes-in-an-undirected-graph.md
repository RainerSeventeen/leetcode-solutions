---
id: 2316
title: Count Unreachable Pairs of Nodes in an Undirected Graph
difficulty: Medium
tags: [depth-first-search, breadth-first-search, union-find, graph]
created: 2026-02-21
---

# 2316. 统计无向图中无法互相到达点对数

## 题目链接
https://leetcode.cn/problems/count-unreachable-pairs-of-nodes-in-an-undirected-graph/

## 题目描述
<p>给你一个整数&nbsp;<code>n</code>&nbsp;，表示一张<strong>&nbsp;无向图</strong>&nbsp;中有 <code>n</code>&nbsp;个节点，编号为&nbsp;<code>0</code>&nbsp;到&nbsp;<code>n - 1</code>&nbsp;。同时给你一个二维整数数组&nbsp;<code>edges</code>&nbsp;，其中&nbsp;<code>edges[i] = [a<sub>i</sub>, b<sub>i</sub>]</code>&nbsp;表示节点&nbsp;<code>a<sub>i</sub></code> 和&nbsp;<code>b<sub>i</sub></code>&nbsp;之间有一条&nbsp;<strong>无向</strong>&nbsp;边。</p>

<p>请你返回 <strong>无法互相到达</strong>&nbsp;的不同 <strong>点对数目</strong>&nbsp;。</p>

<p><strong>示例 1：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2022/05/05/tc-3.png" style="width: 267px; height: 169px;"></p>

<pre><b>输入：</b>n = 3, edges = [[0,1],[0,2],[1,2]]
<b>输出：</b>0
<b>解释：</b>所有点都能互相到达，意味着没有点对无法互相到达，所以我们返回 0 。
</pre>

<p><strong>示例 2：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2022/05/05/tc-2.png" style="width: 295px; height: 269px;"></p>

<pre><b>输入：</b>n = 7, edges = [[0,2],[0,5],[2,4],[1,6],[5,4]]
<b>输出：</b>14
<b>解释：</b>总共有 14 个点对互相无法到达：
[[0,1],[0,3],[0,6],[1,2],[1,3],[1,4],[1,5],[2,3],[2,6],[3,4],[3,5],[3,6],[4,6],[5,6]]
所以我们返回 14 。
</pre>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= edges.length &lt;= 2 * 10<sup>5</sup></code></li>
	<li><code>edges[i].length == 2</code></li>
	<li><code>0 &lt;= a<sub>i</sub>, b<sub>i</sub> &lt; n</code></li>
	<li><code>a<sub>i</sub> != b<sub>i</sub></code></li>
	<li>不会有重复边。</li>
</ul>


## 解题思路

先用并查集把无向图中连通的点合并，并维护每个连通块大小。
收集所有连通块大小后，按“前缀剩余点数”累计 `size * remaining`。
这样每对跨连通块点只会被计算一次。
- 时间复杂度: $O((n + m)\alpha(n))$
- 空间复杂度: $O(n)$

## 相关专题
- [图论算法](../../topics/graph-algorithms.md)

## 代码
```python
class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        # 并查集
        father = list(range(n))
        size = [1] * n
        def find(u):
            if father[u] != u:
                father[u] = find(father[u])
            return father[u]
        def union(a, b):
            a = find(a)
            b = find(b)
            if a == b:
                return
            if size[a] < size[b]:
                a, b = b, a
            father[b] = a
            size[a] += size[b]

        for s, e in edges:
            union(s, e)
        
        # 构造结果
        ret = 0
        tar = []
        count = n
        for i in range(n):
            if find(i) == i:
                tar.append(size[i])
        for t in tar:
            count -= t
            ret += t * count
        return ret
```
