---
id: 3488
title: Closest Equal Element Queries
difficulty: Medium
tags: [array, hash-table, binary-search]
created: 2026-04-25
---

# 3488. 距离最小相等元素查询

## 题目链接
https://leetcode.cn/problems/closest-equal-element-queries/

## 题目描述
<p>给你一个&nbsp;<strong>环形&nbsp;</strong>数组&nbsp;<code>nums</code>&nbsp;和一个数组&nbsp;<code>queries</code>&nbsp;。</p>

<p>对于每个查询&nbsp;<code>i</code>&nbsp;，你需要找到以下内容：</p>

<ul>
	<li>数组&nbsp;<code>nums</code>&nbsp;中下标&nbsp;<code>queries[i]</code>&nbsp;处的元素与&nbsp;<strong>任意&nbsp;</strong>其他下标&nbsp;<code>j</code>（满足&nbsp;<code>nums[j] == nums[queries[i]]</code>）之间的&nbsp;<strong>最小&nbsp;</strong>距离。如果不存在这样的下标&nbsp;<code>j</code>，则该查询的结果为 <code>-1</code> 。</li>
</ul>

<p>返回一个数组&nbsp;<code>answer</code>，其大小与&nbsp;<code>queries</code>&nbsp;相同，其中&nbsp;<code>answer[i]</code>&nbsp;表示查询<code>i</code>的结果。</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">nums = [1,3,1,4,1,3,2], queries = [0,3,5]</span></p>

<p><strong>输出：</strong> <span class="example-io">[2,-1,3]</span></p>

<p><strong>解释：</strong></p>

<ul>
	<li>查询 0：下标&nbsp;<code>queries[0] = 0</code>&nbsp;处的元素为&nbsp;<code>nums[0] = 1</code>&nbsp;。最近的相同值下标为 2，距离为 2。</li>
	<li>查询 1：下标&nbsp;<code>queries[1] = 3</code>&nbsp;处的元素为&nbsp;<code>nums[3] = 4</code>&nbsp;。不存在其他包含值 4 的下标，因此结果为 -1。</li>
	<li>查询 2：下标&nbsp;<code>queries[2] = 5</code>&nbsp;处的元素为&nbsp;<code>nums[5] = 3</code>&nbsp;。最近的相同值下标为 1，距离为 3（沿着循环路径：<code>5 -&gt; 6 -&gt; 0 -&gt; 1</code>）。</li>
</ul>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">nums = [1,2,3,4], queries = [0,1,2,3]</span></p>

<p><strong>输出：</strong> <span class="example-io">[-1,-1,-1,-1]</span></p>

<p><strong>解释：</strong></p>

<p>数组&nbsp;<code>nums</code>&nbsp;中的每个值都是唯一的，因此没有下标与查询的元素值相同。所有查询的结果均为 -1。</p>
</div>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= queries.length &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>6</sup></code></li>
	<li><code>0 &lt;= queries[i] &lt; nums.length</code></li>
</ul>


## 解题思路

先把每个数值出现的下标收集成递增列表。环形距离可以通过在每个列表前后各加一个哨兵来处理：前哨兵是最后一个下标减 `n`，后哨兵是第一个下标加 `n`。对每个查询，在对应值的下标列表中二分找到查询下标，答案就是左右最近相同值下标距离的较小值；若该值只出现一次则返回 `-1`。

- 时间复杂度: $O(n+q\log n)$，其中 `n` 为 `nums` 长度，`q` 为 `queries` 长度。

- 空间复杂度: $O(n)$

## 相关专题

- [二分算法](../../topics/binary-search.md)

## 代码
```python
class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        # CV
        indices = defaultdict(list)
        for i, x in enumerate(nums):
            indices[x].append(i)

        n = len(nums)
        for p in indices.values():
            # 前后各加一个哨兵
            i0 = p[0]
            p.insert(0, p[-1] - n)
            p.append(i0 + n)

        for qi, i in enumerate(queries):
            p = indices[nums[i]]
            if len(p) == 3:
                queries[qi] = -1
            else:
                j = bisect_left(p, i)
                queries[qi] = min(i - p[j - 1], p[j + 1] - i)
        return queries
```
