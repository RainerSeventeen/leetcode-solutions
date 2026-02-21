---
id: 203
title: Remove Linked List Elements
difficulty: Easy
tags: [recursion, linked-list]
created: 2026-02-21
---

# 203. 移除链表元素

## 题目链接
https://leetcode.cn/problems/remove-linked-list-elements/

## 题目描述
给你一个链表的头节点 <code>head</code> 和一个整数 <code>val</code> ，请你删除链表中所有满足 <code>Node.val == val</code> 的节点，并返回 <strong>新的头节点</strong> 。

<p><strong>示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/03/06/removelinked-list.jpg" style="width: 500px; height: 142px;" />
<pre>
<strong>输入：</strong>head = [1,2,6,3,4,5,6], val = 6
<strong>输出：</strong>[1,2,3,4,5]
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>head = [], val = 1
<strong>输出：</strong>[]
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>head = [7,7,7,7], val = 7
<strong>输出：</strong>[]
</pre>

<p><strong>提示：</strong></p>

<ul>
	<li>列表中的节点数目在范围 <code>[0, 10<sup>4</sup>]</code> 内</li>
	<li><code>1 <= Node.val <= 50</code></li>
	<li><code>0 <= val <= 50</code></li>
</ul>


## 解题思路

先创建虚拟头结点指向原链表，避免删除头节点时特殊判断。
遍历时检查当前节点的下一个节点，若值等于 `val` 就摘链并释放。
否则指针后移，直到链表末尾，最后返回 `dummyHead->next`。
- 时间复杂度: $O(n)$
- 空间复杂度: $O(1)$

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
    ListNode* removeElements(ListNode* head, int val) {
        // 虚拟头结点
        ListNode* dummyHead = new ListNode(0);
        dummyHead->next = head;
        ListNode* p = dummyHead;
        while (p->next != nullptr){
            if(p->next->val == val){
                ListNode* tmp = p->next;
                p->next = tmp->next;
                delete tmp;
            }
            else{
                p = p->next;
            }
        }
        head = dummyHead->next;
        delete dummyHead;
        return head;

        
    }
};
```
