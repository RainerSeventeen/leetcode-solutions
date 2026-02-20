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
暂无（需要从LeetCode获取）

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
