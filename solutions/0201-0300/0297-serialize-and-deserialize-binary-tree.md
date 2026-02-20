---
id: 297
title: 二叉树的序列化与反序列化
difficulty: Medium
tags: [tree, depth-first-search, breadth-first-search, design, string, binary-tree]
created: 2026-02-20
---

# 297. 二叉树的序列化与反序列化

## 题目链接
https://leetcode.cn/problems/serialize-and-deserialize-binary-tree/

## 题目描述
暂无（需要从LeetCode获取）

## 解题思路
序列化/反序列化的关键是：遍历时必须把空指针也编码出来，否则无法唯一还原结构。

这里用**前序遍历（根-左-右）**，并用 `#` 作为空节点标记：

- **序列化**：前序遍历整棵树；遇到非空节点就写入 `val`，遇到空节点就写入 `#`；最后用逗号拼接成字符串。
- **反序列化**：按逗号切分得到 token 序列，并用迭代器按顺序消费：
  - 读到 `#` 返回 `None`；
  - 否则创建节点，再递归构造其左子树与右子树（因为前序序列中左子树的 token 紧随其后）。

边界情况：空树会被序列化为单个 `#`，反序列化时直接返回 `None`。

- 时间复杂度: $O(n)$
- 空间复杂度: $O(n)$

## 代码
```python
class Codec:
    def serialize(self, root):
        # 前序遍历
        ret: str = []
        def preTraversal(curr):
            nonlocal ret
            if curr is None:
                ret.append('#')
                return

            ret.append(str(curr.val)) 
            preTraversal(curr.left)
            preTraversal(curr.right)

        preTraversal(root)
        # print(ret)
        return ','.join(ret)

    def deserialize(self, data):
        it = iter(data.split(','))
        def build():
            x = next(it)
            if x == '#':
                return None
            node = TreeNode(int(x))
            node.left = build()
            node.right = build()
            return node
        
        return build()
```
