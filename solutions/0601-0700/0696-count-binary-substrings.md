---
id: 696
title: Count Binary Substrings
difficulty: Easy
tags: [two-pointers, string]
created: 2026-02-21
---

# 696. 计数二进制子串

## 题目链接
https://leetcode.cn/problems/count-binary-substrings/

## 题目描述
<p>给定一个字符串&nbsp;<code>s</code>，统计并返回具有相同数量 <code>0</code> 和 <code>1</code> 的非空（连续）子字符串的数量，并且这些子字符串中的所有 <code>0</code> 和所有 <code>1</code> 都是成组连续的。</p>

<p>重复出现（不同位置）的子串也要统计它们出现的次数。</p>
&nbsp;

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>s = "00110011"
<strong>输出：</strong>6
<strong>解释：</strong>6 个子串满足具有相同数量的连续 1 和 0 ："0011"、"01"、"1100"、"10"、"0011" 和 "01" 。
注意，一些重复出现的子串（不同位置）要统计它们出现的次数。
另外，"00110011" 不是有效的子串，因为所有的 0（还有 1 ）没有组合在一起。</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>s = "10101"
<strong>输出：</strong>4
<strong>解释：</strong>有 4 个子串："10"、"01"、"10"、"01" ，具有相同数量的连续 1 和 0 。
</pre>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>5</sup></code></li>
	<li><code>s[i]</code> 为 <code>'0'</code> 或 <code>'1'</code></li>
</ul>


## 解题思路

用 `pre` 记录上一段连续字符长度，`curr` 记录当前段长度。
遍历时若字符变化就把 `pre=curr` 并重置 `curr`，随后继续累加当前段。
当 `curr <= pre` 时，说明可以形成一个新的有效子串，答案加一。
- 时间复杂度: $O(n)$
- 空间复杂度: $O(1)$

## 代码
```python
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        # 每一次 01 翻转的时候开始统计
        pre = 0 # 统计上一个连续值的数量
        pre_ch = '#'
        curr = 0 # 统计当前连续值
        ret = 0
        n = len(s)
        for ch in s:
            # print(pre_ch, ch, end=" | ")
            if pre_ch != ch: # 不相等，轮换
                pre = curr
                pre_ch = ch
                curr = 0
            curr += 1
            if curr <= pre:
                ret += 1
            # print(pre, curr, ret)
        return ret
```
