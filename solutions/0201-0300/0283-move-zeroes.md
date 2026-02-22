---
id: 283
title: 移动零
difficulty: Medium
tags: [array, two-pointers]
created: 2026-02-20
---

# 283. 移动零

## 题目链接
https://leetcode.cn/problems/move-zeroes/

## 题目描述

<p>给定一个数组 <code>nums</code>，编写一个函数将所有 <code>0</code> 移动到数组的末尾，同时保持非零元素的相对顺序。</p>

<p><strong>请注意</strong>&nbsp;，必须在不复制数组的情况下原地对数组进行操作。</p>

<p><strong>示例 1:</strong></p>

<pre>
<strong>输入:</strong> nums = <code>[0,1,0,3,12]</code>
<strong>输出:</strong> <code>[1,3,12,0,0]</code>
</pre>

<p><strong>示例 2:</strong></p>

<pre>
<strong>输入:</strong> nums = <code>[0]</code>
<strong>输出:</strong> <code>[0]</code></pre>

<p><strong>提示</strong>:</p>
<meta charset="UTF-8" />

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>4</sup></code></li>
	<li><code>-2<sup>31</sup>&nbsp;&lt;= nums[i] &lt;= 2<sup>31</sup>&nbsp;- 1</code></li>
</ul>

<p><b>进阶：</b>你能尽量减少完成的操作次数吗？</p>

## 解题思路
要求“原地”把所有 `0` 移到数组末尾，并且保持非零元素的相对顺序不变（稳定）。

用双指针做一次线性扫描即可：

- `fast` 从左到右遍历数组，负责“读”每个元素。
- `slow` 指向下一个应该放置“非零元素”的位置（也可以理解为当前已整理好的非零区间长度）。
- 当 `nums[fast] != 0` 时，把它写到 `nums[slow]`，并让 `slow += 1`。
- 扫描结束后，`[0, slow)` 都是按原相对顺序排列的非零元素；把 `[slow, n)` 全部填充为 `0` 即可。

边界情况：

- 全是 `0`：`slow` 始终为 `0`，最终整段填 `0` 不影响结果。
- 没有 `0`：`slow` 最终等于 `n`，第二段填充循环不会执行。

- 时间复杂度: $O(n)$
- 空间复杂度: $O(1)$

## 代码
```python
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        # 原地修改不返回， 把所有不是 0 的全部向前移动
        n = len(nums)
        slow = 0
        for fast in range(n):
            if nums[fast] != 0:
                nums[slow] = nums[fast]
                slow += 1
        while slow < n:
            nums[slow] = 0
            slow += 1
```
