---
id: 76
title: Minimum Window Substring
difficulty: Hard
tags: [hash-table, string, sliding-window]
created: 2026-02-20
---

# 76. 最小覆盖子串

## 题目链接
https://leetcode.cn/problems/minimum-window-substring/

## 题目描述
<p>给定两个字符串&nbsp;<code>s</code> 和&nbsp;<code>t</code>，长度分别是&nbsp;<code>m</code> 和&nbsp;<code>n</code>，返回 s 中的&nbsp;<strong>最短窗口 <span data-keyword="substring-nonempty">子串</span></strong>，使得该子串包含 <code>t</code> 中的每一个字符（<strong>包括重复字符</strong>）。如果没有这样的子串，返回空字符串<em>&nbsp;</em><code>""</code>。</p>

<p>测试用例保证答案唯一。</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>s = "ADOBECODEBANC", t = "ABC"
<strong>输出：</strong>"BANC"
<strong>解释：</strong>最小覆盖子串 "BANC" 包含来自字符串 t 的 'A'、'B' 和 'C'。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>s = "a", t = "a"
<strong>输出：</strong>"a"
<strong>解释：</strong>整个字符串 s 是最小覆盖子串。
</pre>

<p><strong>示例 3:</strong></p>

<pre>
<strong>输入:</strong> s = "a", t = "aa"
<strong>输出:</strong> ""
<strong>解释:</strong> t 中两个字符 'a' 均应包含在 s 的子串中，
因此没有符合条件的子字符串，返回空字符串。</pre>

<p><strong>提示：</strong></p>

<ul>
	<li><code>m == s.length</code></li>
	<li><code>n == t.length</code></li>
	<li><code>1 &lt;= m, n &lt;= 10<sup>5</sup></code></li>
	<li><code>s</code> 和 <code>t</code> 由英文字母组成</li>
</ul>

<strong>进阶：</strong>你能设计一个在 <code>O(m + n)</code> 时间内解决此问题的算法吗？


## 解题思路

滑动窗口 + 计数匹配。

目标：在 `s` 中找到最短子串，使其包含 `t` 的全部字符（含重复次数）。

做法：

1. 统计 `t` 的需求计数 `need[c]`，并维护 `missing` 表示“还缺多少个字符”（也可以用满足的种类数 `formed`）。
2. 用双指针 `[l, r]` 扩张右端 `r`：
   - 把 `s[r]` 加入窗口计数 `window[c]`
   - 若 `window[c]` 没超过 `need[c]`（即这次加入确实补上了一个需求），则 `missing -= 1`
3. 当 `missing == 0` 时，说明窗口已经覆盖 `t`：
   - 尝试收缩左端 `l`，只要移除 `s[l]` 不会破坏覆盖（即移除后 `window[c]` 仍 `>= need[c]`），就持续收缩以获得更短窗口
   - 一旦移除会让某个必需字符不足（`window[c] < need[c]`），窗口失效，停止收缩，继续扩张 `r`

不变量：

- 扩张阶段保证“尽快满足覆盖”，收缩阶段保证“在覆盖前提下尽量短”，两者交替可以覆盖所有最优解。

边界：

- `t` 为空时答案是空串。
- `len(s) < len(t)` 一定无解。

- 时间复杂度: $O(|s|+|t|)$
- 空间复杂度: $O(\Sigma)$

其中 $\Sigma$ 为字符集大小；若固定为 ASCII/小写字母，可视为常数。

## 相关专题
- [滑动窗口与双指针](../../topics/sliding-window-and-two-pointers.md)

## 代码
```python
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = {}
        n = len(s)
        for c in t:
            need[c] = need.get(c, 0) + 1
        missing = len(need) # 表示窗口还缺多少字母种类
        l, r = 0, 0 # [l, r)
        best_l = 0
        ret = float('inf') # 表示最短窗口
        for r, ch in enumerate(s):  # [l , r]
            if ch in need:
                need[ch] -= 1
                if need[ch] == 0:
                    missing -= 1
            while missing == 0: # 窗口齐了，开始收缩左边
                # 左压缩窗口
                window = r - l + 1
                if window < ret:
                    best_l = l
                    ret = window
                if s[l] in need:
                    need[s[l]] += 1
                    if need[s[l]] == 1:
                        missing += 1
                l += 1
            
        return "" if ret == float('inf') else s[best_l:best_l + ret]
```
