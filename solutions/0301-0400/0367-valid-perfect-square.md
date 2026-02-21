---
id: 367
title: Valid Perfect Square
difficulty: Easy
tags: [math, binary-search]
created: 2026-02-21
---

# 367. 有效的完全平方数

## 题目链接
https://leetcode.cn/problems/valid-perfect-square/

## 题目描述
<p>给你一个正整数 <code>num</code> 。如果 <code>num</code> 是一个完全平方数，则返回 <code>true</code> ，否则返回 <code>false</code> 。</p>

<p><strong>完全平方数</strong> 是一个可以写成某个整数的平方的整数。换句话说，它可以写成某个整数和自身的乘积。</p>

<p>不能使用任何内置的库函数，如&nbsp; <code>sqrt</code> 。</p>

<p><strong class="example">示例 1：</strong></p>

<pre>
<strong>输入：</strong>num = 16
<strong>输出：</strong>true
<strong>解释：</strong>返回 true ，因为 4 * 4 = 16 且 4 是一个整数。
</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<strong>输入：</strong>num = 14
<strong>输出：</strong>false
<strong>解释：</strong>返回 false ，因为 3.742 * 3.742 = 14 但 3.742 不是一个整数。
</pre>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= num &lt;= 2<sup>31</sup> - 1</code></li>
</ul>


## 解题思路

对区间 `[0, 46341]` 做二分查找，寻找是否存在 `mid * mid == num`。  
每次比较平方值与 `num`：小了就右移左边界，大了就左移右边界。  
乘法使用 `long long` 防止中间结果溢出。  
- 时间复杂度: $O(\log n)$
- 空间复杂度: $O(1)$

## 代码
```cpp
class Solution {
public:
    bool isPerfectSquare(int num) {
        int left = 0;
        int right = 46341 ;
        if (num  == 1)
            return true;
        while (left < right){
            int middle = left + (right - left) / 2;
            long long power = middle * middle;
            if (power < num){
                left = middle + 1;
            }
            else if (power > num){
                right = middle;
            }
            else if (power == num) {
                return true;
            }
        }
        return false;
    }
};
```
