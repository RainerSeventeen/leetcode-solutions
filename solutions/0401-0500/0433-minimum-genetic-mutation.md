---
id: 433
title: Minimum Genetic Mutation
difficulty: Medium
tags: [breadth-first-search, hash-table, string]
created: 2026-02-21
---

# 433. 最小基因变化

## 题目链接
https://leetcode.cn/problems/minimum-genetic-mutation/

## 题目描述
<p>基因序列可以表示为一条由 8 个字符组成的字符串，其中每个字符都是 <code>'A'</code>、<code>'C'</code>、<code>'G'</code> 和 <code>'T'</code> 之一。</p>

<p>假设我们需要调查从基因序列&nbsp;<code>start</code> 变为 <code>end</code> 所发生的基因变化。一次基因变化就意味着这个基因序列中的一个字符发生了变化。</p>

<ul>
	<li>例如，<code>"AACCGGTT" --&gt; "AACCGGTA"</code> 就是一次基因变化。</li>
</ul>

<p>另有一个基因库 <code>bank</code> 记录了所有有效的基因变化，只有基因库中的基因才是有效的基因序列。（变化后的基因必须位于基因库 <code>bank</code> 中）</p>

<p>给你两个基因序列 <code>start</code> 和 <code>end</code> ，以及一个基因库 <code>bank</code> ，请你找出并返回能够使&nbsp;<code>start</code> 变化为 <code>end</code> 所需的最少变化次数。如果无法完成此基因变化，返回 <code>-1</code> 。</p>

<p>注意：起始基因序列&nbsp;<code>start</code> 默认是有效的，但是它并不一定会出现在基因库中。</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>start = "AACCGGTT", end = "AACCGGTA", bank = ["AACCGGTA"]
<strong>输出：</strong>1
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>start = "AACCGGTT", end = "AAACGGTA", bank = ["AACCGGTA","AACCGCTA","AAACGGTA"]
<strong>输出：</strong>2
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>start = "AAAAACCC", end = "AACCCCCC", bank = ["AAAACCCC","AAACCCCC","AACCCCCC"]
<strong>输出：</strong>3
</pre>

<p><strong>提示：</strong></p>

<ul>
	<li><code>start.length == 8</code></li>
	<li><code>end.length == 8</code></li>
	<li><code>0 &lt;= bank.length &lt;= 10</code></li>
	<li><code>bank[i].length == 8</code></li>
	<li><code>start</code>、<code>end</code> 和 <code>bank[i]</code> 仅由字符 <code>['A', 'C', 'G', 'T']</code> 组成</li>
</ul>


## 解题思路

使用 BFS 按步数扩展，每层表示一次突变，首次到达终点即为最少步数。
对当前基因的每一位尝试替换为 `A/C/G/T`，若新基因在基因库中就入队。
基因库用集合并在入队时删除，避免重复访问。
- 时间复杂度: $O(m \cdot L)$
- 空间复杂度: $O(m)$

## 相关专题
- [图论算法](../../topics/graph-algorithms.md)

## 代码
```python
class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        n = len(startGene)
        q = deque([startGene])
        # 建立 hash 并执行删除
        bk = set(bank)
        if endGene not in bk:
            return -1
        count = 0
        while q:
            count += 1
            for _ in range(len(q)):
            # 尝试改变每一个位，判断是否在表格中
                curr = q.pop()
                print(count, curr)
                for i in range(n):
                    for ch in "ACGT":
                        if ch == curr[i]:
                            continue
                        nxt = curr[:i] + ch + curr[i+1:]
                        if nxt == endGene:
                            return count
                        if nxt in bk:
                            bk.remove(nxt)
                            q.appendleft(nxt)
        return -1
```
