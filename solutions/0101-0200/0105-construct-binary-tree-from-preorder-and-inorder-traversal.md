---
id: 105
title: Construct Binary Tree from Preorder and Inorder Traversal
difficulty: Medium
tags: [tree, array, hash-table, divide-and-conquer, binary-tree]
created: 2026-02-20
---

# 105. 从前序与中序遍历序列构造二叉树

## 题目链接
https://leetcode.cn/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

## 题目描述
<p>给定两个整数数组&nbsp;<code>preorder</code> 和 <code>inorder</code>&nbsp;，其中&nbsp;<code>preorder</code> 是二叉树的<strong>先序遍历</strong>， <code>inorder</code>&nbsp;是同一棵树的<strong>中序遍历</strong>，请构造二叉树并返回其根节点。</p>

<p><strong>示例 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/02/19/tree.jpg" style="height: 302px; width: 277px;" />
<pre>
<strong>输入</strong><strong>:</strong> preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
<strong>输出:</strong> [3,9,20,null,null,15,7]
</pre>

<p><strong>示例 2:</strong></p>

<pre>
<strong>输入:</strong> preorder = [-1], inorder = [-1]
<strong>输出:</strong> [-1]
</pre>

<p><strong>提示:</strong></p>

<ul>
	<li><code>1 &lt;= preorder.length &lt;= 3000</code></li>
	<li><code>inorder.length == preorder.length</code></li>
	<li><code>-3000 &lt;= preorder[i], inorder[i] &lt;= 3000</code></li>
	<li><code>preorder</code>&nbsp;和&nbsp;<code>inorder</code>&nbsp;均 <strong>无重复</strong> 元素</li>
	<li><code>inorder</code>&nbsp;均出现在&nbsp;<code>preorder</code></li>
	<li><code>preorder</code>&nbsp;<strong>保证</strong> 为二叉树的前序遍历序列</li>
	<li><code>inorder</code>&nbsp;<strong>保证</strong> 为二叉树的中序遍历序列</li>
</ul>



## 解题思路

利用前序与中序的性质递归建树。

关键性质：

- 前序遍历：`[根 | 左子树... | 右子树...]`，因此**前序的第一个元素一定是当前子树的根**。
- 中序遍历：`[左子树... | 根 | 右子树...]`，根在中序中的位置把左右子树分割开。

做法：

1. 用哈希表 `pos[val]` 记录每个值在中序数组中的下标，便于 $O(1)$ 定位根。
2. 递归函数 `build(pre_l, pre_r, in_l, in_r)` 表示构建这两段区间对应的子树：
   - 根值 `root_val = preorder[pre_l]`
   - 根在中序的位置 `k = pos[root_val]`
   - 左子树大小 `left_size = k - in_l`
   - 左子树区间：
     - 前序：`[pre_l+1, pre_l+left_size]`
     - 中序：`[in_l, k-1]`
   - 右子树区间：
     - 前序：`[pre_l+left_size+1, pre_r]`
     - 中序：`[k+1, in_r]`
3. 递归构造左右子树并挂到根上。

不变量与边界：

- 每次递归中，`preorder[pre_l]` 一定是当前区间的根；左右子树区间长度必须一致（用 `left_size` 保证）。
- 当区间为空（例如 `pre_l > pre_r` 或 `in_l > in_r`）返回空节点。

- 时间复杂度: $O(n)$
- 空间复杂度: $O(n)$

说明：哈希表用于中序下标定位为 $O(n)$；递归栈最坏为 $O(h)$。

## 相关专题
- [链表、树与回溯](../../topics/linked-list-tree-backtracking.md)

## 代码
```python
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        n = len(preorder)
        pos = {v: i for i, v in enumerate(inorder)}  # O(n)
        def build(pre_a, pre_b, in_a, in_b):
            if pre_a == pre_b:
                return None
            # 中分节点
            root_val = preorder[pre_a] # 前序遍历的第一个
            mid_idx = pos[root_val]
            left_len = mid_idx - in_a
            root = TreeNode(root_val)
            root.left = build(pre_a + 1, pre_a + 1 + left_len, in_a, mid_idx)
            root.right = build(pre_a + 1 + left_len, pre_b, mid_idx + 1, in_b)
            return root
        ret = build(0, n, 0, n)
        return ret
```
