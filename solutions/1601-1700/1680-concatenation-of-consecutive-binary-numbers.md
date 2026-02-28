---
id: 1680
title: Concatenation of Consecutive Binary Numbers
difficulty: Medium
tags: [bit-manipulation, math, simulation]
created: 2026-02-28
---

# 1680. 连接连续二进制数字

## 题目链接
https://leetcode.cn/problems/concatenation-of-consecutive-binary-numbers/

## 题目描述
<p>给你一个整数 <code>n</code> ，请你将 <code>1</code> 到 <code>n</code> 的二进制表示连接起来，并返回连接结果对应的 <strong>十进制</strong> 数字对 <code>10<sup>9</sup> + 7</code> 取余的结果。</p>

<p><strong>示例 1：</strong></p>

<pre><b>输入：</b>n = 1
<b>输出：</b>1
<strong>解释：</strong>二进制的 "1" 对应着十进制的 1 。
</pre>

<p><strong>示例 2：</strong></p>

<pre><b>输入：</b>n = 3
<b>输出：</b>27
<strong>解释：</strong>二进制下，1，2 和 3 分别对应 "1" ，"10" 和 "11" 。
将它们依次连接，我们得到 "11011" ，对应着十进制的 27 。
</pre>

<p><strong>示例 3：</strong></p>

<pre><b>输入：</b>n = 12
<b>输出：</b>505379714
<b>解释：</b>连接结果为 "1101110010111011110001001101010111100" 。
对应的十进制数字为 118505380540 。
对 10<sup>9</sup> + 7 取余后，结果为 505379714 。
</pre>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 10<sup>5</sup></code></li>
</ul>


## 解题思路

依次把 `1..n` 的二进制串拼接到答案后面。  
当处理到 `i` 时，先用 `i.bit_length()` 得到其二进制位数 `w`，把当前答案左移 `w` 位腾出空间，再按位或上 `i`，并对 `10^9+7` 取模即可。

- 时间复杂度: $O(n)$，每个整数处理一次。

- 空间复杂度: $O(1)$，只使用常数额外变量。

## 相关专题
- [位运算](../../topics/bit-operations.md)

## 代码
```python
class Solution:
    def concatenatedBinary(self, n: int) -> int:
        # 暴力算法，乘法和加法是可以中途取模的
        MOD = 1_000_000_007
        ans = 0
        for i in range(1, n + 1):
            w = i.bit_length()
            ans = (ans << w | i) % MOD
        return ans
```
