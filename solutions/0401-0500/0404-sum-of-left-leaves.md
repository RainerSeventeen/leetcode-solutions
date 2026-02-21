---
id: 404
title: Sum of Left Leaves
difficulty: Easy
tags: [tree, depth-first-search, breadth-first-search, binary-tree]
created: 2026-02-21
---

# 404. 左叶子之和

## 题目链接
https://leetcode.cn/problems/sum-of-left-leaves/

## 题目描述
<p>给定二叉树的根节点&nbsp;<code>root</code>&nbsp;，返回所有左叶子之和。</p>

<p><strong>示例 1：</strong></p>

<p><img src="https://assets.leetcode.com/uploads/2021/04/08/leftsum-tree.jpg" /></p>

<pre>
<strong>输入:</strong> root = [3,9,20,null,null,15,7] 
<strong>输出:</strong> 24 
<strong>解释:</strong> 在这个二叉树中，有两个左叶子，分别是 9 和 15，所以返回 24
</pre>

<p><strong>示例&nbsp;2:</strong></p>

<pre>
<strong>输入:</strong> root = [1]
<strong>输出:</strong> 0
</pre>

<p><strong>提示:</strong></p>

<ul>
	<li>节点数在&nbsp;<code>[1, 1000]</code>&nbsp;范围内</li>
	<li><code>-1000 &lt;= Node.val &lt;= 1000</code></li>
</ul>



## 解题思路

递归遍历二叉树，并携带当前节点是否为“左孩子”的标记。
当遇到叶子节点且标记为左孩子时累加其值，最后返回总和。
- 时间复杂度: $O(n)$
- 空间复杂度: $O(h)$

## 代码
```cpp
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:

    void _sumOfLeftLeaves(TreeNode* curr, bool is_left, int& sum) {
        if (!curr->left && !curr->right) {
            // 是叶子
            if (is_left) {
                // 左叶子，累加
                sum += curr->val;
                return;
            }
        } else {
            // 不是叶子
            if (curr->left) _sumOfLeftLeaves(curr->left, true, sum);
            if (curr->right) _sumOfLeftLeaves(curr->right, false, sum);
        }

    }
    
    int sumOfLeftLeaves(TreeNode* root) {
        int sum = 0;
        _sumOfLeftLeaves(root, false, sum);
        return sum;
    }
    
    
};
```
