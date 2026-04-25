---
id: 2452
title: Words Within Two Edits of Dictionary
difficulty: Medium
tags: [trie, array, string]
created: 2026-04-25
---

# 2452. 距离字典两次编辑以内的单词

## 题目链接
https://leetcode.cn/problems/words-within-two-edits-of-dictionary/

## 题目描述
<p>给你两个字符串数组&nbsp;<code>queries</code> 和&nbsp;<code>dictionary</code>&nbsp;。数组中所有单词都只包含小写英文字母，且长度都相同。</p>

<p>一次 <strong>编辑</strong>&nbsp;中，你可以从 <code>queries</code>&nbsp;中选择一个单词，将任意一个字母修改成任何其他字母。从&nbsp;<code>queries</code>&nbsp;中找到所有满足以下条件的字符串：<strong>不超过</strong>&nbsp;两次编辑内，字符串与&nbsp;<code>dictionary</code>&nbsp;中某个字符串相同。</p>

<p>请你返回<em>&nbsp;</em><code>queries</code>&nbsp;中的单词列表，这些单词距离&nbsp;<code>dictionary</code>&nbsp;中的单词&nbsp;<strong>编辑次数</strong>&nbsp;不超过&nbsp;<strong>两次</strong>&nbsp;。单词返回的顺序需要与&nbsp;<code>queries</code>&nbsp;中原本顺序相同。</p>

<p><strong>示例 1：</strong></p>

<pre><b>输入：</b>queries = ["word","note","ants","wood"], dictionary = ["wood","joke","moat"]
<b>输出：</b>["word","note","wood"]
<strong>解释：</strong>
- 将 "word" 中的 'r' 换成 'o' ，得到 dictionary 中的单词 "wood" 。
- 将 "note" 中的 'n' 换成 'j' 且将 't' 换成 'k' ，得到 "joke" 。
- "ants" 需要超过 2 次编辑才能得到 dictionary 中的单词。
- "wood" 不需要修改（0 次编辑），就得到 dictionary 中相同的单词。
所以我们返回 ["word","note","wood"] 。
</pre>

<p><strong>示例 2：</strong></p>

<pre><b>输入：</b>queries = ["yes"], dictionary = ["not"]
<b>输出：</b>[]
<strong>解释：</strong>
"yes" 需要超过 2 次编辑才能得到 "not" 。
所以我们返回空数组。
</pre>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= queries.length, dictionary.length &lt;= 100</code></li>
	<li><code>n == queries[i].length == dictionary[j].length</code></li>
	<li><code>1 &lt;= n &lt;= 100</code></li>
	<li>所有&nbsp;<code>queries[i]</code> 和&nbsp;<code>dictionary[j]</code>&nbsp;都只包含小写英文字母。</li>
</ul>


## 解题思路

枚举每个查询单词，再枚举字典中的单词。由于题目给定所有单词长度相同，只需要逐位比较不同字符数量；一旦差异超过 2 就可以提前停止。若存在某个字典单词与查询单词差异不超过 2，则保留该查询单词。

- 时间复杂度: $O(qdm)$，其中 `q` 为 `queries` 长度，`d` 为 `dictionary` 长度，`m` 为单词长度。

- 空间复杂度: $O(1)$，不计返回值。

## 相关专题

- [字符串](../../topics/string-algorithms.md)

## 代码
```python
class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        # 1. 只能换字母，所以长度相同
        # 2. 指针遍历
        ans = []
        for q in queries:
            n = len(q)
            for wd in dictionary:
                if len(wd) != n:
                    continue
                cnt, i = 0, 0
                while i < n and cnt <= 2:
                    if q[i] != wd[i]:
                        cnt += 1
                    i += 1
                if i == n and cnt <= 2:
                    ans.append(q)
                    break
        return ans
```
