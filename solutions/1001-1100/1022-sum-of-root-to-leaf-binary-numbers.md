---
id: 1022
title: Sum of Root To Leaf Binary Numbers
difficulty: Easy
tags: [tree, depth-first-search, binary-tree]
created: 2026-02-24
---

# 1022. 从根到叶的二进制数之和

## 题目链接
https://leetcode.cn/problems/sum-of-root-to-leaf-binary-numbers/

## 题目描述
<p>给出一棵二叉树，其上每个结点的值都是&nbsp;<code>0</code>&nbsp;或&nbsp;<code>1</code>&nbsp;。每一条从根到叶的路径都代表一个从最高有效位开始的二进制数。</p>

<ul>
	<li>例如，如果路径为&nbsp;<code>0 -&gt; 1 -&gt; 1 -&gt; 0 -&gt; 1</code>，那么它表示二进制数&nbsp;<code>01101</code>，也就是&nbsp;<code>13</code>&nbsp;。</li>
</ul>

<p>对树上的每一片叶子，我们都要找出从根到该叶子的路径所表示的数字。</p>

<p>返回这些数字之和。题目数据保证答案是一个 <strong>32 位 </strong>整数。</p>

<p><strong>示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2019/04/04/sum-of-root-to-leaf-binary-numbers.png" />
<pre>
<strong>输入：</strong>root = [1,0,1,0,1,0,1]
<strong>输出：</strong>22
<strong>解释：</strong>(100) + (101) + (110) + (111) = 4 + 5 + 6 + 7 = 22
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>root = [0]
<strong>输出：</strong>0
</pre>

<p><strong>提示：</strong></p>

<ul>
	<li>树中的节点数在&nbsp;<code>[1, 1000]</code>&nbsp;范围内</li>
	<li><code>Node.val</code>&nbsp;仅为 <code>0</code> 或 <code>1</code>&nbsp;</li>
</ul>


## 解题思路

DFS 遍历整棵树，并把“根到当前节点的二进制值”作为状态向下传。
到达节点时先执行 `curr = (curr << 1) | root.val`，等价于在二进制末尾追加当前位；
如果是叶子就把该路径值累加到答案，否则继续递归左右子树。
- 时间复杂度: $O(n)$
- 空间复杂度: $O(h)$，$h$ 为树高（递归栈）

## 相关专题
- [链表、树与回溯](../../topics/linked-list-tree-backtracking.md)

## 代码
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        # DFS 直接遍历, 使用位运算移位
        ret = 0
        def dfs(root, curr):
            nonlocal ret
            curr = (curr << 1) | root.val
            # print(format(curr, 'b'))
            if not root.left and not root.right:
                # 叶子结点
                ret += curr
                return
            if root.left:
                dfs(root.left, curr)
            if root.right:
                dfs(root.right, curr)
        dfs(root, 0)
        return ret
```
