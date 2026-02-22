---
id: 24
title: Swap Nodes in Pairs
difficulty: Medium
tags: [recursion, linked-list]
created: 2026-02-21
---

# 24. 两两交换链表中的节点

## 题目链接
https://leetcode.cn/problems/swap-nodes-in-pairs/

## 题目描述
<p>给你一个链表，两两交换其中相邻的节点，并返回交换后链表的头节点。你必须在不修改节点内部的值的情况下完成本题（即，只能进行节点交换）。</p>

<p><strong>示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/10/03/swap_ex1.jpg" style="width: 422px; height: 222px;" />
<pre>
<strong>输入：</strong>head = [1,2,3,4]
<strong>输出：</strong>[2,1,4,3]
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>head = []
<strong>输出：</strong>[]
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>head = [1]
<strong>输出：</strong>[1]
</pre>

<p><strong>提示：</strong></p>

<ul>
	<li>链表中节点的数目在范围 <code>[0, 100]</code> 内</li>
	<li><code>0 &lt;= Node.val &lt;= 100</code></li>
</ul>


## 解题思路

使用虚拟头结点统一处理头节点交换，遍历链表时每次取相邻两个节点做重连。
把 `before->next` 指向第二个节点，再让第二个指向第一个，完成一组交换。
随后将指针移动到下一组起点，直到剩余节点不足两个为止。
- 时间复杂度: $O(n)$
- 空间复杂度: $O(1)$

## 相关专题
- [链表、树与回溯](../../topics/linked-list-tree-backtracking.md)

## 代码
```cpp
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* swapPairs(ListNode* head) {
        ListNode dummy(0, head);
        ListNode *before = &dummy;
        ListNode *cur1 = head;
        bool is_double = true;
        if (!head || !head->next) {
            return head;    // 空或者1个节点 
        }
        ListNode *cur2 = head->next;
        while (cur2 != nullptr) {
            if (!is_double) {
                // 需要偶数才执行操作，奇数直接跳过一轮
                before = before->next;
                cur1 = cur1->next;
                cur2 = cur2->next;
                is_double = !is_double;
                continue;
            }
            
            before->next = cur1->next;
            cur1->next = cur2->next;
            cur2->next = cur1;
            
            before = before->next;
            // cur1 = cur1;
            cur2 = cur1->next;
            is_double = !is_double;
        }
    return dummy.next;
    }
};
```
