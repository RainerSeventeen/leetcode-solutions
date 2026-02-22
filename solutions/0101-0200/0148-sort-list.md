---
id: 148
title: Sort List
difficulty: Medium
tags: [linked-list, two-pointers, divide-and-conquer, sorting, merge-sort]
created: 2026-02-20
---

# 148. 排序链表

## 题目链接
https://leetcode.cn/problems/sort-list/

## 题目描述
<p>给你链表的头结点&nbsp;<code>head</code>&nbsp;，请将其按 <strong>升序</strong> 排列并返回 <strong>排序后的链表</strong> 。</p>

<ul>
</ul>

<p><strong>示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/09/14/sort_list_1.jpg" style="width: 450px;" />
<pre>
<b>输入：</b>head = [4,2,1,3]
<b>输出：</b>[1,2,3,4]
</pre>

<p><strong>示例 2：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/09/14/sort_list_2.jpg" style="width: 550px;" />
<pre>
<b>输入：</b>head = [-1,5,3,4,0]
<b>输出：</b>[-1,0,3,4,5]
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<b>输入：</b>head = []
<b>输出：</b>[]
</pre>

<p><b>提示：</b></p>

<ul>
	<li>链表中节点的数目在范围&nbsp;<code>[0, 5 * 10<sup>4</sup>]</code>&nbsp;内</li>
	<li><code>-10<sup>5</sup>&nbsp;&lt;= Node.val &lt;= 10<sup>5</sup></code></li>
</ul>

<p><b>进阶：</b>你可以在&nbsp;<code>O(n&nbsp;log&nbsp;n)</code> 时间复杂度和常数级空间复杂度下，对链表进行排序吗？</p>


## 解题思路

链表的排序是归并排序算法

1. 反复二分法，直到只有两个节点（链表的二分法使用快慢指针实现的）
2. 比较两个链表的头，把较小的那个接到结果链表后面（此时两个链表各自内部已经排序完毕，只要左右各自轮流比较即可）

注意这里不涉及到反转操作，反转一定会出现 `cur.next = prev`这种操作

这个递归还是想了很久，感觉掌握还是不够好，要多练习递归

- 时间复杂度: $O(n \log n)$
- 空间复杂度: $O(\log n)$

空间复杂度来自递归栈深度。
## 相关专题
- [链表、树与回溯](../../topics/linked-list-tree-backtracking.md)

## 代码
```python
class Solution:
    @staticmethod
    def _find_mid(head):
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow  # 左半尾，方便断开

    @staticmethod
    def merge(l1, l2):
        dummy = ListNode(0)
        curr = dummy
        while l1 and l2:
            if l1.val > l2.val:
                curr.next = l2
                l2 = l2.next
            else:
                curr.next = l1
                l1 = l1.next
            curr = curr.next
        curr.next = l1 or l2
        return dummy.next

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        mid = self._find_mid(head)
        right = mid.next
        mid.next = None  # 断链

        left = self.sortList(head)
        right = self.sortList(right)
        return self.merge(left, right)
```
