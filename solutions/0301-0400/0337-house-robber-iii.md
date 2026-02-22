---
id: 337
title: House Robber III
difficulty: Medium
tags: [tree, depth-first-search, dynamic-programming, binary-tree]
created: 2026-02-20
---

# 337. 打家劫舍 III

## 题目链接
https://leetcode.cn/problems/house-robber-iii/

## 题目描述
<p>小偷又发现了一个新的可行窃的地区。这个地区只有一个入口，我们称之为<meta charset="UTF-8" />&nbsp;<code>root</code>&nbsp;。</p>

<p>除了<meta charset="UTF-8" />&nbsp;<code>root</code>&nbsp;之外，每栋房子有且只有一个“父“房子与之相连。一番侦察之后，聪明的小偷意识到“这个地方的所有房屋的排列类似于一棵二叉树”。 如果 <strong>两个直接相连的房子在同一天晚上被打劫</strong> ，房屋将自动报警。</p>

<p>给定二叉树的&nbsp;<code>root</code>&nbsp;。返回&nbsp;<em><strong>在不触动警报的情况下</strong>&nbsp;，小偷能够盗取的最高金额</em>&nbsp;。</p>

<p><strong>示例 1:</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2021/03/10/rob1-tree.jpg" /></p>

<pre>
<strong>输入: </strong>root = [3,2,3,null,3,null,1]
<strong>输出:</strong> 7 
<strong>解释:</strong>&nbsp;小偷一晚能够盗取的最高金额 3 + 3 + 1 = 7</pre>

<p><strong>示例 2:</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2021/03/10/rob2-tree.jpg" /></p>

<pre>
<strong>输入: </strong>root = [3,4,5,1,3,null,1]
<strong>输出:</strong> 9
<strong>解释:</strong>&nbsp;小偷一晚能够盗取的最高金额 4 + 5 = 9
</pre>

<p><strong>提示：</strong></p>

<p><meta charset="UTF-8" /></p>

<ul>
	<li>树的节点数在&nbsp;<code>[1, 10<sup>4</sup>]</code> 范围内</li>
	<li><code>0 &lt;= Node.val &lt;= 10<sup>4</sup></code></li>
</ul>

## 解题思路
树形 DP：每个节点只有“偷/不偷”两种选择，但选择会影响子节点是否可偷，因此对每个节点返回两种状态的最优值。

定义 `dfs(node)` 返回一个二元组：

- `not_rob`：在以 `node` 为根的子树中，**不偷** `node` 能获得的最大金额。
- `rob`：在以 `node` 为根的子树中，**偷** `node` 能获得的最大金额。

后序遍历（先算左右子树）后可得到转移：

- 如果偷当前节点：孩子节点都不能偷  
  `rob = node.val + left.not_rob + right.not_rob`
- 如果不偷当前节点：孩子节点可偷可不偷，取最大  
  `not_rob = max(left.not_rob, left.rob) + max(right.not_rob, right.rob)`

整棵树答案是 `max(dfs(root))`。

边界：空节点返回 `(0, 0)`。

- 时间复杂度: $O(n)$
- 空间复杂度: $O(h)$

## 相关专题
- [动态规划](../../topics/dynamic-programming.md)

## 代码
```python
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return (0, 0)  # (不偷, 偷)

            l0, l1 = dfs(node.left)
            r0, r1 = dfs(node.right)

            not_rob = max(l0, l1) + max(r0, r1) # 孩子可以偷也可以不偷
            rob = l0 + r0 + node.val    # 一定不能偷

            return (not_rob, rob)

        return max(dfs(root))
```
