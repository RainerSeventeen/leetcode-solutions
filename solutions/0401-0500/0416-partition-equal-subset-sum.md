---
id: 416
title: Partition Equal Subset Sum
difficulty: Medium
tags: [array, dynamic-programming]
created: 2026-02-20
---

# 416. 分割等和子集

## 题目链接
https://leetcode.cn/problems/partition-equal-subset-sum/

## 题目描述
<p>给你一个 <strong>只包含正整数 </strong>的 <strong>非空 </strong>数组 <code>nums</code> 。请你判断是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,5,11,5]
<strong>输出：</strong>true
<strong>解释：</strong>数组可以分割成 [1, 5, 5] 和 [11] 。</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,2,3,5]
<strong>输出：</strong>false
<strong>解释：</strong>数组不能分割成两个元素和相等的子集。
</pre>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 <= nums.length <= 200</code></li>
	<li><code>1 <= nums[i] <= 100</code></li>
</ul>


## 解题思路

把问题转成 0/1 背包：

- 若总和 `sum(nums)` 为奇数，无法平分，直接返回 `False`。
- 目标容量 `target = sum(nums) // 2`。
- `dp[j]` 表示：是否存在一个子集，其元素和**恰好为** `j`（布尔 DP）。

遍历每个数 `x`，容量从大到小更新：

`dp[j] |= dp[j - x]`

最终检查 `dp[target]` 是否为 `True`。

- 时间复杂度: $O(n * target)$
- 空间复杂度: $O(target)$

## 相关专题
- [动态规划](../../topics/dynamic-programming.md)

## 代码
```python
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        target = total // 2
        dp = [False] * (target + 1) # 是否存在一个子集，其元素和恰好为 j
        dp[0] = True    # 什么都不选就是 0，必定存在
        for num in nums:
            for j in range(target, num - 1, -1):
                dp[j] |= dp[j - num]
            if dp[target]:
                return True

        return dp[target]
```
