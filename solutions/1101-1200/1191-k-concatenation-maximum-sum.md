---
id: 1191
title: K-Concatenation Maximum Sum
difficulty: Medium
tags: [array, dynamic-programming]
created: 2026-03-04
---

# 1191. K 次串联后最大子数组之和

## 题目链接
https://leetcode.cn/problems/k-concatenation-maximum-sum/

## 题目描述
<p>给定一个整数数组&nbsp;<code>arr</code>&nbsp;和一个整数&nbsp;<code>k</code>&nbsp;，通过重复&nbsp;<code>k</code>&nbsp;次来修改数组。</p>

<p>例如，如果&nbsp;<code>arr = [1, 2]</code>&nbsp;，<meta charset="UTF-8" />&nbsp;<code>k = 3</code>&nbsp;，那么修改后的数组将是 <code>[1, 2, 1, 2, 1, 2]</code> 。</p>

<p>返回修改后的数组中的最大的子数组之和。注意，子数组长度可以是 <code>0</code>，在这种情况下它的总和也是 <code>0</code>。</p>

<p>由于&nbsp;<strong>结果可能会很大</strong>，需要返回的<meta charset="UTF-8" />&nbsp;<code>10<sup>9</sup>&nbsp;+ 7</code>&nbsp;的&nbsp;<strong>模</strong>&nbsp;。</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>arr = [1,2], k = 3
<strong>输出：</strong>9
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>arr = [1,-2,1], k = 5
<strong>输出：</strong>2
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>arr = [-1,-2], k = 7
<strong>输出：</strong>0
</pre>

<p><strong>提示：</strong></p>
<meta charset="UTF-8" />

<ul>
	<li><code>1 &lt;= arr.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= k &lt;= 10<sup>5</sup></code></li>
	<li><code>-10<sup>4</sup>&nbsp;&lt;= arr[i] &lt;= 10<sup>4</sup></code></li>
</ul>


## 解题思路

把问题分成两种情况：

1. `k = 1` 或 `k = 2` 时，直接在最多两段 `arr` 上做一次 Kadane，得到最大子数组和。
2. `k > 2` 时：
   - 若 `sum(arr) <= 0`，最优子数组不会因为多拼接而继续变大，答案仍是前两段内的最大子数组和。
   - 若 `sum(arr) > 0`，最优子数组会跨越中间完整数组，答案为“前两段的最大子数组和 + (k-2) * sum(arr)”。

这样只需遍历最多两次原数组即可。

- 时间复杂度: $O(n)$，其中 $n$ 是 `arr` 的长度。

- 空间复杂度: $O(1)$。

## 相关专题
- [动态规划](../../topics/dynamic-programming.md)

## 代码
```python
class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        # 最大前缀和减去最小前缀和，就是最大子数组的值
        # 数组总和 > 0 才能跨多个数组组成连缀，此时最小值一定在第一个，最大值在最后一个
        # k <= 2, 直接算
        MOD = 1_000_000_007
        cnt = 0
        mx = 0
        s = sum(arr)
        for _ in range(min(k, 2)):
            for n in arr: 
                cnt += n
                mx = max(mx, cnt)
                cnt = max(0, cnt)
        if k <= 2:
            return mx % MOD
        if s < 0:
            return mx % MOD
        else:
            return (mx + ((k - min(k, 2)) * s) % MOD)
```
