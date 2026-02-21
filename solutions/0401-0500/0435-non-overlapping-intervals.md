---
id: 435
title: Non-overlapping Intervals
difficulty: Medium
tags: [greedy, array, dynamic-programming, sorting]
created: 2026-02-21
---

# 435. 无重叠区间

## 题目链接
https://leetcode.cn/problems/non-overlapping-intervals/

## 题目描述
<p>给定一个区间的集合&nbsp;<code>intervals</code>&nbsp;，其中 <code>intervals[i] = [start<sub>i</sub>, end<sub>i</sub>]</code>&nbsp;。返回 <em>需要移除区间的最小数量，使剩余区间互不重叠&nbsp;</em>。</p>

<p><strong>注意</strong>&nbsp;只在一点上接触的区间是&nbsp;<strong>不重叠的</strong>。例如&nbsp;<code>[1, 2]</code>&nbsp;和&nbsp;<code>[2, 3]</code>&nbsp;是不重叠的。</p>

<p><strong>示例 1:</strong></p>

<pre>
<strong>输入:</strong> intervals = [[1,2],[2,3],[3,4],[1,3]]
<strong>输出:</strong> 1
<strong>解释:</strong> 移除 [1,3] 后，剩下的区间没有重叠。
</pre>

<p><strong>示例 2:</strong></p>

<pre>
<strong>输入:</strong> intervals = [ [1,2], [1,2], [1,2] ]
<strong>输出:</strong> 2
<strong>解释:</strong> 你需要移除两个 [1,2] 来使剩下的区间没有重叠。
</pre>

<p><strong>示例 3:</strong></p>

<pre>
<strong>输入:</strong> intervals = [ [1,2], [2,3] ]
<strong>输出:</strong> 0
<strong>解释:</strong> 你不需要移除任何区间，因为它们已经是无重叠的了。
</pre>

<p><strong>提示:</strong></p>

<ul>
	<li><code>1 &lt;= intervals.length &lt;= 10<sup>5</sup></code></li>
	<li><code>intervals[i].length == 2</code></li>
	<li><code>-5 * 10<sup>4</sup>&nbsp;&lt;= start<sub>i</sub>&nbsp;&lt; end<sub>i</sub>&nbsp;&lt;= 5 * 10<sup>4</sup></code></li>
</ul>


## 解题思路

- 先按区间左端点升序排序，再线性扫描判断是否重叠。
- 若重叠就删除一个并保留右端点更小的区间，以便给后续区间留出更多空间。

- 时间复杂度: $O(n \log n)$

- 空间复杂度: $O(\log n)$

## 代码
```cpp
class Solution {
public:
    static bool cmp(vector<int>& a, vector<int>& b){
        return a[0] < b[0];
    }
    
    int eraseOverlapIntervals(vector<vector<int>>& intervals) {
        // 用总数量，减去重叠的区间数量即可得到最优解
        sort(intervals.begin(), intervals.end(), cmp);
        int right = intervals[0][0];
        int count = 0;
        for (int i = 0; i < intervals.size(); i++) {
            if (intervals[i][0] < right) {
                count++;
                right = min(right, intervals[i][1]);
            } else {
                right = intervals[i][1];
            }
        }
        return count;
    }
};
```
