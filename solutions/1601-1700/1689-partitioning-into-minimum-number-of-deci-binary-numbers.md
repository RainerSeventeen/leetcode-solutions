---
id: 1689
title: Partitioning Into Minimum Number Of Deci-Binary Numbers
difficulty: Medium
tags: [greedy, string]
created: 2026-03-01
---

# 1689. 十-二进制数的最少数目

## 题目链接
https://leetcode.cn/problems/partitioning-into-minimum-number-of-deci-binary-numbers/

## 题目描述
<p>如果一个十进制数字不含任何前导零，且每一位上的数字不是 <code>0</code> 就是 <code>1</code> ，那么该数字就是一个 <strong>十-二进制数</strong> 。例如，<code>101</code> 和 <code>1100</code> 都是 <strong>十-二进制数</strong>，而 <code>112</code> 和 <code>3001</code> 不是。</p>

<p>给你一个表示十进制整数的字符串 <code>n</code> ，返回和为 <code>n</code> 的 <strong>十-二进制数 </strong>的最少数目。</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>n = "32"
<strong>输出：</strong>3
<strong>解释：</strong>10 + 11 + 11 = 32
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>n = "82734"
<strong>输出：</strong>8
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>n = "27346209830709182346"
<strong>输出：</strong>9
</pre>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n.length &lt;= 10<sup>5</sup></code></li>
	<li><code>n</code> 仅由数字组成</li>
	<li><code>n</code> 不含任何前导零并总是表示正整数</li>
</ul>


## 解题思路

十-二进制数每一位只能贡献 `0` 或 `1`。  
若 `n` 的某一位是 `d`，至少需要 `d` 个数在该位贡献 `1`，因此答案下界是所有位的最大数字。  
同时构造上也能达到这个下界，所以答案就是字符串中的最大字符。

- 时间复杂度: $O(n)$，其中 $n$ 是字符串长度。
- 空间复杂度: $O(1)$。

## 相关专题
- [贪心与思维](../../topics/greedy-and-thinking.md)

## 代码
```python
class Solution:
    def minPartitions(self, n: str) -> int:
        # 简洁 api 做法
        return int(max(n))
```
