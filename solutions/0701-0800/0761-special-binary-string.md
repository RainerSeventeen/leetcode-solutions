---
id: 761
title: Special Binary String
difficulty: Hard
tags: [string, divide-and-conquer, sorting]
created: 2026-02-20
---

# 761. 特殊的二进制字符串

## 题目链接
https://leetcode.cn/problems/special-binary-string/

## 题目描述
<p><strong>特殊的二进制字符串</strong> 是具有以下两个性质的二进制序列：</p>

<ul>
	<li><code>0</code> 的数量与 <code>1</code> 的数量相等。</li>
	<li>二进制序列的每一个前缀码中 <code>1</code> 的数量要大于等于 <code>0</code> 的数量。</li>
</ul>

<p>给定一个特殊的二进制字符串&nbsp;<code>s</code>。</p>

<p>一次移动操作包括选择字符串 <code>s</code> 中的两个连续的、非空的、特殊子串，并交换它们。两个字符串是连续的，如果第一个字符串的最后一个字符与第二个字符串的第一个字符的索引相差正好为 1。</p>

<p>返回在字符串上应用任意次操作后可能得到的字典序最大的字符串。</p>

<p><strong>示例 1:</strong></p>

<pre>
<strong>输入:</strong> S = "11011000"
<strong>输出:</strong> "11100100"
<strong>解释:</strong>
将子串 "10" （在 s[1] 出现） 和 "1100" （在 s[3] 出现）进行交换。
这是在进行若干次操作后按字典序排列最大的结果。
</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<b>输入：</b>s = "10"
<b>输出：</b>"10"
</pre>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 50</code></li>
	<li><code>s[i]</code>&nbsp;为&nbsp;<code>'0'</code> 或&nbsp;<code>'1'</code>。</li>
	<li><code>s</code>&nbsp;是一个特殊的二进制字符串。</li>
</ul>


## 解题思路

这题可以视为一个左右括号的匹配过程, 本质上是一个贪心算法, 合法的串只有可能是两种情况

1. 并列: () + () + (())

2. 嵌套: ((()))

对于所有的块我们都要递归的进入到最深层, 然后对其中的并列块进行排序, 然后再补上外层即可

贪心的思想在于, 对于一个最大字典序的特殊串, 他的内部一定是递归地所有的特殊串都是最大的

- 时间复杂度: $O(n^2)$

- 空间复杂度: $O(n)$

## 相关专题
- [字符串](../../topics/string-algorithms.md)

## 代码
```python
class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        if len(s) <= 2:
            return s # 终止条件

        substr = [] # 该层级的所有并列串的集合
        balance = 0
        start = 0 # 1的开始下标
        for i, ch in enumerate(s):
            if ch == '1':
                balance += 1
            else:
                balance -= 1
                # 特殊串区间 [start + balance , i]
                if balance == 0: # 题目保证不会 < 0
                    # 必然是嵌套串, 进入递归, 去除外部后进行排序
                    in_str = self.makeLargestSpecial(s[start + 1:i])
                    substr.append('1' + in_str + '0')
                    start = i + 1                   
        substr.sort(reverse=True)
        return ''.join(substr)

```
