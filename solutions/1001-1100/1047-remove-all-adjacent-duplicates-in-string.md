---
id: 1047
title: Remove All Adjacent Duplicates In String
difficulty: Easy
tags: [stack, string]
created: 2026-02-21
---

# 1047. 删除字符串中的所有相邻重复项

## 题目链接
https://leetcode.cn/problems/remove-all-adjacent-duplicates-in-string/

## 题目描述
<p>给出由小写字母组成的字符串&nbsp;<code>s</code>，<strong>重复项删除操作</strong>会选择两个相邻且相同的字母，并删除它们。</p>

<p>在 <code>s</code> 上反复执行重复项删除操作，直到无法继续删除。</p>

<p>在完成所有重复项删除操作后返回最终的字符串。答案保证唯一。</p>

<p><strong>示例：</strong></p>

<pre>
<strong>输入：</strong>"abbaca"
<strong>输出：</strong>"ca"
<strong>解释：</strong>
例如，在 "abbaca" 中，我们可以删除 "bb" 由于两字母相邻且相同，这是此时唯一可以执行删除操作的重复项。之后我们得到字符串 "aaca"，其中又只有 "aa" 可以执行重复项删除操作，所以最后的字符串为 "ca"。
</pre>

<p><strong>提示：</strong></p>

<ol>
	<li><code>1 &lt;= s.length &lt;= 10<sup>5</sup></code></li>
	<li><code>s</code> 仅由小写英文字母组成。</li>
</ol>


## 解题思路

把结果串 `res` 当作栈使用，遍历原串逐个处理字符。
若当前字符与栈顶相同就弹出，否则压入，最终 `res` 即为删除相邻重复后的字符串。
- 时间复杂度: $O(n)$
- 空间复杂度: $O(n)$

## 相关专题
- [常用数据结构](../../topics/common-data-structures.md)

## 代码
```cpp
#include <string>
#include <algorithm>

class Solution {
public:
    string removeDuplicates(const std::string& s) {
        std::string res;
        res.reserve(s.size());
        for (char c : s) {
            if (!res.empty() && res.back() == c) res.pop_back();
            else res.push_back(c);
        }
        return res;
    }
};
```
