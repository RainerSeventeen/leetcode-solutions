---
id: 541
title: Reverse String II
difficulty: Easy
tags: [two-pointers, string]
created: 2026-02-21
---

# 541. 反转字符串 II

## 题目链接
https://leetcode.cn/problems/reverse-string-ii/

## 题目描述
<p>给定一个字符串 <code>s</code> 和一个整数 <code>k</code>，从字符串开头算起，每计数至 <code>2k</code> 个字符，就反转这 <code>2k</code> 字符中的前 <code>k</code> 个字符。</p>

<ul>
	<li>如果剩余字符少于 <code>k</code> 个，则将剩余字符全部反转。</li>
	<li>如果剩余字符小于 <code>2k</code> 但大于或等于 <code>k</code> 个，则反转前 <code>k</code> 个字符，其余字符保持原样。</li>
</ul>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>s = "abcdefg", k = 2
<strong>输出：</strong>"bacdfeg"
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>s = "abcd", k = 2
<strong>输出：</strong>"bacd"
</pre>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>4</sup></code></li>
	<li><code>s</code> 仅由小写英文组成</li>
	<li><code>1 &lt;= k &lt;= 10<sup>4</sup></code></li>
</ul>


## 解题思路

按步长 `2k` 遍历字符串，每段只反转前 `k` 个字符。
当剩余字符不足 `k` 时反转全部，介于 `k` 到 `2k` 时只反转前 `k`，与题意一致。
使用库函数 `reverse` 原地交换字符即可。
- 时间复杂度: $O(n)$
- 空间复杂度: $O(1)$

## 代码
```cpp
#include <utility>
#include <algorithm>
class Solution {
public:
    string reverseStr(string s, int k) {
        for (int i = 0; i < s.length(); i += 2 * k) {
            int n = s.size();
            auto first = s.begin() + i;
            auto last = s.begin() + min(i + k, n);
            reverse(first, last);
        }
        return s;
    }
};
```
