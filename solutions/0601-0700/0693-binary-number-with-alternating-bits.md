---
id: 693
title: Binary Number with Alternating Bits
difficulty: Easy
tags: [bit-manipulation]
created: 2026-02-21
---

# 693. 交替位二进制数

## 题目链接
https://leetcode.cn/problems/binary-number-with-alternating-bits/

## 题目描述
<p>给定一个正整数，检查它的二进制表示是否总是 0、1 交替出现：换句话说，就是二进制表示中相邻两位的数字永不相同。</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>n = 5
<strong>输出：</strong>true
<strong>解释：</strong>5 的二进制表示是：101
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>n = 7
<strong>输出：</strong>false
<strong>解释：</strong>7 的二进制表示是：111.</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>n = 11
<strong>输出：</strong>false
<strong>解释：</strong>11 的二进制表示是：1011.</pre>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 2<sup>31</sup> - 1</code></li>
</ul>


## 解题思路

从最低位开始逐位右移，比较当前位和上一位是否相同。
如果出现相同相邻位，立即返回 `False`。
全部位检查通过则为交替比特，返回 `True`。
- 时间复杂度: $O(\log n)$
- 空间复杂度: $O(1)$

## 相关专题
- [位运算](../../topics/bit-operations.md)

## 代码
```python
class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        curr = n
        pre = curr & 1
        # print(f"{curr:b}")
        while curr != 0:
            curr = curr >> 1
            bit = curr & 1
            # print(pre, bit)
            if bit == pre:
                return False
            pre = bit
        return True
```
