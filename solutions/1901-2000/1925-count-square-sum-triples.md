---
id: 1925
title: Count Square Sum Triples
difficulty: Easy
tags: [math, enumeration]
created: 2026-02-21
---

# 1925. 统计平方和三元组的数目

## 题目链接
https://leetcode.cn/problems/count-square-sum-triples/

## 题目描述
<p>一个 <strong>平方和三元组</strong> <code>(a,b,c)</code> 指的是满足 <code>a<sup>2</sup> + b<sup>2</sup> = c<sup>2</sup></code> 的 <strong>整数 </strong>三元组 <code>a</code>，<code>b</code> 和 <code>c</code> 。</p>

<p>给你一个整数 <code>n</code> ，请你返回满足<em> </em><code>1 &lt;= a, b, c &lt;= n</code> 的 <strong>平方和三元组</strong> 的数目。</p>

<p><strong>示例 1：</strong></p>

<pre><b>输入：</b>n = 5
<b>输出：</b>2
<b>解释：</b>平方和三元组为 (3,4,5) 和 (4,3,5) 。
</pre>

<p><strong>示例 2：</strong></p>

<pre><b>输入：</b>n = 10
<b>输出：</b>4
<b>解释：</b>平方和三元组为 (3,4,5)，(4,3,5)，(6,8,10) 和 (8,6,10) 。
</pre>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 250</code></li>
</ul>


## 解题思路

- 双重循环枚举 `a` 和 `b`，计算 `a^2 + b^2` 后开方得到候选 `c`。
- 若 `c` 在范围内且满足 `c*c == a^2+b^2`，说明形成勾股三元组并计数。

- 时间复杂度: $O(n^2)$

- 空间复杂度: $O(1)$

## 代码
```cpp
class Solution {
public:
    int countTriples(int n) {
        int count = 0;
        for (int i = 1; i < n; i++) {
            for (int j = 1; j < n; j++) {
                int sum = i * i + j * j;
                int rt = sqrt(sum);
                if (rt > n) break;
                if (rt * rt == sum) count++;
            }
        }
        return count;
    }
};
```
