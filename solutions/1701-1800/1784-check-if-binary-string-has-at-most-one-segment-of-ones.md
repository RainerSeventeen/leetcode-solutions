---
id: 1784
title: Check if Binary String Has at Most One Segment of Ones
difficulty: Easy
tags: [string]
created: 2026-03-06
---

# 1784. 检查二进制字符串字段

## 题目链接
https://leetcode.cn/problems/check-if-binary-string-has-at-most-one-segment-of-ones/

## 题目描述
<p>给你一个二进制字符串 <code>s</code> ，该字符串 <strong>不含前导零</strong> 。</p>

<p>如果 <code>s</code> 包含 <strong>零个或一个由连续的 <code>'1'</code> 组成的字段</strong> ，返回 <code>true</code>​​​ 。否则，返回 <code>false</code> 。</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>s = "1001"
<strong>输出：</strong>false
<strong>解释：</strong>由连续若干个&nbsp;<code>'1'</code> 组成的字段数量为 2，返回 false
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>s = "110"
<strong>输出：</strong>true</pre>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 100</code></li>
	<li><code>s[i]</code>​​​​ 为 <code>'0'</code> 或 <code>'1'</code></li>
	<li><code>s[0]</code> 为 <code>'1'</code></li>
</ul>


## 解题思路

遍历字符串，统计由字符变化产生的 `'1'` 段起点数量。  
用 `pre` 记录前一个字符，当 `ch != pre` 且 `ch == '1'` 时，说明遇到一个新的连续 `'1'` 字段，计数加一。  
最后判断字段数是否不超过 1 即可。

- 时间复杂度: $O(n)$，其中 `n` 为字符串长度。

- 空间复杂度: $O(1)$。

## 相关专题
- [滑动窗口与双指针](../../topics/sliding-window-and-two-pointers.md)

## 代码
```python
class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        cnt = 0
        pre = '#'
        for ch in s:
            if ch != pre and ch == '1':
                cnt += 1
            pre = ch
        return cnt <= 1
```
