---
id: 437
title: Path Sum III
difficulty: Medium
tags: [tree, depth-first-search, binary-tree]
created: 2026-02-20
---

# 437. 路径总和 III

## 题目链接
https://leetcode.cn/problems/path-sum-iii/

## 题目描述

<p>给定一个二叉树的根节点 <code>root</code> ，和一个整数 <code>targetSum</code> ，求该二叉树里节点值之和等于 <code>targetSum</code> 的 <strong>路径</strong> 的数目。</p>

<p><strong>路径</strong> 不需要从根节点开始，也不需要在叶子节点结束，但是路径方向必须是向下的（只能从父节点到子节点）。</p>

<p><strong>示例 1：</strong></p>

<p><img src="https://assets.leetcode.com/uploads/2021/04/09/pathsum3-1-tree.jpg" style="width: 452px; " /></p>

<pre>
<strong>输入：</strong>root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
<strong>输出：</strong>3
<strong>解释：</strong>和等于 8 的路径有 3 条，如图所示。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
<strong>输出：</strong>3
</pre>

<p><strong>提示:</strong></p>

<ul>
	<li>二叉树的节点个数的范围是 <code>[0,1000]</code></li>
	<li><meta charset="UTF-8" /><code>-10<sup>9</sup> <= Node.val <= 10<sup>9</sup></code> </li>
	<li><code>-1000 <= targetSum <= 1000</code> </li>
</ul>

## 解题思路

前缀和 + 哈希表 + DFS 回溯。

DFS 遍历时维护从根到当前节点的前缀和 `currSum`。若存在某个祖先节点的前缀和为 `currSum - targetSum`，说明从该祖先的下一个节点到当前节点的路径和恰好等于 `targetSum`。用哈希表记录路径上各前缀和出现的次数，离开节点时回溯还原计数，以避免跨分支统计。

- 时间复杂度: $O(n)$
- 空间复杂度: $O(n)$

## 相关专题
- [链表、树与回溯](../../topics/linked-list-tree-backtracking.md)

## 代码
```python
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        # 前缀和, target = prefix[curr] - prefix[x] 表示从 x 到 curr 这两个值之间区间
        from collections import defaultdict
        prefix = defaultdict(int)
        prefix[0] = 1 # 允许某个节点自己达成目标
        def dfs(root, currSum):
            if root is None:
                return 0
            
            ret = 0
            currSum += root.val # 前缀和求值
            ret += prefix[currSum - targetSum]

            prefix[currSum] += 1 # 加入前缀表
            ret += dfs(root.left, currSum)
            ret += dfs(root.right, currSum)
            prefix[currSum] -= 1 # 退出节点的时候要回溯，因为前缀已经消失了

            return ret
        return dfs(root, 0)
```
