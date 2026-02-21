---
id: 94
title: Binary Tree Inorder Traversal
difficulty: Easy
tags: [stack, tree, depth-first-search, binary-tree]
created: 2026-02-21
---

# 94. 二叉树的中序遍历

## 题目链接
https://leetcode.cn/problems/binary-tree-inorder-traversal/

## 题目描述
<p>给定一个二叉树的根节点 <code>root</code> ，返回 <em>它的 <strong>中序</strong>&nbsp;遍历</em> 。</p>

<p><strong>示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/09/15/inorder_1.jpg" style="height: 200px; width: 125px;" />
<pre>
<strong>输入：</strong>root = [1,null,2,3]
<strong>输出：</strong>[1,3,2]
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>root = []
<strong>输出：</strong>[]
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>root = [1]
<strong>输出：</strong>[1]
</pre>

<p><strong>提示：</strong></p>

<ul>
	<li>树中节点数目在范围 <code>[0, 100]</code> 内</li>
	<li><code>-100 &lt;= Node.val &lt;= 100</code></li>
</ul>

<p><strong>进阶:</strong>&nbsp;递归算法很简单，你可以通过迭代算法完成吗？</p>


## 解题思路

使用显式栈模拟递归中序遍历（左-根-右）。
先一路压入左子节点，栈顶弹出后访问该节点，再转向其右子树。
重复直到当前节点为空且栈也为空。
- 时间复杂度: $O(n)$
- 空间复杂度: $O(h)$

## 代码
```python
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stk = []
        ret = []
        curr = root

        while curr or stk:
            # 一直向左走
            while curr:
                stk.append(curr)
                curr = curr.left

            # 访问中间节点
            curr = stk.pop()
            ret.append(curr.val)

            # 转向右子树
            curr = curr.right

        return ret
```
