---
id: 394
title: 字符串解码
difficulty: Medium
tags: [stack, recursion, string]
created: 2026-02-20
---

# 394. 字符串解码

## 题目链接
https://leetcode.cn/problems/decode-string/

## 题目描述

<p>给定一个经过编码的字符串，返回它解码后的字符串。</p>

<p>编码规则为: <code>k[encoded_string]</code>，表示其中方括号内部的 <code>encoded_string</code> 正好重复 <code>k</code> 次。注意 <code>k</code> 保证为正整数。</p>

<p>你可以认为输入字符串总是有效的；输入字符串中没有额外的空格，且输入的方括号总是符合格式要求的。</p>

<p>此外，你可以认为原始数据不包含数字，所有的数字只表示重复的次数 <code>k</code> ，例如不会出现像&nbsp;<code>3a</code>&nbsp;或&nbsp;<code>2[4]</code>&nbsp;的输入。</p>

<p>测试用例保证输出的长度不会超过&nbsp;<code>10<sup>5</sup></code>。</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>s = "3[a]2[bc]"
<strong>输出：</strong>"aaabcbc"
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>s = "3[a2[c]]"
<strong>输出：</strong>"accaccacc"
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>s = "2[abc]3[cd]ef"
<strong>输出：</strong>"abcabccdcdcdef"
</pre>

<p><strong>示例 4：</strong></p>

<pre>
<strong>输入：</strong>s = "abc3[cd]xyz"
<strong>输出：</strong>"abccdcdcdxyz"
</pre>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 30</code></li>
	<li><meta charset="UTF-8" /><code>s</code>&nbsp;由小写英文字母、数字和方括号<meta charset="UTF-8" />&nbsp;<code>'[]'</code> 组成</li>
	<li><code>s</code>&nbsp;保证是一个&nbsp;<strong>有效</strong>&nbsp;的输入。</li>
	<li><code>s</code>&nbsp;中所有整数的取值范围为<meta charset="UTF-8" />&nbsp;<code>[1, 300]</code>&nbsp;</li>
</ul>

## 解题思路
字符串存在嵌套形如 `k[encoded]`，自然用栈从内到外解码。

用两个栈配合实现（与代码一致）：

- `num_stk`：存每一层的重复次数 `k`（要处理多位数字，所以用 `num = num * 10 + digit` 累积）。
- `str_stk`：存当前构造中的字符串片段与 `'['` 作为分隔标记。

扫描字符 `c`：

- 若是数字：更新 `num`。
- 若是 `'['`：说明一个 `k` 已结束，把 `num` 入 `num_stk`，并把 `'['` 入 `str_stk`，然后清空 `num`。
- 若是 `']'`：从 `str_stk` 里弹出直到遇到 `'['`，拼出这一层的 `repeat_str`；再弹出 `k = num_stk.pop()`，把 `repeat_str * k` 作为一个整体压回 `str_stk`。
- 若是字母：直接压入 `str_stk`。

最终把 `str_stk` 连接起来就是答案。

边界：

- 支持多位重复次数（例如 `12[a]`）。
- 嵌套多层时，总是先处理最内层 `]`，符合栈的后进先出。

- 时间复杂度: $O(|s| + |ans|)$
- 空间复杂度: $O(|ans|)$

## 代码
```python
class Solution:
    def decodeString(self, s: str) -> str:
        str_stk = []
        num_stk = []
        num = 0

        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)
            elif c == '[':
                num_stk.append(num)
                num = 0 # 这个数字处理完了，清空并入栈
                str_stk.append(c)
            elif c == ']':
                parts = []
                while str_stk and str_stk[-1] != '[':
                    parts.append(str_stk.pop())
                str_stk.pop()  # 弹出 '['
                repeat_str = "".join(reversed(parts)) # 注意这里弹出来是颠倒的
                k = num_stk.pop()
                str_stk.append(repeat_str * k) # 放回栈中                                    
            else:  
                str_stk.append(c)

        return "".join(str_stk)
```
