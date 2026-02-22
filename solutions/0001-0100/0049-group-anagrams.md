---
id: 49
title: 字母异位词分组
difficulty: Medium
tags: [array, hash-table, string, sorting]
created: 2026-02-20
---

# 49. 字母异位词分组

## 题目链接
https://leetcode.cn/problems/group-anagrams/

## 题目描述

<p>给你一个字符串数组，请你将 <span data-keyword="anagram">字母异位词</span> 组合在一起。可以按任意顺序返回结果列表。</p>

<p><strong>示例 1:</strong></p>

<div class="example-block">
<p><strong>输入:</strong> strs = ["eat", "tea", "tan", "ate", "nat", "bat"]</p>

<p><strong>输出: </strong>[["bat"],["nat","tan"],["ate","eat","tea"]]</p>

<p><strong>解释：</strong></p>

<ul>
	<li>在 strs 中没有字符串可以通过重新排列来形成 <code>"bat"</code>。</li>
	<li>字符串 <code>"nat"</code> 和 <code>"tan"</code> 是字母异位词，因为它们可以重新排列以形成彼此。</li>
	<li>字符串 <code>"ate"</code>&nbsp;，<code>"eat"</code>&nbsp;和 <code>"tea"</code> 是字母异位词，因为它们可以重新排列以形成彼此。</li>
</ul>
</div>

<p><strong>示例 2:</strong></p>

<div class="example-block">
<p><strong>输入:</strong> strs = [""]</p>

<p><strong>输出: </strong>[[""]]</p>
</div>

<p><strong>示例 3:</strong></p>

<div class="example-block">
<p><strong>输入:</strong> strs = ["a"]</p>

<p><strong>输出: </strong>[["a"]]</p>
</div>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= strs.length &lt;= 10<sup>4</sup></code></li>
	<li><code>0 &lt;= strs[i].length &lt;= 100</code></li>
	<li><code>strs[i]</code>&nbsp;仅包含小写字母</li>
</ul>

## 解题思路
异位词的本质是：**每个字符出现次数相同**。因此可以把每个字符串映射成一个“可比较的特征（key）”，再把 key 相同的字符串分到同一组。

常见 key 有两种：

1. **排序后的字符串**作为 key（例如 `eat -> aet`），实现简单，但每个字符串需要排序。
2. **26 维计数向量**作为 key（只含小写字母时），例如 `cnt[0..25]`，把计数向量转成元组作为字典 key。

本题采用第 2 种：遍历每个单词，统计 26 个字母次数得到 `key = tuple(cnt)`，用哈希表 `mp[key]` 维护同组元素列表。

边界与实现细节：

- 空字符串会得到全 0 计数向量，天然会被分到同一组。
- Python 中如果用 `dict.get(key, [])` 取默认空列表，**对这个默认列表的 append 不会写回字典**（因为它没有被放入 `dict`）。应使用 `defaultdict(list)` 或 `setdefault` 来保证“取出来的就是字典里那份列表”。

复杂度说明：设字符串数量为 $n$，平均长度为 $k$，统计计数需要扫描每个字符一次。

- 时间复杂度: $O(nk)$
- 空间复杂度: $O(n)$

## 相关专题
- [常用数据结构](../../topics/common-data-structures.md)

## 代码
```python
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = {}
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            key = tuple(count)
            mp.setdefault(key, []).append(s)
        return list(mp.values())
```
