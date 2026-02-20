---
id: 4
title: Median of Two Sorted Arrays
difficulty: Hard
tags: [array, binary-search, divide-and-conquer]
created: 2026-02-20
---

# 4. Median of Two Sorted Arrays

## 题目链接
https://leetcode.cn/problems/median-of-two-sorted-arrays/

## 题目描述
<p>给定两个大小分别为 <code>m</code> 和 <code>n</code> 的正序（从小到大）数组&nbsp;<code>nums1</code> 和&nbsp;<code>nums2</code>。请你找出并返回这两个正序数组的 <strong>中位数</strong> 。</p>

<p>算法的时间复杂度应该为 <code>O(log (m+n))</code> 。</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums1 = [1,3], nums2 = [2]
<strong>输出：</strong>2.00000
<strong>解释：</strong>合并数组 = [1,2,3] ，中位数 2
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums1 = [1,2], nums2 = [3,4]
<strong>输出：</strong>2.50000
<strong>解释：</strong>合并数组 = [1,2,3,4] ，中位数 (2 + 3) / 2 = 2.5
</pre>

<p><strong>提示：</strong></p>

<ul>
	<li><code>nums1.length == m</code></li>
	<li><code>nums2.length == n</code></li>
	<li><code>0 &lt;= m &lt;= 1000</code></li>
	<li><code>0 &lt;= n &lt;= 1000</code></li>
	<li><code>1 &lt;= m + n &lt;= 2000</code></li>
	<li><code>-10<sup>6</sup> &lt;= nums1[i], nums2[i] &lt;= 10<sup>6</sup></code></li>
</ul>



## 解题思路

二分答案不在“值域”，而在“切分位置”。设 `A` 为较短数组（长度 `m`），`B` 为较长数组（长度 `n`）。我们在 `A` 中二分切分点 `i`，从而让左半部分元素个数为：

`i + j = (m + n + 1) // 2`，其中 `j = half - i` 是 `B` 的切分点。

切分正确的充要条件是左右两侧有序不交叉：

- `A_left <= B_right`
- `B_left <= A_right`

其中 `A_left = A[i-1]`、`A_right = A[i]`（`i==0`/`i==m` 用 `-inf/+inf` 处理边界），`B` 同理。

若 `A_left > B_right`，说明 `i` 取大了，需要左移；否则右移。找到合法切分后：

- 若总长度为奇数，中位数为 `max(A_left, B_left)`；
- 若为偶数，中位数为 `(max(A_left, B_left) + min(A_right, B_right)) / 2`。

- 时间复杂度: $O(\log \min(m,n))$
- 空间复杂度: $O(1)$

## 代码
```python
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        if len(A) > len(B):
            A, B = B, A

        m, n = len(A), len(B)
        half = (m + n + 1) // 2

        low, high = 0, m
        while low <= high:
            i = (low + high) // 2
            j = half - i

            A_left  = A[i - 1] if i > 0 else float("-inf")
            A_right = A[i]     if i < m else float("inf")
            B_left  = B[j - 1] if j > 0 else float("-inf")
            B_right = B[j]     if j < n else float("inf")

            if A_left > B_right:
                high = i - 1
            elif B_left > A_right:
                low = i + 1
            else:
                left_max = max(A_left, B_left)
                if (m + n) % 2 == 1:
                    return float(left_max)
                right_min = min(A_right, B_right)
                return (left_max + right_min) / 2.0

        raise RuntimeError("unreachable")
```
