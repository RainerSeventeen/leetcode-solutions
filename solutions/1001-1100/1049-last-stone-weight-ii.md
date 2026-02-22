---
id: 1049
title: Last Stone Weight II
difficulty: Medium
tags: [array, dynamic-programming]
created: 2026-02-21
---

# 1049. 最后一块石头的重量 II

## 题目链接
https://leetcode.cn/problems/last-stone-weight-ii/

## 题目描述
<p>有一堆石头，用整数数组&nbsp;<code>stones</code> 表示。其中&nbsp;<code>stones[i]</code> 表示第 <code>i</code> 块石头的重量。</p>

<p>每一回合，从中选出<strong>任意两块石头</strong>，然后将它们一起粉碎。假设石头的重量分别为&nbsp;<code>x</code> 和&nbsp;<code>y</code>，且&nbsp;<code>x &lt;= y</code>。那么粉碎的可能结果如下：</p>

<ul>
	<li>如果&nbsp;<code>x == y</code>，那么两块石头都会被完全粉碎；</li>
	<li>如果&nbsp;<code>x != y</code>，那么重量为&nbsp;<code>x</code>&nbsp;的石头将会完全粉碎，而重量为&nbsp;<code>y</code>&nbsp;的石头新重量为&nbsp;<code>y-x</code>。</li>
</ul>

<p>最后，<strong>最多只会剩下一块 </strong>石头。返回此石头 <strong>最小的可能重量 </strong>。如果没有石头剩下，就返回 <code>0</code>。</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>stones = [2,7,4,1,8,1]
<strong>输出：</strong>1
<strong>解释：</strong>
组合 2 和 4，得到 2，所以数组转化为 [2,7,1,8,1]，
组合 7 和 8，得到 1，所以数组转化为 [2,1,1,1]，
组合 2 和 1，得到 1，所以数组转化为 [1,1,1]，
组合 1 和 1，得到 0，所以数组转化为 [1]，这就是最优值。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>stones = [31,26,33,21,40]
<strong>输出：</strong>5
</pre>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= stones.length &lt;= 30</code></li>
	<li><code>1 &lt;= stones[i] &lt;= 100</code></li>
</ul>


## 解题思路

- 把石头分成两堆，目标是让两堆和尽量接近，即在 `sum/2` 内尽量装满。
- 用 0/1 背包求不超过 `sum/2` 的最大可达重量 `dp[target]`，结果为 `sum-2*dp[target]`。

- 时间复杂度: $O(n \times sum)$

- 空间复杂度: $O(sum)$

## 相关专题
- [动态规划](../../topics/dynamic-programming.md)

## 代码
```cpp
class Solution {
public:
    int lastStoneWeightII(vector<int>& stones) {
        // 01 背包变化形态，把重量分为最接近的两组
        int sum = 0;
        for (int &a : stones) sum += a;
        int target = sum / 2;
        int item = stones.size(); // 物品总数量
        vector<int> dp(target + 1, 0);
        for (int i = 0; i < item; i++) {
            for (int j = target; j >= stones[i]; j--) {
                dp[j] = max (
                    dp[j], dp[j - stones[i]] + stones[i]
                );
            }
        }
        return abs(sum - 2 * dp[target]);
    }
};
```
