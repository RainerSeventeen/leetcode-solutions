---
id: 762
title: Prime Number of Set Bits in Binary Representation
difficulty: Easy
tags: [bit-manipulation, math]
created: 2026-02-21
---

# 762. 二进制表示中质数个计算置位

## 题目链接
https://leetcode.cn/problems/prime-number-of-set-bits-in-binary-representation/

## 题目描述
<p>给你两个整数&nbsp;<code>left</code>&nbsp;和&nbsp;<code>right</code> ，在闭区间 <code>[left, right]</code>&nbsp;范围内，统计并返回 <strong>计算置位位数为质数</strong> 的整数个数。</p>

<p><strong>计算置位位数</strong> 就是二进制表示中 <code>1</code> 的个数。</p>

<ul>
	<li>例如， <code>21</code>&nbsp;的二进制表示&nbsp;<code>10101</code>&nbsp;有 <code>3</code> 个计算置位。</li>
</ul>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>left = 6, right = 10
<strong>输出：</strong>4
<strong>解释：</strong>
6 -&gt; 110 (2 个计算置位，2 是质数)
7 -&gt; 111 (3 个计算置位，3 是质数)
9 -&gt; 1001 (2 个计算置位，2 是质数)
10-&gt; 1010 (2 个计算置位，2 是质数)
共计 4 个计算置位为质数的数字。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>left = 10, right = 15
<strong>输出：</strong>5
<strong>解释：</strong>
10 -&gt; 1010 (2 个计算置位, 2 是质数)
11 -&gt; 1011 (3 个计算置位, 3 是质数)
12 -&gt; 1100 (2 个计算置位, 2 是质数)
13 -&gt; 1101 (3 个计算置位, 3 是质数)
14 -&gt; 1110 (3 个计算置位, 3 是质数)
15 -&gt; 1111 (4 个计算置位, 4 不是质数)
共计 5 个计算置位为质数的数字。
</pre>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= left &lt;= right &lt;= 10<sup>6</sup></code></li>
	<li><code>0 &lt;= right - left &lt;= 10<sup>4</sup></code></li>
</ul>


## 解题思路

- 遍历区间内每个整数，用 `bit_count()` 计算二进制 1 的个数。
- 对该计数做素数判断（试除到平方根），是素数则答案加一。

- 时间复杂度: $O(right-left+1)$

- 空间复杂度: $O(1)$

## 代码
```python
class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        def is_prime(n):
            if n < 2:
                return False
            if n == 2:
                return True
            if n % 2 == 0:
                return False
            # 只需要判断到 sqrt(n)
            for i in range(3, int(math.sqrt(n)) + 1, 2):
                if n % i == 0:
                    return False
            return True
        # 位运算模拟
        ret = 0
        for n in range(left, right + 1):
            c = n.bit_count()
            if is_prime(c):
                ret += 1
        return ret
```
