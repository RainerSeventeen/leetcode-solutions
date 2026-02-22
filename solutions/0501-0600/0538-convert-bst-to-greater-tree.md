---
id: 538
title: 把二叉搜索树转换为累加树
difficulty: Medium
tags: [tree, depth-first-search, binary-search-tree, binary-tree]
created: 2026-02-20
---

# 538. 把二叉搜索树转换为累加树

## 题目链接
https://leetcode.cn/problems/convert-bst-to-greater-tree/

## 题目描述

<p>给出二叉<strong> 搜索 </strong>树的根节点，该树的节点值各不相同，请你将其转换为累加树（Greater Sum Tree），使每个节点 <code>node</code>&nbsp;的新值等于原树中大于或等于&nbsp;<code>node.val</code>&nbsp;的值之和。</p>

<p>提醒一下，二叉搜索树满足下列约束条件：</p>

<ul>
	<li>节点的左子树仅包含键<strong> 小于 </strong>节点键的节点。</li>
	<li>节点的右子树仅包含键<strong> 大于</strong> 节点键的节点。</li>
	<li>左右子树也必须是二叉搜索树。</li>
</ul>

<p><strong>注意：</strong>本题和 1038:&nbsp;<a href="https://leetcode.cn/problems/binary-search-tree-to-greater-sum-tree/">https://leetcode.cn/problems/binary-search-tree-to-greater-sum-tree/</a> 相同</p>

<p><strong>示例 1：</strong></p>

<p><strong><img alt="" src="https://assets.leetcode.cn/aliyun-lc-upload/uploads/2019/05/03/tree.png" style="height: 364px; width: 534px;"></strong></p>

<pre><strong>输入：</strong>[4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]
<strong>输出：</strong>[30,36,21,36,35,26,15,null,null,null,33,null,null,null,8]
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>root = [0,null,1]
<strong>输出：</strong>[1,null,1]
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>root = [1,0,2]
<strong>输出：</strong>[3,3,2]
</pre>

<p><strong>示例 4：</strong></p>

<pre><strong>输入：</strong>root = [3,2,4,1]
<strong>输出：</strong>[7,9,4,10]
</pre>

<p><strong>提示：</strong></p>

<ul>
	<li>树中的节点数介于 <code>0</code>&nbsp;和 <code>10<sup>4</sup></code><sup>&nbsp;</sup>之间。</li>
	<li>每个节点的值介于 <code>-10<sup>4</sup></code>&nbsp;和&nbsp;<code>10<sup>4</sup></code>&nbsp;之间。</li>
	<li>树中的所有值 <strong>互不相同</strong> 。</li>
	<li>给定的树为二叉搜索树。</li>
</ul>

## 解题思路
利用 BST 的性质：中序遍历（左-根-右）是递增序；反过来做 **右-根-左** 的遍历，就会按从大到小访问节点。

维护一个累加和 `total`，表示“已经访问过的（比当前节点大的）所有节点值之和”。在反中序遍历过程中：

1. 先递归右子树（先处理更大的值）。
2. `total += node.val`，然后把 `node.val` 更新为 `total`。
3. 再递归左子树。

这样每个节点都会被替换成“原值 + 所有比它大的节点值之和”，满足题意。

边界：空树直接返回 `None`。

- 时间复杂度: $O(n)$
- 空间复杂度: $O(h)$

## 相关专题
- [链表、树与回溯](../../topics/linked-list-tree-backtracking.md)

## 代码
```python
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        total = 0
        def dfs(root):
            if root is None:
                return
            # 右中左
            nonlocal total
            dfs(root.right)
            total += root.val
            root.val = total
            dfs(root.left)
        dfs(root)
        return root
```
