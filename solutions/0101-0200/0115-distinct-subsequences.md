---
id: 115
title: Distinct Subsequences
difficulty: Hard
tags: [string, dynamic-programming]
created: 2026-02-21
---

# 115. 不同的子序列

## 题目链接
https://leetcode.cn/problems/distinct-subsequences/

## 题目描述
<p>给你两个字符串 <code>s</code><strong> </strong>和 <code>t</code> ，统计并返回在 <code>s</code> 的 <strong>子序列</strong> 中 <code>t</code> 出现的个数。</p>

<p>测试用例保证结果在 32 位有符号整数范围内。</p>

<p><strong>示例&nbsp;1：</strong></p>

<pre>
<strong>输入：</strong>s = "rabbbit", t = "rabbit"<code>
<strong>输出</strong></code><strong>：</strong><code>3
</code><strong>解释：</strong>
如下所示, 有 3 种可以从 s 中得到 <code>"rabbit" 的方案</code>。
<code><strong><u>rabb</u></strong>b<strong><u>it</u></strong></code>
<code><strong><u>ra</u></strong>b<strong><u>bbit</u></strong></code>
<code><strong><u>rab</u></strong>b<strong><u>bit</u></strong></code></pre>

<p><strong>示例&nbsp;2：</strong></p>

<pre>
<strong>输入：</strong>s = "babgbag", t = "bag"
<code><strong>输出</strong></code><strong>：</strong><code>5
</code><strong>解释：</strong>
如下所示, 有 5 种可以从 s 中得到 <code>"bag" 的方案</code>。 
<code><strong><u>ba</u></strong>b<u><strong>g</strong></u>bag</code>
<code><strong><u>ba</u></strong>bgba<strong><u>g</u></strong></code>
<code><u><strong>b</strong></u>abgb<strong><u>ag</u></strong></code>
<code>ba<u><strong>b</strong></u>gb<u><strong>ag</strong></u></code>
<code>babg<strong><u>bag</u></strong></code>
</pre>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length, t.length &lt;= 1000</code></li>
	<li><code>s</code> 和 <code>t</code> 由英文字母组成</li>
</ul>


## 解题思路

- 定义 `dp[i][j]` 为 `s` 前 `i` 个字符中形成 `t` 前 `j` 个字符的方案数。
- 字符相等时可选“用或不用当前字符”，不等时只能继承上一行结果。

- 时间复杂度: $O(m \times n)$

- 空间复杂度: $O(m \times n)$

## 相关专题
- [动态规划](../../topics/dynamic-programming.md)

## 代码
```cpp
class Solution {
public:
    int numDistinct(string s, string t) {
        // 编辑问题
        int m = s.size();
        int n = t.size();
        vector<vector<unsigned long long>> dp(m + 1, vector<unsigned long long>(n + 1, 0));

        for (int i = 0; i <= m; i++) dp[i][0] = 1;

        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                if (s[i - 1] == t[j - 1]) {
                    dp[i][j] = dp[i - 1][j] + dp[i - 1][j - 1]; // 可以用可以不用
                } else {
                    dp[i][j] = dp[i - 1][j]; // 只删除 s
                }
            }
        }
        return int(dp[m][n]);
    }
};
```
