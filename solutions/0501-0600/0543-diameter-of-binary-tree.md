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
暂无（需要从LeetCode获取）

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
