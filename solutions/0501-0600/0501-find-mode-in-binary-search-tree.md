---
id: 501
title: Find Mode in Binary Search Tree
difficulty: Easy
tags: [tree, depth-first-search, binary-search-tree, binary-tree]
created: 2026-02-21
---

# 501. 二叉搜索树中的众数

## 题目链接
https://leetcode.cn/problems/find-mode-in-binary-search-tree/

## 题目描述
<p>给你一个含重复值的二叉搜索树（BST）的根节点 <code>root</code> ，找出并返回 BST 中的所有 <a href="https://baike.baidu.com/item/%E4%BC%97%E6%95%B0/44796" target="_blank">众数</a>（即，出现频率最高的元素）。</p>

<p>如果树中有不止一个众数，可以按 <strong>任意顺序</strong> 返回。</p>

<p>假定 BST 满足如下定义：</p>

<ul>
	<li>结点左子树中所含节点的值 <strong>小于等于</strong> 当前节点的值</li>
	<li>结点右子树中所含节点的值 <strong>大于等于</strong> 当前节点的值</li>
	<li>左子树和右子树都是二叉搜索树</li>
</ul>

<p><strong>示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/03/11/mode-tree.jpg" style="width: 142px; height: 222px;" />
<pre>
<strong>输入：</strong>root = [1,null,2,2]
<strong>输出：</strong>[2]
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>root = [0]
<strong>输出：</strong>[0]
</pre>

<p><strong>提示：</strong></p>

<ul>
	<li>树中节点的数目在范围 <code>[1, 10<sup>4</sup>]</code> 内</li>
	<li><code>-10<sup>5</sup> &lt;= Node.val &lt;= 10<sup>5</sup></code></li>
</ul>

<p><strong>进阶：</strong>你可以不使用额外的空间吗？（假设由递归产生的隐式调用栈的开销不被计算在内）</p>


## 解题思路

利用 BST 的中序遍历有序性，连续相同值会相邻出现。
遍历时记录前驱节点和当前计数，动态维护最大频次 `max_count` 与众数结果集。
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
class Solution {
public:
    vector<int> findMode(TreeNode* root) {
        pre = nullptr;
        max_count = 0;
        result = {};
        int count = 0;
        _findMode(root, count);
        return result;
    }
private:
    vector<int> result;
    TreeNode* pre;
    int max_count;

    void _findMode(TreeNode* root, int& count) {
        // 中序遍历
        if (!root) return;
        if (root->left)
            _findMode(root->left, count);
            
        if (pre) {
            if (pre->val == root->val) {
                count++;
                if (count == max_count) {
                    result.push_back(root->val);
                } else if (count > max_count) {
                    result.clear();
                    result.push_back(root->val); 
                    max_count = count;
                }
            } else {
                // 新数值
                count = 1;
                if (count == max_count) {
                    result.push_back(root->val);
                }
            }
        } else {
            // 第一次进入 , pre == nullptr
            result.push_back(root->val);
            count = 1;
            max_count = 1;
        }
        pre = root;
        if (root->right)
            _findMode(root->right, count);
    }
};
```
