---
id: 46
title: 全排列
difficulty: Medium
tags: [array, backtracking]
created: 2026-02-20
---

# 46. 全排列

## 题目链接
https://leetcode.cn/problems/permutations/

## 题目描述

<p>给定一个不含重复数字的数组 <code>nums</code> ，返回其 <em>所有可能的全排列</em> 。你可以 <strong>按任意顺序</strong> 返回答案。</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,2,3]
<strong>输出：</strong>[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [0,1]
<strong>输出：</strong>[[0,1],[1,0]]
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>nums = [1]
<strong>输出：</strong>[[1]]
</pre>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 6</code></li>
	<li><code>-10 &lt;= nums[i] &lt;= 10</code></li>
	<li><code>nums</code> 中的所有整数 <strong>互不相同</strong></li>
</ul>

## 解题思路
回溯生成全排列。用 `used[i]` 标记 `nums[i]` 是否已放入当前排列 `curr`：

- 每一层递归选择一个尚未使用的元素加入 `curr`，并把 `used[i]=True`；
- 当 `len(curr) == n`，得到一个完整排列，拷贝加入结果；
- 回溯时撤销选择：弹出 `curr` 末尾并恢复 `used[i]=False`。

`used` 保证每个元素在一条路径中只出现一次，递归树恰好覆盖全部 `n!` 种排列。

- 时间复杂度: $O(n \cdot n!)$
- 空间复杂度: $O(n)$

## 相关专题
- [链表、树与回溯](../../topics/linked-list-tree-backtracking.md)

## 代码
```python
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        used = [False] * n
        ret = []
        curr = []

        def backtrace():
            if len(curr) == n:
                ret.append(curr.copy())
                return

            for i in range(n):
                if used[i]:
                    continue
                used[i] = True
                curr.append(nums[i])
                backtrace()
                curr.pop()
                used[i] = False

        backtrace()
        print(ret)
        return ret
```
