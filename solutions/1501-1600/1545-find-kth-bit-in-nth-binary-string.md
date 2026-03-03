---
id: 1545
title: Find Kth Bit in Nth Binary String
difficulty: Medium
tags: [recursion, string, simulation]
created: 2026-03-03
---

# 1545. 找出第 N 个二进制字符串中的第 K 位

## 题目链接
https://leetcode.cn/problems/find-kth-bit-in-nth-binary-string/

## 题目描述
<p>给你两个正整数 <code>n</code> 和 <code>k</code>，二进制字符串  <code>S<sub>n</sub></code> 的形成规则如下：</p>

<ul>
	<li><code>S<sub>1</sub> = "0"</code></li>
	<li>当 <code>i > 1</code> 时，<code>S<sub>i</sub> = S<sub>i-1</sub> + "1" + reverse(invert(S<sub>i-1</sub>))</code></li>
</ul>

<p>其中 <code>+</code> 表示串联操作，<code>reverse(x)</code> 返回反转 <code>x</code> 后得到的字符串，而 <code>invert(x)</code> 则会翻转 x 中的每一位（0 变为 1，而 1 变为 0）。</p>

<p>例如，符合上述描述的序列的前 4 个字符串依次是：</p>

<ul>
	<li><code>S<sub>1 </sub>= "0"</code></li>
	<li><code>S<sub>2 </sub>= "0<strong>1</strong>1"</code></li>
	<li><code>S<sub>3 </sub>= "011<strong>1</strong>001"</code></li>
	<li><code>S<sub>4</sub> = "0111001<strong>1</strong>0110001"</code></li>
</ul>

<p>请你返回  <code>S<sub>n</sub></code> 的 <strong>第 <code>k</code> 位字符</strong> ，题目数据保证 <code>k</code> 一定在 <code>S<sub>n</sub></code> 长度范围以内。</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>n = 3, k = 1
<strong>输出：</strong>"0"
<strong>解释：</strong>S<sub>3</sub> 为 "<strong>0</strong>111001"，其第 1 位为 "0" 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>n = 4, k = 11
<strong>输出：</strong>"1"
<strong>解释：</strong>S<sub>4</sub> 为 "0111001101<strong>1</strong>0001"，其第 11 位为 "1" 。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>n = 1, k = 1
<strong>输出：</strong>"0"
</pre>

<p><strong>示例 4：</strong></p>

<pre>
<strong>输入：</strong>n = 2, k = 3
<strong>输出：</strong>"1"
</pre>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 <= n <= 20</code></li>
	<li><code>1 <= k <= 2<sup>n</sup> - 1</code></li>
</ul>


## 解题思路

利用构造定义的对称性递归定位第 `k` 位。

- `S_n` 长度为 `2^n - 1`，中点位置 `mid = 2^(n-1)`，该位恒为 `1`。
- 若 `k < mid`，答案与 `S_{n-1}` 的第 `k` 位相同，递归到左半部分。
- 若 `k > mid`，它对应右半部分 `reverse(invert(S_{n-1}))`，可映射到 `S_{n-1}` 的镜像位置 `new_k = 2^n - k`，再把结果位取反。
- 递归终点是 `n = 1`，此时 `S_1 = "0"`。

- 时间复杂度: $O(n)$

- 空间复杂度: $O(n)$（递归调用栈）

## 相关专题
- [链表、树与回溯](../../topics/linked-list-tree-backtracking.md)

## 代码
```python
class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        # k 范围 [1, 2 ^ n  - 1]
        def dfs(n, k):
            if n == 1:
                return '0'
            mid = 1 << (n - 1)  # 2^(n-1)
            if k == mid:
                return '1'
            elif k < mid:
                return dfs(n - 1, k)
            else:
                new_k = (1 << n) - k
                c = dfs(n - 1, new_k)
                # 翻转
                return '1' if c == '0' else '0'

        return dfs(n, k)
```
