---
id: 347
title: 前 K 个高频元素
difficulty: Medium
tags: [array, hash-table, divide-and-conquer, bucket-sort, counting, quickselect, sorting, heap-priority-queue]
created: 2026-02-20
---

# 347. 前 K 个高频元素

## 题目链接
https://leetcode.cn/problems/top-k-frequent-elements/

## 题目描述
暂无（需要从LeetCode获取）

## 解题思路
先用哈希表统计每个元素出现次数，然后用大小为 `k` 的小顶堆维护当前“出现次数最多的 k 个元素”。

具体做法：

- `Counter(nums)` 得到 `freq[x]`。
- 遍历 `(x, cnt)`：
  - 若堆大小 `< k`，直接入堆 `(cnt, x)`；
  - 否则比较 `cnt` 与堆顶最小频次：
    - 若 `cnt` 更大，用 `heapreplace` 把堆顶替换掉；
    - 否则跳过。

这样堆里始终保存频次最大的 `k` 个元素（堆顶是这 `k` 个里频次最小的那个，便于淘汰）。

边界：`k == 1` 或 `k == len(去重元素数)` 都能自然覆盖；题目保证答案唯一或不要求顺序时，直接输出堆中元素即可。

- 时间复杂度: $O(n\\log k)$
- 空间复杂度: $O(n)$

## 代码
```python
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp = Counter(nums)
        heap = []
        for key, val in mp.items():
            if len(heap) < k:
                heapq.heappush(heap, (val, key))
            elif val > heap[0][0]:
                heapq.heapreplace(heap, (val, key))

        return [key for _, key in heap]
```
