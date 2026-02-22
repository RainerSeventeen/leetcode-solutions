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

<p>给定一个仅包含数字&nbsp;<code>2-9</code>&nbsp;的字符串，返回所有它能表示的字母组合。答案可以按 <strong>任意顺序</strong> 返回。</p>

<p>给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。</p>

<p><img src="https://pic.leetcode.cn/1752723054-mfIHZs-image.png" style="width: 200px;" /></p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>digits = "23"
<strong>输出：</strong>["ad","ae","af","bd","be","bf","cd","ce","cf"]
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>digits = "2"
<strong>输出：</strong>["a","b","c"]
</pre>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= digits.length &lt;= 4</code></li>
	<li><code>digits[i]</code> 是范围 <code>['2', '9']</code> 的一个数字。</li>
</ul>

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
