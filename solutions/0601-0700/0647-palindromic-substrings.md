---
id: 647
title: Palindromic Substrings
difficulty: Medium
tags: [two-pointers, string, dynamic-programming]
created: 2026-02-20
---

# 647. 回文子串

## 题目链接
https://leetcode.cn/problems/palindromic-substrings/

## 题目描述

<p>给你一个字符串 <code>s</code> ，请你统计并返回这个字符串中 <strong>回文子串</strong> 的数目。</p>

<p><strong>回文字符串</strong> 是正着读和倒过来读一样的字符串。</p>

<p><strong>子字符串</strong> 是字符串中的由连续字符组成的一个序列。</p>

<p><strong class="example">示例 1：</strong></p>

<pre>
<strong>输入：</strong>s = "abc"
<strong>输出：</strong>3
<strong>解释：</strong>三个回文子串: "a", "b", "c"
</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<strong>输入：</strong>s = "aaa"
<strong>输出：</strong>6
<strong>解释：</strong>6个回文子串: "a", "a", "a", "aa", "aa", "aaa"</pre>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 1000</code></li>
	<li><code>s</code> 由小写英文字母组成</li>
</ul>

## 解题思路

区间 DP。`dp[l][r]` 表示子串 `s[l..r]` 是否为回文串。

状态转移：若 `s[l] == s[r]`，且区间长度 `<= 2`（单字符或双字符直接成立）或内部子串 `dp[l+1][r-1]` 已是回文，则 `dp[l][r] = True`，答案加一。枚举顺序：外层按右边界 `r` 从小到大，内层按左边界 `l` 从 `r` 到 `0`，保证子问题先于父问题计算。

- 时间复杂度: $O(n^2)$
- 空间复杂度: $O(n^2)$

## 代码
```python
class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        ret = 0

        for r in range(n):
            for l in range(r, -1, -1):
                if s[l] == s[r]:
                    if r - l <= 2 or dp[l + 1][r - 1]:
                        dp[l][r] = True
                        ret += 1
        return ret
```
