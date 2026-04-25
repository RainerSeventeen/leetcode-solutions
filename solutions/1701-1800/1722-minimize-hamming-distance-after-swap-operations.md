---
id: 1722
title: Minimize Hamming Distance After Swap Operations
difficulty: Medium
tags: [depth-first-search, union-find, array]
created: 2026-04-25
---

# 1722. 执行交换操作后的最小汉明距离

## 题目链接
https://leetcode.cn/problems/minimize-hamming-distance-after-swap-operations/

## 题目描述
<p>给你两个整数数组 <code>source</code> 和 <code>target</code> ，长度都是 <code>n</code> 。还有一个数组 <code>allowedSwaps</code> ，其中每个 <code>allowedSwaps[i] = [a<sub>i</sub>, b<sub>i</sub>]</code> 表示你可以交换数组 <code>source</code> 中下标为 <code>a<sub>i</sub></code> 和 <code>b<sub>i</sub></code>（<strong>下标从 0 开始</strong>）的两个元素。注意，你可以按 <strong>任意</strong> 顺序 <strong>多次</strong> 交换一对特定下标指向的元素。</p>

<p>相同长度的两个数组 <code>source</code> 和 <code>target</code> 间的 <strong>汉明距离</strong> 是元素不同的下标数量。形式上，其值等于满足 <code>source[i] != target[i]</code> （<strong>下标从 0 开始</strong>）的下标 <code>i</code>（<code>0 &lt;= i &lt;= n-1</code>）的数量。</p>

<p>在对数组 <code>source</code> 执行 <strong>任意</strong> 数量的交换操作后，返回 <code>source</code> 和 <code>target</code> 间的 <strong>最小汉明距离</strong> 。</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>source = [1,2,3,4], target = [2,1,4,5], allowedSwaps = [[0,1],[2,3]]
<strong>输出：</strong>1
<strong>解释：</strong>source 可以按下述方式转换：
- 交换下标 0 和 1 指向的元素：source = [<strong>2</strong>,<strong>1</strong>,3,4]
- 交换下标 2 和 3 指向的元素：source = [2,1,<strong>4</strong>,<strong>3</strong>]
source 和 target 间的汉明距离是 1 ，二者有 1 处元素不同，在下标 3 。
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>source = [1,2,3,4], target = [1,3,2,4], allowedSwaps = []
<strong>输出：</strong>2
<strong>解释：</strong>不能对 source 执行交换操作。
source 和 target 间的汉明距离是 2 ，二者有 2 处元素不同，在下标 1 和下标 2 。</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>source = [5,1,2,4,3], target = [1,5,4,2,3], allowedSwaps = [[0,4],[4,2],[1,3],[1,4]]
<strong>输出：</strong>0
</pre>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == source.length == target.length</code></li>
	<li><code>1 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= source[i], target[i] &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= allowedSwaps.length &lt;= 10<sup>5</sup></code></li>
	<li><code>allowedSwaps[i].length == 2</code></li>
	<li><code>0 &lt;= a<sub>i</sub>, b<sub>i</sub> &lt;= n - 1</code></li>
	<li><code>a<sub>i</sub> != b<sub>i</sub></code></li>
</ul>


## 解题思路

允许交换的下标构成无向图，同一连通块内的 `source` 元素可以任意重排。对每个连通块 DFS，使用哈希表统计 `source` 中元素出现次数加一、`target` 中元素出现次数减一，最终无法抵消的数量就是该连通块内两边多出来的元素数，除以 2 后累加到答案。

- 时间复杂度: $O(n+m)$，其中 `n` 为数组长度，`m` 为 `allowedSwaps` 长度。

- 空间复杂度: $O(n+m)$

## 相关专题

- [常用数据结构](../../topics/common-data-structures.md)

## 代码
```python
class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        n = len(source)
        g = [[] for _ in range(n)]
        for i, j in allowedSwaps:
            g[i].append(j)  # 建图
            g[j].append(i)

        def dfs(x: int) -> None:
            vis[x] = True  # 避免重复访问
            # 抵消相同的元素，最终剩下 source 和 target 各自多出来的元素（对称差）
            diff[source[x]] += 1
            diff[target[x]] -= 1
            for y in g[x]:
                if not vis[y]:
                    dfs(y)

        vis = [False] * n
        ans = 0
        for x in range(n):
            if not vis[x]:
                diff = defaultdict(int)
                dfs(x)
                ans += sum(map(abs, diff.values()))
        return ans // 2  # 有 ans // 2 对多出来的元素
```
