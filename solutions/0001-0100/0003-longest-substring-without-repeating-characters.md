---
id: 3
title: Longest Substring Without Repeating Characters
difficulty: Medium
tags: [hash-table, string, sliding-window]
created: 2026-02-20
---

# 3. 无重复字符的最长子串

## 题目链接
https://leetcode.cn/problems/longest-substring-without-repeating-characters/

## 题目描述
<p>给定一个字符串 <code>s</code> ，请你找出其中不含有重复字符的&nbsp;<strong>最长 <span data-keyword="substring-nonempty">子串</span></strong><strong>&nbsp;</strong>的长度。</p>

<p><strong>示例&nbsp;1:</strong></p>

<pre>
<strong>输入: </strong>s = "abcabcbb"
<strong>输出: </strong>3 
<strong>解释:</strong> 因为无重复字符的最长子串是 <code>"abc"</code>，所以其长度为 3。注意 "bca" 和 "cab" 也是正确答案。
</pre>

<p><strong>示例 2:</strong></p>

<pre>
<strong>输入: </strong>s = "bbbbb"
<strong>输出: </strong>1
<strong>解释: </strong>因为无重复字符的最长子串是 <code>"b"</code>，所以其长度为 1。
</pre>

<p><strong>示例 3:</strong></p>

<pre>
<strong>输入: </strong>s = "pwwkew"
<strong>输出: </strong>3
<strong>解释: </strong>因为无重复字符的最长子串是&nbsp;<code>"wke"</code>，所以其长度为 3。
&nbsp;    请注意，你的答案必须是 <strong>子串 </strong>的长度，<code>"pwke"</code>&nbsp;是一个<em>子序列，</em>不是子串。
</pre>

<p><strong>提示：</strong></p>

<ul>
	<li><code>0 &lt;= s.length &lt;= 5 * 10<sup>4</sup></code></li>
	<li><code>s</code>&nbsp;由英文字母、数字、符号和空格组成</li>
</ul>



## 解题思路

滑动窗口 + 集合去重。维护一个窗口 `[l, r)`，保证窗口内字符都不重复（不变量），并用 `set` 记录窗口内字符：

- 固定左端 `l`，不断右扩 `r`，只要 `s[r]` 不在集合中就加入并更新答案；
- 一旦 `s[r]` 已出现，说明再扩会破坏不变量，此时左端右移：移除 `s[l]`，进入下一轮。

由于每个字符最多被 `r` 加入一次、被 `l` 移除一次，整体是线性的。

- 时间复杂度: $O(n)$
- 空间复杂度: $O(\min(n, |\Sigma|))$

## 相关专题
- [滑动窗口与双指针](../../topics/sliding-window-and-two-pointers.md)

## 代码
```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 双指针滑动窗口
        n = len(s)
        mp = set()
        r = 0
        ret = 0
        for l in range(n): # 闭区间区间窗口 [l, r]
            while r < n and s[r] not in mp: # 不在则加入，同时最长长度更新
                mp.add(s[r])
                ret = max(r - l + 1, ret)
                r += 1
            mp.discard(s[l]) # 左边界前移
        return ret
```
