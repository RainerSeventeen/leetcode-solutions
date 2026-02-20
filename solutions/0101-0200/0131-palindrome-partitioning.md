---
id: 131
title: Palindrome Partitioning
difficulty: Medium
tags: [string, dynamic-programming, backtracking]
created: 2026-02-20
---

# 131. 分割回文串

## 题目链接
https://leetcode.cn/problems/palindrome-partitioning/

## 题目描述
<p>给你一个字符串 <code>s</code>，请你将<em> </em><code>s</code><em> </em>分割成一些 <span data-keyword="substring-nonempty">子串</span>，使每个子串都是 <strong><span data-keyword="palindrome-string">回文串</span></strong> 。返回 <code>s</code> 所有可能的分割方案。</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>s = "aab"
<strong>输出：</strong>[["a","a","b"],["aa","b"]]
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>s = "a"
<strong>输出：</strong>[["a"]]
</pre>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 16</code></li>
	<li><code>s</code> 仅由小写英文字母组成</li>
</ul>


## 解题思路

这题本质是“在字符串里放切割点”，回溯路径保存当前切出的回文子串。递归函数用一个起点 `curr` 表示当前还未处理的后缀，从 `curr + 1` 到 `end` 枚举右边界，每次取左闭右开区间 `[curr, i)`，只有是回文时才加入路径并继续递归。

判断回文使用双指针，在当前区间内向中间收缩。每当 `curr` 走到字符串末尾，说明找到一组完整切分，加入答案。通过“先判断回文再递归”可以减少无效分支。

- 时间复杂度: $O(n^2 \cdot 2^n)$
- 空间复杂度: $O(n)$

不计答案存储。

## 代码
```cpp
class Solution {
public:
    vector<vector<string>> partition(string s) {
        auto curr = s.begin();
        traceback(s, curr);
        return ret;
    }

private:
    vector<vector<string>> ret;
    vector<string> path;

    void traceback(const string& s, string::iterator curr) {
        if ((curr - s.begin()) >= static_cast<long>(s.size())) {
            ret.push_back(path);
            return;
        }

        for (auto i = curr + 1; i <= s.end(); i++) {
            if (!is_palindrome(curr, i)) continue;
            path.push_back(string(curr, i));
            traceback(s, i);
            path.pop_back();
        }
    }

    bool is_palindrome(string::iterator first, string::iterator last) {
        if (first == last) return true;
        --last;
        while (first < last) {
            if (*first != *last) return false;
            ++first;
            --last;
        }
        return true;
    }
};
```
