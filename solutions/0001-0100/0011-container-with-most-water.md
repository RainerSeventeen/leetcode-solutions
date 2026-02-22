---
id: 11
title: Container With Most Water
difficulty: Medium
tags: [greedy, array, two-pointers]
created: 2026-02-20
---

# 11. 盛最多水的容器

## 题目链接
https://leetcode.cn/problems/container-with-most-water/

## 题目描述
<p>给定一个长度为 <code>n</code> 的整数数组&nbsp;<code>height</code>&nbsp;。有&nbsp;<code>n</code>&nbsp;条垂线，第 <code>i</code> 条线的两个端点是&nbsp;<code>(i, 0)</code>&nbsp;和&nbsp;<code>(i, height[i])</code>&nbsp;。</p>

<p>找出其中的两条线，使得它们与&nbsp;<code>x</code>&nbsp;轴共同构成的容器可以容纳最多的水。</p>

<p>返回容器可以储存的最大水量。</p>

<p><strong>说明：</strong>你不能倾斜容器。</p>

<p><strong>示例 1：</strong></p>

<p><img alt="" src="https://aliyun-lc-upload.oss-cn-hangzhou.aliyuncs.com/aliyun-lc-upload/uploads/2018/07/25/question_11.jpg" /></p>

<pre>
<strong>输入：</strong>[1,8,6,2,5,4,8,3,7]
<strong>输出：</strong>49 
<strong>解释：</strong>图中垂直线代表输入数组 [1,8,6,2,5,4,8,3,7]。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为&nbsp;49。</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>height = [1,1]
<strong>输出：</strong>1
</pre>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == height.length</code></li>
	<li><code>2 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= height[i] &lt;= 10<sup>4</sup></code></li>
</ul>



## 解题思路

双指针从两端向中间收缩。当前面积为 `(r - l) * min(height[l], height[r])`，决定高度的是较短的一侧。

当我们把宽度缩小 1 时，若移动较长的一侧，`min(height[l], height[r])` 不可能变大（短板没变），面积只会更小；因此每次都移动较短指针，才有机会通过“提高短板”来得到更大面积。

- 时间复杂度: $O(n)$
- 空间复杂度: $O(1)$

## 代码
```python
class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        l, r = 0, n - 1
        size = 0
        while l < r:
            if height[l] < height[r]:
                size = max(size, (r - l) * height[l])
                l += 1
            else:
                size = max(size, (r - l) * height[r])
                r -= 1
        return size
```
