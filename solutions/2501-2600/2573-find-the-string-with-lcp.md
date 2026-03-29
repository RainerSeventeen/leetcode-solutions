---
id: 2573
title: Find the String with LCP
difficulty: Hard
tags: [greedy, union-find, array, string, dynamic-programming, matrix]
created: 2026-03-29
---

# 2573. 找出对应 LCP 矩阵的字符串

## 题目链接
https://leetcode.cn/problems/find-the-string-with-lcp/

## 题目描述
<p>对任一由 <code>n</code> 个小写英文字母组成的字符串 <code>word</code> ，我们可以定义一个 <code>n x n</code> 的矩阵，并满足：</p>

<ul>
	<li><code>lcp[i][j]</code> 等于子字符串&nbsp;<code>word[i,...,n-1]</code> 和 <code>word[j,...,n-1]</code> 之间的最长公共前缀的长度。</li>
</ul>

<p>给你一个 <code>n x n</code> 的矩阵 <code>lcp</code> 。返回与 <code>lcp</code> 对应的、按字典序最小的字符串&nbsp;<code>word</code> 。如果不存在这样的字符串，则返回空字符串。</p>

<p>对于长度相同的两个字符串 <code>a</code> 和 <code>b</code> ，如果在 <code>a</code> 和 <code>b</code> 不同的第一个位置，字符串 <code>a</code> 的字母在字母表中出现的顺序先于 <code>b</code> 中的对应字母，则认为字符串 <code>a</code> 按字典序比字符串 <code>b</code> 小。例如，<code>"aabd"</code> 在字典上小于 <code>"aaca"</code> ，因为二者不同的第一位置是第三个字母，而&nbsp;<code>'b'</code> 先于 <code>'c'</code> 出现。</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>lcp = [[4,0,2,0],[0,3,0,1],[2,0,2,0],[0,1,0,1]]
<strong>输出：</strong>"abab"
<strong>解释：</strong>lcp 对应由两个交替字母组成的任意 4 字母字符串，字典序最小的是 "abab" 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>lcp = [[4,3,2,1],[3,3,2,1],[2,2,2,1],[1,1,1,1]]
<strong>输出：</strong>"aaaa"
<strong>解释：</strong>lcp 对应只有一个不同字母的任意 4 字母字符串，字典序最小的是 "aaaa" 。 
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>lcp = [[4,3,2,1],[3,3,2,1],[2,2,2,1],[1,1,1,3]]
<strong>输出：</strong>""
<strong>解释：</strong>lcp[3][3] 无法等于 3 ，因为 word[3,...,3] 仅由单个字母组成；因此，不存在答案。
</pre>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n ==&nbsp;</code><code>lcp.length == </code><code>lcp[i].length</code>&nbsp;<code>&lt;= 1000</code></li>
	<li><code><font face="monospace">0 &lt;= lcp[i][j] &lt;= n</font></code></li>
</ul>


## 解题思路

先按字典序从小到大贪心构造字符串。对于当前还未填字母的位置 `i`，只要 `lcp[i][j] > 0`，就说明 `s[i]` 和 `s[j]` 必须相同，因此把这些位置统一赋成当前最小可用字母。这样能保证答案字典序最小。

构造完成后，再从后往前检查整张 `lcp` 矩阵是否成立。若 `s[i] != s[j]`，实际 LCP 必为 `0`；否则实际 LCP 等于右下角相邻子问题的结果加一。只要有一处不一致，就说明不存在合法字符串。

- 时间复杂度: $O(n^2)$

- 空间复杂度: $O(n)$

## 相关专题
- [贪心与思维](../../topics/greedy-and-thinking.md)

## 代码
```python
class Solution:
    def findTheString(self, lcp: List[List[int]]) -> str:
        # CV 
        n = len(lcp)
        s = [''] * n
        i = 0  # s[i] 没有填字母
        for c in ascii_lowercase:
            for j in range(i, n):
                if lcp[i][j]:  # s[j] == s[i]
                    s[j] = c
            # 找下一个空位
            while i < n and s[i]:
                i += 1
            if i == n:  # 没有空位
                break

        if i < n:  # 还有空位
            return ""

        # 验证 s 是否符合 lcp 矩阵
        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                # 计算后缀 [i,n-1] 和后缀 [j,n-1] 的实际 LCP
                actual_lcp = 0 if s[i] != s[j] else (1 if i == n - 1 or j == n - 1 else lcp[i + 1][j + 1] + 1)
                if lcp[i][j] != actual_lcp:  # 矛盾
                    return ""
        return ''.join(s)
```
