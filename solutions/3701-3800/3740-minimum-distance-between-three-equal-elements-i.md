---
id: 3740
title: Minimum Distance Between Three Equal Elements I
difficulty: Easy
tags: [array, hash-table]
created: 2026-04-10
---

# 3740. 三个相等元素之间的最小距离 I

## 题目链接
https://leetcode.cn/problems/minimum-distance-between-three-equal-elements-i/

## 题目描述
<p>给你一个整数数组 <code>nums</code>。</p>

<p>如果满足 <code>nums[i] == nums[j] == nums[k]</code>，且 <code>(i, j, k)</code> 是 3 个&nbsp;<strong>不同&nbsp;</strong>下标，那么三元组 <code>(i, j, k)</code> 被称为&nbsp;<strong>有效三元组&nbsp;</strong>。</p>

<p><strong>有效三元组&nbsp;</strong>的&nbsp;<strong>距离&nbsp;</strong>被定义为 <code>abs(i - j) + abs(j - k) + abs(k - i)</code>，其中 <code>abs(x)</code> 表示 <code>x</code> 的&nbsp;<strong>绝对值&nbsp;</strong>。</p>

<p>返回一个整数，表示 <strong>有效三元组&nbsp;</strong>的&nbsp;<strong>最小&nbsp;</strong>可能距离。如果不存在&nbsp;<strong>有效三元组&nbsp;</strong>，返回 <code>-1</code>。</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">nums = [1,2,1,1,3]</span></p>

<p><strong>输出：</strong> <span class="example-io">6</span></p>

<p><strong>解释：</strong></p>

<p>最小距离对应的有效三元组是&nbsp;<code>(0, 2, 3)</code>&nbsp;。</p>

<p><code>(0, 2, 3)</code> 是一个有效三元组，因为 <code>nums[0] == nums[2] == nums[3] == 1</code>。它的距离为 <code>abs(0 - 2) + abs(2 - 3) + abs(3 - 0) = 2 + 1 + 3 = 6</code>。</p>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">nums = [1,1,2,3,2,1,2]</span></p>

<p><strong>输出：</strong> <span class="example-io">8</span></p>

<p><strong>解释：</strong></p>

<p>最小距离对应的有效三元组是&nbsp;<code>(2, 4, 6)</code>&nbsp;。</p>

<p><code>(2, 4, 6)</code> 是一个有效三元组，因为 <code>nums[2] == nums[4] == nums[6] == 2</code>。它的距离为 <code>abs(2 - 4) + abs(4 - 6) + abs(6 - 2) = 2 + 2 + 4 = 8</code>。</p>
</div>

<p><strong class="example">示例 3：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">nums = [1]</span></p>

<p><strong>输出：</strong> <span class="example-io">-1</span></p>

<p><strong>解释：</strong></p>

<p>不存在有效三元组，因此答案为 -1。</p>
</div>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n == nums.length &lt;= 100</code></li>
	<li><code>1 &lt;= nums[i] &lt;= n</code></li>
</ul>


## 解题思路

- 先按数值分组记录每个元素出现的位置。
- 对于同一个数值，任意有效三元组按下标排序后，其距离等于最左和最右下标差的两倍。
- 所以只要扫描每个位置列表里的连续三个下标，维护最小的 `2 * (idxs[i+2] - idxs[i])` 就行。

- 时间复杂度: $O(n)$，其中 `n` 是数组长度。
- 空间复杂度: $O(n)$，用于保存各个数值对应的下标列表。

## 相关专题
- [常用数据结构](../../topics/common-data-structures.md)

## 代码
```python
class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        # 实际上是最左和最右距离的两倍
        cnt = defaultdict(list)
        for i, num in enumerate(nums):
            cnt[num].append(i)
        
        ans = inf
        for num, idxs in cnt.items():
            m = len(idxs)
            if m < 3:
                continue
            for i in range(0, m - 2):
                j = i + 2
                ans = min(ans, 2 * (idxs[j] - idxs[i]))
        return -1 if ans == inf else ans
```
