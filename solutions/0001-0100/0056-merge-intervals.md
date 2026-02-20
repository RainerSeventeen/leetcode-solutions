---
id: 56
title: Merge Intervals
difficulty: Medium
tags: [array, sorting]
created: 2026-02-20
---

# 56. Merge Intervals

## 题目链接
https://leetcode.cn/problems/merge-intervals/

## 题目描述
<p>以数组 <code>intervals</code> 表示若干个区间的集合，其中单个区间为 <code>intervals[i] = [start<sub>i</sub>, end<sub>i</sub>]</code> 。请你合并所有重叠的区间，并返回&nbsp;<em>一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间</em>&nbsp;。</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>intervals = [[1,3],[2,6],[8,10],[15,18]]
<strong>输出：</strong>[[1,6],[8,10],[15,18]]
<strong>解释：</strong>区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
</pre>

<p><strong>示例&nbsp;2：</strong></p>

<pre>
<strong>输入：</strong>intervals = [[1,4],[4,5]]
<strong>输出：</strong>[[1,5]]
<strong>解释：</strong>区间 [1,4] 和 [4,5] 可被视为重叠区间。</pre>

<p><strong class="example">示例 3：</strong></p>

<pre>
<b>输入：</b>intervals = [[4,7],[1,4]]
<b>输出：</b>[[1,7]]
<b>解释：</b>区间 [1,4] 和 [4,7] 可被视为重叠区间。
</pre>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= intervals.length &lt;= 10<sup>4</sup></code></li>
	<li><code>intervals[i].length == 2</code></li>
	<li><code>0 &lt;= start<sub>i</sub> &lt;= end<sub>i</sub> &lt;= 10<sup>4</sup></code></li>
</ul>



## 解题思路

把区间按左端点升序排序后线性合并。

排序后有一个关键性质：如果当前合并后的区间是 `[cur_l, cur_r]`，下一个区间是 `[l, r]`：

- 若 `l > cur_r`：两者不相交，当前区间可以“定稿”加入答案，并开始新的 `[l, r]`。
- 若 `l <= cur_r`：两者相交/相邻（题目通常把相交定义为 `l <= cur_r`），可以合并为 `[cur_l, max(cur_r, r)]`。

不变量：

- `ans` 中的区间始终两两不重叠且按左端点有序；`cur` 始终表示“尚未写入 ans 的最后一个合并结果”。

边界：

- 输入为空直接返回空。
- 只有一个区间时无需合并。

复杂度说明：主要开销来自排序；合并本身只需一次线性扫描。

- 时间复杂度: $O(n\log n)$
- 空间复杂度: $O(1)$

## 代码
```python
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x : (x[0], x[1]))
        ret = []
        path = intervals[0].copy()
        for interval in intervals:
            # 可以扩展
            if interval[0] <= path[1]:
                path[1] = max(interval[1], path[1]) # 扩展右区间
            else: # 断开了
                ret.append(path.copy())
                path = interval.copy()
        if path:
            ret.append(path)
        return ret
```
