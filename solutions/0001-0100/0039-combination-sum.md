---
id: 39
title: 组合总和
difficulty: Medium
tags: [array, backtracking]
created: 2026-02-20
---

# 39. 组合总和

## 题目链接
https://leetcode.cn/problems/combination-sum/

## 题目描述

<p>给你一个 <strong>无重复元素</strong> 的整数数组&nbsp;<code>candidates</code> 和一个目标整数&nbsp;<code>target</code>&nbsp;，找出&nbsp;<code>candidates</code>&nbsp;中可以使数字和为目标数&nbsp;<code>target</code> 的 所有<em>&nbsp;</em><strong>不同组合</strong> ，并以列表形式返回。你可以按 <strong>任意顺序</strong> 返回这些组合。</p>

<p><code>candidates</code> 中的 <strong>同一个</strong> 数字可以 <strong>无限制重复被选取</strong> 。如果至少一个数字的被选数量不同，则两种组合是不同的。&nbsp;</p>

<p>对于给定的输入，保证和为&nbsp;<code>target</code> 的不同组合数少于 <code>150</code> 个。</p>

<p><strong>示例&nbsp;1：</strong></p>

<pre>
<strong>输入：</strong>candidates = [2,3,6,7], target = 7
<strong>输出：</strong>[[2,2,3],[7]]
<strong>解释：</strong>
2 和 3 可以形成一组候选，2 + 2 + 3 = 7 。注意 2 可以使用多次。
7 也是一个候选， 7 = 7 。
仅有这两种组合。</pre>

<p><strong>示例&nbsp;2：</strong></p>

<pre>
<strong>输入: </strong>candidates = [2,3,5], target = 8
<strong>输出: </strong>[[2,2,2,2],[2,3,3],[3,5]]</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入: </strong>candidates = [2], target = 1
<strong>输出: </strong>[]
</pre>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= candidates.length &lt;= 30</code></li>
	<li><code>2 &lt;= candidates[i] &lt;= 40</code></li>
	<li><code>candidates</code> 的所有元素 <strong>互不相同</strong></li>
	<li><code>1 &lt;= target &lt;= 40</code></li>
</ul>

## 解题思路
回溯枚举“选哪些数”来凑出 `target`。由于同一个数可以重复使用，递归时可以继续从当前下标 `idx` 选择。

实现要点：

- 先对 `candidates` 排序，便于剪枝；
- `backtrace(idx, path, left)` 表示：从 `candidates[idx:]` 中选数，当前已选为 `path`，还剩 `left` 需要凑；
- 枚举 `i in [idx, n)`：把 `candidates[i]` 放入 `path`，递归到 `backtrace(i, ..., left - candidates[i])`（注意仍传 `i`，允许重复选）；
- 若 `left == 0` 记录一组解；若 `candidates[i] > left`，后续更大，直接 `break` 剪枝。

递归深度最多为 $T = \lfloor target / \min(candidates) \rfloor$，每层最多有 `n` 个分支（粗略上界）。

- 时间复杂度: $O(n^{T})$
- 空间复杂度: $O(T)$

## 相关专题
- [链表、树与回溯](../../topics/linked-list-tree-backtracking.md)

## 代码
```python
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ret = []
        n = len(candidates)
        def backtrace(idx, path, left):
            if left == 0:
               ret.append(path.copy())
               return

            for i in range(idx, n):
                if candidates[i] > left:
                path.append(candidates[i])
                    break
                backtrace(i, path, left - candidates[i])
                path.pop()
        backtrace(0, [], target)
        return ret
```
