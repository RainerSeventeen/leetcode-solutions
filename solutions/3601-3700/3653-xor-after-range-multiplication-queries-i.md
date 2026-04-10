---
id: 3653
title: XOR After Range Multiplication Queries I
difficulty: Medium
tags: [array, divide-and-conquer, simulation]
created: 2026-04-10
---

# 3653. 区间乘法查询后的异或 I

## 题目链接
https://leetcode.cn/problems/xor-after-range-multiplication-queries-i/

## 题目描述
<p>给你一个长度为 <code>n</code> 的整数数组 <code>nums</code> 和一个大小为 <code>q</code> 的二维整数数组 <code>queries</code>，其中 <code>queries[i] = [l<sub>i</sub>, r<sub>i</sub>, k<sub>i</sub>, v<sub>i</sub>]</code>。</p>

<p>对于每个查询，按以下步骤执行操作：</p>

<ul>
	<li>设定 <code>idx = l<sub>i</sub></code>。</li>
	<li>当 <code>idx &lt;= r<sub>i</sub></code> 时：
	<ul>
		<li>更新：<code>nums[idx] = (nums[idx] * v<sub>i</sub>) % (10<sup>9</sup> + 7)</code></li>
		<li>将 <code>idx += k<sub>i</sub></code>。</li>
	</ul>
	</li>
</ul>

<p>在处理完所有查询后，返回数组 <code>nums</code> 中所有元素的&nbsp;<strong>按位异或&nbsp;</strong>结果。</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">nums = [1,1,1], queries = [[0,2,1,4]]</span></p>

<p><strong>输出：</strong> <span class="example-io">4</span></p>

<p><strong>解释：</strong></p>

<ul>
	<li>唯一的查询 <code>[0, 2, 1, 4]</code> 将下标&nbsp;0 到下标&nbsp;2 的每个元素乘以 4。</li>
	<li>数组从 <code>[1, 1, 1]</code> 变为 <code>[4, 4, 4]</code>。</li>
	<li>所有元素的异或为 <code>4 ^ 4 ^ 4 = 4</code>。</li>
</ul>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">nums = [2,3,1,5,4], queries = [[1,4,2,3],[0,2,1,2]]</span></p>

<p><strong>输出：</strong> <span class="example-io">31</span></p>

<p><strong>解释：</strong></p>

<ul>
	<li>第一个查询 <code>[1, 4, 2, 3]</code> 将下标&nbsp;1 和 3 的元素乘以 3，数组变为 <code>[2, 9, 1, 15, 4]</code>。</li>
	<li>第二个查询 <code>[0, 2, 1, 2]</code> 将下标&nbsp;0、1 和 2 的元素乘以 2，数组变为 <code>[4, 18, 2, 15, 4]</code>。</li>
	<li>所有元素的异或为 <code>4 ^ 18 ^ 2 ^ 15 ^ 4 = 31</code>。</li>
</ul>
</div>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n == nums.length &lt;= 10<sup>3</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
	<li><code>1 &lt;= q == queries.length &lt;= 10<sup>3</sup></code></li>
	<li><code>queries[i] = [l<sub>i</sub>, r<sub>i</sub>, k<sub>i</sub>, v<sub>i</sub>]</code></li>
	<li><code>0 &lt;= l<sub>i</sub> &lt;= r<sub>i</sub> &lt; n</code></li>
	<li><code>1 &lt;= k<sub>i</sub> &lt;= n</code></li>
	<li><code>1 &lt;= v<sub>i</sub> &lt;= 10<sup>5</sup></code></li>
</ul>


## 解题思路

- 直接按题意模拟每个查询即可。
- 对于每个 `[l, r, k, v]`，从 `l` 开始每隔 `k` 个位置更新一次 `nums[i] = nums[i] * v % MOD`。
- 所有查询结束后再把整个数组异或一遍得到答案。

- 时间复杂度: $O(nq)$，更精确地说是遍历所有受影响位置的总次数再加上一遍数组异或，其中 `n` 和 `q` 分别是数组长度与查询数。
- 空间复杂度: $O(1)$。

## 相关专题
- [常用数据结构](../../topics/common-data-structures.md)

## 代码
```python
class Solution:
    MOD = 10**9 + 7
    
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        for l, r, k, v in queries:
            for i in range(l, r + 1, k):
                nums[i] = (nums[i] * v) % self.MOD
        
        res = 0
        for x in nums:
            res ^= x
        
        return res
```
