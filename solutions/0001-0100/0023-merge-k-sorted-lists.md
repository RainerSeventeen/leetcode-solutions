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

<p>给你一个链表数组，每个链表都已经按升序排列。</p>

<p>请你将所有链表合并到一个升序链表中，返回合并后的链表。</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>lists = [[1,4,5],[1,3,4],[2,6]]
<strong>输出：</strong>[1,1,2,3,4,4,5,6]
<strong>解释：</strong>链表数组如下：
[
  1-&gt;4-&gt;5,
  1-&gt;3-&gt;4,
  2-&gt;6
]
将它们合并到一个有序链表中得到。
1-&gt;1-&gt;2-&gt;3-&gt;4-&gt;4-&gt;5-&gt;6
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>lists = []
<strong>输出：</strong>[]
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>lists = [[]]
<strong>输出：</strong>[]
</pre>

<p><strong>提示：</strong></p>

<ul>
	<li><code>k == lists.length</code></li>
	<li><code>0 &lt;= k &lt;= 10^4</code></li>
	<li><code>0 &lt;= lists[i].length &lt;= 500</code></li>
	<li><code>-10^4 &lt;= lists[i][j] &lt;= 10^4</code></li>
	<li><code>lists[i]</code> 按 <strong>升序</strong> 排列</li>
	<li><code>lists[i].length</code> 的总和不超过 <code>10^4</code></li>
</ul>

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
