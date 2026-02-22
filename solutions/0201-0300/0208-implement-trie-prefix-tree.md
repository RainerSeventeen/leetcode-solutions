---
id: 208
title: Implement Trie (Prefix Tree)
difficulty: Medium
tags: [design, trie, hash-table, string]
created: 2026-02-20
---

# 208. 实现 Trie (前缀树)

## 题目链接
https://leetcode.cn/problems/implement-trie-prefix-tree/

## 题目描述
<p><strong><a href="https://baike.baidu.com/item/字典树/9825209?fr=aladdin" target="_blank">Trie</a></strong>（发音类似 "try"）或者说 <strong>前缀树</strong> 是一种树形数据结构，用于高效地存储和检索字符串数据集中的键。这一数据结构有相当多的应用情景，例如自动补全和拼写检查。</p>

<p>请你实现 Trie 类：</p>

<ul>
	<li><code>Trie()</code> 初始化前缀树对象。</li>
	<li><code>void insert(String word)</code> 向前缀树中插入字符串 <code>word</code> 。</li>
	<li><code>boolean search(String word)</code> 如果字符串 <code>word</code> 在前缀树中，返回 <code>true</code>（即，在检索之前已经插入）；否则，返回 <code>false</code> 。</li>
	<li><code>boolean startsWith(String prefix)</code> 如果之前已经插入的字符串&nbsp;<code>word</code> 的前缀之一为 <code>prefix</code> ，返回 <code>true</code> ；否则，返回 <code>false</code> 。</li>
</ul>

<p><strong>示例：</strong></p>

<pre>
<strong>输入</strong>
["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
<strong>输出</strong>
[null, null, true, false, true, null, true]

<strong>解释</strong>
Trie trie = new Trie();
trie.insert("apple");
trie.search("apple");   // 返回 True
trie.search("app");     // 返回 False
trie.startsWith("app"); // 返回 True
trie.insert("app");
trie.search("app");     // 返回 True
</pre>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= word.length, prefix.length &lt;= 2000</code></li>
	<li><code>word</code> 和 <code>prefix</code> 仅由小写英文字母组成</li>
	<li><code>insert</code>、<code>search</code> 和 <code>startsWith</code> 调用次数 <strong>总计</strong> 不超过 <code>3 * 10<sup>4</sup></code> 次</li>
</ul>


## 解题思路

使用 `dict` 可以省去一个 标记 curr 节点代表的字符

- 时间复杂度: $O(L)$
- 空间复杂度: $O(n)$

其中 `L` 为单词/前缀长度，`n` 为所有已插入单词的总字符数。
## 相关专题
- [常用数据结构](../../topics/common-data-structures.md)

## 代码
```python
class Trie:
    def __init__(self):
        self.children = {} # 下一个的一组树形 
        self.is_node = False

    def insert(self, word: str) -> None:
        node = self
        for c in word:
            node = node.children.setdefault(c, Trie())
        node.is_node = True

    def search(self, word: str) -> bool:
        node = self
        for s in word:
            node = node.children.get(s, None)
            if node is None:
                return False
        return node.is_node

    def startsWith(self, prefix: str) -> bool:
        node = self
        for s in prefix:
            node = node.children.get(s, None)
            if node is None:
                return False
        return True
```
