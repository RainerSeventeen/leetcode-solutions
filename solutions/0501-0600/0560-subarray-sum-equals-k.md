---
id: 560
title: 和为 K 的子数组
difficulty: Medium
tags: [array, hash-table, prefix-sum]
created: 2026-02-20
---

# 560. 和为 K 的子数组

## 题目链接
https://leetcode.cn/problems/subarray-sum-equals-k/

## 题目描述

<p>给你一个整数数组 <code>nums</code> 和一个整数&nbsp;<code>k</code> ，请你统计并返回 <em>该数组中和为&nbsp;<code>k</code><strong>&nbsp;</strong>的子数组的个数&nbsp;</em>。</p>

<p>子数组是数组中元素的连续非空序列。</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,1,1], k = 2
<strong>输出：</strong>2
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,2,3], k = 3
<strong>输出：</strong>2
</pre>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 2 * 10<sup>4</sup></code></li>
	<li><code>-1000 &lt;= nums[i] &lt;= 1000</code></li>
	<li><code>-10<sup>7</sup> &lt;= k &lt;= 10<sup>7</sup></code></li>
</ul>

## 解题思路
连续子数组和 = 前缀和的差，是该题的标准切入点（数组里可能有负数，因此无法用滑动窗口保证单调）。

定义前缀和 `pre[i] = nums[0] + ... + nums[i]`。若某段子数组 `(j+1..i)` 的和为 `k`，则：

`pre[i] - pre[j] = k`  ⇒  `pre[j] = pre[i] - k`

因此在遍历到当前位置的前缀和 `total` 时，只要知道此前出现过多少次 `total - k`，就能确定以当前位置结尾、和为 `k` 的子数组数量。

实现细节：

- 用哈希表 `count` 记录“某个前缀和出现的次数”。
- 初始化 `count[0] = 1`，表示空前缀（这样当 `total == k` 时能正确计数）。
- 逐个元素累加 `total`：
  - 累加答案：`ret += count[total - k]`
  - 再把当前前缀和入表：`count[total] += 1`

边界：`k` 可以为 0；数组元素可为负数/0 都不影响正确性。

- 时间复杂度: $O(n)$
- 空间复杂度: $O(n)$

## 代码
```python
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        total = 0
        count = defaultdict(int)
        count[0] = 1
        ret = 0
        for n in nums:
            total += n # 当前位置的前缀和
            ret += count[total -  k]    # 找已经遇到的更小的前缀和点
            count[total] += 1
        return ret
```
