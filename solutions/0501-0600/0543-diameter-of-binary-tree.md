---
id: 543
title: 二叉树的直径
difficulty: Medium
tags: [tree, depth-first-search, binary-tree]
created: 2026-02-20
---

# 543. 二叉树的直径

## 题目链接
https://leetcode.cn/problems/diameter-of-binary-tree/

## 题目描述

<p>给你一棵二叉树的根节点，返回该树的 <strong>直径</strong> 。</p>

<p>二叉树的 <strong>直径</strong> 是指树中任意两个节点之间最长路径的 <strong>长度</strong> 。这条路径可能经过也可能不经过根节点 <code>root</code> 。</p>

<p>两节点之间路径的 <strong>长度</strong> 由它们之间边数表示。</p>

<p><strong class="example">示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/03/06/diamtree.jpg" style="width: 292px; height: 302px;" />
<pre>
<strong>输入：</strong>root = [1,2,3,4,5]
<strong>输出：</strong>3
<strong>解释：</strong>3 ，取路径 [4,2,1,3] 或 [5,2,1,3] 的长度。
</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<strong>输入：</strong>root = [1,2]
<strong>输出：</strong>1
</pre>

<p><strong>提示：</strong></p>

<ul>
	<li>树中节点数目在范围 <code>[1, 10<sup>4</sup>]</code> 内</li>
	<li><code>-100 &lt;= Node.val &lt;= 100</code></li>
</ul>

## 解题思路
二叉树直径可以理解为：任意两点间最长路径的**边数**。路径不一定经过根。

用一次 DFS 同时计算“深度”和更新“直径”：

- `dfs(node)` 返回以 `node` 为根的子树的最大深度（从 `node` 向下走到叶子节点的节点数）。
- 对于某个节点，若左子树深度为 `l`、右子树深度为 `r`，那么经过该节点的最长路径边数就是 `l + r`（左边向下 `l` 条边、右边向下 `r` 条边，对应代码里用深度计数的相加）。
- 用全局变量 `ret` 在遍历过程中取最大值即可。

边界：空节点深度为 0；单节点树直径为 0。

- 时间复杂度: $O(n)$
- 空间复杂度: $O(h)$

## 代码
```python
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ret = 0
        
        def dfs(root):
            if root is None:
                return 0
            
            l = dfs(root.left)
            r = dfs(root.right)
            nonlocal ret
            ret = max(l + r, ret)
            return max(l, r) + 1
        dfs(root)
        return ret
```
