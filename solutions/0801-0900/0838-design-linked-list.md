---
id: 838
title: Design Linked List
difficulty: Medium
tags: [design, linked-list]
created: 2026-02-21
---

# 838. 设计链表

## 题目链接
https://leetcode.cn/problems/design-linked-list/

## 题目描述
<p>你可以选择使用单链表或者双链表，设计并实现自己的链表。</p>

<p>单链表中的节点应该具备两个属性：<code>val</code> 和 <code>next</code> 。<code>val</code> 是当前节点的值，<code>next</code> 是指向下一个节点的指针/引用。</p>

<p>如果是双向链表，则还需要属性&nbsp;<code>prev</code>&nbsp;以指示链表中的上一个节点。假设链表中的所有节点下标从 <strong>0</strong> 开始。</p>

<p>实现 <code>MyLinkedList</code> 类：</p>

<ul>
	<li><code>MyLinkedList()</code> 初始化 <code>MyLinkedList</code> 对象。</li>
	<li><code>int get(int index)</code> 获取链表中下标为 <code>index</code> 的节点的值。如果下标无效，则返回 <code>-1</code> 。</li>
	<li><code>void addAtHead(int val)</code> 将一个值为 <code>val</code> 的节点插入到链表中第一个元素之前。在插入完成后，新节点会成为链表的第一个节点。</li>
	<li><code>void addAtTail(int val)</code> 将一个值为 <code>val</code> 的节点追加到链表中作为链表的最后一个元素。</li>
	<li><code>void addAtIndex(int index, int val)</code> 将一个值为 <code>val</code> 的节点插入到链表中下标为 <code>index</code> 的节点之前。如果 <code>index</code> 等于链表的长度，那么该节点会被追加到链表的末尾。如果 <code>index</code> 比长度更大，该节点将 <strong>不会插入</strong> 到链表中。</li>
	<li><code>void deleteAtIndex(int index)</code> 如果下标有效，则删除链表中下标为 <code>index</code> 的节点。</li>
</ul>

<p><strong class="example">示例：</strong></p>

<pre>
<strong>输入</strong>
["MyLinkedList", "addAtHead", "addAtTail", "addAtIndex", "get", "deleteAtIndex", "get"]
[[], [1], [3], [1, 2], [1], [1], [1]]
<strong>输出</strong>
[null, null, null, null, 2, null, 3]

<strong>解释</strong>
MyLinkedList myLinkedList = new MyLinkedList();
myLinkedList.addAtHead(1);
myLinkedList.addAtTail(3);
myLinkedList.addAtIndex(1, 2);    // 链表变为 1-&gt;2-&gt;3
myLinkedList.get(1);              // 返回 2
myLinkedList.deleteAtIndex(1);    // 现在，链表变为 1-&gt;3
myLinkedList.get(1);              // 返回 3
</pre>

<p><strong>提示：</strong></p>

<ul>
	<li><code>0 &lt;= index, val &lt;= 1000</code></li>
	<li>请不要使用内置的 LinkedList 库。</li>
	<li>调用 <code>get</code>、<code>addAtHead</code>、<code>addAtTail</code>、<code>addAtIndex</code> 和 <code>deleteAtIndex</code> 的次数不超过 <code>2000</code> 。</li>
</ul>


## 解题思路

实现单链表并引入虚拟头结点，统一头部插入和删除的边界处理。
`get`、`addAtIndex`、`deleteAtIndex` 都通过遍历定位到目标位置前驱，再执行指针重连。
`addAtHead` 为头插，`addAtTail` 遍历到末尾追加。
- 时间复杂度: $O(n)$
- 空间复杂度: $O(n)$

## 代码
```cpp
class MyLinkedList {
    public:
        struct LinkNode {
            LinkNode* next;
            int val;
            LinkNode(int val): val(val), next(nullptr){};
        };
        LinkNode* head = nullptr;
        LinkNode* dummy;
    
        
        MyLinkedList() {
            dummy = new LinkNode(0); // 虚拟结点
            head = dummy->next; // 对外头结点
        }
        
        int get(int index) {
            LinkNode* cur = head;
            for (int i = 0; i < index; i++){
                // i = 0 代表头结点head
                if (cur->next != nullptr){
                    cur = cur->next; // cur指针的值被赋值为next
                }
                else{
                    return -1;
                }
            }
            if (cur == nullptr) // 空链表
                return -1;
            return cur->val;
        }
        
        void addAtHead(int val) {
            LinkNode* added = new LinkNode (val);
            added->next = head;
            dummy->next = added;
            head = added;
        }
        
        void addAtTail(int val) {
            LinkNode* cur = dummy;
            while (cur->next != nullptr){
                cur = cur->next;
            }
            LinkNode* added = new LinkNode(val);
            cur->next = added;
            if (head == nullptr)
                head = added;
        }
        
        void addAtIndex(int index, int val) {
            LinkNode* pre = dummy;
            LinkNode* cur = head;
            for (int i = 0; i < index; i++){
                // i = 0 代表头结点head
                if (cur == nullptr){
                    // 空链表且 index > 0
                    return;
                }
                else if (cur->next != nullptr){
                    pre = cur;
                    cur = cur->next; // cur指针的值被赋值为next
                }
                else if (i == index - 1 && cur->next == nullptr){
                    addAtTail(val);
                    return;
                    // 应该添加到末尾
                }
                else
                    return; // 没找到目标
            }
            LinkNode* added = new LinkNode(val);
            added->next = cur;
            pre->next = added;
            if (head == nullptr || index == 0)
                head = added;
        }
        
        void deleteAtIndex(int index) {
            if (index == 0){
                LinkNode* tmp = head;
                if (head != nullptr)
                    head = head->next;
                delete tmp;
                return;
            }
            LinkNode* pre = dummy;
            LinkNode* cur = head;
            for (int i = 0; i < index; i++){
                if (head == nullptr) // 空链表删除多余元素
                    return;
                // i = 0 代表头结点head
                else if (cur->next != nullptr){
                    pre = cur;
                    cur = cur->next; // cur指针的值被赋值为next
                }
                else 
                    return; // 没找到目标
            }
            pre->next = cur->next;
            delete cur;
        }
        
    
};

/**
 * Your MyLinkedList object will be instantiated and called as such:
 * MyLinkedList* obj = new MyLinkedList();
 * int param_1 = obj->get(index);
 * obj->addAtHead(val);
 * obj->addAtTail(val);
 * obj->addAtIndex(index,val);
 * obj->deleteAtIndex(index);
 */
```
