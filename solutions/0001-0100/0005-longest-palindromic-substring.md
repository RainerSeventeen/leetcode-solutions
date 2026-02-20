---
id: 5
title: Longest Palindromic Substring
difficulty: Medium
tags: [two-pointers, string, dynamic-programming]
created: 2026-02-20
---

# 5. Longest Palindromic Substring

## 题目链接
https://leetcode.cn/problems/longest-palindromic-substring/

## 题目描述
<p>给你一个字符串 <code>s</code>，找到 <code>s</code> 中最长的 <span data-keyword="palindromic-string">回文</span> <span data-keyword="substring-nonempty">子串</span>。</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>s = "babad"
<strong>输出：</strong>"bab"
<strong>解释：</strong>"aba" 同样是符合题意的答案。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>s = "cbbd"
<strong>输出：</strong>"bb"
</pre>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 1000</code></li>
	<li><code>s</code> 仅由数字和英文字母组成</li>
</ul>



## 解题思路

使用 Manacher 算法把“以每个位置为中心的回文扩展”摊平成线性时间。

关键点：

- 预处理：在字符间插入分隔符 `#`，并在两端加哨兵 `^/$`，把奇偶长度回文统一成“奇回文”。
- 定义 `p[i]` 为预处理串中以 `i` 为中心的回文半径（能向左右扩展的长度）。
- 维护当前“最右回文”的中心 `center` 与其右边界 `right`：
  - 对于新位置 `i`，其关于 `center` 的镜像点为 `mirror = 2*center - i`；
  - 若 `i < right`，可先令 `p[i] = min(right - i, p[mirror])`，再从该半径继续暴力扩展；
  - 扩展后若 `i + p[i] > right`，更新 `center/right`。
- 过程中记录最大 `p[i]` 及对应中心，即得到最长回文；最后把预处理下标换回原串下标。

- 时间复杂度: $O(n)$
- 空间复杂度: $O(n)$

## 代码
```python
class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 预处理
        t = "^#" + "#".join(s) + "#$"
        n = len(t)
        p = [0] * n # 回文半径长度

        # center/right：当前已知“最右回文”的中心与其右边界（right 为该回文最右端索引）
        center = 0
        right = 0

        best_center = 0     # z最长字符串在预处理串 t 中的中心位置

        # 线性扫描每个中心 i
        for i in range(1, n - 1):
            mirror = 2 * center - i  # i 关于 center 的对称点

            #  i 在当前最右回文覆盖范围内，可以用对称性给 p[i] 一个下界
            if i < right:
                # right - i：i 到右边界还剩多少可用空间
                # p[mirror]：对称点的半径
                p[i] = min(right - i, p[mirror])

            # 在已有半径基础上继续向两侧暴力扩展
            while t[i + p[i] + 1] == t[i - p[i] - 1]:
                p[i] += 1

            # 如果以 i 为中心的回文超出了当前 right，则更新 center/right
            if i + p[i] > right:
                center = i
                right = i + p[i]

            # 维护全局最优
            if p[i] > p[best_center]:
                best_center = i

        # 映射回原串，注意到原来的 radius 就是回文串长度
        start = (best_center - p[best_center]) // 2
        return s[start:start + p[best_center]]
```
