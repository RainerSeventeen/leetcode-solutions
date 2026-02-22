---
id: 234
title: Palindrome Linked List
difficulty: Easy
tags: [stack, recursion, linked-list, two-pointers]
created: 2026-02-20
---

# 234. 回文链表

## 题目链接
https://leetcode.cn/problems/palindrome-linked-list/

## 题目描述
<p>给你一个单链表的头节点 <code>head</code> ，请你判断该链表是否为<span data-keyword="palindrome-sequence">回文链表</span>。如果是，返回 <code>true</code> ；否则，返回 <code>false</code> 。</p>

<p><strong>示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/03/03/pal1linked-list.jpg" style="width: 422px; height: 62px;" />
<pre>
<strong>输入：</strong>head = [1,2,2,1]
<strong>输出：</strong>true
</pre>

<p><strong>示例 2：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/03/03/pal2linked-list.jpg" style="width: 182px; height: 62px;" />
<pre>
<strong>输入：</strong>head = [1,2]
<strong>输出：</strong>false
</pre>

<p><strong>提示：</strong></p>

<ul>
	<li>链表中节点数目在范围<code>[1, 10<sup>5</sup>]</code> 内</li>
	<li><code>0 &lt;= Node.val &lt;= 9</code></li>
</ul>

<p><strong>进阶：</strong>你能否用&nbsp;<code>O(n)</code> 时间复杂度和 <code>O(1)</code> 空间复杂度解决此题？</p>


## 解题思路

有两种方式，如果需要 O(1) 的空间复杂度需要对原来的链表进行修改

如果不允许修改就使用栈的方式

重点在于计算清除中间节点和终止数量，一般推荐从0开始+对0空节点的特殊判断（本题题目限定了不会有空节点）

另外如果使用了翻转链表的方式，注意使用快慢指针的方式来找到中间节点

- 时间复杂度: $O(n)$
- 空间复杂度: $O(1)$
## 相关专题
- [链表、树与回溯](../../topics/linked-list-tree-backtracking.md)

## 代码
```python
class Solution:
    def reverseList(self, head):
        # 从 head 开始翻转后续所有的链表
        curr = head
        pre = None
        while curr:
            temp = curr.next
            curr.next = pre
            pre = curr
            curr = temp
        return pre

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # 快慢指针找到中间位置，原地翻转
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 如果 fast 不为空，说明是奇数长度，需要跳过中间节点
        if fast:
            slow = slow.next

        second = self.reverseList(slow)
        first = head
        while second is not None:
            if first.val != second.val:
                return False
            first = first.next
            second = second.next

        return True
```
