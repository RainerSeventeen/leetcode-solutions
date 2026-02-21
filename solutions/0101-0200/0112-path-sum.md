---
id: 112
title: Path Sum
difficulty: Easy
tags: [tree, depth-first-search, breadth-first-search, binary-tree]
created: 2026-02-21
---

# 112. 路径总和

## 题目链接
https://leetcode.cn/problems/path-sum/

## 题目描述
<p>给你二叉树的根节点&nbsp;<code>root</code> 和一个表示目标和的整数&nbsp;<code>targetSum</code> 。判断该树中是否存在 <strong>根节点到叶子节点</strong> 的路径，这条路径上所有节点值相加等于目标和&nbsp;<code>targetSum</code> 。如果存在，返回 <code>true</code> ；否则，返回 <code>false</code> 。</p>

<p><strong>叶子节点</strong> 是指没有子节点的节点。</p>

<p><strong>示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/01/18/pathsum1.jpg" style="width: 500px; height: 356px;" />
<pre>
<strong>输入：</strong>root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
<strong>输出：</strong>true
<strong>解释：</strong>等于目标和的根节点到叶节点路径如上图所示。
</pre>

<p><strong>示例 2：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/01/18/pathsum2.jpg" />
<pre>
<strong>输入：</strong>root = [1,2,3], targetSum = 5
<strong>输出：</strong>false
<strong>解释：</strong>树中存在两条根节点到叶子节点的路径：
(1 --&gt; 2): 和为 3
(1 --&gt; 3): 和为 4
不存在 sum = 5 的根节点到叶子节点的路径。</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>root = [], targetSum = 0
<strong>输出：</strong>false
<strong>解释：</strong>由于树是空的，所以不存在根节点到叶子节点的路径。
</pre>

<p><strong>提示：</strong></p>

<ul>
	<li>树中节点的数目在范围 <code>[0, 5000]</code> 内</li>
	<li><code>-1000 &lt;= Node.val &lt;= 1000</code></li>
	<li><code>-1000 &lt;= targetSum &lt;= 1000</code></li>
</ul>


## 解题思路

深度优先遍历所有根到叶路径，递归时累加当前路径和。
到叶子节点时判断是否等于目标值，找到即通过标记提前结束后续搜索。
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
    bool hasPathSum(TreeNode* root, int targetSum) {
        if (!root) return false;
        bool found = false;
        int sum = 0;
        _hasPathSum(root, sum, targetSum, found);
        return found;
    }

    void _hasPathSum(TreeNode* curr, int& sum, const int tar, bool& found) {
        if (found) return;
        sum += curr->val;
        int curr_sum = sum; // 存放当前状态

        if (sum == tar && (!curr->left && !curr->right)) {
            // 找到了
            found = true;
            return;
        }
        if (curr->left) _hasPathSum(curr->left, sum, tar, found);
        sum = curr_sum;
        if (curr->right) _hasPathSum(curr->right, sum, tar, found);
        sum = curr_sum;
    }
};
```
