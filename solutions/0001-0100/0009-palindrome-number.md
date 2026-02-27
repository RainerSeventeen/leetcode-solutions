---
id: 9
title: Palindrome Number
difficulty: Easy
tags: [math]
created: 2026-02-27
---

# 9. 回文数

## 题目链接
https://leetcode.cn/problems/palindrome-number/

## 题目描述
<p>给你一个整数 <code>x</code> ，如果 <code>x</code> 是一个回文整数，返回 <code>true</code> ；否则，返回 <code>false</code> 。</p>

<p><span data-keyword="palindrome-integer">回文数</span>是指正序（从左向右）和倒序（从右向左）读都是一样的整数。</p>

<ul>
	<li>例如，<code>121</code> 是回文，而 <code>123</code> 不是。</li>
</ul>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>x = 121
<strong>输出：</strong>true
</pre>

<p><strong>示例&nbsp;2：</strong></p>

<pre>
<strong>输入：</strong>x = -121
<strong>输出：</strong>false
<strong>解释：</strong>从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>x = 10
<strong>输出：</strong>false
<strong>解释：</strong>从右向左读, 为 01 。因此它不是一个回文数。
</pre>

<p><strong>提示：</strong></p>

<ul>
	<li><code>-2<sup>31</sup>&nbsp;&lt;= x &lt;= 2<sup>31</sup>&nbsp;- 1</code></li>
</ul>

<p><strong>进阶：</strong>你能不将整数转为字符串来解决这个问题吗？</p>


## 解题思路

- 不把数字转成字符串。先排除负数和末尾为 0（但不是 0 本身）的情况。
- 用 `r` 反转 `x` 的后半部分：每轮取 `x` 的个位拼到 `r` 末尾，同时 `x` 去掉个位。
- 当 `r >= x` 时停止。若位数为偶数，应有 `r == x`；若位数为奇数，中间位可忽略，应有 `x == r // 10`。

- 时间复杂度: $O(\log_{10}x)$

- 空间复杂度: $O(1)$

## 相关专题
- [数学算法](../../topics/math-algorithms.md)

## 代码
```python
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0): # 末尾是 0，最高位不是0
            return False
        r = 0
        while r < x: # r >= x 表示位数已经移动完毕了
            r = r * 10 + x % 10  # 把 r 左移，补充 x 的最低位
            x = x // 10 # x 右移
        return r == x or x == r // 10 # r 有可能多拿了一位中心对称位
```

```python
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if str(x) == str(x)[::-1]:
            return True
        else:
            return False
```
