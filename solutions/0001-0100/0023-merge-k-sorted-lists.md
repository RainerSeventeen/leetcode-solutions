---
id: 23
title: 合并 K 个升序链表
difficulty: Medium
tags: [linked-list, divide-and-conquer, heap-priority-queue, merge-sort]
created: 2026-02-20
---

# 23. 合并 K 个升序链表

## 题目链接
https://leetcode.cn/problems/merge-k-sorted-lists/

## 题目描述
暂无（需要从LeetCode获取）

## 解题思路
最小堆按“当前节点值”做 k 路归并。

- 初始化：把每条链表的头结点入堆；
- 循环：每次弹出堆顶最小节点接到结果链表尾部，再把该节点的 `next` 入堆；
- 直到堆为空，说明所有节点都已合并。

Python 的 `heapq` 不能直接比较 `ListNode`，因此入堆时用 `(val, uid, node)`：`uid` 是自增唯一编号，用来在 `val` 相等时打破比较关系。

堆的规模最多为 `k`，每个节点都会入堆/出堆一次。

- 时间复杂度: $O(N \log k)$
- 空间复杂度: $O(k)$

## 代码
```python
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        heapq.heapify(heap)
        uid = 0
        
        for node in lists:
            if node:
                uid += 1
                heapq.heappush(heap, (node.val, uid, node))
            
        dummy = ListNode()
        curr = dummy
        while heap: # 只要非空
            _, _, nd = heapq.heappop(heap)
            curr.next = nd
            curr = curr.next
            if nd.next is not None:
                uid += 1
                heapq.heappush(heap, (nd.next.val, uid, nd.next))
        return dummy.next
```
