---
id: 797
title: All Paths From Source to Target
difficulty: Medium
tags: [depth-first-search, breadth-first-search, graph, backtracking]
created: 2026-02-21
---

# 797. 所有可能的路径

## 题目链接
https://leetcode.cn/problems/all-paths-from-source-to-target/

## 题目描述
<p>给你一个有&nbsp;<code>n</code>&nbsp;个节点的 <strong>有向无环图（DAG）</strong>，请你找出从节点 <code>0</code>&nbsp;到节点 <code>n-1</code>&nbsp;的所有路径并输出（<strong>不要求按特定顺序</strong>）</p>

<p><meta charset="UTF-8" />&nbsp;<code>graph[i]</code>&nbsp;是一个从节点 <code>i</code> 可以访问的所有节点的列表（即从节点 <code>i</code> 到节点&nbsp;<code>graph[i][j]</code>存在一条有向边）。</p>

<p><strong>示例 1：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2020/09/28/all_1.jpg" /></p>

<pre>
<strong>输入：</strong>graph = [[1,2],[3],[3],[]]
<strong>输出：</strong>[[0,1,3],[0,2,3]]
<strong>解释：</strong>有两条路径 0 -&gt; 1 -&gt; 3 和 0 -&gt; 2 -&gt; 3
</pre>

<p><strong>示例 2：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2020/09/28/all_2.jpg" /></p>

<pre>
<strong>输入：</strong>graph = [[4,3,1],[3,2,4],[3],[4],[]]
<strong>输出：</strong>[[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]
</pre>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == graph.length</code></li>
	<li><code>2 &lt;= n &lt;= 15</code></li>
	<li><code>0 &lt;= graph[i][j] &lt; n</code></li>
	<li><code>graph[i][j] != i</code>（即不存在自环）</li>
	<li><code>graph[i]</code> 中的所有元素 <strong>互不相同</strong></li>
	<li>保证输入为 <strong>有向无环图（DAG）</strong></li>
</ul>



## 解题思路

图是 DAG，使用 DFS 回溯枚举从 `0` 到 `n-1` 的所有路径。
递归时把下一节点加入 `path`，到终点就拷贝当前路径到答案。
返回上一层前执行 `pop` 回溯，继续尝试其它分支。
- 时间复杂度: $O(P \cdot n)$
- 空间复杂度: $O(n)$

## 代码
```python
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        ret = []
        n = len(graph)
        # visited = [False] * n  这是用来防止环路的，但是 DAG 是没有环的
        def dfs(path, curr):
            if curr == n - 1:
                ret.append(path.copy())
                return
            for nxt in graph[curr]:
                    path.append(nxt)
                    dfs(path, nxt)
                    path.pop()
        dfs([0], 0)
        return ret
```
