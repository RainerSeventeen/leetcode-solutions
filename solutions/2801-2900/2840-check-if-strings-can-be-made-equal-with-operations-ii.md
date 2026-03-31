---
id: 2840
title: Check if Strings Can be Made Equal With Operations II
difficulty: Medium
tags: [hash-table, string, sorting]
created: 2026-03-31
---

# 2840. 判断通过操作能否让字符串相等 II

## 题目链接
https://leetcode.cn/problems/check-if-strings-can-be-made-equal-with-operations-ii/

## 题目描述
<p>给你两个字符串&nbsp;<code>s1</code>&nbsp;和&nbsp;<code>s2</code>&nbsp;，两个字符串长度都为&nbsp;<code>n</code>&nbsp;，且只包含&nbsp;<strong>小写&nbsp;</strong>英文字母。</p>

<p>你可以对两个字符串中的 <strong>任意一个</strong>&nbsp;执行以下操作 <strong>任意</strong>&nbsp;次：</p>

<ul>
	<li>选择两个下标&nbsp;<code>i</code> 和&nbsp;<code>j</code>&nbsp;，满足 <code>i &lt; j</code>&nbsp;且 <code>j - i</code>&nbsp;是 <strong>偶数</strong>，然后 <strong>交换</strong> 这个字符串中两个下标对应的字符。</li>
</ul>

<p>如果你可以让字符串<em>&nbsp;</em><code>s1</code><em> </em>和<em>&nbsp;</em><code>s2</code>&nbsp;相等，那么返回 <code>true</code>&nbsp;，否则返回 <code>false</code>&nbsp;。</p>

<p><strong class="example">示例 1：</strong></p>

<pre>
<b>输入：</b>s1 = "abcdba", s2 = "cabdab"
<b>输出：</b>true
<b>解释：</b>我们可以对 s1 执行以下操作：
- 选择下标 i = 0 ，j = 2 ，得到字符串 s1 = "cbadba" 。
- 选择下标 i = 2 ，j = 4 ，得到字符串 s1 = "cbbdaa" 。
- 选择下标 i = 1 ，j = 5 ，得到字符串 s1 = "cabdab" = s2 。
</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<b>输入：</b>s1 = "abe", s2 = "bea"
<b>输出：</b>false
<b>解释：</b>无法让两个字符串相等。
</pre>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == s1.length == s2.length</code></li>
	<li><code>1 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>s1</code> 和&nbsp;<code>s2</code>&nbsp;只包含小写英文字母。</li>
</ul>


## 解题思路

- 由于只能交换同奇偶性的下标，所以每个字符串内部，偶数位和奇数位都可以分别任意重排。
- 因此只要分别收集 `s1` 和 `s2` 的偶数位字符、奇数位字符，再判断两组字符排序后是否完全一致即可。
- 时间复杂度: $O(n \log n)$，其中 `n` 是字符串长度；排序两组长度总和为 `n` 的字符数组是主要开销。

- 空间复杂度: $O(n)$，用于保存奇偶位字符数组。

## 相关专题
- [贪心与思维](../../topics/greedy-and-thinking.md)

## 代码
```python
class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        n = len(s1)
        # 偶数下标会多一个，如果n是奇数
        m_0 = n // 2 + 1 if n & 1 else n // 2
        m_1 = n // 2
        # 奇偶 统计
        a_1 = [0] * m_1
        b_1 = [0] * m_1
        a_0 = [0] * m_0
        b_0 = [0] * m_0

        for i in range(n):
            if i & 1 == 0:
                a_0[i // 2] = s1[i]
                b_0[i // 2] = s2[i]
            else:
                a_1[i // 2] = s1[i]
                b_1[i // 2] = s2[i]

        if sorted(a_0) == sorted(b_0) and sorted(a_1) == sorted(b_1):
            return True
        else:
            return False
```
