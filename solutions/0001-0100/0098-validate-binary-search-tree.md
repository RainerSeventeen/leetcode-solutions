---
id: 98
title: Validate Binary Search Tree
difficulty: Medium
tags: [tree, depth-first-search, binary-search-tree, binary-tree]
created: 2026-02-20
---

# 98. 验证二叉搜索树

## 题目链接
https://leetcode.cn/problems/validate-binary-search-tree/

## 题目描述
<p>给你一个二叉树的根节点 <code>root</code> ，判断其是否是一个有效的二叉搜索树。</p>

<p><strong>有效</strong> 二叉搜索树定义如下：</p>

<ul>
	<li>节点的左<span data-keyword="subtree">子树</span>只包含<strong>&nbsp;严格小于 </strong>当前节点的数。</li>
	<li>节点的右子树只包含 <strong>严格大于</strong> 当前节点的数。</li>
	<li>所有左子树和右子树自身必须也是二叉搜索树。</li>
</ul>

<p><strong>示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/12/01/tree1.jpg" style="width: 302px; height: 182px;" />
<pre>
<strong>输入：</strong>root = [2,1,3]
<strong>输出：</strong>true
</pre>

<p><strong>示例 2：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/12/01/tree2.jpg" style="width: 422px; height: 292px;" />
<pre>
<strong>输入：</strong>root = [5,1,4,null,null,3,6]
<strong>输出：</strong>false
<strong>解释：</strong>根节点的值是 5 ，但是右子节点的值是 4 。
</pre>

<p><strong>提示：</strong></p>

<ul>
	<li>树中节点数目范围在<code>[1, 10<sup>4</sup>]</code> 内</li>
	<li><code>-2<sup>31</sup> &lt;= Node.val &lt;= 2<sup>31</sup> - 1</code></li>
</ul>


## 解题思路

二叉搜索树的中序遍历结果必须严格递增。递归做中序遍历时，维护一个“上一个访问到的值” `maxVal`。如果当前节点值 `<= maxVal`，就可以直接判定不是合法 BST。

- 时间复杂度: $O(n)$
- 空间复杂度: $O(h)$，`h` 为树高

## 代码
```cpp
class Solution {
public:
    bool isValidBST(TreeNode* root) {
        long long maxVal = LLONG_MIN;
        return dfs(root, maxVal);
    }

private:
    bool dfs(TreeNode* node, long long& maxVal) {
        if (!node) return true;

        if (!dfs(node->left, maxVal)) return false;
        if (node->val <= maxVal) return false;
        maxVal = node->val;
        return dfs(node->right, maxVal);
    }
};
```
