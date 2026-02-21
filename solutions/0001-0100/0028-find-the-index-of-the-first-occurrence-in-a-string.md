---
id: 28
title: Find the Index of the First Occurrence in a String
difficulty: Easy
tags: [two-pointers, string, string-matching]
created: 2026-02-21
---

# 28. 找出字符串中第一个匹配项的下标

## 题目链接
https://leetcode.cn/problems/find-the-index-of-the-first-occurrence-in-a-string/

## 题目描述
<p>给你两个字符串&nbsp;<code>haystack</code> 和 <code>needle</code> ，请你在 <code>haystack</code> 字符串中找出 <code>needle</code> 字符串的第一个匹配项的下标（下标从 0 开始）。如果&nbsp;<code>needle</code> 不是 <code>haystack</code> 的一部分，则返回&nbsp; <code>-1</code><strong> </strong>。</p>

<p><strong class="example">示例 1：</strong></p>

<pre>
<strong>输入：</strong>haystack = "sadbutsad", needle = "sad"
<strong>输出：</strong>0
<strong>解释：</strong>"sad" 在下标 0 和 6 处匹配。
第一个匹配项的下标是 0 ，所以返回 0 。
</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<strong>输入：</strong>haystack = "leetcode", needle = "leeto"
<strong>输出：</strong>-1
<strong>解释：</strong>"leeto" 没有在 "leetcode" 中出现，所以返回 -1 。
</pre>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= haystack.length, needle.length &lt;= 10<sup>4</sup></code></li>
	<li><code>haystack</code> 和 <code>needle</code> 仅由小写英文字符组成</li>
</ul>


## 解题思路

使用 KMP：先为 `needle` 构建 `next` 数组，表示前后缀最长匹配长度。
扫描 `haystack` 时失配就按 `next` 回退模式串指针，匹配完成时返回起始下标。
- 时间复杂度: $O(n+m)$
- 空间复杂度: $O(m)$

## 代码
```cpp
#include <vector>
class Solution {
public:

    vector<int> getNext(string needle) {
        vector<int> next;
        next.resize(needle.size());
        // 1. 初始化
        int i = 0, j = 0;
        for (int i = 1; i < needle.size(); i++) {
            // 2. 不相等
            while (j > 0 && needle[j] != needle[i]) {
                j = next[j - 1];
            }
            // 3. 相等
            if (needle[i] == needle[j]) {
                j++;
            }
            // 4. 赋值
            next[i] = j;
        }
        return next;
    }

    int strStr(string haystack, string needle) {
        // 使用 KMP 算法
        vector<int> next = getNext(needle);
        
        // next pointer, target pointer
        int np = 0, tp = 0;
        for (tp = 0; tp < haystack.size(); tp++) {
            while (haystack[tp] != needle[np] && np > 0) {
                // 不相等，np回退
                np = next[np - 1];
            }
            if (haystack[tp] == needle[np]) {
                np++;
            }
            if (np == needle.size()) {
                // 找到了
                return (tp - needle.size() + 1);
            }
        }
    return -1;
    }
};
```
