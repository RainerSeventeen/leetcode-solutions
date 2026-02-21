---
id: 257
title: Binary Tree Paths
difficulty: Easy
tags: [tree, depth-first-search, string, backtracking, binary-tree]
created: 2026-02-21
---

# 257. 二叉树的所有路径

## 题目链接
https://leetcode.cn/problems/binary-tree-paths/

## 题目描述
<p>给你一个二叉树的根节点 <code>root</code> ，按 <strong>任意顺序</strong> ，返回所有从根节点到叶子节点的路径。</p>

<p><strong>叶子节点</strong> 是指没有子节点的节点。</p>
&nbsp;

<p><strong>示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/03/12/paths-tree.jpg" style="width: 207px; height: 293px;" />
<pre>
<strong>输入：</strong>root = [1,2,3,null,5]
<strong>输出：</strong>["1-&gt;2-&gt;5","1-&gt;3"]
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>root = [1]
<strong>输出：</strong>["1"]
</pre>

<p><strong>提示：</strong></p>

<ul>
	<li>树中节点的数目在范围 <code>[1, 100]</code> 内</li>
	<li><code>-100 &lt;= Node.val &lt;= 100</code></li>
</ul>


## 解题思路

使用 DFS + 回溯维护当前路径字符串，进入节点时追加 `->val`，返回时恢复长度。
走到叶子节点就把当前完整路径加入结果，继续遍历左右子树。
- 时间复杂度: $O(n^2)$
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
#include <string>
#include <vector>
#include <sstream> // std::to_string
class Solution {
public:

    vector<string> ret;

    void _binaryTreePath(TreeNode* curr, string& path) {
        int old = path.size();
        path += "->";
        string val = std::to_string(curr->val);
        path += val;
        if (curr->left == nullptr && curr->right == nullptr) {
            // 到此结束
            this->ret.push_back(path);
            path.resize(old);
            return;
        }
        // 否则继续递归
        if (curr->left != nullptr) {
            _binaryTreePath(curr->left, path);
        }
        if (curr->right != nullptr) {
            _binaryTreePath(curr->right, path);
        }
        // 退出来后要回溯
        path.resize(old);
    }

    vector<string> binaryTreePaths(TreeNode* root) {
        this->ret = {};
        string path = std::to_string(root->val);

        // 根就是叶子
        if (!root->left && !root->right) {
            ret.push_back(path);
            return ret;
        }
        
        if (root->right)
            _binaryTreePath(root->right, path);
        if (root->left)
            _binaryTreePath(root->left, path);
        return this->ret;
    }
    

};
```
