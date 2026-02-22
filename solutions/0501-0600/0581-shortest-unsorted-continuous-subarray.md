---
id: 581
title: Shortest Unsorted Continuous Subarray
difficulty: Medium
tags: [stack, greedy, array, two-pointers, sorting, monotonic-stack]
created: 2026-02-20
---

# 581. 最短无序连续子数组

## 题目链接
https://leetcode.cn/problems/shortest-unsorted-continuous-subarray/

## 题目描述
<p>给你一个整数数组 <code>nums</code> ，你需要找出一个 <strong>连续子数组</strong> ，如果对这个子数组进行升序排序，那么整个数组都会变为升序排序。</p>

<p>请你找出符合题意的 <strong>最短</strong> 子数组，并输出它的长度。</p>

<div class="original__bRMd">
<div>
<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [2,6,4,8,10,9,15]
<strong>输出：</strong>5
<strong>解释：</strong>你只需要对 [6, 4, 8, 10, 9] 进行升序排序，那么整个表都会变为升序排序。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,2,3,4]
<strong>输出：</strong>0
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>nums = [1]
<strong>输出：</strong>0
</pre>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 <= nums.length <= 10<sup>4</sup></code></li>
	<li><code>-10<sup>5</sup> <= nums[i] <= 10<sup>5</sup></code></li>
</ul>

<p><strong>进阶：</strong>你可以设计一个时间复杂度为 <code>O(n)</code> 的解决方案吗？</p>
</div>
</div>



## 解题思路

目标是找最短区间 `[l, r]`，只要把这一段排序，整个数组就有序。

用两次线性扫描直接确定边界（无需排序）：

1. **从左到右**维护当前最大值 `max_num`：
   - 若 `nums[i] >= max_num`，更新 `max_num`；
   - 否则说明 `nums[i]` 破坏了非降序（它应该出现在更靠左的位置），所以右边界 `r` 至少要扩展到 `i`。
2. **从右到左**维护当前最小值 `min_num`：
   - 若 `nums[j] <= min_num`，更新 `min_num`；
   - 否则说明 `nums[j]` 破坏了非降序（它应该出现在更靠右的位置），所以左边界 `l` 需要扩展到 `j`。

如果第一次扫描后 `r == -1`，说明数组本身已经有序，答案为 0；否则返回 `r - l + 1`。

直观理解：最终 `[l, r]` 覆盖了所有“相对次序不对”的元素；把这一段排好序，外侧元素与区间边界也会自动对齐。

- 时间复杂度: $O(n)$
- 空间复杂度: $O(1)$

## 相关专题
- [贪心与思维](../../topics/greedy-and-thinking.md)

## 代码
```python
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, -1
        max_num = float('-inf')
        min_num = float('inf')
        for i in range(n):
            if nums[i] >= max_num: # 递增允许
                max_num = nums[i]
            else:
                r = i   # 破坏递增了
        if r == -1:
            return 0 # 有序
        for j in range(n - 1, -1, -1):
            if nums[j] <= min_num:
                min_num = nums[j]
            else:
                l = j
        return r - l + 1
```
