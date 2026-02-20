---
id: 516
title: Longest Palindromic Subsequence
difficulty: Medium
tags: [string, dynamic-programming]
created: 2026-02-20
---

# 516. 最长回文子序列

## 题目链接
https://leetcode.cn/problems/longest-palindromic-subsequence/

## 题目描述
<p>给你一个字符串 <code>s</code> ，找出其中最长的回文子序列，并返回该序列的长度。</p>

<p>子序列定义为：不改变剩余字符顺序的情况下，删除某些字符或者不删除任何字符形成的一个序列。</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>s = "bbbab"
<strong>输出：</strong>4
<strong>解释：</strong>一个可能的最长回文子序列为 "bbbb" 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>s = "cbbd"
<strong>输出：</strong>2
<strong>解释：</strong>一个可能的最长回文子序列为 "bb" 。
</pre>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 <= s.length <= 1000</code></li>
	<li><code>s</code> 仅由小写英文字母组成</li>
</ul>


## 解题思路

区间 DP。设 `dp[i][j]` 为子串 `s[i..j]` 的最长回文子序列长度。

- 当 `s[i] == s[j]`：`dp[i][j] = dp[i + 1][j - 1] + 2`
- 否则：`dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])`

单字符区间初始化为 1。由于依赖 `i+1`，`i` 需要从后往前枚举。

- 时间复杂度: `O(n^2)`
- 空间复杂度: `O(n^2)`

## 代码
```python
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            dp[i][i] = 1
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
        return dp[0][n - 1]
```
