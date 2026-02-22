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

<p>给你一个整数数组 <code>nums</code> 和一个整数 <code>k</code> ，请你返回其中出现频率前 <code>k</code> 高的元素。你可以按 <strong>任意顺序</strong> 返回答案。</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>nums = [1,1,1,2,2,3], k = 2</span></p>

<p><strong>输出：</strong><span class="example-io">[1,2]</span></p>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>nums = [1], k = 1</span></p>

<p><span class="example-io"><b>输出：</b>[1]</span></p>
</div>

<p><strong class="example">示例 3：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>nums = [1,2,1,2,1,2,3,1,3,2], k = 2</span></p>

<p><strong>输出：</strong><span class="example-io">[1,2]</span></p>
</div>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>-10<sup>4</sup>&nbsp;&lt;= nums[i] &lt;= 10<sup>4</sup></code></li>
	<li><code>k</code> 的取值范围是 <code>[1, 数组中不相同的元素的个数]</code></li>
	<li>题目数据保证答案唯一，换句话说，数组中前 <code>k</code> 个高频元素的集合是唯一的</li>
</ul>

<p><strong>进阶：</strong>你所设计算法的时间复杂度 <strong>必须</strong> 优于 <code>O(n log n)</code> ，其中 <code>n</code><em>&nbsp;</em>是数组大小。</p>

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

## 相关专题
- [常用数据结构](../../topics/common-data-structures.md)

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
