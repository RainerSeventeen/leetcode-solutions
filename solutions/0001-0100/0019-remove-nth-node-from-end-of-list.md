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
暂无（需要从LeetCode获取）

## 解题思路
快慢指针一次遍历定位“倒数第 n 个节点”的前驱。

- 先用 `dummy` 指向 `head`，统一处理“删除头结点”的边界；
- 让 `fast` 从 `dummy` 出发先走 `n` 步，使得 `fast` 与 `slow` 间距为 `n`；
- 然后两者同步前进，直到 `fast.next` 为空，此时 `slow.next` 正好是要删除的节点；
- 执行 `slow.next = slow.next.next` 完成删除。

- 时间复杂度: $O(n)$
- 空间复杂度: $O(1)$

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
