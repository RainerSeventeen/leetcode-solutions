---
id: 438
title: Find All Anagrams in a String
difficulty: Medium
tags: [hash-table, string, sliding-window]
created: 2026-02-20
---

# 438. 找到字符串中所有字母异位词

## 题目链接
https://leetcode.cn/problems/find-all-anagrams-in-a-string/

## 题目描述

<p>给定两个字符串&nbsp;<code>s</code>&nbsp;和 <code>p</code>，找到&nbsp;<code>s</code><strong>&nbsp;</strong>中所有&nbsp;<code>p</code><strong>&nbsp;</strong>的&nbsp;<strong><span data-keyword="anagram">异位词</span>&nbsp;</strong>的子串，返回这些子串的起始索引。不考虑答案输出的顺序。</p>

<p><strong>示例&nbsp;1:</strong></p>

<pre>
<strong>输入: </strong>s = "cbaebabacd", p = "abc"
<strong>输出: </strong>[0,6]
<strong>解释:</strong>
起始索引等于 0 的子串是 "cba", 它是 "abc" 的异位词。
起始索引等于 6 的子串是 "bac", 它是 "abc" 的异位词。
</pre>

<p><strong>&nbsp;示例 2:</strong></p>

<pre>
<strong>输入: </strong>s = "abab", p = "ab"
<strong>输出: </strong>[0,1,2]
<strong>解释:</strong>
起始索引等于 0 的子串是 "ab", 它是 "ab" 的异位词。
起始索引等于 1 的子串是 "ba", 它是 "ab" 的异位词。
起始索引等于 2 的子串是 "ab", 它是 "ab" 的异位词。
</pre>

<p><strong>提示:</strong></p>

<ul>
	<li><code>1 &lt;= s.length, p.length &lt;= 3 * 10<sup>4</sup></code></li>
	<li><code>s</code>&nbsp;和&nbsp;<code>p</code>&nbsp;仅包含小写字母</li>
</ul>

## 解题思路

固定长度滑动窗口 + 差值数组。

用 `diff[26]` 记录模式串 `p` 与当前窗口各字符的频次差（`p` 中加、窗口中减），再用 `diff_count` 统计差值不为 0 的字符个数。窗口滑动时动态更新移出/移入字符对 `diff_count` 的影响：当 `diff_count == 0` 时，当前窗口是 `p` 的异位词。

- 时间复杂度: $O(m+n)$
- 空间复杂度: $O(1)$

字母表大小固定为 26。

## 代码
```python
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        offset = ord('a')
        m, n = len(s), len(p)
        if n > m:
            return []

        diff = [0] * 26
        for c in p:
            diff[ord(c) - offset] += 1
        for c in s[:n]:
            diff[ord(c) - offset] -= 1

        diff_count = sum(1 for x in diff if x != 0)
        ret = []

        for i in range(m - n + 1):
            if diff_count == 0:
                ret.append(i)
            if i == m - n:
                break  # 最后一个窗口不需要再滑动，和初始化结合控制边界

            out_idx = ord(s[i]) - offset
            in_idx = ord(s[i + n]) - offset

            # out：窗口移出一个字符 => diff[out] += 1
            before = diff[out_idx]
            diff[out_idx] += 1
            after = diff[out_idx]
            if before == 0 and after != 0:
                diff_count += 1
            elif before != 0 and after == 0:
                diff_count -= 1

            # in：窗口移入一个字符 => diff[in] -= 1
            before = diff[in_idx]
            diff[in_idx] -= 1
            after = diff[in_idx]
            if before == 0 and after != 0:
                diff_count += 1
            elif before != 0 and after == 0:
                diff_count -= 1

        return ret
```
