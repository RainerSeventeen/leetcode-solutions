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

<p>序列化是将一个数据结构或者对象转换为连续的比特位的操作，进而可以将转换后的数据存储在一个文件或者内存中，同时也可以通过网络传输到另一个计算机环境，采取相反方式重构得到原数据。</p>

<p>请设计一个算法来实现二叉树的序列化与反序列化。这里不限定你的序列 / 反序列化算法执行逻辑，你只需要保证一个二叉树可以被序列化为一个字符串并且将这个字符串反序列化为原始的树结构。</p>

<p><strong>提示: </strong>输入输出格式与 LeetCode 目前使用的方式一致，详情请参阅&nbsp;<a href="https://leetcode.cn/help-center/3812581/">LeetCode 序列化二叉树的格式</a>。你并非必须采取这种方式，你也可以采用其他的方法解决这个问题。</p>

<p><strong>示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/09/15/serdeser.jpg" style="width: 442px; height: 324px;" />
<pre>
<strong>输入：</strong>root = [1,2,3,null,null,4,5]
<strong>输出：</strong>[1,2,3,null,null,4,5]
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>root = []
<strong>输出：</strong>[]
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>root = [1]
<strong>输出：</strong>[1]
</pre>

<p><strong>示例 4：</strong></p>

<pre>
<strong>输入：</strong>root = [1,2]
<strong>输出：</strong>[1,2]
</pre>

<p><strong>提示：</strong></p>

<ul>
	<li>树中结点数在范围 <code>[0, 10<sup>4</sup>]</code> 内</li>
	<li><code>-1000 &lt;= Node.val &lt;= 1000</code></li>
</ul>

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

## 相关专题
- [链表、树与回溯](../../topics/linked-list-tree-backtracking.md)

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
