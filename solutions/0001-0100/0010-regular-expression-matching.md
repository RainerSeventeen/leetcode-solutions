---
id: 10
title: Regular Expression Matching
difficulty: Hard
tags: [recursion, string, dynamic-programming]
created: 2026-02-20
---

# 10. 正则表达式匹配

## 题目链接
https://leetcode.cn/problems/regular-expression-matching/

## 题目描述
<p>给你一个字符串&nbsp;<code>s</code>&nbsp;和一个字符规律&nbsp;<code>p</code>，请你来实现一个支持 <code>'.'</code>&nbsp;和&nbsp;<code>'*'</code>&nbsp;的正则表达式匹配。</p>

<ul>
	<li><code>'.'</code> 匹配任意单个字符</li>
	<li><code>'*'</code> 匹配零个或多个前面的那一个元素</li>
</ul>

<p>所谓匹配，是要涵盖&nbsp;<strong>整个&nbsp;</strong>字符串&nbsp;<code>s</code> 的，而不是部分字符串。</p>
&nbsp;

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>s = "aa", p = "a"
<strong>输出：</strong>false
<strong>解释：</strong>"a" 无法匹配 "aa" 整个字符串。
</pre>

<p><strong>示例 2:</strong></p>

<pre>
<strong>输入：</strong>s = "aa", p = "a*"
<strong>输出：</strong>true
<strong>解释：</strong>因为 '*' 代表可以匹配零个或多个前面的那一个元素, 在这里前面的元素就是 'a'。因此，字符串 "aa" 可被视为 'a' 重复了一次。
</pre>

<p><strong>示例&nbsp;3：</strong></p>

<pre>
<strong>输入：</strong>s = "ab", p = ".*"
<strong>输出：</strong>true
<strong>解释：</strong>".*" 表示可匹配零个或多个（'*'）任意字符（'.'）。
</pre>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length&nbsp;&lt;= 20</code></li>
	<li><code>1 &lt;= p.length&nbsp;&lt;= 20</code></li>
	<li><code>s</code>&nbsp;只包含从&nbsp;<code>a-z</code>&nbsp;的小写字母。</li>
	<li><code>p</code>&nbsp;只包含从&nbsp;<code>a-z</code>&nbsp;的小写字母，以及字符&nbsp;<code>.</code>&nbsp;和&nbsp;<code>*</code>。</li>
	<li>保证每次出现字符&nbsp;<code>*</code> 时，前面都匹配到有效的字符</li>
</ul>



## 解题思路

典型 DP。令 `dp[i][j]` 表示 `s[:i]` 是否能匹配 `p[:j]`（下标按“长度”计，方便处理空串）。

状态转移分两类：

1) `p[j-1] != '*'`：当前字符必须一一匹配  
`dp[i][j] = dp[i-1][j-1] and match(s[i-1], p[j-1])`，其中 `match` 表示字符相等或模式为 `'.'`。

2) `p[j-1] == '*'`：`*` 作用于前一个字符 `p[j-2]`，有两种选择  
- 取 0 次：`dp[i][j] |= dp[i][j-2]`（直接把“x*”整体删掉）  
- 取 >= 1 次：若 `match(s[i-1], p[j-2])`，则 `dp[i][j] |= dp[i-1][j]`（消耗掉 `s` 的一个字符，模式仍停在 `j`）

初始化：`dp[0][0] = True`；当 `p` 形如 `a*b*c*...` 时，空串可匹配，所以对 `dp[0][j]` 需要沿着 `*` 做 `dp[0][j] = dp[0][j-2]` 的初始化。

- 时间复杂度: $O(mn)$
- 空间复杂度: $O(mn)$

## 代码
```python
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m = len(s) + 1
        n = len(p) + 1
        dp = [[False] * n for _ in range(m)] # dp[i][j]表示 s[:i] 匹配 p[:j]
        
        # 初始化
        dp[0][0] = True
        for j in range(2, n):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]

        def _match(sc, pc):
            return pc == '.' or sc == pc

        for i in range(1, m):
            for j in range(1, n):
                sc = s[i - 1]
                pc = p[j - 1]
                if pc != "*":
                    dp[i][j] = dp[i - 1][j - 1] and _match(sc, pc)
                else:
                    dp[i][j] = dp[i][j - 2] # 跳过不匹配
                    dp[i][j] |= _match(sc, p[j - 2]) and dp[i - 1][j]    # 尝试匹配一次
        return dp[m - 1][n - 1]
```
