---
id: 799
title: Champagne Tower
difficulty: Medium
tags: [dynamic-programming]
created: 2026-02-21
---

# 799. 香槟塔

## 题目链接
https://leetcode.cn/problems/champagne-tower/

## 题目描述
<p>我们把玻璃杯摆成金字塔的形状，其中&nbsp;<strong>第一层</strong>&nbsp;有 <code>1</code> 个玻璃杯， <strong>第二层</strong>&nbsp;有 <code>2</code> 个，依次类推到第 100 层，每个玻璃杯将盛有香槟。</p>

<p>从顶层的第一个玻璃杯开始倾倒一些香槟，当顶层的杯子满了，任何溢出的香槟都会立刻等流量的流向左右两侧的玻璃杯。当左右两边的杯子也满了，就会等流量的流向它们左右两边的杯子，依次类推。（当最底层的玻璃杯满了，香槟会流到地板上）</p>

<p>例如，在倾倒一杯香槟后，最顶层的玻璃杯满了。倾倒了两杯香槟后，第二层的两个玻璃杯各自盛放一半的香槟。在倒三杯香槟后，第二层的香槟满了 - 此时总共有三个满的玻璃杯。在倒第四杯后，第三层中间的玻璃杯盛放了一半的香槟，他两边的玻璃杯各自盛放了四分之一的香槟，如下图所示。</p>

<p><img alt="" src="https://s3-lc-upload.s3.amazonaws.com/uploads/2018/03/09/tower.png" style="height: 241px; width: 350px;" /></p>

<p>现在当倾倒了非负整数杯香槟后，返回第 <code>i</code> 行 <code>j</code>&nbsp;个玻璃杯所盛放的香槟占玻璃杯容积的比例（ <code>i</code> 和 <code>j</code>&nbsp;都从0开始）。</p>

<pre>
<strong>示例 1:</strong>
<strong>输入:</strong> poured(倾倒香槟总杯数) = 1, query_glass(杯子的位置数) = 1, query_row(行数) = 1
<strong>输出:</strong> 0.00000
<strong>解释:</strong> 我们在顶层（下标是（0，0））倒了一杯香槟后，没有溢出，因此所有在顶层以下的玻璃杯都是空的。

<strong>示例 2:</strong>
<strong>输入:</strong> poured(倾倒香槟总杯数) = 2, query_glass(杯子的位置数) = 1, query_row(行数) = 1
<strong>输出:</strong> 0.50000
<strong>解释:</strong> 我们在顶层（下标是（0，0）倒了两杯香槟后，有一杯量的香槟将从顶层溢出，位于（1，0）的玻璃杯和（1，1）的玻璃杯平分了这一杯香槟，所以每个玻璃杯有一半的香槟。
</pre>

<p><meta charset="UTF-8" /></p>

<p><strong>示例 3:</strong></p>

<pre>
<strong>输入:</strong> poured = 100000009, query_row = 33, query_glass = 17
<strong>输出:</strong> 1.00000
</pre>

<p><strong>提示:</strong></p>

<ul>
	<li><code>0 &lt;=&nbsp;poured &lt;= 10<sup>9</sup></code></li>
	<li><code>0 &lt;= query_glass &lt;= query_row&nbsp;&lt; 100</code></li>
</ul>


## 解题思路

用一维动态规划按“行”模拟香槟下溢过程。  
`dp[i]` 表示当前行第 `i` 个杯子里实际流到的香槟量（可能大于 1）。

从第 0 行开始，初始 `dp = [poured]`。每次处理一整行时，创建下一行 `nxt`：

- 对当前杯子量 `val`，只有超出 1 的部分会向下流，溢出量为 `max(0, val - 1) / 2`；
- 这部分平均分给下一行相邻两个杯子：`nxt[i]` 和 `nxt[i + 1]`；
- 处理完当前行后令 `dp = nxt`，继续下一行。

迭代到 `query_row` 后，目标杯子的答案是 `min(1, dp[query_glass])`（杯子最多装满 1）。

- 时间复杂度：$O(\text{query\_row}^2)$

- 空间复杂度：$O(\text{query\_row})$

## 代码
```python
class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        dp = [float(poured)]

        for r in range(query_row):
            nxt = [0.0] * (len(dp) + 1)
            for i, val in enumerate(dp):
                overflow = max(0.0, val - 1.0) / 2.0
                nxt[i] += overflow
                nxt[i + 1] += overflow
            dp = nxt

        return min(1.0, dp[query_glass])
```
