---
id: 383
title: Ransom Note
difficulty: Easy
tags: [hash-table, string, counting]
created: 2026-02-21
---

# 383. 赎金信

## 题目链接
https://leetcode.cn/problems/ransom-note/

## 题目描述
<p>给你两个字符串：<code>ransomNote</code> 和 <code>magazine</code> ，判断 <code>ransomNote</code> 能不能由 <code>magazine</code> 里面的字符构成。</p>

<p>如果可以，返回 <code>true</code> ；否则返回 <code>false</code> 。</p>

<p><code>magazine</code> 中的每个字符只能在 <code>ransomNote</code> 中使用一次。</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>ransomNote = "a", magazine = "b"
<strong>输出：</strong>false
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>ransomNote = "aa", magazine = "ab"
<strong>输出：</strong>false
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>ransomNote = "aa", magazine = "aab"
<strong>输出：</strong>true
</pre>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= ransomNote.length, magazine.length &lt;= 10<sup>5</sup></code></li>
	<li><code>ransomNote</code> 和 <code>magazine</code> 由小写英文字母组成</li>
</ul>


## 解题思路

用长度为 26 的计数数组统计 `magazine` 每个字母出现次数。
再遍历 `ransomNote`，对应计数减一；一旦出现负数说明该字符不够用。
遍历结束都合法则可以拼出赎金信。
- 时间复杂度: $O(m+n)$
- 空间复杂度: $O(1)$

## 代码
```cpp
class Solution {
public:
    bool canConstruct(string ransomNote, string magazine) {
        int table_r[26] = {0};
        for (char c : magazine) {
            table_r[c - 'a'] += 1;
        }
        for (char c : ransomNote) {
            table_r[c - 'a'] -= 1;
            if (table_r[c - 'a'] < 0) {
                return false;
            }
        }
        return true;
    }
};
```
