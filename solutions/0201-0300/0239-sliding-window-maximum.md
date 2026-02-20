---
id: 239
title: 滑动窗口最大值
difficulty: Medium
tags: [queue, array, sliding-window, monotonic-queue, heap-priority-queue]
created: 2026-02-20
---

# 239. 滑动窗口最大值

## 题目链接
https://leetcode.cn/problems/sliding-window-maximum/

## 题目描述
暂无（需要从LeetCode获取）

## 解题思路
单调队列（deque）维护窗口最大值，做到线性时间。

队列里存**下标**（不是值），并保持对应的 `nums[idx]` **单调递减**，这样队首永远是当前窗口最大值的下标。

对每个位置 `r`（右端）：

1. 把队尾所有“比 `nums[r]` 小或相等”的下标弹出：它们在 `r` 存在的情况下永远不可能成为最大值（且会更早过期）。
2. 把 `r` 入队。
3. 维护窗口左端 `l = r - k + 1`：
   - 若队首下标 `< l`，说明已经滑出窗口，弹出队首。
4. 当 `r >= k - 1` 时，窗口形成，此时最大值为 `nums[deque[0]]`。

不变量：

- 队列下标严格递增（按时间入队），对应的值单调递减；因此队首最大且一定在窗口内（通过第 3 步保证）。

补充：也可用大顶堆（优先队列）+ 延迟删除，但复杂度为 $O(n\log k)$，单调队列更优。

- 时间复杂度: $O(n)$
- 空间复杂度: $O(k)$

说明：每个下标最多入队/出队一次，因此队列操作总次数为线性。

## 代码
```python
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        q = deque()  # 存下标，保证 nums[q] 单调递减（队首最大）

        for i in range(k):
            while q and nums[q[-1]] <= nums[i]:
                q.pop()          # 从队尾弹出更小/相等的
            q.append(i)
        ret = [nums[q[0]]]

        for i in range(k, n):
            if q and q[0] <= i - k:
                q.popleft() # 先移除过期（只可能在队首）
            while q and nums[q[-1]] <= nums[i]:
                q.pop() # 比当前值来的早，还比当前值小，没有任何维护的意义

            q.append(i)
            ret.append(nums[q[0]])

        return ret
```
