---
id: 78
title: Subsets
difficulty: Medium
tags: [bit-manipulation, array, backtracking]
created: 2026-02-20
---

# 78. 子集

## 题目链接
https://leetcode.cn/problems/subsets/

## 题目描述
<p>给你一个整数数组&nbsp;<code>nums</code> ，数组中的元素 <strong>互不相同</strong> 。返回该数组所有可能的<span data-keyword="subset">子集</span>（幂集）。</p>

<p>解集 <strong>不能</strong> 包含重复的子集。你可以按 <strong>任意顺序</strong> 返回解集。</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,2,3]
<strong>输出：</strong>[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [0]
<strong>输出：</strong>[[],[0]]
</pre>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10</code></li>
	<li><code>-10 &lt;= nums[i] &lt;= 10</code></li>
	<li><code>nums</code> 中的所有元素 <strong>互不相同</strong></li>
</ul>



## 解题思路

回溯/枚举所有选择。

对每个元素只有两种决策：选 / 不选，因此共有 $2^n$ 个子集。用 DFS 构造当前路径 `path`：

- 递归函数 `dfs(i)` 表示“处理到下标 `i`（含之前都已决定）”
- 当 `i == n` 时，把当前 `path` 加入答案
- 否则：
  1. 不选 `nums[i]`，递归 `dfs(i+1)`
  2. 选 `nums[i]`：`path.append(nums[i])`，递归 `dfs(i+1)`，回溯 `path.pop()`

不变量：

- `path` 始终等于当前分支已经选择的元素集合；进入/退出递归时必须成对 append/pop，保证状态可复用。

边界：

- 输入为空时仍然有一个子集：空集 `[]`。

- 时间复杂度: $O(n\cdot 2^n)$
- 空间复杂度: $O(n)$

说明：上述空间复杂度不计输出；输出本身需要 $O(n\cdot 2^n)$。

## 代码
```python
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ret = [[]]
        n = len(nums)
        def dfs(idx, path):
            if idx >= n:
                return
            for i in range(idx, n):
                path.append(nums[i])
                ret.append(path.copy())
                dfs(i + 1, path)
                path.pop()
        dfs(0, [])
        return ret
```
