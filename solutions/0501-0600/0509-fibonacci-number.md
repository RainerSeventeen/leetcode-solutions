---
id: 509
title: Fibonacci Number
difficulty: Easy
tags: [recursion, memoization, math, dynamic-programming]
created: 2026-02-21
---

# 509. 斐波那契数

## 题目链接
https://leetcode.cn/problems/fibonacci-number/

## 题目描述
<p><strong>斐波那契数</strong>&nbsp;（通常用&nbsp;<code>F(n)</code> 表示）形成的序列称为 <strong>斐波那契数列</strong> 。该数列由&nbsp;<code>0</code> 和 <code>1</code> 开始，后面的每一项数字都是前面两项数字的和。也就是：</p>

<pre>
F(0) = 0，F(1)&nbsp;= 1
F(n) = F(n - 1) + F(n - 2)，其中 n &gt; 1
</pre>

<p>给定&nbsp;<code>n</code> ，请计算 <code>F(n)</code> 。</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>n = 2
<strong>输出：</strong>1
<strong>解释：</strong>F(2) = F(1) + F(0) = 1 + 0 = 1
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>n = 3
<strong>输出：</strong>2
<strong>解释：</strong>F(3) = F(2) + F(1) = 1 + 1 = 2
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>n = 4
<strong>输出：</strong>3
<strong>解释：</strong>F(4) = F(3) + F(2) = 2 + 1 = 3
</pre>

<p><strong>提示：</strong></p>

<ul>
	<li><code>0 &lt;= n &lt;= 30</code></li>
</ul>


## 解题思路

- 使用滚动数组保存最近两个斐波那契值，避免维护完整 DP 数组。
- 从小到大迭代更新，当前值等于前两项之和，最终返回第 `n` 项。

- 时间复杂度: $O(n)$

- 空间复杂度: $O(1)$

## 代码
```cpp
class Solution {
public:
    int fib(int n) {
        // dp 数组只使用3个数也行
        if (n == 0) return 0;
        if (n <= 2) return 1;
        vector<int> dp;
        dp.resize(2);
        // 初始化
        dp[0] = 1;
        dp[1] = 1;
        // 滚动数组，一个个循环切换
        for (int i = 2; i < n; i++) {
            int target = dp[0] + dp[1];
            dp[1] = dp[0];
            dp[0] = target;
        }
        return dp[0];
    }
};
```
