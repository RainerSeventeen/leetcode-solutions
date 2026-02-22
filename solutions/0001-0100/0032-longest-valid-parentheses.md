---
id: 32
title: 最长有效括号
difficulty: Medium
tags: [stack, string, dynamic-programming]
created: 2026-02-20
---

# 32. 最长有效括号

## 题目链接
https://leetcode.cn/problems/longest-valid-parentheses/

## 题目描述

<p>给你一个只包含 <code>'('</code> 和 <code>')'</code> 的字符串，找出最长有效（格式正确且连续）括号 <span data-keyword="substring">子串</span> 的长度。</p>

<p>左右括号匹配，即每个左括号都有对应的右括号将其闭合的字符串是格式正确的，比如&nbsp;<code>"(()())"</code>。</p>

<div class="original__bRMd">
<div>
<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>s = "(()"
<strong>输出：</strong>2
<strong>解释：</strong>最长有效括号子串是 "()"
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>s = ")()())"
<strong>输出：</strong>4
<strong>解释：</strong>最长有效括号子串是 "()()"
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>s = ""
<strong>输出：</strong>0
</pre>

<p><strong>提示：</strong></p>

<ul>
	<li><code>0 &lt;= s.length &lt;= 3 * 10<sup>4</sup></code></li>
	<li><code>s[i]</code> 为 <code>'('</code> 或 <code>')'</code></li>
</ul>
</div>
</div>

## 解题思路
这里用 DP（代码实现亦如此）。定义 `dp[i]` 为“以 `i` 结尾的最长有效括号长度”，只在 `s[i] == ')'` 时可能更新。

讨论两种转移：

1) 形如 `...()`：若 `s[i-1] == '('`，则  
`dp[i] = (dp[i-2] if i>=2 else 0) + 2`。

2) 形如 `...))`：若 `s[i-1] == ')'`，先令 `pre = dp[i-1]` 表示前一段有效长度，尝试跨过它去找与 `s[i]` 匹配的 `'('`：  
`j = i - pre - 1`。若 `j>=0` 且 `s[j] == '('`，则  
`dp[i] = pre + 2 + (dp[j-1] if j>=1 else 0)`，其中最后一项用于把更左侧的有效串拼接上。

遍历过程中维护全局最大值即可。边界主要集中在 `i-2`、`j-1` 可能越界，需要按 0 处理。

- 时间复杂度: $O(n)$
- 空间复杂度: $O(n)$

## 代码
```python
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        dp = [0] * n  # dp[i]: 以 i 结尾的最长有效括号长度
        ret = 0
        for i in range(1, n):
            if s[i] == '(':
                continue  # 以 '(' 结尾不可能是有效括号
            if s[i - 1] == '(':
                # 情况1：紧邻 ()
                dp[i] = (dp[i - 2] if i >= 2 else 0) + 2
            else:
                # 情况2：...))  尝试跨过 dp[i-1] 那段去找 '('
                pre = dp[i - 1]
                j = i - pre - 1  # 可能与 s[i] 匹配的 '(' 位置
                if j >= 0 and s[j] == '(':
                    dp[i] = pre + 2 + (dp[j - 1] if j >= 1 else 0)
            ret = max(ret, dp[i])
        return ret
```
