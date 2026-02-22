---
id: 53
title: Maximum Subarray
difficulty: Medium
tags: [array, divide-and-conquer, dynamic-programming]
created: 2026-02-20
---

# 53. 最大子数组和

## 题目链接
https://leetcode.cn/problems/maximum-subarray/

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

经典的 Kadane 算法（动态规划/贪心一体）：

定义 `cur` 表示“**必须以当前位置结尾**的最大子数组和”，`ans` 表示全局最大值。

当遍历到 `x = nums[i]` 时，只有两种选择：

- 把 `x` 接到前面的最优尾部子数组后面：和为 `cur + x`
- 重新从 `x` 开始一个子数组：和为 `x`

因此状态转移为：`cur = max(x, cur + x)`，并用 `ans = max(ans, cur)` 更新答案。

不变量与边界：

- `cur` 始终代表“以 i 结尾”的最优值，所以更新 `ans` 时一定覆盖到所有可能的结尾位置。
- 如果数组全为负数，初始化 `cur = ans = nums[0]` 能保证答案是“最大的那个负数”，不会被错误地置为 0。

- 时间复杂度: $O(n)$
- 空间复杂度: $O(1)$

## 相关专题
- [动态规划](../../topics/dynamic-programming.md)

## 代码
```python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # 前缀和
        ret = float('-inf')
        curr = 0
        for n in nums:
            curr += n
            ret = max(ret, curr)
            if curr < 0:
                curr = 0
        return ret
```
