---
id: 1758
title: Minimum Changes To Make Alternating Binary String
difficulty: Easy
tags: [string]
created: 2026-03-05
---

# 1758. 生成交替二进制字符串的最少操作数

## 题目链接
https://leetcode.cn/problems/minimum-changes-to-make-alternating-binary-string/

## 题目描述
<p>给你一个仅由字符 <code>'0'</code> 和 <code>'1'</code> 组成的字符串 <code>s</code> 。一步操作中，你可以将任一 <code>'0'</code> 变成 <code>'1'</code> ，或者将 <code>'1'</code> 变成 <code>'0'</code> 。</p>

<p><strong>交替字符串</strong> 定义为：如果字符串中不存在相邻两个字符相等的情况，那么该字符串就是交替字符串。例如，字符串 <code>"010"</code> 是交替字符串，而字符串 <code>"0100"</code> 不是。</p>

<p>返回使 <code>s</code> 变成 <strong>交替字符串</strong> 所需的 <strong>最少</strong> 操作数。</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>s = "0100"
<strong>输出：</strong>1
<strong>解释：</strong>如果将最后一个字符变为 '1' ，s 就变成 "0101" ，即符合交替字符串定义。
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>s = "10"
<strong>输出：</strong>0
<strong>解释：</strong>s 已经是交替字符串。
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>s = "1111"
<strong>输出：</strong>2
<strong>解释：</strong>需要 2 步操作得到 "0101" 或 "1010" 。
</pre>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>4</sup></code></li>
	<li><code>s[i]</code> 是 <code>'0'</code> 或 <code>'1'</code></li>
</ul>


## 解题思路

交替串只有两种目标形态：`0101...` 和 `1010...`。遍历字符串时统计与 `0101...` 不同的位置数 `diff`，那么变成该形态需要 `diff` 次翻转；而变成另一种形态需要 `n - diff` 次翻转（每个位置恰好相反）。答案取二者最小值即可。

- 时间复杂度: $O(n)$，其中 $n$ 是字符串长度。

- 空间复杂度: $O(1)$。

## 相关专题
- [贪心与思维](../../topics/greedy-and-thinking.md)

## 代码
```python
class Solution:
    def minOperations(self, s: str) -> int:
        diff = 0    # 计算 0101 序列需要翻转数量
        for i, n in enumerate(s):
            if (i & 1) != int(n):
                diff += 1
        return min(len(s) - diff, diff)
```
