---
id: 110
title: Balanced Binary Tree
difficulty: Easy
tags: [tree, depth-first-search, binary-tree]
created: 2026-02-20
---

# 110. 平衡二叉树

## 题目链接
https://leetcode.cn/problems/balanced-binary-tree/

## 题目描述
<p>给定一个二叉树，判断它是否是 <span data-keyword="height-balanced">平衡二叉树</span> &nbsp;</p>

<p><strong>示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/10/06/balance_1.jpg" style="width: 342px; height: 221px;" />
<pre>
<strong>输入：</strong>root = [3,9,20,null,null,15,7]
<strong>输出：</strong>true
</pre>

<p><strong>示例 2：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/10/06/balance_2.jpg" style="width: 452px; height: 301px;" />
<pre>
<strong>输入：</strong>root = [1,2,2,3,3,null,null,4,4]
<strong>输出：</strong>false
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>root = []
<strong>输出：</strong>true
</pre>

<p><strong>提示：</strong></p>

<ul>
	<li>树中的节点数在范围 <code>[0, 5000]</code> 内</li>
	<li><code>-10<sup>4</sup> &lt;= Node.val &lt;= 10<sup>4</sup></code></li>
</ul>


## 解题思路

使用后序遍历计算每个节点高度。若某个节点左右子树高度差大于 `1`，返回 `-1` 作为“不平衡”标记并向上剪枝。最终只需判断根节点递归结果是否为 `-1`。

- 时间复杂度: $O(n)$
- 空间复杂度: $O(h)$

其中 `h` 为树高。

## 代码
```cpp
class Solution {
public:
    bool isBalanced(TreeNode* root) {
        return getHeight(root) != -1;
    }

private:
    int getHeight(TreeNode* node) {
        if (!node) return 0;

        int left = getHeight(node->left);
        if (left == -1) return -1;
        int right = getHeight(node->right);
        if (right == -1) return -1;

        if (abs(left - right) > 1) return -1;
        return max(left, right) + 1;
    }
};
```
