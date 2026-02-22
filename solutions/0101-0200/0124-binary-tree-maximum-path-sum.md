---
id: 124
title: Binary Tree Maximum Path Sum
difficulty: Medium
tags: [tree, depth-first-search, dynamic-programming, binary-tree]
created: 2026-02-20
---

# 124. 二叉树中的最大路径和

## 题目链接
https://leetcode.cn/problems/binary-tree-maximum-path-sum/

## 题目描述

<p>二叉树中的<strong> 路径</strong> 被定义为一条节点序列，序列中每对相邻节点之间都存在一条边。同一个节点在一条路径序列中 <strong>至多出现一次</strong> 。该路径<strong> 至少包含一个 </strong>节点，且不一定经过根节点。</p>

<p><strong>路径和</strong> 是路径中各节点值的总和。</p>

<p>给你一个二叉树的根节点 <code>root</code> ，返回其 <strong>最大路径和</strong> 。</p>

<p><strong>示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/10/13/exx1.jpg" style="width: 322px; height: 182px;" />
<pre>
<strong>输入：</strong>root = [1,2,3]
<strong>输出：</strong>6
<strong>解释：</strong>最优路径是 2 -&gt; 1 -&gt; 3 ，路径和为 2 + 1 + 3 = 6</pre>

<p><strong>示例 2：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/10/13/exx2.jpg" />
<pre>
<strong>输入：</strong>root = [-10,9,20,null,null,15,7]
<strong>输出：</strong>42
<strong>解释：</strong>最优路径是 15 -&gt; 20 -&gt; 7 ，路径和为 15 + 20 + 7 = 42
</pre>

<p><strong>提示：</strong></p>

<ul>
	<li>树中节点数目范围是 <code>[1, 3 * 10<sup>4</sup>]</code></li>
	<li><code>-1000 &lt;= Node.val &lt;= 1000</code></li>
</ul>

## 解题思路

后序遍历（DFS）+ 全局最大值。

对每个节点，递归计算左右子树向上能贡献的最大路径值（负数贡献直接截断为 0）。以当前节点为"拐点"（路径最高点）时，路径可以同时接入左右两侧，此时更新全局最大值；但向上传递时路径不能分叉，只能取 `max(左, 右) + 自身`。

- 时间复杂度: $O(n)$
- 空间复杂度: $O(h)$

其中 `n` 为节点数，`h` 为树高（递归栈深度）。

## 代码
```python
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ret_max = float("-inf")
        def backTraversal(root):
            if root is None:
                return 0

            # 后序遍历, 屏蔽负数
            left = max(backTraversal(root.left), 0)
            right = max(backTraversal(root.right), 0)
            # 向上传递的值包含 root
            ret = max(root.val + left, root.val + right)   # 不能够左右都包含，向上路径不能分叉
            nonlocal ret_max
            ret_max = max(ret_max, root.val + left + right)   # 允许分叉的点就是全局最大值
            return ret
            
        backTraversal(root)
        return ret_max
```
