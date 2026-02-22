---
id: 108
title: Convert Sorted Array to Binary Search Tree
difficulty: Easy
tags: [tree, binary-search-tree, array, divide-and-conquer, binary-tree]
created: 2026-02-20
---

# 108. 将有序数组转换为二叉搜索树

## 题目链接
https://leetcode.cn/problems/convert-sorted-array-to-binary-search-tree/

## 题目描述
<p>给你一个整数数组 <code>nums</code> ，其中元素已经按 <strong>升序</strong> 排列，请你将其转换为一棵 <span data-keyword="height-balanced">平衡</span> 二叉搜索树。</p>

<p><strong>示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/02/18/btree1.jpg" style="width: 302px; height: 222px;" />
<pre>
<strong>输入：</strong>nums = [-10,-3,0,5,9]
<strong>输出：</strong>[0,-3,9,-10,null,5]
<strong>解释：</strong>[0,-10,5,null,-3,null,9] 也将被视为正确答案：
<img alt="" src="https://assets.leetcode.com/uploads/2021/02/18/btree2.jpg" style="width: 302px; height: 222px;" />
</pre>

<p><strong>示例 2：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/02/18/btree.jpg" style="width: 342px; height: 142px;" />
<pre>
<strong>输入：</strong>nums = [1,3]
<strong>输出：</strong>[3,1]
<strong>解释：</strong>[1,null,3] 和 [3,1] 都是高度平衡二叉搜索树。
</pre>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>4</sup></code></li>
	<li><code>-10<sup>4</sup> &lt;= nums[i] &lt;= 10<sup>4</sup></code></li>
	<li><code>nums</code> 按 <strong>严格递增</strong> 顺序排列</li>
</ul>


## 解题思路

有序数组构造平衡 BST 的核心是“每次取中点做根”。递归处理区间 `[left, right)`：区间为空时返回 `nullptr`，否则取中点建根节点，再由左半区间和右半区间分别构造左、右子树。

- 时间复杂度: $O(n)$
- 空间复杂度: $O(\log n)$

递归深度为 $O(\log n)$。

## 相关专题
- [链表、树与回溯](../../topics/linked-list-tree-backtracking.md)

## 代码
```cpp
class Solution {
public:
    TreeNode* sortedArrayToBST(vector<int>& nums) {
        return build(nums, 0, static_cast<int>(nums.size()));
    }

private:
    TreeNode* build(const vector<int>& nums, int left, int right) {
        if (left >= right) return nullptr;

        int mid = left + (right - left) / 2;
        TreeNode* root = new TreeNode(nums[mid]);
        root->left = build(nums, left, mid);
        root->right = build(nums, mid + 1, right);
        return root;
    }
};
```
