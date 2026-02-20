---
id: 139
title: Word Break
difficulty: Medium
tags: [trie, memoization, array, hash-table, string, dynamic-programming]
created: 2026-02-20
---

# 139. 单词拆分

## 题目链接
https://leetcode.cn/problems/word-break/

## 题目描述

<p>给你一个字符串 <code>s</code> 和一个字符串列表 <code>wordDict</code> 作为字典。如果可以利用字典中出现的一个或多个单词拼接出 <code>s</code>&nbsp;则返回 <code>true</code>。</p>

<p><strong>注意：</strong>不要求字典中出现的单词全部都使用，并且字典中的单词可以重复使用。</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入:</strong> s = "leetcode", wordDict = ["leet", "code"]
<strong>输出:</strong> true
<strong>解释:</strong> 返回 true 因为 "leetcode" 可以由 "leet" 和 "code" 拼接成。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入:</strong> s = "applepenapple", wordDict = ["apple", "pen"]
<strong>输出:</strong> true
<strong>解释:</strong> 返回 true 因为 "applepenapple" 可以由 "apple" "pen" "apple" 拼接成。
&nbsp;    注意，你可以重复使用字典中的单词。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入:</strong> s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
<strong>输出:</strong> false
</pre>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 300</code></li>
	<li><code>1 &lt;= wordDict.length &lt;= 1000</code></li>
	<li><code>1 &lt;= wordDict[i].length &lt;= 20</code></li>
	<li><code>s</code> 和 <code>wordDict[i]</code> 仅由小写英文字母组成</li>
	<li><code>wordDict</code> 中的所有字符串 <strong>互不相同</strong></li>
</ul>

## 解题思路

动态规划。`dp[i]` 表示 `s[:i]` 是否可以被字典中的单词拼接而成。

枚举每个分割点 `j`（1 到 n），再枚举字典中所有单词 `w`（长度为 `L`）：若 `dp[j-L]` 为真，且 `s[j-L:j] == w`，则 `dp[j] = True`。递推的起点 `dp[0] = True` 表示空字符串合法。

- 时间复杂度: $O(n \cdot m \cdot L)$
- 空间复杂度: $O(n)$

其中 `n` 为字符串长度，`m` 为字典单词数，`L` 为单词平均长度（切片比较代价）。

## 代码
```python
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        m = len(wordDict)
        n = len(s)
        dp = [False] * (n + 1) # 前 i 个字符 s[:i] 是否可以拆分
        dp[0] = True # 递推的起点，可以拆分
        for j in range(1, n + 1):
            for w in wordDict:
                L = len(w)
                if dp[j - L] == True and s[j - L:j] == w:
                    dp[j] = True
					break 	# 一旦找到就去下一个分割点了
        return dp[n]
```
