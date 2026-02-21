---
id: 127
title: Word Ladder
difficulty: Hard
tags: [breadth-first-search, hash-table, string]
created: 2026-02-21
---

# 127. 单词接龙

## 题目链接
https://leetcode.cn/problems/word-ladder/

## 题目描述
<p>字典&nbsp;<code>wordList</code> 中从单词 <code>beginWord</code><em>&nbsp;</em>到&nbsp;<code>endWord</code> 的 <strong>转换序列 </strong>是一个按下述规格形成的序列<meta charset="UTF-8" />&nbsp;<code>beginWord -&gt; s<sub>1</sub>&nbsp;-&gt; s<sub>2</sub>&nbsp;-&gt; ... -&gt; s<sub>k</sub></code>：</p>

<ul>
	<li>每一对相邻的单词只差一个字母。</li>
	<li><meta charset="UTF-8" />&nbsp;对于&nbsp;<code>1 &lt;= i &lt;= k</code>&nbsp;时，每个<meta charset="UTF-8" />&nbsp;<code>s<sub>i</sub></code>&nbsp;都在<meta charset="UTF-8" />&nbsp;<code>wordList</code>&nbsp;中。注意， <code>beginWord</code><em>&nbsp;</em>不需要在<meta charset="UTF-8" />&nbsp;<code>wordList</code>&nbsp;中。<meta charset="UTF-8" /></li>
	<li><code>s<sub>k</sub>&nbsp;== endWord</code></li>
</ul>

<p>给你两个单词<em> </em><code>beginWord</code><em>&nbsp;</em>和 <code>endWord</code> 和一个字典 <code>wordList</code> ，返回 <em>从&nbsp;<code>beginWord</code> 到&nbsp;<code>endWord</code> 的 <strong>最短转换序列</strong> 中的 <strong>单词数目</strong></em> 。如果不存在这样的转换序列，返回 <code>0</code> 。</p>
&nbsp;

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
<strong>输出：</strong>5
<strong>解释：</strong>一个最短转换序列是 "hit" -&gt; "hot" -&gt; "dot" -&gt; "dog" -&gt; "cog", 返回它的长度 5。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
<strong>输出：</strong>0
<strong>解释：</strong>endWord "cog" 不在字典中，所以无法进行转换。</pre>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= beginWord.length &lt;= 10</code></li>
	<li><code>endWord.length == beginWord.length</code></li>
	<li><code>1 &lt;= wordList.length &lt;= 5000</code></li>
	<li><code>wordList[i].length == beginWord.length</code></li>
	<li><code>beginWord</code>、<code>endWord</code> 和 <code>wordList[i]</code> 由小写英文字母组成</li>
	<li><code>beginWord != endWord</code></li>
	<li><code>wordList</code> 中的所有字符串 <strong>互不相同</strong></li>
</ul>


## 解题思路

使用 BFS 从 `beginWord` 分层扩展，层数即转换步数。
对每个位置尝试替换 26 个字母，若新词在词典集合中则入队并立刻删除去重。
首次遇到 `endWord` 时返回当前层数加一。
- 时间复杂度: $O(N \cdot L \cdot 26)$
- 空间复杂度: $O(N)$

## 代码
```python
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_map = set(wordList)
        n = len(beginWord)
        q = deque([beginWord])
        path_count = 0
        while q:
            path_count += 1 # 路径数量
            for _ in range(len(q)):
                w = q.pop()    
                for i in range(n):
                    for alpha in range(26): # 替换第 i 个字母
                        build = w[0:i] + chr(alpha + ord('a')) + w[i + 1:n]
                        if build in word_map:
                            if build == endWord:
                                return path_count + 1
                            print(path_count, w, build)
                            q.appendleft(build)
                            word_map.remove(build) # 移除, 去重
        return 0
```
