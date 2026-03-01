---
id: 2266
title: Count Number of Texts
difficulty: Medium
tags: [hash-table, math, string, dynamic-programming]
created: 2026-03-01
---

# 2266. 统计打字方案数

## 题目链接
https://leetcode.cn/problems/count-number-of-texts/

## 题目描述
<p>Alice 在给 Bob 用手机打字。数字到字母的 <strong>对应</strong>&nbsp;如下图所示。</p>

<p><img alt="" src="https://pic.leetcode.cn/1722224025-gsUAIv-image.png" style="width: 200px; height: 162px;" /></p>

<p>为了 <strong>打出</strong>&nbsp;一个字母，Alice 需要 <strong>按</strong>&nbsp;对应字母 <code>i</code>&nbsp;次，<code>i</code>&nbsp;是该字母在这个按键上所处的位置。</p>

<ul>
	<li>比方说，为了按出字母&nbsp;<code>'s'</code>&nbsp;，Alice 需要按&nbsp;<code>'7'</code>&nbsp;四次。类似的， Alice 需要按&nbsp;<code>'5'</code>&nbsp;两次得到字母&nbsp;&nbsp;<code>'k'</code>&nbsp;。</li>
	<li>注意，数字&nbsp;<code>'0'</code> 和&nbsp;<code>'1'</code>&nbsp;不映射到任何字母，所以&nbsp;Alice <strong>不</strong>&nbsp;使用它们。</li>
</ul>

<p>但是，由于传输的错误，Bob 没有收到 Alice 打字的字母信息，反而收到了 <strong>按键的字符串信息</strong>&nbsp;。</p>

<ul>
	<li>比方说，Alice 发出的信息为&nbsp;<code>"bob"</code>&nbsp;，Bob 将收到字符串&nbsp;<code>"2266622"</code>&nbsp;。</li>
</ul>

<p>给你一个字符串&nbsp;<code>pressedKeys</code>&nbsp;，表示 Bob 收到的字符串，请你返回 Alice <strong>总共可能发出多少种文字信息</strong>&nbsp;。</p>

<p>由于答案可能很大，将它对&nbsp;<code>10<sup>9</sup> + 7</code>&nbsp;<strong>取余</strong> 后返回。</p>

<p><strong>示例 1：</strong></p>

<pre>
<b>输入：</b>pressedKeys = "22233"
<b>输出：</b>8
<strong>解释：</strong>
Alice 可能发出的文字信息包括：
"aaadd", "abdd", "badd", "cdd", "aaae", "abe", "bae" 和 "ce" 。
由于总共有 8 种可能的信息，所以我们返回 8 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<b>输入：</b>pressedKeys = "222222222222222222222222222222222222"
<b>输出：</b>82876089
<strong>解释：</strong>
总共有 2082876103 种 Alice 可能发出的文字信息。
由于我们需要将答案对 10<sup>9</sup> + 7 取余，所以我们返回 2082876103 % (10<sup>9</sup> + 7) = 82876089 。
</pre>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= pressedKeys.length &lt;= 10<sup>5</sup></code></li>
	<li><code>pressedKeys</code> 只包含数字&nbsp;<code>'2'</code>&nbsp;到&nbsp;<code>'9'</code>&nbsp;。</li>
</ul>


## 解题思路

先按连续相同数字分组。设一段长度为 `len`：
- 若按键是 `2/3/4/5/6/8`（每键 3 个字母），该段方案数是 3 阶爬楼梯 `f[len]`。
- 若按键是 `7/9`（每键 4 个字母），该段方案数是 4 阶爬楼梯 `g[len]`。

整串答案就是每一段方案数相乘后取模。

- 时间复杂度: $O(n)$，其中 $n$ 是 `pressedKeys` 长度。
- 空间复杂度: $O(n)$，用于预处理 `f/g`。

## 相关专题
- [动态规划](../../topics/dynamic-programming.md)

## 代码
```python
class Solution:
    def countTexts(self, pressedKeys: str) -> int:
        MOD = 1_000_000_007
        # 每一个子串内都是一个爬楼梯问题：
        # 预处理好所有可能用到的值（因为值太多容易递归栈溢出）
        f = [1, 1, 2, 4] # 3 个字母
        g = [1, 1, 2, 4] # 4 个字母
        n = len(pressedKeys)
        for _ in range(n):
            # 内部本质爬楼梯
            f.append((f[-1] + f[-2] + f[-3]) % MOD)
            g.append((g[-1] + g[-2] + g[-3] + g[-4]) % MOD)
        
        pre_ch = pressedKeys[0]
        pre_idx = 0
        idx = 0 # 从第一个数开始算
        ret = 1
        while idx < n:
            if pre_ch != pressedKeys[idx]:
                l = idx - pre_idx
                ret = ret * (g[l] if pre_ch in "79" else f[l]) % MOD
                pre_idx = idx
            pre_ch = pressedKeys[idx]
            idx += 1
        l = idx - pre_idx
        ret = ret * (g[l] if pre_ch in "79" else f[l]) % MOD
        return ret
```
