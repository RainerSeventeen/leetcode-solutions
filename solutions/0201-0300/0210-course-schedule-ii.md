---
id: 210
title: Course Schedule II
difficulty: Medium
tags: [depth-first-search, breadth-first-search, graph, topological-sort]
created: 2026-02-21
---

# 210. 课程表 II

## 题目链接
https://leetcode.cn/problems/course-schedule-ii/

## 题目描述
<p>现在你总共有 <code>numCourses</code> 门课需要选，记为&nbsp;<code>0</code>&nbsp;到&nbsp;<code>numCourses - 1</code>。给你一个数组&nbsp;<code>prerequisites</code> ，其中 <code>prerequisites[i] = [a<sub>i</sub>, b<sub>i</sub>]</code> ，表示在选修课程 <code>a<sub>i</sub></code> 前 <strong>必须</strong> 先选修&nbsp;<code>b<sub>i</sub></code> 。</p>

<ul>
	<li>例如，想要学习课程 <code>0</code> ，你需要先完成课程&nbsp;<code>1</code> ，我们用一个匹配来表示：<code>[0,1]</code> 。</li>
</ul>

<p>返回你为了学完所有课程所安排的学习顺序。可能会有多个正确的顺序，你只要返回 <strong>任意一种</strong> 就可以了。如果不可能完成所有课程，返回 <strong>一个空数组</strong> 。</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>numCourses = 2, prerequisites = [[1,0]]
<strong>输出：</strong>[0,1]
<strong>解释：</strong>总共有 2 门课程。要学习课程 1，你需要先完成课程 0。因此，正确的课程顺序为 <code>[0,1] 。</code>
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
<strong>输出：</strong>[0,2,1,3]
<strong>解释：</strong>总共有 4 门课程。要学习课程 3，你应该先完成课程 1 和课程 2。并且课程 1 和课程 2 都应该排在课程 0 之后。
因此，一个正确的课程顺序是&nbsp;<code>[0,1,2,3]</code> 。另一个正确的排序是&nbsp;<code>[0,2,1,3]</code> 。</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>numCourses = 1, prerequisites = []
<strong>输出：</strong>[0]
</pre>

<strong>提示：</strong>

<ul>
	<li><code>1 &lt;= numCourses &lt;= 2000</code></li>
	<li><code>0 &lt;= prerequisites.length &lt;= numCourses * (numCourses - 1)</code></li>
	<li><code>prerequisites[i].length == 2</code></li>
	<li><code>0 &lt;= a<sub>i</sub>, b<sub>i</sub> &lt; numCourses</code></li>
	<li><code>a<sub>i</sub> != b<sub>i</sub></code></li>
	<li>所有<code>[a<sub>i</sub>, b<sub>i</sub>]</code> <strong>互不相同</strong></li>
</ul>


## 解题思路

先建图并统计每门课的入度，入度为 0 的课程先入队。
每次弹出一门可学课程，把它加入答案，并把它指向课程的入度减 1。
若某门课入度减到 0，就继续入队；最后若数量不足 `numCourses` 说明有环。
- 时间复杂度: $O(n + m)$
- 空间复杂度: $O(n + m)$

## 代码
```python
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # 队列 + 入度数组 + 出度邻接表
        # 表： graph[a] =[b], a -> b
        graph = [[] for _ in range(numCourses)]
        in_count = [0] * numCourses # 入度计数
        for a, b in prerequisites:
            graph[b].append(a)
            in_count[a] += 1

        start = [i for i in range(numCourses) if in_count[i] == 0]
        q = deque(start)

        ret = []
        while q:
            nxt = q.pop()
            ret.append(nxt)
            for e in graph[nxt]:
                in_count[e] -= 1
                if in_count[e] == 0:
                    q.appendleft(e)
        
        
        return [] if len(ret) != numCourses else ret
```
