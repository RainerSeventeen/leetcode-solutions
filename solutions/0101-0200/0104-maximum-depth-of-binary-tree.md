---
id: 104
title: Maximum Depth of Binary Tree
difficulty: Easy
tags: [tree, depth-first-search, breadth-first-search, binary-tree]
created: 2026-02-21
---

# 104. 二叉树的最大深度

## 题目链接
https://leetcode.cn/problems/maximum-depth-of-binary-tree/

## 题目描述
<p>给定一个二叉树 <code>root</code> ，返回其最大深度。</p>

<p>二叉树的 <strong>最大深度</strong> 是指从根节点到最远叶子节点的最长路径上的节点数。</p>

<p><strong>示例 1：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2020/11/26/tmp-tree.jpg" style="width: 400px; height: 277px;" /></p>

<pre>
<b>输入：</b>root = [3,9,20,null,null,15,7]
<b>输出：</b>3
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<b>输入：</b>root = [1,null,2]
<b>输出：</b>2
</pre>

<p><strong>提示：</strong></p>

<ul>
	<li>树中节点的数量在&nbsp;<code>[0, 10<sup>4</sup>]</code>&nbsp;区间内。</li>
	<li><code>-100 &lt;= Node.val &lt;= 100</code></li>
</ul>


## 解题思路

- 使用递归 DFS，节点为空返回 0，非空时分别计算左右子树最大深度。
- 当前节点深度等于 `max(左子树深度, 右子树深度) + 1`，最终返回根节点结果。

- 时间复杂度: $O(n)$

- 空间复杂度: $O(h)$

## 代码
```python
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(curr):
            if curr is None:
                return 0
            l = dfs(curr.left)
            r = dfs(curr.right)
            return max(l , r) + 1
        return dfs(root)
```
