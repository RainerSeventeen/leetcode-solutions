---
id: 67
title: Add Binary
difficulty: Easy
tags: [bit-manipulation, math, string, simulation]
created: 2026-02-21
---

# 67. 二进制求和

## 题目链接
https://leetcode.cn/problems/add-binary/

## 题目描述
<p>给你两个二进制字符串 <code>a</code> 和 <code>b</code> ，以二进制字符串的形式返回它们的和。</p>

<p><strong>示例&nbsp;1：</strong></p>

<pre>
<strong>输入:</strong>a = "11", b = "1"
<strong>输出：</strong>"100"</pre>

<p><strong>示例&nbsp;2：</strong></p>

<pre>
<strong>输入：</strong>a = "1010", b = "1011"
<strong>输出：</strong>"10101"</pre>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= a.length, b.length &lt;= 10<sup>4</sup></code></li>
	<li><code>a</code> 和 <code>b</code> 仅由字符 <code>'0'</code> 或 <code>'1'</code> 组成</li>
	<li>字符串如果不是 <code>"0"</code> ，就不含前导零</li>
</ul>


## 解题思路

双指针从两个字符串末尾向前逐位相加，并维护进位 `carry`。
每轮取当前位和进位计算新位，写入结果数组后继续左移指针。
循环结束后把结果反转拼接即可。
- 时间复杂度: $O(\max(m,n))$
- 空间复杂度: $O(\max(m,n))$

## 代码
```python
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i, j = len(a) - 1, len(b) - 1
        carry = 0
        ret = []
        while i >= 0 or j >= 0 or carry != 0:
            adda = int(a[i]) if i >= 0 else 0
            addb = int(b[j]) if j >= 0 else 0
            total = adda + addb + carry
            carry = total // 2
            total = total % 2
            ret.append(str(total))
            i -= 1
            j -= 1
        return "".join(ret[::-1])
```
