---
id: 222
title: Count Complete Tree Nodes
difficulty: Easy
tags: [bit-manipulation, tree, binary-search, binary-tree]
created: 2026-02-21
---

# 222. 完全二叉树的节点个数

## 题目链接
https://leetcode.cn/problems/count-complete-tree-nodes/

## 题目描述
<p>给你一棵<strong> 完全二叉树</strong> 的根节点 <code>root</code> ，求出该树的节点个数。</p>

<p><a href="https://baike.baidu.com/item/%E5%AE%8C%E5%85%A8%E4%BA%8C%E5%8F%89%E6%A0%91/7773232?fr=aladdin">完全二叉树</a> 的定义如下：在完全二叉树中，除了最底层节点可能没填满外，其余每层节点数都达到最大值，并且最下面一层的节点都集中在该层最左边的若干位置。若最底层为第 <code>h</code> 层（从第 0 层开始），则该层包含 <code>1~&nbsp;2<sup>h</sup></code>&nbsp;个节点。</p>

<p><strong>示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/01/14/complete.jpg" style="width: 372px; height: 302px;" />
<pre>
<strong>输入：</strong>root = [1,2,3,4,5,6]
<strong>输出：</strong>6
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>root = []
<strong>输出：</strong>0
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>root = [1]
<strong>输出：</strong>1
</pre>

<p><strong>提示：</strong></p>

<ul>
	<li>树中节点的数目范围是<code>[0, 5 * 10<sup>4</sup>]</code></li>
	<li><code>0 &lt;= Node.val &lt;= 5 * 10<sup>4</sup></code></li>
	<li>题目数据保证输入的树是 <strong>完全二叉树</strong></li>
</ul>

<p><strong>进阶：</strong>遍历树来统计节点是一种时间复杂度为 <code>O(n)</code> 的简单解决方案。你可以设计一个更快的算法吗？</p>


## 解题思路

利用完全二叉树性质：分别计算当前子树最左高度和最右高度。
若两者相等则该子树是满二叉树，可直接用公式 `(2^h-1)` 计数；否则递归统计左右子树。
- 时间复杂度: $O((\log n)^2)$
- 空间复杂度: $O(\log n)$

## 相关专题
- [链表、树与回溯](../../topics/linked-list-tree-backtracking.md)

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

#include <cmath>
class Solution {
public:
    int countNodes(TreeNode* root) {
        // 完全二叉树方法
        int count = 0;
        _countTree(root, count);
        return count;

    }

    void _countTree(TreeNode* curr, int& count) {
        if (curr == nullptr) return; // 空指针直接返回
        int left = 0; 
        int right = 0;
        TreeNode* tmp = curr;
        while (tmp != nullptr) {
            tmp = tmp->left;
            left++;
        }
        tmp = curr;
        while (tmp!= nullptr) {
            tmp = tmp->right;
            right++;
        }
        if (right == left) {
            // 满二叉树，终止递归
            count += (1 << left) - 1;
        } else {
            // 不是满二叉树，继续分开递归
            count++; //本节点
            _countTree(curr->left, count);
            _countTree(curr->right,count);
        }
        
    }
};
```
