---
id: 450
title: Delete Node in a BST
difficulty: Medium
tags: [tree, binary-search-tree, binary-tree]
created: 2026-02-20
---

# 450. 删除二叉搜索树中的节点

## 题目链接
https://leetcode.cn/problems/delete-node-in-a-bst/

## 题目描述
<p>给定一个二叉搜索树的根节点 <strong>root </strong>和一个值 <strong>key</strong>，删除二叉搜索树中的&nbsp;<strong>key&nbsp;</strong>对应的节点，并保证二叉搜索树的性质不变。返回二叉搜索树（有可能被更新）的根节点的引用。</p>

<p>一般来说，删除节点可分为两个步骤：</p>

<ol>
	<li>首先找到需要删除的节点；</li>
	<li>如果找到了，删除它。</li>
</ol>

<p><strong>示例 1:</strong></p>

<p><img src="https://assets.leetcode.com/uploads/2020/09/04/del_node_1.jpg" style="width: 800px;" /></p>

<pre>
<strong>输入：</strong>root = [5,3,6,2,4,null,7], key = 3
<strong>输出：</strong>[5,4,6,2,null,null,7]
<strong>解释：</strong>给定需要删除的节点值是 3，所以我们首先找到 3 这个节点，然后删除它。
一个正确的答案是 [5,4,6,2,null,null,7], 如下图所示。
另一个正确答案是 [5,2,6,null,4,null,7]。

<img src="https://assets.leetcode.com/uploads/2020/09/04/del_node_supp.jpg" style="width: 350px;" />
</pre>

<p><strong>示例 2:</strong></p>

<pre>
<strong>输入:</strong> root = [5,3,6,2,4,null,7], key = 0
<strong>输出:</strong> [5,3,6,2,4,null,7]
<strong>解释:</strong> 二叉树不包含值为 0 的节点
</pre>

<p><strong>示例 3:</strong></p>

<pre>
<strong>输入:</strong> root = [], key = 0
<strong>输出:</strong> []</pre>

<p><strong>提示:</strong></p>

<ul>
	<li>节点数的范围&nbsp;<code>[0, 10<sup>4</sup>]</code>.</li>
	<li><code>-10<sup>5</sup>&nbsp;&lt;= Node.val &lt;= 10<sup>5</sup></code></li>
	<li>节点值唯一</li>
	<li><code>root</code>&nbsp;是合法的二叉搜索树</li>
	<li><code>-10<sup>5</sup>&nbsp;&lt;= key &lt;= 10<sup>5</sup></code></li>
</ul>

<p><strong>进阶：</strong> 要求算法时间复杂度为&nbsp;O(h)，h 为树的高度。</p>


## 解题思路

先按 BST 查找逻辑定位目标节点。删除时分几种情况：没找到就返回原子树；叶子节点直接删除并返回空；只有一侧子树时返回该子树；左右子树都存在时，用右子树顶替当前节点，并把左子树挂到右子树最左节点上。

- 时间复杂度: $O(h)$，`h` 为树高
- 空间复杂度: $O(h)$（递归栈）

## 代码
```cpp
class Solution {
public:
    TreeNode* deleteNode(TreeNode* root, int key) {
        if (!root) return nullptr;

        if (root->val == key) {
            if (!root->left && !root->right) {
                delete root;
                return nullptr;
            }
            if (!root->left) {
                TreeNode* rightNode = root->right;
                delete root;
                return rightNode;
            }
            if (!root->right) {
                TreeNode* leftNode = root->left;
                delete root;
                return leftNode;
            }

            TreeNode* cur = root->right;
            while (cur->left) cur = cur->left;
            cur->left = root->left;
            TreeNode* newRoot = root->right;
            delete root;
            return newRoot;
        }

        if (key < root->val) root->left = deleteNode(root->left, key);
        if (key > root->val) root->right = deleteNode(root->right, key);
        return root;
    }
};
```
