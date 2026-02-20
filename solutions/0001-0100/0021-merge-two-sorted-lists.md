---
id: 21
title: 合并两个有序链表
difficulty: Medium
tags: [recursion, linked-list]
created: 2026-02-20
---

# 21. 合并两个有序链表

## 题目链接
https://leetcode.cn/problems/merge-two-sorted-lists/

## 题目描述
暂无（需要从LeetCode获取）

## 解题思路
双指针归并两个有序链表。维护 `l1/l2` 指向当前未合并的节点，并用 `dummy/curr` 构造结果：

- 每次比较 `l1.val` 与 `l2.val`，把较小节点接到 `curr.next`，并推进对应指针；
- 当某一条链表耗尽时，把另一条剩余部分整体接到末尾即可。

因为直接复用原链表节点，所以不需要额外开新节点（除哨兵头）。

- 时间复杂度: $O(m+n)$
- 空间复杂度: $O(1)$

## 代码
```python
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        l1, l2 = list1, list2
        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        curr.next = l1 if l1 is not None else l2
        return dummy.next
```
