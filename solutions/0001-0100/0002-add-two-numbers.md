---
id: 2
title: Add Two Numbers
difficulty: Medium
tags: [recursion, linked-list, math]
created: 2026-02-20
---

# 2. 两数相加

## 题目链接
https://leetcode.cn/problems/add-two-numbers/

## 题目描述
<p>给你两个&nbsp;<strong>非空</strong> 的链表，表示两个非负的整数。它们每位数字都是按照&nbsp;<strong>逆序</strong>&nbsp;的方式存储的，并且每个节点只能存储&nbsp;<strong>一位</strong>&nbsp;数字。</p>

<p>请你将两个数相加，并以相同形式返回一个表示和的链表。</p>

<p>你可以假设除了数字 0 之外，这两个数都不会以 0&nbsp;开头。</p>

<p><strong class="example">示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.cn/aliyun-lc-upload/uploads/2021/01/02/addtwonumber1.jpg" style="width: 483px; height: 342px;" />
<pre>
<strong>输入：</strong>l1 = [2,4,3], l2 = [5,6,4]
<strong>输出：</strong>[7,0,8]
<strong>解释：</strong>342 + 465 = 807.
</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<strong>输入：</strong>l1 = [0], l2 = [0]
<strong>输出：</strong>[0]
</pre>

<p><strong class="example">示例 3：</strong></p>

<pre>
<strong>输入：</strong>l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
<strong>输出：</strong>[8,9,9,9,0,0,0,1]
</pre>

<p><strong>提示：</strong></p>

<ul>
	<li>每个链表中的节点数在范围 <code>[1, 100]</code> 内</li>
	<li><code>0 &lt;= Node.val &lt;= 9</code></li>
	<li>题目数据保证列表表示的数字不含前导零</li>
</ul>



## 解题思路

按“竖式加法”从低位到高位模拟即可。用指针同时遍历 `l1`、`l2`，并维护一个进位 `carry`：

- 当前位和为 `x + y + carry`（不存在的位当作 0）；
- 新节点值为 `sum % 10`，更新 `carry = sum // 10`；
- 任一链表先结束就继续用另一条链表补齐；
- 遍历结束后若 `carry != 0`，再补一个最高位节点。

用 `dummy` 作为结果链表的哨兵头，统一处理“第一节点/删除空头”等边界。

- 时间复杂度: $O(\max(m,n))$
- 空间复杂度: $O(\max(m,n))$

## 代码
```python
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        p1, p2 = l1, l2
        pre = 0 # 低位来的进位
        while p1 and p2:
            s = p1.val + p2.val + pre
            pre = s // 10
            new = ListNode(val=s % 10)
            curr.next = new
            curr = new
            p1, p2 = p1.next, p2.next
        left = p1 if p1 is not None else p2
        while left is not None: # 有一个没结束
            s = left.val + pre
            pre = s // 10
            new = ListNode(val=s % 10)
            curr.next = new
            curr = new
            left = left.next
        if pre != 0: # 还有进位
            new = ListNode(val=pre)
            curr.next = new
        return dummy.next
```
