---
id: 338
title: 比特位计数
difficulty: Medium
tags: [bit-manipulation, dynamic-programming]
created: 2026-02-20
---

# 338. 比特位计数

## 题目链接
https://leetcode.cn/problems/counting-bits/

## 题目描述
暂无（需要从LeetCode获取）

## 解题思路
要计算 `0..n` 每个数的二进制 `1` 的个数（popcount），可以用 DP 复用已算结果。

关键观察：`i >> 1` 相当于去掉 `i` 的最低位，因此：

- `bits(i) = bits(i >> 1) + (i & 1)`

其中 `(i & 1)` 表示最低位是否为 `1`。按从小到大填表即可。

边界：`dp[0] = 0`。

- 时间复杂度: $O(n)$
- 空间复杂度: $O(n)$

## 代码
```python
class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n + 1)
        for num in range(1, n + 1):
            dp[num] = dp[num >> 1] + (num & 1) 
        return dp
```
