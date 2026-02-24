---
id: 851
title: Loud and Rich
difficulty: Medium
tags: [depth-first-search, graph, topological-sort, array]
created: 2026-02-24
---

# 851. 喧闹和富有

## 题目链接
https://leetcode.cn/problems/loud-and-rich/

## 题目描述
<p>有一组 <code>n</code> 个人作为实验对象，从 <code>0</code> 到 <code>n - 1</code> 编号，其中每个人都有不同数目的钱，以及不同程度的安静值（quietness）。为了方便起见，我们将编号为&nbsp;<code>x</code>&nbsp;的人简称为 "person&nbsp;<code>x</code>&nbsp;"。</p>

<p>给你一个数组 <code>richer</code> ，其中 <code>richer[i] = [a<sub>i</sub>, b<sub>i</sub>]</code> 表示 person&nbsp;<code>a<sub>i</sub></code>&nbsp;比 person&nbsp;<code>b<sub>i</sub></code>&nbsp;更有钱。另给你一个整数数组 <code>quiet</code> ，其中&nbsp;<code>quiet[i]</code> 是 person <code>i</code> 的安静值。<code>richer</code> 中所给出的数据 <strong>逻辑自洽</strong>（也就是说，在 person <code>x</code> 比 person <code>y</code> 更有钱的同时，不会出现 person <code>y</code> 比 person <code>x</code> 更有钱的情况 ）。</p>

<p>现在，返回一个整数数组 <code>answer</code> 作为答案，其中&nbsp;<code>answer[x] = y</code>&nbsp;的前提是，在所有拥有的钱肯定不少于&nbsp;person&nbsp;<code>x</code>&nbsp;的人中，person&nbsp;<code>y</code>&nbsp;是最不安静的人（也就是安静值&nbsp;<code>quiet[y]</code>&nbsp;最小的人）。</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>richer = [[1,0],[2,1],[3,1],[3,7],[4,3],[5,3],[6,3]], quiet = [3,2,5,4,6,1,7,0]
<strong>输出：</strong>[5,5,2,5,4,5,6,7]
<strong>解释： </strong>
answer[0] = 5，
person 5 比 person 3 有更多的钱，person 3 比 person 1 有更多的钱，person 1 比 person 0 有更多的钱。
唯一较为安静（有较低的安静值 quiet[x]）的人是 person 7，
但是目前还不清楚他是否比 person 0 更有钱。
answer[7] = 7，
在所有拥有的钱肯定不少于 person 7 的人中（这可能包括 person 3，4，5，6 以及 7），
最安静（有较低安静值 quiet[x]）的人是 person 7。
其他的答案也可以用类似的推理来解释。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>richer = [], quiet = [0]
<strong>输出：</strong>[0]
</pre>
&nbsp;

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == quiet.length</code></li>
	<li><code>1 &lt;= n &lt;= 500</code></li>
	<li><code>0 &lt;= quiet[i] &lt; n</code></li>
	<li><code>quiet</code> 的所有值 <strong>互不相同</strong></li>
	<li><code>0 &lt;= richer.length &lt;= n * (n - 1) / 2</code></li>
	<li><code>0 &lt;= a<sub>i</sub>, b<sub>i</sub> &lt; n</code></li>
	<li><code>a<sub>i </sub>!= b<sub>i</sub></code></li>
	<li><code>richer</code> 中的所有数对 <strong>互不相同</strong></li>
	<li>对<strong> </strong><code>richer</code> 的观察在逻辑上是一致的</li>
</ul>


## 解题思路

把关系 `a > b` 建图为 `a -> b`，并统计每个点入度。  
`ret[i]` 表示“在所有肯定不少于 `i` 的人里，当前最安静的那个人编号”，初始为 `i` 本人。
对入度为 0 的点做拓扑 BFS：从 `curr` 走向 `nxt` 时，用 `ret[curr]` 去更新 `ret[nxt]`，
表示把“更有钱前驱集合里更安静的人”向后传递。最后得到每个节点答案。
- 时间复杂度: $O(n+m)$，其中 $n$ 是人数，$m$ 是 `richer` 边数
- 空间复杂度: $O(n+m)$

## 相关专题
- [图论算法](../../topics/graph-algorithms.md)

## 代码
```python
class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        # 建立邻接表
        n = len(quiet)
        in_count = [0] * n
        ret = list(range(n))
        edge = [[] for _ in range(n)] # edge[a] = [b] 表示 a > b
        for a, b in richer:
            edge[a].append(b)
            in_count[b] += 1
        q = deque()
        for i, n in enumerate(in_count):
            if n == 0:
                q.append(i)
        # print(q)
        while q:
            curr = q.popleft()
            # print(f"{curr}, {max_quiet}")
            # 移除入度
            for nxt in edge[curr]:
                # nxt 的前驱是 curr
                # ret 存放前驱里 quiet 最小的那个下标
                in_count[nxt] -= 1
                if quiet[ret[nxt]] > quiet[ret[curr]]: # 尝试和自己当前的quiet 比较
                    ret[nxt] = ret[curr]    # nxt 可能有多个前驱，不能直接覆盖
                if in_count[nxt] == 0:
                    q.append(nxt)
        return ret
```
