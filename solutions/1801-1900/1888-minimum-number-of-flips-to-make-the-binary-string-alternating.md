---
id: 1888
title: Minimum Number of Flips to Make the Binary String Alternating
difficulty: Medium
tags: [string, dynamic-programming, sliding-window]
created: 2026-03-07
---

# 1888. 使二进制字符串字符交替的最少反转次数

## 题目链接
https://leetcode.cn/problems/minimum-number-of-flips-to-make-the-binary-string-alternating/

## 题目描述
<p>给你一个二进制字符串 <code>s</code> 。你可以按任意顺序执行以下两种操作任意次：</p>

<ul>
	<li><strong>类型 1 ：删除</strong> 字符串 <code>s</code> 的第一个字符并将它 <strong>添加</strong> 到字符串结尾。</li>
	<li><strong>类型 2 ：选择 </strong>字符串 <code>s</code> 中任意一个字符并将该字符 <strong>反转 </strong>，也就是如果值为 <code>'0'</code> ，则反转得到 <code>'1'</code> ，反之亦然。</li>
</ul>

<p>请你返回使 <code>s</code> 变成 <strong>交替</strong> 字符串的前提下， <strong>类型 2 </strong>的 <strong>最少</strong> 操作次数 。</p>

<p>我们称一个字符串是 <strong>交替</strong> 的，需要满足任意相邻字符都不同。</p>

<ul>
	<li>比方说，字符串 <code>"010"</code> 和 <code>"1010"</code> 都是交替的，但是字符串 <code>"0100"</code> 不是。</li>
</ul>

<p><strong>示例 1：</strong></p>

<pre><b>输入：</b>s = "111000"
<b>输出：</b>2
<b>解释：</b>执行第一种操作两次，得到 s = "100011" 。
然后对第三个和第六个字符执行第二种操作，得到 s = "10<strong>1</strong>01<strong>0</strong>" 。
</pre>

<p><strong>示例 2：</strong></p>

<pre><b>输入：</b>s = "010"
<b>输出：</b>0
<strong>解释：</strong>字符串已经是交替的。
</pre>

<p><strong>示例 3：</strong></p>

<pre><b>输入：</b>s = "1110"
<b>输出：</b>1
<b>解释：</b>对第二个字符执行第二种操作，得到 s = "1<strong>0</strong>10" 。
</pre>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>5</sup></code></li>
	<li><code>s[i]</code> 要么是 <code>'0'</code> ，要么是 <code>'1'</code> 。</li>
</ul>


## 解题思路

把字符串看成环，类型 1 操作（首字符移到末尾）等价于在 `s + s` 上选一个长度为 `n` 的连续子串。  
对任意长度为 `n` 的窗口，只需统计它与交替模式 `0101...` 的不匹配数 `cnt`，则变成交替串的最少翻转次数是 `min(cnt, n - cnt)`（另一种交替模式 `1010...` 互补）。

代码用定长滑动窗口在长度 `2n-1` 的下标范围内扫描：
- 右端加入新字符时，若与当前位置奇偶期望不同则 `cnt += 1`。
- 当窗口满 `n` 后，用 `ans = min(ans, cnt, n - cnt)` 更新答案。
- 左端滑出字符时，若它原先贡献了不匹配则把 `cnt` 减回去。

这样可在线性时间内枚举所有可能“旋转后”的字符串并取最小翻转次数。

- 时间复杂度: $O(n)$，其中 `n` 是字符串长度；每个位置至多入窗、出窗各一次。

- 空间复杂度: $O(1)$，只使用常数个计数变量。

## 相关专题
- [滑动窗口与双指针](../../topics/sliding-window-and-two-pointers.md)

## 代码
```python
class Solution:
    def minFlips(self, s: str) -> int:
        # 定长滑动窗口题目, 一个是 cnt 另一个是 n - cnt
        ans = n = len(s) # 初始 ans 设置为最大的，然后逐步更新更小的
        cnt = 0 # 偶数开始的数量
        for i in range(n * 2 - 1): # - 1是因为最后一个和第一个是一样的
            # 先新增右边，后统计值，最后收缩左边，通过判断 left 来决定窗口是否建立完毕
            if (ord(s[i % n]) - ord('0')) != i & 1:
                cnt += 1
            left = i - n + 1 # 左边被移除的那个下标
            if left < 0:    # 窗口没有建立完毕
                continue
            ans = min(ans, cnt, n - cnt)
            if ord(s[left]) % 2 != left % 2: # 移除左边那个值, 实际上是 0 的 ord 是偶数
                cnt -= 1
        return ans
```
