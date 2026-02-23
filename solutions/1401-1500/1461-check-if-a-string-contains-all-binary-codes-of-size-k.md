---
id: 1461
title: Check If a String Contains All Binary Codes of Size K
difficulty: Medium
tags: [bit-manipulation, hash-table, string, hash-function, rolling-hash]
created: 2026-02-23
---

# 1461. 检查一个字符串是否包含所有长度为 K 的二进制子串

## 题目链接
https://leetcode.cn/problems/check-if-a-string-contains-all-binary-codes-of-size-k/

## 题目描述
<p>给你一个二进制字符串&nbsp;<code>s</code>&nbsp;和一个整数&nbsp;<code>k</code>&nbsp;。如果所有长度为 <code>k</code>&nbsp;的二进制字符串都是 <code>s</code>&nbsp;的子串，请返回 <code>true</code> ，否则请返回 <code>false</code> 。</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>s = "00110110", k = 2
<strong>输出：</strong>true
<strong>解释：</strong>长度为 2 的二进制串包括 "00"，"01"，"10" 和 "11"。它们分别是 s 中下标为 0，1，3，2 开始的长度为 2 的子串。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>s = "0110", k = 1
<strong>输出：</strong>true
<strong>解释：</strong>长度为 1 的二进制串包括 "0" 和 "1"，显然它们都是 s 的子串。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>s = "0110", k = 2
<strong>输出：</strong>false
<strong>解释：</strong>长度为 2 的二进制串 "00" 没有出现在 s 中。
</pre>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 5 * 10<sup>5</sup></code></li>
	<li><code>s[i]</code> 不是<code>'0'</code> 就是 <code>'1'</code></li>
	<li><code>1 &lt;= k &lt;= 20</code></li>
</ul>


## 解题思路

用长度为 `2^k` 的布尔数组 `mp` 记录每个长度为 `k` 的二进制子串是否出现。维护一个长度为 `k` 的滑动窗口整数值 `x`：

- 每读入一个字符，执行 `x = ((x << 1) & mask) | int(ch)`，其中 `mask = (1 << k) - 1` 用于只保留低 `k` 位；
- 当下标 `i >= k - 1` 时，`x` 就对应当前窗口的二进制值；
- 若该值首次出现则标记并计数，最后判断计数是否等于 `2^k`。

这样避免了对子串切片和字符串哈希，整趟线性扫描即可完成判断。

- 时间复杂度: $O(n)$，其中 $n$ 是 `s` 的长度。
- 空间复杂度: $O(2^k)$，用于记录所有可能的 `k` 位二进制值是否出现。

## 相关专题
- [字符串](../../topics/string-algorithms.md)

## 代码
```python
class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        # 位运算+数组判断
        # 循环移动，将所有字符串化作 int 检查是否所有的 int 都出现过
        mp = [False] * (1 << k) # 2 ** k
        mask = (1 << k) - 1 # k 位 全部为 1 的掩码
        cnt = x = 0
        for i, ch in enumerate(s): # i 是右边界
            x = ((x << 1) & mask) | int(ch)  # 尾部加上 ch
            # print(f"{i}, {x:b}, {int(ch)}")
            if i >= k - 1 and mp[x] != True:
                mp[x] = True
                cnt += 1
        return cnt == (1 << k)
```
