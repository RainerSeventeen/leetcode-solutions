---
id: 17
title: 电话号码的字母组合
difficulty: Medium
tags: [hash-table, string, backtracking]
created: 2026-02-20
---

# 17. 电话号码的字母组合

## 题目链接
https://leetcode.cn/problems/letter-combinations-of-a-phone-number/

## 题目描述
暂无（需要从LeetCode获取）

## 解题思路
回溯枚举所有位置的选择。用数字到字母的映射表 `mp`，从左到右构造长度为 `n` 的路径 `path`：

- 递归到第 `idx` 位时，遍历该数字对应的所有字母，把字母加入 `path`，递归到 `idx+1`；
- 当 `idx == n`，说明每一位都选定，加入结果；
- 回溯时弹出最后一个字符，尝试下一个分支。

边界：`digits` 为空时没有组合，直接返回空列表。

最坏情况下每一位都有 4 个分支，总组合数为 `4^n`，生成每个字符串需要 `O(n)` 的拼接/拷贝。

- 时间复杂度: $O(4^n \cdot n)$
- 空间复杂度: $O(n)$

## 代码
```python
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mp = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno',
              'pqrs', 'tuv', 'wxyz']
        n = len(digits)
        ret = []
        if not digits:
            return []
        def backtrace(path, idx):
            if idx == n:
                ret.append("".join(path))
                return
            for c in mp[int(digits[idx])]:
                path.append(c)
                backtrace(path, idx + 1) # 下一个字母
                path.pop()
        backtrace([], 0)
        return ret
```
