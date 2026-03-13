---
id: 3296
title: Minimum Number of Seconds to Make Mountain Height Zero
difficulty: Medium
tags: [greedy, array, math, binary-search, heap-priority-queue]
created: 2026-03-13
---

# 3296. 移山所需的最少秒数

## 题目链接
https://leetcode.cn/problems/minimum-number-of-seconds-to-make-mountain-height-zero/

## 题目描述
<p>给你一个整数 <code>mountainHeight</code> 表示山的高度。</p>

<p>同时给你一个整数数组 <code>workerTimes</code>，表示工人们的工作时间（单位：<strong>秒</strong>）。</p>

<p>工人们需要 <strong>同时 </strong>进行工作以 <strong>降低 </strong>山的高度。对于工人 <code>i</code> :</p>

<ul>
	<li>山的高度降低 <code>x</code>，需要花费 <code>workerTimes[i] + workerTimes[i] * 2 + ... + workerTimes[i] * x</code> 秒。例如：

	<ul>
		<li>山的高度降低 1，需要 <code>workerTimes[i]</code> 秒。</li>
		<li>山的高度降低 2，需要 <code>workerTimes[i] + workerTimes[i] * 2</code> 秒，依此类推。</li>
	</ul>
	</li>
</ul>

<p>返回一个整数，表示工人们使山的高度降低到 0 所需的 <strong>最少</strong> 秒数。</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">mountainHeight = 4, workerTimes = [2,1,1]</span></p>

<p><strong>输出：</strong> <span class="example-io">3</span></p>

<p><strong>解释：</strong></p>

<p>将山的高度降低到 0 的一种方式是：</p>

<ul>
	<li>工人 0 将高度降低 1，花费 <code>workerTimes[0] = 2</code> 秒。</li>
	<li>工人 1 将高度降低 2，花费 <code>workerTimes[1] + workerTimes[1] * 2 = 3</code> 秒。</li>
	<li>工人 2 将高度降低 1，花费 <code>workerTimes[2] = 1</code> 秒。</li>
</ul>

<p>因为工人同时工作，所需的最少时间为 <code>max(2, 3, 1) = 3</code> 秒。</p>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">mountainHeight = 10, workerTimes = [3,2,2,4]</span></p>

<p><strong>输出：</strong> <span class="example-io">12</span></p>

<p><strong>解释：</strong></p>

<ul>
	<li>工人 0 将高度降低 2，花费 <code>workerTimes[0] + workerTimes[0] * 2 = 9</code> 秒。</li>
	<li>工人 1 将高度降低 3，花费 <code>workerTimes[1] + workerTimes[1] * 2 + workerTimes[1] * 3 = 12</code> 秒。</li>
	<li>工人 2 将高度降低 3，花费 <code>workerTimes[2] + workerTimes[2] * 2 + workerTimes[2] * 3 = 12</code> 秒。</li>
	<li>工人 3 将高度降低 2，花费 <code>workerTimes[3] + workerTimes[3] * 2 = 12</code> 秒。</li>
</ul>

<p>所需的最少时间为 <code>max(9, 12, 12, 12) = 12</code> 秒。</p>
</div>

<p><strong class="example">示例 3：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">mountainHeight = 5, workerTimes = [1]</span></p>

<p><strong>输出：</strong> <span class="example-io">15</span></p>

<p><strong>解释：</strong></p>

<p>这个示例中只有一个工人，所以答案是 <code>workerTimes[0] + workerTimes[0] * 2 + workerTimes[0] * 3 + workerTimes[0] * 4 + workerTimes[0] * 5 = 15</code> 秒。</p>
</div>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= mountainHeight &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= workerTimes.length &lt;= 10<sup>4</sup></code></li>
	<li><code>1 &lt;= workerTimes[i] &lt;= 10<sup>6</sup></code></li>
</ul>


## 解题思路

- 先用 `2 * workerTimes[i]` 等差级数推导出每个工人在 `time` 内最多能降低的高度，`can_finish(time)` 累加所有工人的贡献并与 `mountainHeight` 比较。
- 把时间视作答案空间，在 `1` 到 `max(workerTimes) * mountainHeight * (mountainHeight + 1) // 2` 闭区间内用二分答案模板找到最小满足 `can_finish` 的 `time`。
- 时间复杂度: $O(n \log(\max(workerTimes) \cdot mountainHeight^2))$，其中 $n = len(workerTimes)$。
- 空间复杂度: $O(1)$。

## 相关专题
- [二分算法](../../topics/binary-search.md)

## 代码
```python
from math import isqrt
from typing import List


def binary_search_min(left: int, right: int, check) -> int:
    while left < right:
        mid = (left + right) // 2
        if check(mid):
            right = mid
        else:
            left = mid + 1
    return left


class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        max_time = max(workerTimes) * mountainHeight * (mountainHeight + 1) // 2

        def can_finish(time: int) -> bool:
            total = 0
            for w in workerTimes:
                work = time // w
                k = int(-1 + isqrt(1 + 8 * work)) // 2
                total += k
            return total >= mountainHeight

        return binary_search_min(1, max_time, can_finish)
```
- [常用数据结构](../../topics/common-data-structures.md)
