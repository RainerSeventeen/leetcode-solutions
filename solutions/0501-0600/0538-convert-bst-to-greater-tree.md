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
暂无（需要从LeetCode获取）

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
