---
id: 617
title: Merge Two Binary Trees
difficulty: Easy
tags: [tree, depth-first-search, breadth-first-search, binary-tree]
created: 2026-02-20
---

# 617. 合并二叉树

## 题目链接
https://leetcode.cn/problems/merge-two-binary-trees/

## 题目描述
<p>给你两棵二叉树： <code>root1</code> 和 <code>root2</code> 。</p>

<p>想象一下，当你将其中一棵覆盖到另一棵之上时，两棵树上的一些节点将会重叠（而另一些不会）。你需要将这两棵树合并成一棵新二叉树。合并的规则是：如果两个节点重叠，那么将这两个节点的值相加作为合并后节点的新值；否则，<strong>不为</strong> null 的节点将直接作为新二叉树的节点。</p>

<p>返回合并后的二叉树。</p>

<p><strong>注意:</strong> 合并过程必须从两个树的根节点开始。</p>

<p><strong>示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/02/05/merge.jpg" style="height: 163px; width: 600px;" />
<pre>
<strong>输入：</strong>root1 = [1,3,2,5], root2 = [2,1,3,null,4,null,7]
<strong>输出：</strong>[3,4,5,5,4,null,7]
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>root1 = [1], root2 = [1,2]
<strong>输出：</strong>[2,2]
</pre>

<p><strong>提示：</strong></p>

<ul>
	<li>两棵树中的节点数目在范围 <code>[0, 2000]</code> 内</li>
	<li><code>-10<sup>4</sup> &lt;= Node.val &lt;= 10<sup>4</sup></code></li>
</ul>



## 解题思路

从两棵树的根同时出发做 DFS（前序/后序都可以），在每个位置合并对应节点：

- 若 `root1` 为空，合并结果就是 `root2`（反之亦然）。
- 若两者都非空，创建新节点 `val = root1.val + root2.val`，再递归合并左右子树。

代码里创建的是**新树节点**（不修改原树）。如果题目允许，也可以选择在 `root1` 上原地累加并复用节点，思路一致。

边界：两棵树都为空时返回 `None`。

- 时间复杂度: $O(n_1 + n_2)$
- 空间复杂度: $O(h_1 + h_2)$

## 代码
```python
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        # 先序遍历
        def pretraversal(r1, r2):
            if not r1:
                return r2
            if not r2:
                return r1
            curr = TreeNode(r1.val + r2.val)
            curr.left = pretraversal(r1.left, r2.left)
            curr.right = pretraversal(r1.right, r2.right)
            return curr

        return pretraversal(root1, root2)
```
