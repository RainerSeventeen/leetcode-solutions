---
id: 144
title: Binary Tree Preorder Traversal
difficulty: Easy
tags: [stack, tree, depth-first-search, binary-tree]
created: 2026-02-21
---

# 144. 二叉树的前序遍历

## 题目链接
https://leetcode.cn/problems/binary-tree-preorder-traversal/

## 题目描述
<p>给你二叉树的根节点 <code>root</code> ，返回它节点值的&nbsp;<strong>前序</strong><em>&nbsp;</em>遍历。</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><strong>输入：</strong><span class="example-io">root = [1,null,2,3]</span></p>

<p><strong>输出：</strong><span class="example-io">[1,2,3]</span></p>

<p><strong>解释：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2024/08/29/screenshot-2024-08-29-202743.png" style="width: 200px; height: 264px;" /></p>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>root = [1,2,3,4,5,null,8,null,null,6,7,9]</span></p>

<p><span class="example-io"><b>输出：</b>[1,2,4,5,6,7,3,8,9]</span></p>

<p><strong>解释：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2024/08/29/tree_2.png" style="width: 350px; height: 286px;" /></p>
</div>

<p><strong class="example">示例 3：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>root = []</span></p>

<p><span class="example-io"><b>输出：</b>[]</span></p>
</div>

<p><strong class="example">示例 4：</strong></p>

<div class="example-block">
<p><strong>输入：</strong><span class="example-io">root = [1]</span></p>

<p><span class="example-io"><b>输出：</b>[1]</span></p>
</div>

<p><strong>提示：</strong></p>

<ul>
	<li>树中节点数目在范围 <code>[0, 100]</code> 内</li>
	<li><code>-100 &lt;= Node.val &lt;= 100</code></li>
</ul>

<p><strong>进阶：</strong>递归算法很简单，你可以通过迭代算法完成吗？</p>


## 解题思路

使用栈实现前序遍历，先访问当前节点，再处理左右子树。
为保证访问顺序是“根-左-右”，入栈时先压右子节点再压左子节点。
- 时间复杂度: $O(n)$
- 空间复杂度: $O(h)$

## 相关专题
- [图论算法](../../topics/graph-algorithms.md)

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
#include <vector>
#include <stack>

class Solution {
public:
    vector<int> preorderTraversal(TreeNode* root) {
        vector<int> ret;
        if (!root) return ret;
        stack<TreeNode*> stk;
        stk.push(root);

        while (!stk.empty()) {
            TreeNode* curr = stk.top();
            stk.pop();
            ret.push_back(curr->val);

            if (curr->right) stk.push(curr->right);
            if (curr->left)  stk.push(curr->left);
        }
        return ret;
    }
};
```
