---
id: 338
title: 比特位计数
difficulty: Medium
tags: [bit-manipulation, dynamic-programming]
created: 2026-02-20
---

# 338. 比特位计数

## 题目链接
https://leetcode.cn/problems/counting-bits/

## 题目描述

<p>给你一个整数 <code>n</code> ，对于&nbsp;<code>0 &lt;= i &lt;= n</code> 中的每个 <code>i</code> ，计算其二进制表示中 <strong><code>1</code> 的个数</strong> ，返回一个长度为 <code>n + 1</code> 的数组 <code>ans</code> 作为答案。</p>

<div class="original__bRMd">
<div>
<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>n = 2
<strong>输出：</strong>[0,1,1]
<strong>解释：</strong>
0 --&gt; 0
1 --&gt; 1
2 --&gt; 10
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>n = 5
<strong>输出：</strong>[0,1,1,2,1,2]
<strong>解释：</strong>
0 --&gt; 0
1 --&gt; 1
2 --&gt; 10
3 --&gt; 11
4 --&gt; 100
5 --&gt; 101
</pre>

<p><strong>提示：</strong></p>

<ul>
	<li><code>0 &lt;= n &lt;= 10<sup>5</sup></code></li>
</ul>

<p><strong>进阶：</strong></p>

<ul>
	<li>很容易就能实现时间复杂度为 <code>O(n log n)</code> 的解决方案，你可以在线性时间复杂度 <code>O(n)</code> 内用一趟扫描解决此问题吗？</li>
	<li>你能不使用任何内置函数解决此问题吗？（如，C++ 中的&nbsp;<code>__builtin_popcount</code> ）</li>
</ul>
</div>
</div>

## 解题思路
要计算 `0..n` 每个数的二进制 `1` 的个数（popcount），可以用 DP 复用已算结果。

关键观察：`i >> 1` 相当于去掉 `i` 的最低位，因此：

- `bits(i) = bits(i >> 1) + (i & 1)`

其中 `(i & 1)` 表示最低位是否为 `1`。按从小到大填表即可。

边界：`dp[0] = 0`。

- 时间复杂度: $O(n)$
- 空间复杂度: $O(n)$

## 相关专题
- [位运算](../../topics/bit-operations.md)

## 代码
```python
class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n + 1)
        for num in range(1, n + 1):
            dp[num] = dp[num >> 1] + (num & 1) 
        return dp
```
