---
id: 868
title: Binary Gap
difficulty: Easy
tags: [bit-manipulation]
created: 2026-02-22
---

# 868. 二进制间距

## 题目链接
https://leetcode.cn/problems/binary-gap/

## 题目描述
<p>给定一个正整数 <code>n</code>，找到并返回 <code>n</code> 的二进制表示中两个 <strong>相邻</strong> 1 之间的<strong> 最长距离 </strong>。如果不存在两个相邻的 1，返回 <code>0</code> 。</p>

<p>如果只有 <code>0</code> 将两个 <code>1</code> 分隔开（可能不存在 <code>0</code> ），则认为这两个 1 彼此 <strong>相邻</strong> 。两个 <code>1</code> 之间的距离是它们的二进制表示中位置的绝对差。例如，<code>"1001"</code> 中的两个 <code>1</code> 的距离为 3 。</p>

<ul>
</ul>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>n = 22
<strong>输出：</strong>2
<strong>解释：</strong>22 的二进制是 "10110" 。
在 22 的二进制表示中，有三个 1，组成两对相邻的 1 。
第一对相邻的 1 中，两个 1 之间的距离为 2 。
第二对相邻的 1 中，两个 1 之间的距离为 1 。
答案取两个距离之中最大的，也就是 2 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>n = 8
<strong>输出：</strong>0
<strong>解释：</strong>8 的二进制是 "1000" 。
在 8 的二进制表示中没有相邻的两个 1，所以返回 0 。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>n = 5
<strong>输出：</strong>2
<strong>解释：</strong>5 的二进制是 "101" 。
</pre>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 10<sup>9</sup></code></li>
</ul>


## 解题思路

- 利用位运算循环提取当前最低位的 `1`（`x = n & -n`），其位置为 `x.bit_length() - 1`。
- 维护上一个 `1` 的位置 `pre`，每次遇到新 `1` 就用当前位置减去 `pre` 更新最大距离。
- 然后执行 `n -= x` 移除该最低位 `1`，继续处理下一个 `1`，直到 `n` 为 `0`。

- 时间复杂度: $O(\operatorname{popcount}(n))$（最坏为 $O(\log n)$）

- 空间复杂度: $O(1)$

## 相关专题
- [位运算](../../topics/bit-operations.md)

## 代码
```python
class Solution:
    def binaryGap(self, n: int) -> int:
        dis = 0 # 记录最长距离
        pre = -1
        while n:
            x = n
            x &= -x # 保留最低位 1
            pos = x.bit_length() - 1 # 获取最低位的位置
            if pre != -1:
                dis = max(dis, pos - pre)
            pre = pos
            n -= x
        return dis
```
