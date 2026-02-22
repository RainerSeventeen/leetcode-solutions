---
id: 968
title: Binary Tree Cameras
difficulty: Hard
tags: [tree, depth-first-search, dynamic-programming, binary-tree]
created: 2026-02-20
---

# 968. 监控二叉树

## 题目链接
https://leetcode.cn/problems/binary-tree-cameras/

## 题目描述
<p>给定一个二叉树，我们在树的节点上安装摄像头。</p>

<p>节点上的每个摄影头都可以监视<strong>其父对象、自身及其直接子对象。</strong></p>

<p>计算监控树的所有节点所需的最小摄像头数量。</p>

<p><strong>示例 1：</strong></p>

<p><img alt="" src="https://assets.leetcode.cn/aliyun-lc-upload/uploads/2018/12/29/bst_cameras_01.png" style="height: 163px; width: 138px;"></p>

<pre><strong>输入：</strong>[0,0,null,0,0]
<strong>输出：</strong>1
<strong>解释：</strong>如图所示，一台摄像头足以监控所有节点。
</pre>

<p><strong>示例 2：</strong></p>

<p><img alt="" src="https://assets.leetcode.cn/aliyun-lc-upload/uploads/2018/12/29/bst_cameras_02.png" style="height: 312px; width: 139px;"></p>

<pre><strong>输入：</strong>[0,0,null,0,null,0,null,null,0]
<strong>输出：</strong>2
<strong>解释：</strong>需要至少两个摄像头来监视树的所有节点。 上图显示了摄像头放置的有效位置之一。
</pre>

<p><br>
<strong>提示：</strong></p>

<ol>
	<li>给定树的节点数的范围是&nbsp;<code>[1, 1000]</code>。</li>
	<li>每个节点的值都是 0。</li>
</ol>


## 解题思路

用后序遍历做状态贪心。定义三种状态：`0` 未覆盖、`1` 放摄像头、`2` 已覆盖。遍历到当前节点时，先拿到左右子树状态，再按规则决策：
如果任一孩子未覆盖，则当前节点必须放摄像头；如果任一孩子有摄像头，则当前节点已覆盖；否则当前节点为未覆盖，交给父节点处理。

空节点返回“已覆盖”，这样叶子节点会自然变成“未覆盖”，促使其父节点放摄像头。最后若根节点仍未覆盖，再补一个摄像头。

- 时间复杂度: $O(n)$
- 空间复杂度: $O(h)$

其中 `h` 为树高（递归栈深度）。

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
class Solution {
public:
    int minCameraCover(TreeNode* root) {
        int cnt = 0;
        if (dfs(root, cnt) == 0) cnt++;
        return cnt;
    }

    // 0: 未覆盖, 1: 有摄像头, 2: 已覆盖
    int dfs(TreeNode* node, int& cnt) {
        if (!node) return 2;
        int l = dfs(node->left, cnt);
        int r = dfs(node->right, cnt);
        if (l == 0 || r == 0) {
            cnt++;
            return 1;
        }
        if (l == 1 || r == 1) return 2;
        return 0;
    }
};
```
