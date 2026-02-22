---
id: 718
title: Maximum Length of Repeated Subarray
difficulty: Medium
tags: [array, binary-search, dynamic-programming, sliding-window, hash-function, rolling-hash]
created: 2026-02-20
---

# 718. 最长重复子数组

## 题目链接
https://leetcode.cn/problems/maximum-length-of-repeated-subarray/

## 题目描述
<p>给两个整数数组&nbsp;<code>nums1</code>&nbsp;和&nbsp;<code>nums2</code>&nbsp;，返回 <em>两个数组中 <strong>公共的</strong> 、长度最长的子数组的长度&nbsp;</em>。</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums1 = [1,2,3,2,1], nums2 = [3,2,1,4,7]
<strong>输出：</strong>3
<strong>解释：</strong>长度最长的公共子数组是 [3,2,1] 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums1 = [0,0,0,0,0], nums2 = [0,0,0,0,0]
<strong>输出：</strong>5
</pre>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums1.length, nums2.length &lt;= 1000</code></li>
	<li><code>0 &lt;= nums1[i], nums2[i] &lt;= 100</code></li>
</ul>


## 解题思路

定义 `dp[i][j]` 为：

- `nums1` 前 `i` 个元素与 `nums2` 前 `j` 个元素中，
- 以 `nums1[i-1]`、`nums2[j-1]` 结尾的最长公共子数组长度。

若 `nums1[i-1] == nums2[j-1]`，则 `dp[i][j] = dp[i-1][j-1] + 1`，否则为 `0`。
遍历过程中维护最大值。

- 时间复杂度: $O(nm)$
- 空间复杂度: $O(nm)$

## 相关专题
- [动态规划](../../topics/dynamic-programming.md)

## 代码
```python
class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        n, m = len(nums1), len(nums2)
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        ans = 0
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if nums1[i - 1] == nums2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    ans = max(ans, dp[i][j])
        return ans
```
