---
id: 96
title: Unique Binary Search Trees
difficulty: Medium
tags: [tree, binary-search-tree, math, dynamic-programming, binary-tree]
created: 2026-02-20
---

# 96. 不同的二叉搜索树

## 题目链接
https://leetcode.cn/problems/unique-binary-search-trees/

## 题目描述
<p>给你一个整数 <code>n</code> ，求恰由 <code>n</code> 个节点组成且节点值从 <code>1</code> 到 <code>n</code> 互不相同的 <strong>二叉搜索树</strong> 有多少种？返回满足题意的二叉搜索树的种数。</p>

<p><strong>示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/01/18/uniquebstn3.jpg" style="width: 600px; height: 148px;" />
<pre>
<strong>输入：</strong>n = 3
<strong>输出：</strong>5
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>n = 1
<strong>输出：</strong>1
</pre>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 <= n <= 19</code></li>
</ul>


## 解题思路

令 `dp[i]` 表示由 `i` 个节点组成的不同 BST 数量。枚举根节点 `j`（`1 <= j <= i`）时：

- 左子树有 `j - 1` 个节点，共 `dp[j - 1]` 种。
- 右子树有 `i - j` 个节点，共 `dp[i - j]` 种。

因此：

`dp[i] += dp[j - 1] * dp[i - j]`

边界 `dp[0] = 1`（空树算一种）。

- 时间复杂度: $O(n^2)$
- 空间复杂度: $O(n)$

## 相关专题
- [动态规划](../../topics/dynamic-programming.md)

## 代码
```python
class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0] = 1
        if n >= 1:
            dp[1] = 1
        for i in range(2, n + 1):
            for root in range(1, i + 1):
                dp[i] += dp[root - 1] * dp[i - root]
        return dp[n]
```
