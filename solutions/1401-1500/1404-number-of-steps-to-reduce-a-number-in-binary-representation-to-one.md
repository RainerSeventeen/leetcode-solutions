---
id: 1404
title: Number of Steps to Reduce a Number in Binary Representation to One
difficulty: Medium
tags: [bit-manipulation, string, simulation]
created: 2026-02-26
---

# 1404. 将二进制表示减到 1 的步骤数

## 题目链接
https://leetcode.cn/problems/number-of-steps-to-reduce-a-number-in-binary-representation-to-one/

## 题目描述
<p>给你一个以二进制形式表示的数字 <code>s</code> 。请你返回按下述规则将其减少到 1 所需要的步骤数：</p>

<ul>
	<li>
	<p>如果当前数字为偶数，则将其除以 <code>2</code> 。</p>
	</li>
	<li>
	<p>如果当前数字为奇数，则将其加上 <code>1</code> 。</p>
	</li>
</ul>

<p>题目保证你总是可以按上述规则将测试用例变为 1 。</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>s = "1101"
<strong>输出：</strong>6
<strong>解释：</strong>"1101" 表示十进制数 13 。
Step 1) 13 是奇数，加 1 得到 14&nbsp;
Step 2) 14 是偶数，除 2 得到 7
Step 3) 7  是奇数，加 1 得到 8
Step 4) 8  是偶数，除 2 得到 4&nbsp; 
Step 5) 4  是偶数，除 2 得到 2&nbsp;
Step 6) 2  是偶数，除 2 得到 1&nbsp; 
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>s = "10"
<strong>输出：</strong>1
<strong>解释：</strong>"10" 表示十进制数 2 。
Step 1) 2 是偶数，除 2 得到 1 
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>s = "1"
<strong>输出：</strong>0
</pre>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length&nbsp;&lt;= 500</code></li>
	<li><code>s</code> 由字符 <code>'0'</code> 或 <code>'1'</code> 组成。</li>
	<li><code>s[0] == '1'</code></li>
</ul>


## 解题思路
先把二进制字符串转成大整数，按题意模拟：

- 偶数就右移一位（`// 2`）
- 奇数就加一（`+ 1`）

直到变成 `1`，累计操作次数即答案。

- 时间复杂度: $O(n^2)$，其中 `n` 是二进制串长度；大整数加法/除法的单次开销与位数相关

- 空间复杂度: $O(n)$，用于存储大整数

## 相关专题
- [贪心与思维](../../topics/greedy-and-thinking.md)

## 代码
```python
class Solution:
    def numSteps(self, s: str) -> int:
        num = int(s, 2)
        cnt = 0
        while num != 1:
            if num % 2 == 0:
                num = num // 2
            else:
                num += 1
            cnt += 1
            # print(format(num, 'b'), cnt)            
        return cnt
```
