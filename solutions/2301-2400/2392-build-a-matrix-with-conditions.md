---
id: 2392
title: Build a Matrix With Conditions
difficulty: Hard
tags: [graph, topological-sort, array, matrix]
created: 2026-02-20
---

# 2392. 给定条件下构造矩阵

## 题目链接
https://leetcode.cn/problems/build-a-matrix-with-conditions/

## 题目描述
<p>给你一个 <strong>正</strong>&nbsp;整数&nbsp;<code>k</code>&nbsp;，同时给你：</p>

<ul>
	<li>一个大小为 <code>n</code>&nbsp;的二维整数数组&nbsp;<code>rowConditions</code>&nbsp;，其中&nbsp;<code>rowConditions[i] = [above<sub>i</sub>, below<sub>i</sub>]</code>&nbsp;和</li>
	<li>一个大小为 <code>m</code>&nbsp;的二维整数数组&nbsp;<code>colConditions</code>&nbsp;，其中&nbsp;<code>colConditions[i] = [left<sub>i</sub>, right<sub>i</sub>]</code>&nbsp;。</li>
</ul>

<p>两个数组里的整数都是&nbsp;<code>1</code>&nbsp;到&nbsp;<code>k</code>&nbsp;之间的数字。</p>

<p>你需要构造一个&nbsp;<code>k x k</code>&nbsp;的矩阵，<code>1</code>&nbsp;到&nbsp;<code>k</code>&nbsp;每个数字需要&nbsp;<strong>恰好出现一次</strong>&nbsp;。剩余的数字都是<b>&nbsp;</b><code>0</code>&nbsp;。</p>

<p>矩阵还需要满足以下条件：</p>

<ul>
	<li>对于所有 <code>0</code>&nbsp;到&nbsp;<code>n - 1</code>&nbsp;之间的下标&nbsp;<code>i</code>&nbsp;，数字&nbsp;<code>above<sub>i</sub></code>&nbsp;所在的 <strong>行</strong>&nbsp;必须在数字&nbsp;<code>below<sub>i</sub></code>&nbsp;所在行的上面。</li>
	<li>对于所有 <code>0</code>&nbsp;到 <code>m - 1</code>&nbsp;之间的下标&nbsp;<code>i</code>&nbsp;，数字&nbsp;<code>left<sub>i</sub></code>&nbsp;所在的 <b>列</b>&nbsp;必须在数字&nbsp;<code>right<sub>i</sub></code>&nbsp;所在列的左边。</li>
</ul>

<p>返回满足上述要求的 <strong>任意</strong>&nbsp;矩阵。如果不存在答案，返回一个空的矩阵。</p>

<p><strong>示例 1：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2022/07/06/gridosdrawio.png" style="width: 211px; height: 211px;"></p>

<pre><b>输入：</b>k = 3, rowConditions = [[1,2],[3,2]], colConditions = [[2,1],[3,2]]
<b>输出：</b>[[3,0,0],[0,0,1],[0,2,0]]
<b>解释：</b>上图为一个符合所有条件的矩阵。
行要求如下：
- 数字 1 在第 <strong>1</strong> 行，数字 2 在第 <strong>2</strong>&nbsp;行，1 在 2 的上面。
- 数字 3 在第 <strong>0</strong>&nbsp;行，数字 2 在第 <strong>2</strong>&nbsp;行，3 在 2 的上面。
列要求如下：
- 数字 2 在第 <strong>1</strong>&nbsp;列，数字 1 在第 <strong>2</strong>&nbsp;列，2 在 1 的左边。
- 数字 3 在第 <strong>0</strong>&nbsp;列，数字 2 在第 <strong>1</strong>&nbsp;列，3 在 2 的左边。
注意，可能有多种正确的答案。
</pre>

<p><strong>示例 2：</strong></p>

<pre><b>输入：</b>k = 3, rowConditions = [[1,2],[2,3],[3,1],[2,3]], colConditions = [[2,1]]
<b>输出：</b>[]
<b>解释：</b>由前两个条件可以得到 3 在 1 的下面，但第三个条件是 3 在 1 的上面。
没有符合条件的矩阵存在，所以我们返回空矩阵。
</pre>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 &lt;= k &lt;= 400</code></li>
	<li><code>1 &lt;= rowConditions.length, colConditions.length &lt;= 10<sup>4</sup></code></li>
	<li><code>rowConditions[i].length == colConditions[i].length == 2</code></li>
	<li><code>1 &lt;= above<sub>i</sub>, below<sub>i</sub>, left<sub>i</sub>, right<sub>i</sub> &lt;= k</code></li>
	<li><code>above<sub>i</sub> != below<sub>i</sub></code></li>
	<li><code>left<sub>i</sub> != right<sub>i</sub></code></li>
</ul>


## 解题思路

对 rowConditions 和 colConditions 分别运行 Kahn 拓扑排序，得到数字 1~k 在行方向与列方向的合法顺序。若任一排序检测到环（已处理节点数 < k）则返回空矩阵；否则根据两个拓扑序列分别确定每个数字的行号和列号，再构造 k×k 矩阵，将数字放在对应的交叉位置，其余格填 0。

- 时间复杂度: $O(k + n + m)$

- 空间复杂度: $O(k + n + m)$

## 相关专题
- [图论算法](../../topics/graph-algorithms.md)

## 代码
```python
class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        # above < below, left < right
        # 两轮次拓扑排序就行了
        def build_list(cond): # 返回一个排列好的拓扑顺序, 从小到大
            ret = [0] * k
            q = deque() 
            count = [0] * (k)
            graph = [[] for _ in range(k)]
            # 构建邻接表
            for small, big in cond:
                count[big - 1] += 1
                graph[small - 1].append(big - 1)
            for i, c in enumerate(count):
                if c == 0:
                    q.append(i)
            all_cnt = 0
            while q:
                curr = q.popleft()
                ret[curr] = all_cnt
                all_cnt += 1
                for nxt in graph[curr]:
                    count[nxt] -= 1
                    if count[nxt] == 0:
                        q.append(nxt)
            return ret if all_cnt == k else []
        
        row = build_list(rowConditions) 
        col = build_list(colConditions)
        if not row or not col:
            return []
        ret = [[0] * k for _ in range(k)]
        for num in range(k):
            i, j = row[num], col[num]
            ret[i][j] = num + 1
        return ret
```
