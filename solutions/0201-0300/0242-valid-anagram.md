---
id: 242
title: Valid Anagram
difficulty: Easy
tags: [hash-table, string, sorting]
created: 2026-02-21
---

# 242. 有效的字母异位词

## 题目链接
https://leetcode.cn/problems/valid-anagram/

## 题目描述
<p>给定两个字符串 <code>s</code> 和 <code>t</code> ，编写一个函数来判断 <code>t</code> 是否是 <code>s</code> 的 <span data-keyword="anagram">字母异位词</span>。</p>

<p><strong>示例&nbsp;1:</strong></p>

<pre>
<strong>输入:</strong> s = "anagram", t = "nagaram"
<strong>输出:</strong> true
</pre>

<p><strong>示例 2:</strong></p>

<pre>
<strong>输入:</strong> s = "rat", t = "car"
<strong>输出: </strong>false</pre>

<p><strong>提示:</strong></p>

<ul>
	<li><code>1 &lt;= s.length, t.length &lt;= 5 * 10<sup>4</sup></code></li>
	<li><code>s</code> 和 <code>t</code>&nbsp;仅包含小写字母</li>
</ul>

<p><strong>进阶:&nbsp;</strong>如果输入字符串包含 unicode 字符怎么办？你能否调整你的解法来应对这种情况？</p>


## 解题思路

先判断两字符串长度，不相等可直接返回 `false`。
用哈希表统计 `s` 每个字符频次，再遍历 `t` 逐个抵消计数。
若出现不存在字符或计数减到负数，则不是字母异位词。
- 时间复杂度: $O(n)$
- 空间复杂度: $O(1)$

## 代码
```cpp
#include <unordered_map>
class Solution {
public:
    bool isAnagram(string s, string t) {
        unordered_map<char, int> umap;
        if (s.size() != t.size())
            return false;

        int s_len = s.length();

        for (int i = 0; i < s_len; i++) {
            umap[s[i]] += 1;
        }
        
        for (int i = 0; i < s_len; i++) {
            auto it = umap.find(t[i]);
            if (it == umap.end()) {
                return false;
            }
            umap[t[i]] -= 1;
            if (umap[t[i]] < 0) {
                return false;
            }   
        }
        return true;        
    }
};
```
