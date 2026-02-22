---
id: 101
title: Symmetric Tree
difficulty: Easy
tags: [tree, depth-first-search, breadth-first-search, binary-tree]
created: 2026-02-20
---

# 101. 对称二叉树

## 题目链接
https://leetcode.cn/problems/symmetric-tree/

## 题目描述
<p>给你一个二叉树的根节点 <code>root</code> ， 检查它是否轴对称。</p>

<p><strong>示例 1：</strong></p>
<img alt="" src="https://pic.leetcode.cn/1698026966-JDYPDU-image.png" style="width: 354px; height: 291px;" />
<pre>
<strong>输入：</strong>root = [1,2,2,3,4,4,3]
<strong>输出：</strong>true
</pre>

<p><strong>示例 2：</strong></p>
<img alt="" src="https://pic.leetcode.cn/1698027008-nPFLbM-image.png" style="width: 308px; height: 258px;" />
<pre>
<strong>输入：</strong>root = [1,2,2,null,3,null,3]
<strong>输出：</strong>false
</pre>

<p><strong>提示：</strong></p>

<ul>
	<li>树中节点数目在范围 <code>[1, 1000]</code> 内</li>
	<li><code>-100 &lt;= Node.val &lt;= 100</code></li>
</ul>

<p><strong>进阶：</strong>你可以运用递归和迭代两种方法解决这个问题吗？</p>



## 解题思路

对称二叉树要求：以根为轴，左子树与右子树互为镜像。

把问题转为“同时比较两棵树是否镜像相等”：

定义函数 `isMirror(a, b)`：

- 若 `a` 和 `b` 都为空：镜像相等，返回 `True`
- 若只有一个为空：结构不对称，返回 `False`
- 若 `a.val != b.val`：值不相等，返回 `False`
- 否则继续比较：
  - `a.left` 与 `b.right`
  - `a.right` 与 `b.left`

不变量：

- 每次递归都在比较“应该互为镜像”的两个节点对；比较顺序必须是 `(left, right)` 交叉匹配，否则会把非镜像的结构误判为相同。

边界：

- 空树视为对称。

- 时间复杂度: $O(n)$
- 空间复杂度: $O(h)$

其中 $h$ 为树高（递归栈深度）。

## 代码
```python
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def dfs(l, r):
            if l is None:
                return r is None
            if r is None:
                return l is None
            
            if l.val != r.val:
                return False
            return dfs(l.left, r.right) and dfs(l.right, r.left)
        if root is None:
            return True
        return dfs(root.left, root.right)
```
