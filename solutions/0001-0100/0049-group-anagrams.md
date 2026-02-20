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
暂无（需要从LeetCode获取）

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
