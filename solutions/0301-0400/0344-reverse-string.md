---
id: 344
title: Reverse String
difficulty: Easy
tags: [two-pointers, string]
created: 2026-02-21
---

# 344. 反转字符串

## 题目链接
https://leetcode.cn/problems/reverse-string/

## 题目描述
<p>编写一个函数，其作用是将输入的字符串反转过来。输入字符串以字符数组 <code>s</code> 的形式给出。</p>

<p>不要给另外的数组分配额外的空间，你必须<strong><a href="https://baike.baidu.com/item/原地算法" target="_blank">原地</a>修改输入数组</strong>、使用 O(1) 的额外空间解决这一问题。</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>s = ["h","e","l","l","o"]
<strong>输出：</strong>["o","l","l","e","h"]
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>s = ["H","a","n","n","a","h"]
<strong>输出：</strong>["h","a","n","n","a","H"]</pre>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>5</sup></code></li>
	<li><code>s[i]</code> 都是 <a href="https://baike.baidu.com/item/ASCII" target="_blank">ASCII</a> 码表中的可打印字符</li>
</ul>


## 解题思路

使用双指针分别指向首尾，循环交换两个位置的字符后向中间收缩。
当左右指针相遇或交错时，整个数组已完成原地翻转。
- 时间复杂度: $O(n)$
- 空间复杂度: $O(1)$

## 代码
```cpp
#include <utility>
class Solution {
public:
    void reverseString(vector<char>& s) {
        int i = 0;
        int j = s.size() - 1;
        while (i < j) {
            swap(s[i], s[j]);
            i++;
            j--;
        }
        return;
    }
};
```
