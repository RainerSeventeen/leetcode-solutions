---
id: 399
title: 除法求值
difficulty: Medium
tags: [depth-first-search, breadth-first-search, union-find, graph, array, string, shortest-path]
created: 2026-02-20
---

# 399. 除法求值

## 题目链接
https://leetcode.cn/problems/evaluate-division/

## 题目描述

该题为 LeetCode 会员题（Premium），无法自动获取完整题目描述。

## 解题思路
把每个等式 `a / b = val` 看成一条带权边；查询 `x / y` 本质是在同一个连通分量中求两点比值。用**带权并查集**可以在近似线性的时间内支持合并与查询。

数据结构定义（与代码一致）：

- `father[x]`：`x` 的父节点。
- `devide[x]`：`x / father[x]` 的值（注意是“到父亲”的比值）。

`find(x)` 需要返回 `(root, x/root)`，并做路径压缩：

- 递归先找到父节点 `p` 的根 `root`，得到 `p/root`；
- 更新 `father[x] = root`；
- 同时把 `devide[x]` 乘上 `p/root`，使其变成 `x/root`。

`union(a, b, val)`：已知 `a / b = val`，设 `wa = a/rootA`、`wb = b/rootB`，则

`rootA / rootB = val * wb / wa`

把 `rootA` 挂到 `rootB` 上，并设置 `devide[rootA] = rootA/rootB`，就完成了连通分量的比值维护。

回答查询 `x / y`：

- 若 `x` 或 `y` 不存在，或二者根不同，返回 `-1.0`；
- 否则已知 `wx = x/root`、`wy = y/root`，有 `x / y = wx / wy`。

边界：变量集合事先未知，所以用字典存并查集节点。

- 时间复杂度: $O((E+Q)\,\alpha(V))$
- 空间复杂度: $O(V)$

## 相关专题
- [图论算法](../../topics/graph-algorithms.md)

## 代码
```python
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        father = {}   # father[x] = parent
        devide = {}   # devide[x] = x / father[x]

        def add(x: str) -> None:
            if x not in father:
                father[x] = x
                devide[x] = 1.0

        def find(x: str):
            """
            return (root, x/root)
            devide[x] = x / root
            """
            if x not in father:
                return None, -1.0
            if father[x] == x:
                return x, 1.0

            p = father[x]
            root, w = find(p)          # w = p / root
            father[x] = root
            devide[x] *= w             # (x/p) * (p/root) = x/root
            return root, devide[x]

        def union(a: str, b: str, val: float) -> None:
            """
            a / b = val
            wa = a/rootA
            wb = b/rootB
            rootA / rootB = val * wb / wa
            """
            add(a)
            add(b)

            ra, wa = find(a)
            rb, wb = find(b)
            if ra == rb:
                return
            father[ra] = rb
            devide[ra] = val * wb / wa

        for (a, b), val in zip(equations, values):
            union(a, b, val)

        ret = []
        for x, y in queries:
            if x not in father or y not in father:
                ret.append(-1.0)
                continue
            rx, wx = find(x)
            ry, wy = find(y)
            if rx != ry:
                ret.append(-1.0)
            else:
                ret.append(wx / wy)

        return ret
```
