---
id: 20
title: 有效的括号
difficulty: Medium
tags: [stack, string]
created: 2026-02-20
---

# 20. 有效的括号

## 题目链接
https://leetcode.cn/problems/valid-parentheses/

## 题目描述
暂无（需要从LeetCode获取）

## 解题思路
用栈维护“尚未匹配的左括号”。遍历字符串：

- 遇到左括号就入栈；
- 遇到右括号就检查栈顶是否为对应的左括号：不匹配或栈空则直接返回 `False`，匹配则弹栈。

遍历结束后栈必须为空，才表示所有括号都被正确匹配。

- 时间复杂度: $O(n)$
- 空间复杂度: $O(n)$

## 代码
```python
class Solution:
    def isValid(self, s: str) -> bool:
        mp = {')' : '(', '}'  : '{', ']' : '['}
        stk = []
        for c in s:
            if c not in mp:
                stk.append(c)
            else:
                if not stk or stk.pop() != mp[c]:
                    return False
        return not stk # 最后栈必须是空的
```
