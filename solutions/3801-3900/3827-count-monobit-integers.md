---
id: 3827
title: Count Monobit Integers
difficulty: Easy
tags: [bit-manipulation, enumeration]
created: 2026-02-21
---

# 3827. 统计单比特整数

## 题目链接
https://leetcode.cn/problems/count-monobit-integers/

## 题目描述
<p>给你一个整数&nbsp;<code>n</code>。</p>

<p>如果一个整数的二进制表示中所有位都相同，则称其为<strong>&nbsp;单比特数</strong>（<strong>Monobit</strong>）。</p>

<p>返回范围<code>[0, n]</code>（包括两端）内<strong>&nbsp;单比特数&nbsp;</strong>的个数。</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">n = 1</span></p>

<p><strong>输出：</strong> <span class="example-io">2</span></p>

<p><strong>解释：</strong></p>

<ul>
	<li>范围<code>[0, 1]</code>内的整数对应的二进制表示为<code>"0"</code>和<code>"1"</code>。</li>
	<li>每个表示都由相同的位组成，因此答案是2。</li>
</ul>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">n = 4</span></p>

<p><strong>输出：</strong> <span class="example-io">3</span></p>

<p><strong>解释：</strong></p>

<ul>
	<li>范围<code>[0, 4]</code>内的整数对应的二进制表示为<code>"0"</code>、<code>"1"</code>、<code>"10"</code>、<code>"11"</code>和<code>"100"</code>。</li>
	<li>只有<code>0</code>、<code>1</code>和<code>3</code>满足单比特条件。因此答案是3。</li>
</ul>
</div>

<p><strong>提示：</strong></p>

<ul>
	<li><code>0 &lt;= n &lt;= 1000</code></li>
</ul>


## 解题思路

单比特整数形如 `0, 1, 3, 7, 15...`，即 `2^k-1`。
要求不超过 `n` 的数量，就是满足 `2^k-1 <= n` 的 `k` 个数再加上 `0`。
代码直接用对数计算这个计数。
- 时间复杂度: $O(1)$
- 空间复杂度: $O(1)$

## 代码
```python
import math
class Solution:
    def countMonobit(self, n: int) -> int:
        # 0 和全是 1 的数
        return int(math.log(n + 1, 2) + 1)
```
