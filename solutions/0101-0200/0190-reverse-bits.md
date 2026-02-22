---
id: 190
title: Reverse Bits
difficulty: Easy
tags: [bit-manipulation, divide-and-conquer]
created: 2026-02-21
---

# 190. 颠倒二进制位

## 题目链接
https://leetcode.cn/problems/reverse-bits/

## 题目描述
<p>颠倒给定的 32 位有符号整数的二进制位。</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>n = 43261596</span></p>

<p><span class="example-io"><b>输出：</b>964176192</span></p>

<p><strong>解释：</strong></p>

<table>
	<tbody>
		<tr>
			<th>整数</th>
			<th>二进制</th>
		</tr>
		<tr>
			<td>43261596</td>
			<td>00000010100101000001111010011100</td>
		</tr>
		<tr>
			<td>964176192</td>
			<td>00111001011110000010100101000000</td>
		</tr>
	</tbody>
</table>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>n = 2147483644</span></p>

<p><span class="example-io"><b>输出：</b>1073741822</span></p>

<p><strong>解释：</strong></p>

<table>
	<tbody>
		<tr>
			<th>整数</th>
			<th>二进制</th>
		</tr>
		<tr>
			<td>2147483644</td>
			<td>01111111111111111111111111111100</td>
		</tr>
		<tr>
			<td>1073741822</td>
			<td>00111111111111111111111111111110</td>
		</tr>
	</tbody>
</table>
</div>

<p><strong>提示：</strong></p>

<ul>
	<li><code>0 &lt;= n &lt;= 2<sup>31</sup>&nbsp;- 2</code></li>
	<li><code>n</code>&nbsp;为偶数</li>
</ul>

<p><strong>进阶</strong>: 如果多次调用这个函数，你将如何优化你的算法？</p>


## 解题思路

逐位读取原数第 `i` 位，并把它放到结果的第 `31-i` 位。
循环固定 32 次，用位移和按位与取位，再用按位或写入答案。
最终得到 32 位反转后的整数。
- 时间复杂度: $O(1)$
- 空间复杂度: $O(1)$

## 相关专题
- [位运算](../../topics/bit-operations.md)

## 代码
```cpp
class Solution {
public:
    int reverseBits(int n) {
        int32_t ret = 0;
        for (int i = 0; i < 32; i++) {
            ret |= ((n >> i) & 1) << (31 - i);
        }
        return ret;
    }
};
```
