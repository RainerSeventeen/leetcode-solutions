---
id: 69
title: Sqrt(x)
difficulty: Easy
tags: [math, binary-search]
created: 2026-02-21
---

# 69. x 的平方根 

## 题目链接
https://leetcode.cn/problems/sqrtx/

## 题目描述
<p>给你一个非负整数 <code>x</code> ，计算并返回&nbsp;<code>x</code>&nbsp;的 <strong>算术平方根</strong> 。</p>

<p>由于返回类型是整数，结果只保留 <strong>整数部分 </strong>，小数部分将被 <strong>舍去 。</strong></p>

<p><strong>注意：</strong>不允许使用任何内置指数函数和算符，例如 <code>pow(x, 0.5)</code> 或者 <code>x ** 0.5</code> 。</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>x = 4
<strong>输出：</strong>2
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>x = 8
<strong>输出：</strong>2
<strong>解释：</strong>8 的算术平方根是 2.82842..., 由于返回类型是整数，小数部分将被舍去。
</pre>

<p><strong>提示：</strong></p>

<ul>
	<li><code>0 &lt;= x &lt;= 2<sup>31</sup> - 1</code></li>
</ul>


## 解题思路

本题求的是平方根的整数部分，可转化为“找最大的 `mid` 使 `mid^2 <= x`”。  
在 `[0, 46340]` 上二分，若 `mid^2 <= x` 就记录答案并继续向右找更大的可行值。  
若 `mid^2 > x` 则收缩右边界；最终记录的 `ans` 即为结果。  
- 时间复杂度: $O(\log x)$
- 空间复杂度: $O(1)$

## 代码
```cpp
class Solution {
public:
    int mySqrt(int x) {
        // 建立一个2000的数组
        int left = 0;
        int right = 46340;
        int ans = -1;
        while (left <= right){
            int middle = left + (right - left) / 2;
            long long power = middle * middle;
            if (power <= x){
                left = middle + 1;
                ans = middle;
            }
            else{
                right = middle -1;
            }
        }
        return ans;
    }
};
```
