---
id: 55
title: Jump Game
difficulty: Medium
tags: [greedy, array]
created: 2026-02-20
---

# 55. 跳跃游戏

## 题目链接
https://leetcode.cn/problems/jump-game/

## 题目描述
<p>给你一个整数数组 <code>nums</code> ，你需要找到一个 <strong>非空</strong> 子数组，其和为最大，请你返回最大和。</p>

<p><strong>子数组 </strong>是数组中的一个连续部分。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [-2,1,-3,4,-1,2,1,-5,4]
<strong>输出：</strong>6
<strong>解释：</strong>连续子数组 [4,-1,2,1] 的和最大，为 6 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [5,4,-1,7,8]
<strong>输出：</strong>23
<strong>解释：</strong>连续子数组 [5,4,-1,7,8] 的和最大，为 23 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>-10<sup>4</sup> &lt;= nums[i] &lt;= 10<sup>4</sup></code></li>
</ul>

<p>&nbsp;</p>

<p><strong>进阶：</strong>如果你已经实现复杂度为 <code>O(n)</code> 的解法，尝试使用更为精妙的 <strong>分治</strong> 法求解。</p>

## 解题思路

贪心维护“当前能到达的最远下标”。

设 `far` 表示在扫描到当前位置 `i` 之前（包含 `i`），从起点出发**能到达的最远位置**。遍历数组：

- 若出现 `i > far`，说明当前位置都到不了，更不可能继续向后，直接返回 `False`。
- 否则可以从 `i` 起跳到 `i + nums[i]`，更新 `far = max(far, i + nums[i])`。
- 一旦 `far >= n - 1`，说明已经覆盖到终点，返回 `True`。

不变量：

- 遍历过程中始终有：所有 `<= far` 的位置都是可达的；`far` 是这些可达位置能扩展出的最大覆盖范围。

边界：

- `n <= 1` 时无需跳跃，直接可达。

- 时间复杂度: $O(n)$
- 空间复杂度: $O(1)$

## 相关专题
- [贪心与思维](../../topics/greedy-and-thinking.md)

## 代码
```python
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        i, far = 0, 0
        n = len(nums)
        while i <= far and i < n:
            far = max(far, i + nums[i])
            i += 1
        return i == n
```
