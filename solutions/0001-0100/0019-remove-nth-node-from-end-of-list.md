---
id: 19
title: 删除链表的倒数第 N 个结点
difficulty: Medium
tags: [linked-list, two-pointers]
created: 2026-02-20
---

# 19. 删除链表的倒数第 N 个结点

## 题目链接
https://leetcode.cn/problems/remove-nth-node-from-end-of-list/

## 题目描述

<p>给你一个链表，删除链表的倒数第&nbsp;<code>n</code><em>&nbsp;</em>个结点，并且返回链表的头结点。</p>

<p><strong>示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/10/03/remove_ex1.jpg" style="width: 542px; height: 222px;" />
<pre>
<strong>输入：</strong>head = [1,2,3,4,5], n = 2
<strong>输出：</strong>[1,2,3,5]
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>head = [1], n = 1
<strong>输出：</strong>[]
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>head = [1,2], n = 1
<strong>输出：</strong>[1]
</pre>

<p><strong>提示：</strong></p>

<ul>
	<li>链表中结点的数目为 <code>sz</code></li>
	<li><code>1 &lt;= sz &lt;= 30</code></li>
	<li><code>0 &lt;= Node.val &lt;= 100</code></li>
	<li><code>1 &lt;= n &lt;= sz</code></li>
</ul>

<p><strong>进阶：</strong>你能尝试使用一趟扫描实现吗？</p>

## 解题思路
快慢指针一次遍历定位“倒数第 n 个节点”的前驱。

- 先用 `dummy` 指向 `head`，统一处理“删除头结点”的边界；
- 让 `fast` 从 `dummy` 出发先走 `n` 步，使得 `fast` 与 `slow` 间距为 `n`；
- 然后两者同步前进，直到 `fast.next` 为空，此时 `slow.next` 正好是要删除的节点；
- 执行 `slow.next = slow.next.next` 完成删除。

- 时间复杂度: $O(n)$
- 空间复杂度: $O(1)$

## 相关专题
- [链表、树与回溯](../../topics/linked-list-tree-backtracking.md)

## 代码
```python
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        slow, fast = dummy, dummy
        for i in range(n):
            fast = fast.next
        while fast.next is not None:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return dummy.next
```
