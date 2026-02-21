---
id: 530
title: Minimum Absolute Difference in BST
difficulty: Easy
tags: [tree, depth-first-search, breadth-first-search, binary-search-tree, binary-tree]
created: 2026-02-21
---

# 530. 二叉搜索树的最小绝对差

## 题目链接
https://leetcode.cn/problems/minimum-absolute-difference-in-bst/

## 题目描述
<p>给你一个二叉搜索树的根节点 <code>root</code> ，返回 <strong>树中任意两不同节点值之间的最小差值</strong> 。</p>

<p>差值是一个正数，其数值等于两值之差的绝对值。</p>

<p><strong>示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/02/05/bst1.jpg" style="width: 292px; height: 301px;" />
<pre>
<strong>输入：</strong>root = [4,2,6,1,3]
<strong>输出：</strong>1
</pre>

<p><strong>示例 2：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/02/05/bst2.jpg" style="width: 282px; height: 301px;" />
<pre>
<strong>输入：</strong>root = [1,0,48,null,null,12,49]
<strong>输出：</strong>1
</pre>

<p><strong>提示：</strong></p>

<ul>
	<li>树中节点的数目范围是 <code>[2, 10<sup>4</sup>]</code></li>
	<li><code>0 &lt;= Node.val &lt;= 10<sup>5</sup></code></li>
</ul>

<p><strong>注意：</strong>本题与 783 <a href="https://leetcode.cn/problems/minimum-distance-between-bst-nodes/">https://leetcode.cn/problems/minimum-distance-between-bst-nodes/</a> 相同</p>


## 解题思路

用栈做迭代中序遍历，BST 中序结果递增，只需比较当前节点和前一个节点差值。
每访问一个节点就更新最小差值，最终得到答案。
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

#include <vector>
#include <stack>
#include <cmath>
class Solution {
public:
    int getMinimumDifference(TreeNode* root) {
        result = INT_MAX;
        pre = nullptr;
        _traversal(root);
        return result;
    }

private:
    stack<TreeNode*> stk;
    TreeNode* pre = nullptr;
    int result = INT_MAX;

    void _traversal(TreeNode* root) {
        // 迭代的中序遍历
        TreeNode* curr = root;

        // 左走到底
        while (curr || !stk.empty()) {
            while (curr) {
                stk.push(curr);
                curr=curr->left;
            } 
        // 弹出访问
        curr = stk.top();
        stk.pop();
        if (pre) {
            int delta = abs(pre->val - curr->val);
            result = result < delta ? result : delta;
        }
        pre = curr;

        // 右子树
        curr = curr->right;
        }
    }
};
```
