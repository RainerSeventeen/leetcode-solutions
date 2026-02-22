---
id: 494
title: Target Sum
difficulty: Medium
tags: [array, dynamic-programming, backtracking]
created: 2026-02-20
---

# 494. 目标和

## 题目链接
https://leetcode.cn/problems/target-sum/

## 题目描述
<p>给你一个非负整数数组 <code>nums</code> 和一个整数 <code>target</code> 。</p>

<p>向数组中的每个整数前添加&nbsp;<code>'+'</code> 或 <code>'-'</code> ，然后串联起所有整数，可以构造一个 <strong>表达式</strong> ：</p>

<ul>
	<li>例如，<code>nums = [2, 1]</code> ，可以在 <code>2</code> 之前添加 <code>'+'</code> ，在 <code>1</code> 之前添加 <code>'-'</code> ，然后串联起来得到表达式 <code>"+2-1"</code> 。</li>
</ul>

<p>返回可以通过上述方法构造的、运算结果等于 <code>target</code> 的不同 <strong>表达式</strong> 的数目。</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,1,1,1,1], target = 3
<strong>输出：</strong>5
<strong>解释：</strong>一共有 5 种方法让最终目标和为 3 。
-1 + 1 + 1 + 1 + 1 = 3
+1 - 1 + 1 + 1 + 1 = 3
+1 + 1 - 1 + 1 + 1 = 3
+1 + 1 + 1 - 1 + 1 = 3
+1 + 1 + 1 + 1 - 1 = 3
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [1], target = 1
<strong>输出：</strong>1
</pre>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 20</code></li>
	<li><code>0 &lt;= nums[i] &lt;= 1000</code></li>
	<li><code>0 &lt;= sum(nums[i]) &lt;= 1000</code></li>
	<li><code>-1000 &lt;= target &lt;= 1000</code></li>
</ul>


## 解题思路

设加正号的数之和为 `P`，减号部分之和为 `N`，有：

- `P - N = target`
- `P + N = sum(nums)`

得到 `P = (sum(nums) + target) / 2`。问题转成：从 `nums` 中选若干数，凑出和为 `P` 的方案数（0/1 背包计数）。

`dp[j]` 表示和为 `j` 的方案数，初始化 `dp[0] = 1`，倒序更新：

`dp[j] += dp[j - x]`

- 时间复杂度: $O(n * P)$
- 空间复杂度: $O(P)$

## 相关专题
- [动态规划](../../topics/dynamic-programming.md)

## 代码
```python
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        s = sum(nums)
        n = len(nums)
        if abs(target) > s or (s + target) % 2 != 0:
            return 0    # 无解的情况
        tar = (s + target) // 2 
        dp = [0] * (tar + 1) # 凑出和为 j 的可能的个数（零一背包）
        dp[0] = 1    # 初始化： 0 个数凑出 0 的个数都是 1（等价于第0轮的遍历结果）
        for num in nums:
            for j in range(tar, num - 1, -1): # 零一背包内层需要倒序
                    dp[j] += dp[j - num]
        return dp[tar]
```
