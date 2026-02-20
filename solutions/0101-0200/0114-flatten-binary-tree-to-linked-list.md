---
id: 114
title: Flatten Binary Tree to Linked List
difficulty: Medium
tags: [stack, tree, depth-first-search, linked-list, binary-tree]
created: 2026-02-20
---

# 114. Flatten Binary Tree to Linked List

## 题目链接
https://leetcode.cn/problems/flatten-binary-tree-to-linked-list/

## 题目描述
<p>给你二叉树的根结点 <code>root</code> ，请你将它展开为一个单链表：</p>

<ul>
	<li>展开后的单链表应该同样使用 <code>TreeNode</code> ，其中 <code>right</code> 子指针指向链表中下一个结点，而左子指针始终为 <code>null</code> 。</li>
	<li>展开后的单链表应该与二叉树 <a href="https://baike.baidu.com/item/%E5%85%88%E5%BA%8F%E9%81%8D%E5%8E%86/6442839?fr=aladdin" target="_blank"><strong>先序遍历</strong></a> 顺序相同。</li>
</ul>

<p><strong>示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/01/14/flaten.jpg" style="width: 500px; height: 226px;" />
<pre>
<strong>输入：</strong>root = [1,2,5,3,4,null,6]
<strong>输出：</strong>[1,null,2,null,3,null,4,null,5,null,6]
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>root = []
<strong>输出：</strong>[]
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>root = [0]
<strong>输出：</strong>[0]
</pre>

<p><strong>提示：</strong></p>

<ul>
	<li>树中结点数在范围 <code>[0, 2000]</code> 内</li>
	<li><code>-100 <= Node.val <= 100</code></li>
</ul>

<p><strong>进阶：</strong>你可以使用原地算法（<code>O(1)</code> 额外空间）展开这棵树吗？</p>



## 解题思路

目标是把树原地改成先序遍历顺序的“右链表”（每个节点 `left = None`，`right` 指向下一个节点）。

`O(1)` 额外空间的做法（类似 Morris 思想）：

从根开始沿着 `cur` 向右走：

- 若 `cur.left` 为空：说明该节点已经满足“左空”，直接 `cur = cur.right`
- 否则（存在左子树）：
  1. 找到 `cur.left` 这棵子树的最右节点 `pred`（即先序遍历中左子树的最后一个节点）
  2. 把原来的右子树接到 `pred.right`：`pred.right = cur.right`
  3. 把左子树整体搬到右边：`cur.right = cur.left`，并置空 `cur.left = None`
  4. 继续 `cur = cur.right`

不变量：

- 每次处理完 `cur` 后，`cur` 这个节点满足题目要求（`left` 为空），并且 `cur.right` 指向先序遍历的下一个节点；已处理前缀已经是一条正确的右链。

边界：

- 空树或单节点树不需要处理。

- 时间复杂度: $O(n)$
- 空间复杂度: $O(1)$

## 代码
```python
class Solution:
    def flatten(self, root):
        cur = root
        while cur:
            if cur.left:
                # 1. 找左子树最右节点（展开后左链表的尾）
                pre = cur.left
                while pre.right:
                    pre = pre.right

                # 2. 原右子树接到左子树尾部
                pre.right = cur.right

                # 3. 左子树整体搬到右边
                cur.right = cur.left
                cur.left = None

            # 4. 沿着先序链继续
            cur = cur.right
```
