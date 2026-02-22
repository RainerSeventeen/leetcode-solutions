---
id: 106
title: Construct Binary Tree from Inorder and Postorder Traversal
difficulty: Medium
tags: [tree, array, hash-table, divide-and-conquer, binary-tree]
created: 2026-02-20
---

# 106. 从中序与后序遍历序列构造二叉树

## 题目链接
https://leetcode.cn/problems/construct-binary-tree-from-inorder-and-postorder-traversal/

## 题目描述
<p>给定两个整数数组 <code>inorder</code> 和 <code>postorder</code> ，其中 <code>inorder</code> 是二叉树的中序遍历， <code>postorder</code> 是同一棵树的后序遍历，请你构造并返回这颗&nbsp;<em>二叉树</em>&nbsp;。</p>

<p><strong>示例 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/02/19/tree.jpg" />
<pre>
<b>输入：</b>inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
<b>输出：</b>[3,9,20,null,null,15,7]
</pre>

<p><strong>示例 2:</strong></p>

<pre>
<b>输入：</b>inorder = [-1], postorder = [-1]
<b>输出：</b>[-1]
</pre>

<p><strong>提示:</strong></p>

<ul>
	<li><code>1 &lt;= inorder.length &lt;= 3000</code></li>
	<li><code>postorder.length == inorder.length</code></li>
	<li><code>-3000 &lt;= inorder[i], postorder[i] &lt;= 3000</code></li>
	<li><code>inorder</code>&nbsp;和&nbsp;<code>postorder</code>&nbsp;都由 <strong>不同</strong> 的值组成</li>
	<li><code>postorder</code>&nbsp;中每一个值都在&nbsp;<code>inorder</code>&nbsp;中</li>
	<li><code>inorder</code>&nbsp;<strong>保证</strong>是树的中序遍历</li>
	<li><code>postorder</code>&nbsp;<strong>保证</strong>是树的后序遍历</li>
</ul>


## 解题思路

后序遍历的最后一个元素就是当前子树根节点。在中序数组中定位根节点后，可以切分出左右子树对应区间，再递归构造左右子树并挂接到根节点。这里使用切片写法，逻辑更直观，但会产生数组复制开销。

- 时间复杂度: $O(n^2)$
- 空间复杂度: $O(n^2)$

递归栈与数组切片会引入额外开销。

## 相关专题
- [链表、树与回溯](../../topics/linked-list-tree-backtracking.md)

## 代码
```cpp
class Solution {
public:
    TreeNode* buildTree(vector<int>& inorder, vector<int>& postorder) {
        if (postorder.empty()) return nullptr;
        return build(inorder, postorder);
    }

private:
    TreeNode* build(vector<int> inorder, vector<int> postorder) {
        if (postorder.empty()) return nullptr;

        int rootVal = postorder.back();
        postorder.pop_back();
        TreeNode* root = new TreeNode(rootVal);

        int i = 0;
        for (; i < static_cast<int>(inorder.size()); ++i) {
            if (inorder[i] == rootVal) break;
        }

        vector<int> inLeft(inorder.begin(), inorder.begin() + i);
        vector<int> inRight(inorder.begin() + i + 1, inorder.end());
        vector<int> postLeft(postorder.begin(), postorder.begin() + i);
        vector<int> postRight(postorder.begin() + i, postorder.end());

        root->left = build(inLeft, postLeft);
        root->right = build(inRight, postRight);
        return root;
    }
};
```
