---
id: 474
title: Ones and Zeroes
difficulty: Medium
tags: [array, string, dynamic-programming]
created: 2026-02-21
---

# 474. 一和零

## 题目链接
https://leetcode.cn/problems/ones-and-zeroes/

## 题目描述
<p>给你一个二进制字符串数组 <code>strs</code> 和两个整数 <code>m</code> 和 <code>n</code> 。</p>

<div class="MachineTrans-Lines">
<p class="MachineTrans-lang-zh-CN">请你找出并返回 <code>strs</code> 的最大子集的长度，该子集中 <strong>最多</strong> 有 <code>m</code> 个 <code>0</code> 和 <code>n</code> 个 <code>1</code> 。</p>

<p class="MachineTrans-lang-zh-CN">如果 <code>x</code> 的所有元素也是 <code>y</code> 的元素，集合 <code>x</code> 是集合 <code>y</code> 的 <strong>子集</strong> 。</p>
</div>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>strs = ["10", "0001", "111001", "1", "0"], m = 5, n = 3
<strong>输出：</strong>4
<strong>解释：</strong>最多有 5 个 0 和 3 个 1 的最大子集是 {"10","0001","1","0"} ，因此答案是 4 。
其他满足题意但较小的子集包括 {"0001","1"} 和 {"10","1","0"} 。{"111001"} 不满足题意，因为它含 4 个 1 ，大于 n 的值 3 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>strs = ["10", "0", "1"], m = 1, n = 1
<strong>输出：</strong>2
<strong>解释：</strong>最大的子集是 {"0", "1"} ，所以答案是 2 。
</pre>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= strs.length &lt;= 600</code></li>
	<li><code>1 &lt;= strs[i].length &lt;= 100</code></li>
	<li><code>strs[i]</code>&nbsp;仅由&nbsp;<code>'0'</code> 和&nbsp;<code>'1'</code> 组成</li>
	<li><code>1 &lt;= m, n &lt;= 100</code></li>
</ul>


## 解题思路

- 这是二维 0/1 背包，`dp[i][j]` 表示最多用 `i` 个 0 和 `j` 个 1 能选多少字符串。
- 每个字符串先统计 0/1 数量，再倒序更新容量，避免同一字符串被重复选择。

- 时间复杂度: $O(len(strs) \times m \times n)$

- 空间复杂度: $O(m \times n)$

## 相关专题
- [动态规划](../../topics/dynamic-programming.md)

## 代码
```cpp
class Solution {
public:
    int findMaxForm(vector<string>& strs, int m, int n) {
        // 二维 01 背包问题
        vector<vector<int>> dp(m + 1, vector<int>(n + 1, 0));
        // 初始化为 0 已经完成
        for (string& s : strs) {
            // 计算 0 1 个数
            int zeroNum = 0;
            int oneNum = 0;
            for (char& c : s) {
                if (c == '0') zeroNum++;
                else oneNum++;
            }
            for (int i = m; i >= zeroNum; i--) {
                for (int j = n; j >= oneNum; j--) {
                    dp[i][j] = max(
                        dp[i][j], dp[i - zeroNum][j - oneNum] + 1
                    );
                }
            }
        }
        return dp[m][n];
    }
};
```
