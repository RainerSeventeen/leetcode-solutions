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

树形 DP。对每个节点返回两个状态：

- `not_rob`：不偷当前节点时，子树最大收益。
- `rob`：偷当前节点时，子树最大收益。

设左子树返回 `(ln, lr)`，右子树返回 `(rn, rr)`，则：

- `rob = node.val + ln + rn`（偷当前节点则孩子都不能偷）
- `not_rob = max(ln, lr) + max(rn, rr)`（不偷当前节点则孩子可偷可不偷）

后序遍历一次即可。

- 时间复杂度: `O(n)`
- 空间复杂度: `O(h)`（递归栈，`h` 为树高）

## 代码
```python
class Solution:
    def rob(self, root: Optional["TreeNode"]) -> int:
        not_rob, rob = self._dfs(root)
        return max(not_rob, rob)

    def _dfs(self, node: Optional["TreeNode"]) -> Tuple[int, int]:
        if node is None:
            return 0, 0
        ln, lr = self._dfs(node.left)
        rn, rr = self._dfs(node.right)
        rob = node.val + ln + rn
        not_rob = max(ln, lr) + max(rn, rr)
        return not_rob, rob
```
