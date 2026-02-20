---
id: 84
title: Largest Rectangle in Histogram
difficulty: Hard
tags: [stack, array, monotonic-stack]
created: 2026-02-20
---

# 84. 柱状图中最大的矩形

## 题目链接
https://leetcode.cn/problems/largest-rectangle-in-histogram/

## 题目描述
<p>给定 <em>n</em> 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。</p>

<p>求在该柱状图中，能够勾勒出来的矩形的最大面积。</p>

<p><strong>示例 1:</strong></p>

<p><img src="https://assets.leetcode.com/uploads/2021/01/04/histogram.jpg" /></p>

<pre>
<strong>输入：</strong>heights = [2,1,5,6,2,3]
<strong>输出：</strong>10
<strong>解释：</strong>最大的矩形为图中红色区域，面积为 10
</pre>

<p><strong>示例 2：</strong></p>

<p><img src="https://assets.leetcode.com/uploads/2021/01/04/histogram-1.jpg" /></p>

<pre>
<strong>输入：</strong> heights = [2,4]
<b>输出：</b> 4</pre>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 <= heights.length <=10<sup>5</sup></code></li>
	<li><code>0 <= heights[i] <= 10<sup>4</sup></code></li>
</ul>


## 解题思路

把“每根柱子作为矩形最低高度”来计算最大面积。维护一个单调递增栈（存下标）。当遇到更矮的柱子时，持续弹栈：被弹出的柱子就是当前可结算的高度，当前下标是右边第一个更矮位置，新的栈顶是左边第一个更矮位置。

为了统一处理边界，可以在数组首尾补 `0` 作为哨兵，这样最后会自动清空栈并完成所有结算。

- 时间复杂度: $O(n)$

- 空间复杂度: $O(n)$

## 代码
```cpp
class Solution {
public:
    int largestRectangleArea(vector<int>& heights) {
        vector<int> h;
        h.reserve(heights.size() + 2);
        h.push_back(0);
        for (int x : heights) {
            h.push_back(x);
        }
        h.push_back(0);

        vector<int> stk;
        stk.reserve(h.size());
        int ans = 0;

        for (int i = 0; i < (int)h.size(); ++i) {
            while (!stk.empty() && h[i] < h[stk.back()]) {
                int mid = stk.back();
                stk.pop_back();
                int left = stk.back();
                int width = i - left - 1;
                ans = max(ans, h[mid] * width);
            }
            stk.push_back(i);
        }
        return ans;
    }
};
```
