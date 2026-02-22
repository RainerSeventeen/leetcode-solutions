---
id: 102
title: Binary Tree Level Order Traversal
difficulty: Medium
tags: [tree, breadth-first-search, binary-tree]
created: 2026-02-21
---

# 102. 二叉树的层序遍历

## 题目链接
https://leetcode.cn/problems/binary-tree-level-order-traversal/

## 题目描述
<p>给你二叉树的根节点 <code>root</code> ，返回其节点值的 <strong>层序遍历</strong> 。 （即逐层地，从左到右访问所有节点）。</p>

<p><strong>示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/02/19/tree1.jpg" style="width: 277px; height: 302px;" />
<pre>
<strong>输入：</strong>root = [3,9,20,null,null,15,7]
<strong>输出：</strong>[[3],[9,20],[15,7]]
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>root = [1]
<strong>输出：</strong>[[1]]
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>root = []
<strong>输出：</strong>[]
</pre>

<p><strong>提示：</strong></p>

<ul>
	<li>树中节点数目在范围 <code>[0, 2000]</code> 内</li>
	<li><code>-1000 &lt;= Node.val &lt;= 1000</code></li>
</ul>


## 解题思路

用队列做标准 BFS，外层循环按层处理，内层循环处理当前层固定数量节点。
弹出当前节点后把其左右孩子入队，并把节点值收集到本层数组。
每层结束把本层结果加入答案，直到队列为空。
- 时间复杂度: $O(n)$
- 空间复杂度: $O(n)$

## 相关专题
- [图论算法](../../topics/graph-algorithms.md)

## 代码
```python
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # 规定左进右出， 二重循环保证层级关系
        q = deque()
        if root is None:
            return []
        q.appendleft(root)
        ret = []
        while q:
            size = len(q) # 当前层的节点数量
            level = []
            for _ in range(size):
                curr = q.pop()
                level.append(curr.val)
                if curr.left:
                    q.appendleft(curr.left)
                if curr.right:
                    q.appendleft(curr.right)
            ret.append(level)
        return ret
```
