---
id: 310
title: Minimum Height Trees
difficulty: Medium
tags: [depth-first-search, breadth-first-search, graph, topological-sort]
created: 2026-02-20
---

# 310. 最小高度树

## 题目链接
https://leetcode.cn/problems/minimum-height-trees/

## 题目描述
<p>树是一个无向图，其中任何两个顶点只通过一条路径连接。 换句话说，任何一个没有简单环路的连通图都是一棵树。</p>

<p>给你一棵包含&nbsp;<code>n</code>&nbsp;个节点的树，标记为&nbsp;<code>0</code>&nbsp;到&nbsp;<code>n - 1</code> 。给定数字&nbsp;<code>n</code>&nbsp;和一个有 <code>n - 1</code> 条无向边的 <code>edges</code>&nbsp;列表（每一个边都是一对标签），其中 <code>edges[i] = [a<sub>i</sub>, b<sub>i</sub>]</code> 表示树中节点 <code>a<sub>i</sub></code> 和 <code>b<sub>i</sub></code> 之间存在一条无向边。</p>

<p>可选择树中任何一个节点作为根。当选择节点 <code>x</code> 作为根节点时，设结果树的高度为 <code>h</code> 。在所有可能的树中，具有最小高度的树（即，<code>min(h)</code>）被称为 <strong>最小高度树</strong> 。</p>

<p>请你找到所有的 <strong>最小高度树</strong> 并按 <strong>任意顺序</strong> 返回它们的根节点标签列表。</p>
树的 <strong>高度</strong> 是指根节点和叶子节点之间最长向下路径上边的数量。

<p><strong>示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/09/01/e1.jpg" style="height: 213px; width: 800px;" />
<pre>
<strong>输入：</strong>n = 4, edges = [[1,0],[1,2],[1,3]]
<strong>输出：</strong>[1]
<strong>解释：</strong>如图所示，当根是标签为 1 的节点时，树的高度是 1 ，这是唯一的最小高度树。</pre>

<p><strong>示例 2：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/09/01/e2.jpg" style="height: 321px; width: 800px;" />
<pre>
<strong>输入：</strong>n = 6, edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]
<strong>输出：</strong>[3,4]
</pre>

<ul>
</ul>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 2 * 10<sup>4</sup></code></li>
	<li><code>edges.length == n - 1</code></li>
	<li><code>0 &lt;= a<sub>i</sub>, b<sub>i</sub> &lt; n</code></li>
	<li><code>a<sub>i</sub> != b<sub>i</sub></code></li>
	<li>所有 <code>(a<sub>i</sub>, b<sub>i</sub>)</code> 互不相同</li>
	<li>给定的输入 <strong>保证</strong> 是一棵树，并且 <strong>不会有重复的边</strong></li>
</ul>


## 解题思路

叶节点剪枝（拓扑排序变体）。构建无向图并统计每个节点的度，将所有度为 1 的叶节点入队，每轮批量移除叶节点并更新相邻节点的度，产生新叶节点后继续剪枝，直到剩余节点数 ≤ 2，最终队列中的节点即为最小高度树的根。树的中心最多只有 1~2 个节点，这是该算法正确性的保证。

- 时间复杂度: $O(n)$

- 空间复杂度: $O(n)$

## 相关专题
- [图论算法](../../topics/graph-algorithms.md)

## 代码
```python
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # 树的高度是由最长的那条链路决定的
        # 从两头开始逐步逼近中心可以获取最中间的那（两）个节点
        if n == 1:
            return [0]
        g = [[] for _ in range(n)]
        count = [0] * n # 统计度
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)
            count[u] += 1
            count[v] += 1
        q = deque()
        for i, c in enumerate(count):
            if c == 1:
                q.append(i)
        left = n
        while left > 2:
            for _ in range(len(q)): # 一轮拿走所有的 deg = 1的节点
                curr = q.popleft()
                left -= 1
                # 移除所有的相关的度
                for nxt in g[curr]:
                    count[nxt] -= 1
                    if count[nxt] == 1:
                        q.append(nxt)
        return list(q)
```
