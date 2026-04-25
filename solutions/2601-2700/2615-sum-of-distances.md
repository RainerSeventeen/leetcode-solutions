---
id: 2615
title: Sum of Distances
difficulty: Medium
tags: [array, hash-table, prefix-sum]
created: 2026-04-25
---

# 2615. 等值距离和

## 题目链接
https://leetcode.cn/problems/sum-of-distances/

## 题目描述
<p>给你一个下标从 <strong>0</strong> 开始的整数数组 <code>nums</code> 。现有一个长度等于 <code>nums.length</code> 的数组 <code>arr</code> 。对于满足 <code>nums[j] == nums[i]</code> 且 <code>j != i</code> 的所有 <code>j</code> ，<code>arr[i]</code> 等于所有 <code>|i - j|</code> 之和。如果不存在这样的 <code>j</code> ，则令 <code>arr[i]</code> 等于 <code>0</code> 。</p>

<p>返回数组<em> </em><code>arr</code><em> 。</em></p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,3,1,1,2]
<strong>输出：</strong>[5,0,3,4,0]
<strong>解释：</strong>
i = 0 ，nums[0] == nums[2] 且 nums[0] == nums[3] 。因此，arr[0] = |0 - 2| + |0 - 3| = 5 。 
i = 1 ，arr[1] = 0 因为不存在值等于 3 的其他下标。
i = 2 ，nums[2] == nums[0] 且 nums[2] == nums[3] 。因此，arr[2] = |2 - 0| + |2 - 3| = 3 。
i = 3 ，nums[3] == nums[0] 且 nums[3] == nums[2] 。因此，arr[3] = |3 - 0| + |3 - 2| = 4 。 
i = 4 ，arr[4] = 0 因为不存在值等于 2 的其他下标。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [0,5,3]
<strong>输出：</strong>[0,0,0]
<strong>解释：</strong>因为 nums 中的元素互不相同，对于所有 i ，都有 arr[i] = 0 。
</pre>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
</ul>


## 解题思路

先把相同数值出现的下标分组。对于同一组有序下标，预处理下标前缀和，枚举当前下标 `idx` 时，左侧距离和为 `j * idx - pre[j]`，右侧距离和为 `(pre[m] - pre[j + 1]) - (m - j - 1) * idx`，两部分相加就是答案。

- 时间复杂度: $O(n)$，其中 `n` 为 `nums` 长度。

- 空间复杂度: $O(n)$

## 相关专题

- [常用数据结构](../../topics/common-data-structures.md)

## 代码
```python
class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        pos = defaultdict(list)
        n = len(nums)

        # 记录每个值出现的所有下标
        for i, x in enumerate(nums):
            pos[x].append(i)

        ans = [0] * n

        for indexes in pos.values():
            m = len(indexes)
            if m == 1:
                continue

            # 下标前缀和
            pre = [0] * (m + 1)
            for i in range(m):
                pre[i + 1] = pre[i] + indexes[i]    # 下标位置前缀和

            for j, idx in enumerate(indexes):
                left = j * idx - pre[j]
                right = (pre[m] - pre[j + 1]) - (m - j - 1) * idx
                ans[idx] = left + right

        return ans
```
