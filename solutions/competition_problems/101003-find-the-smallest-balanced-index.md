---
id: 101003
title: Find the Smallest Balanced Index
difficulty: Medium
tags: []
created: 2026-03-08
---

# 101003. 找出最小平衡下标

## 题目链接
https://leetcode.cn/problems/find-the-smallest-balanced-index/

## 题目描述
<p>给你一个整数数组 <code>nums</code>。</p>

<p>如果某个下标&nbsp;<code>i</code> 满足以下条件，则称其为 <strong>平衡下标</strong>：&nbsp;<code>i</code> 左侧所有元素的总和等于 <code>i</code> 右侧所有元素的乘积。</p>

<p>如果左侧没有元素，则总和视为 0。同样，如果右侧没有元素，则乘积视为 1。</p>

<p>要求返回最小的 <strong>平衡下标</strong>，如果不存在平衡下标，则返回 -1。</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">nums = [2,1,2]</span></p>

<p><strong>输出：</strong> <span class="example-io">1</span></p>

<p><strong>解释：</strong></p>

<p>对于下标&nbsp;<code>i = 1</code>：</p>

<ul>
	<li>左侧总和 = <code>nums[0] = 2</code></li>
	<li>右侧乘积 = <code>nums[2] = 2</code></li>
	<li>由于左侧总和等于右侧乘积，下标 1 是平衡下标。</li>
</ul>

<p>没有更小的下标满足条件，因此答案是 1。</p>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">nums = [2,8,2,2,5]</span></p>

<p><strong>输出：</strong> <span class="example-io">2</span></p>

<p><strong>解释：</strong></p>

<p>对于下标&nbsp;<code>i = 2</code>：</p>

<ul>
	<li>左侧总和 = <code>2 + 8 = 10</code></li>
	<li>右侧乘积 = <code>2 * 5 = 10</code></li>
	<li>由于左侧总和等于右侧乘积，下标&nbsp;2 是平衡下标。</li>
</ul>

<p>没有更小的下标满足条件，因此答案是 2。</p>
</div>

<p><strong class="example">示例 3：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">nums = [1]</span></p>

<p><strong>输出：</strong> <span class="example-io">-1</span></p>

<p>对于下标&nbsp;<code>i = 0</code>：</p>

<ul>
	<li>左侧为空，因此左侧总和为 0。</li>
	<li>右侧为空，因此右侧乘积为 1。</li>
	<li>由于左侧总和不等于右侧乘积，下标&nbsp;0 不是平衡下标。</li>
</ul>

<p>因此，不存在平衡下标，答案是 -1。</p>
</div>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
</ul>


## 解题思路

枚举平衡下标时，左边是前缀和，右边是后缀乘积。

先预处理：

- `pre_sum[i]` 表示 `i` 左侧元素之和。
- `after_times[i]` 表示 `i` 右侧元素之积。

由于 `nums[i] >= 1`，从右往左看时，后缀乘积只会不减。题目中的左侧和最多是 `10^5 * 10^9 = 10^14`，所以一旦某个后缀乘积已经超过 `10^14`，更左边的后缀乘积只会更大，不可能再和任何左侧和相等，可以直接停止。

然后从右往左枚举下标：

- 如果右侧乘积等于左侧和，就更新答案。
- 如果右侧乘积已经大于左侧和，那么更左边的右侧乘积只会更大、左侧和只会更小，也可以直接停止。

这样就能在线性时间内找到最小平衡下标。

- 时间复杂度: $O(n)$。

- 空间复杂度: $O(n)$，用于保存前缀和与后缀乘积数组。

## 代码
```python
class Solution:
    def smallestBalancedIndex(self, nums: list[int]) -> int:
        # 求和可以算，乘积要截断
        times_mx = 10 ** 14
        # 计算前缀和
        n = len(nums)
        pre_sum = [0] * n
        for i in range(1, n):
            pre_sum[i] = nums[i - 1] + pre_sum[i - 1]
        # 计算后缀乘法，超过阈值直接 inf
        after_times = [inf] * n
        after_times[n - 1] = 1
        for i in range(n - 2, -1, -1):
            after_times[i] = after_times[i + 1] * nums[i + 1]
            if after_times[i] > times_mx:
                break # 超了直接退出, 左边是不可能的下标了
        # 从右边向左找，乘积越来越大，加法越来越小
        mn_idx = inf
        for i in range(n - 1, -1, -1):
            if after_times[i] > times_mx:   # 只会越来越大，已经超出了
                break
            if after_times[i] == pre_sum[i]:
                mn_idx = min(mn_idx, i)
            elif after_times[i] > pre_sum[i]:
                break

        return -1 if mn_idx == inf else mn_idx
```
