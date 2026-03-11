---
id: 1009
title: Complement of Base 10 Integer
difficulty: Easy
tags: [bit-manipulation]
created: 2026-03-11
---

# 1009. 十进制整数的反码

## 题目链接
https://leetcode.cn/problems/complement-of-base-10-integer/

## 题目描述
<p>每个非负整数&nbsp;<code>N</code>&nbsp;都有其二进制表示。例如，&nbsp;<code>5</code>&nbsp;可以被表示为二进制&nbsp;<code>&quot;101&quot;</code>，<code>11</code> 可以用二进制&nbsp;<code>&quot;1011&quot;</code>&nbsp;表示，依此类推。注意，除&nbsp;<code>N = 0</code>&nbsp;外，任何二进制表示中都不含前导零。</p>

<p>二进制的反码表示是将每个&nbsp;<code>1</code>&nbsp;改为&nbsp;<code>0</code>&nbsp;且每个&nbsp;<code>0</code>&nbsp;变为&nbsp;<code>1</code>。例如，二进制数&nbsp;<code>&quot;101&quot;</code>&nbsp;的二进制反码为&nbsp;<code>&quot;010&quot;</code>。</p>

<p>给你一个十进制数&nbsp;<code>N</code>，请你返回其二进制表示的反码所对应的十进制整数。</p>

<ol>
</ol>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>5
<strong>输出：</strong>2
<strong>解释：</strong>5 的二进制表示为 &quot;101&quot;，其二进制反码为 &quot;010&quot;，也就是十进制中的 2 。
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>7
<strong>输出：</strong>0
<strong>解释：</strong>7 的二进制表示为 &quot;111&quot;，其二进制反码为 &quot;000&quot;，也就是十进制中的 0 。
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>10
<strong>输出：</strong>5
<strong>解释：</strong>10 的二进制表示为 &quot;1010&quot;，其二进制反码为 &quot;0101&quot;，也就是十进制中的 5 。
</pre>

<p><strong>提示：</strong></p>

<ol>
	<li><code>0 &lt;= N &lt; 10^9</code></li>
	<li>本题与 476：<a href="https://leetcode.cn/problems/number-complement/">https://leetcode.cn/problems/number-complement/</a> 相同</li>
</ol>


## 解题思路
先处理特殊情况 `n = 0`，它的二进制表示看作 `0`，反码就是 `1`，直接返回即可。

对于 `n > 0`，不断左移 `mask`，直到它严格大于 `n`。这样 `mask - 1` 就会变成一个和 `n` 二进制长度相同、且每一位都是 `1` 的数。最后用 `(mask - 1) ^ n` 把这一段有效二进制位逐位翻转，得到答案。

- 时间复杂度: $O(\log n)$

- 空间复杂度: $O(1)$

## 相关专题
- [位运算](../../topics/bit-operations.md)

## 代码
```python
class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0:
            return 1
        mask = 1
        while mask <= n:
            mask <<= 1

        return (mask - 1) ^ n # 1 ^ x 表示翻转
```
