---
id: 3852
title: Smallest Pair With Different Frequencies
difficulty: Easy
tags: []
created: 2026-03-01
---

# 3852. 不同频率的最小数对

## 题目链接
https://leetcode.cn/problems/smallest-pair-with-different-frequencies/

## 题目描述
<p>给你一个整数数组 <code>nums</code>。</p>

<p>从 <code>nums</code> 中找出两个 <strong>互不相同</strong> 的值 <code>x</code> 和 <code>y</code>，使得：</p>

<ul>
	<li><code>x &lt; y</code></li>
	<li><code>x</code> 和 <code>y</code> 在 <code>nums</code> 中的频率不同。</li>
</ul>

<p>在所有满足条件的数对中：</p>

<ul>
	<li>选择 <code>x</code> 的值尽可能小的数对。</li>
	<li>如果存在多个 <code>x</code> 相同的数对，选择 <code>y</code> 的值尽可能小的那个。</li>
</ul>

<p>返回一个整数数组 <code>[x, y]</code>。如果不存在有效的数对，返回 <code>[-1, -1]</code>。</p>

<p>一个值 <code>x</code> 的 <strong>频率</strong> 是指它在数组中出现的次数。</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">nums = [1,1,2,2,3,4]</span></p>

<p><strong>输出：</strong> <span class="example-io">[1,3]</span></p>

<p><strong>解释：</strong></p>

<p>最小的值是 1，频率为 2。比 1 大且频率与 1 不同的最小值是 3，其频率为 1。因此，答案是 <code>[1, 3]</code>。</p>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">nums = [1,5]</span></p>

<p><strong>输出：</strong> <span class="example-io">[-1,-1]</span></p>

<p><strong>解释：</strong></p>

<p>两个值的频率相同，因此不存在有效的数对。返回 <code>[-1, -1]</code>。</p>
</div>

<p><strong class="example">示例 3：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">nums = [7]</span></p>

<p><strong>输出：</strong> <span class="example-io">[-1,-1]</span></p>

<p><strong>解释：</strong></p>

<p>数组中只有一个值，因此不存在有效的数对。返回 <code>[-1, -1]</code>。</p>
</div>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 100</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 100</code></li>
</ul>


## 解题思路

先统计每个值的出现次数，再按数值升序枚举左端点 `x`。  
对每个 `x`，从小到大找第一个频率与 `x` 不同的 `y`，立即返回 `[x, y]`。  
因为枚举顺序是按数值升序，所以首次命中的就是题目要求的字典序最小可行数对。

- 时间复杂度: $O(m^2)$，其中 $m$ 是不同数字的个数。
- 空间复杂度: $O(m)$，用于频率表和排序数组。

## 相关专题
- [常用数据结构](../../topics/common-data-structures.md)

## 代码
```python
from collections import defaultdict

class Solution:
    def minDistinctFreqPair(self, nums: list[int]) -> list[int]:
        # 哈希统计
        # 列表排序
        mp = defaultdict(int)
        for n in nums:
            mp[n] += 1

        lst = sorted(mp.items(), key= lambda kv: (kv[0], kv[1]))
        n = len(lst)
        first = 0
        for first in range(n):
            # first
            curr, fre = lst[first]
            for nxt in range(first, n):
                if lst[nxt][1] == fre:
                    continue
                else:
                    return [curr, lst[nxt][0]]
        else:
            return [-1, -1]
```
