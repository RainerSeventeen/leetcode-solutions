---
id: 3186
title: Maximum Total Damage With Spell Casting
difficulty: Medium
tags: [array, hash-table, two-pointers, binary-search, dynamic-programming, counting, sorting]
created: 2026-03-02
---

# 3186. 施咒的最大总伤害

## 题目链接
https://leetcode.cn/problems/maximum-total-damage-with-spell-casting/

## 题目描述
<p>一个魔法师有许多不同的咒语。</p>

<p>给你一个数组&nbsp;<code>power</code>&nbsp;，其中每个元素表示一个咒语的伤害值，可能会有多个咒语有相同的伤害值。</p>

<p>已知魔法师使用伤害值为&nbsp;<code>power[i]</code>&nbsp;的咒语时，他们就&nbsp;<strong>不能</strong>&nbsp;使用伤害为&nbsp;<code>power[i] - 2</code>&nbsp;，<code>power[i] - 1</code>&nbsp;，<code>power[i] + 1</code>&nbsp;或者&nbsp;<code>power[i] + 2</code>&nbsp;的咒语。</p>

<p>每个咒语最多只能被使用 <strong>一次</strong>&nbsp;。</p>

<p>请你返回这个魔法师可以达到的伤害值之和的 <strong>最大值</strong>&nbsp;。</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>power = [1,1,3,4]</span></p>

<p><span class="example-io"><b>输出：</b>6</span></p>

<p><strong>解释：</strong></p>

<p>可以使用咒语 0，1，3，伤害值分别为 1，1，4，总伤害值为 6 。</p>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>power = [7,1,6,6]</span></p>

<p><span class="example-io"><b>输出：</b>13</span></p>

<p><strong>解释：</strong></p>

<p>可以使用咒语 1，2，3，伤害值分别为 1，6，6，总伤害值为 13 。</p>
</div>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= power.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= power[i] &lt;= 10<sup>9</sup></code></li>
</ul>


## 解题思路

- 先用 `Counter` 统计每个伤害值 `x` 出现次数，把问题转成在有序去重数组 `a` 上做选择：选了 `x` 就不能选 `x-2,x-1,x+1,x+2`。
- 设 `f[i]` 表示只看 `a` 的前 `i` 个值（`a[0..i-1]`）时的最大总伤害。遍历当前值 `x=a[i]` 时，维护指针 `j`，使得 `a[0..j-1]` 都满足 `< x-2`，即可与 `x` 共存。
- 转移为 `f[i+1] = max(f[i], f[j] + x * cnt[x])`：不选 `x` 或选 `x` 两种情况取最大。

- 时间复杂度: $O(n + m \log m)$，其中 `n` 是 `power` 长度，`m` 是不同伤害值个数。计数是 $O(n)$，排序去重值是 $O(m \log m)$，DP 双指针扫描是 $O(m)$。

- 空间复杂度: $O(m)$，用于计数表、去重数组与 DP 数组。

## 相关专题
- [动态规划](../../topics/dynamic-programming.md)

## 代码
```python
class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        cnt = Counter(power)
        a = sorted(cnt) # 需要去重复， a 一定是去重后的值
        f = [0] * (len(a) + 1)  #  a[0..j-1] 中选择可以拿到的最大值
        j = 0
        for i, x in enumerate(a):
            while a[j] < x - 2: # 从左到右找，找到第一个不符合条件的值
                j += 1
            # f[j] 指向 x - 2 的值
            f[i + 1] = max(f[i], f[j] + x * cnt[x])
        return f[-1]

        # 记忆化搜索算法，会超时的
        # @cache
        # def dfs(i): # 从 [a[0], a[i]] 数字中选择的可得到的最大值，注意不是下标，是数值
        #     # 1. 选择 i
        #     if i < 0:
        #         return 0
        #     j = i # 从这里开始找上一个 -2 的值
        #     while j >= 0 and a[j] >= a[i] - 2:
        #         j -= 1
        #     chose = dfs(j) + a[i] * cnt[a[i]] # 上一个可选值的最大值
        #     # 2. 不选择
        #     not_chose = dfs(i - 1)
        #     return max(not_chose, chose)
        # return dfs(n - 1)
```
