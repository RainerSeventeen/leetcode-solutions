---
id: 583
title: Delete Operation for Two Strings
difficulty: Medium
tags: [string, dynamic-programming]
created: 2026-02-21
---

# 583. 两个字符串的删除操作

## 题目链接
https://leetcode.cn/problems/delete-operation-for-two-strings/

## 题目描述
<p>给定两个单词&nbsp;<code>word1</code>&nbsp;和<meta charset="UTF-8" />&nbsp;<code>word2</code>&nbsp;，返回使得<meta charset="UTF-8" />&nbsp;<code>word1</code>&nbsp;和&nbsp;<meta charset="UTF-8" />&nbsp;<code>word2</code><em>&nbsp;</em><strong>相同</strong>所需的<strong>最小步数</strong>。</p>

<p><strong>每步&nbsp;</strong>可以删除任意一个字符串中的一个字符。</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入:</strong> word1 = "sea", word2 = "eat"
<strong>输出:</strong> 2
<strong>解释:</strong> 第一步将 "sea" 变为 "ea" ，第二步将 "eat "变为 "ea"
</pre>

<p><strong>示例 &nbsp;2:</strong></p>

<pre>
<b>输入：</b>word1 = "leetcode", word2 = "etco"
<b>输出：</b>4
</pre>

<p><strong>提示：</strong></p>
<meta charset="UTF-8" />

<ul>
	<li><code>1 &lt;= word1.length, word2.length &lt;= 500</code></li>
	<li><code>word1</code>&nbsp;和&nbsp;<code>word2</code>&nbsp;只包含小写英文字母</li>
</ul>


## 解题思路

- 先转化为最长公共子序列（LCS）问题，公共部分不用删除。
- 用一维滚动 DP 计算 LCS 长度，最终答案为 `m + n - 2 * lcs`。

- 时间复杂度: $O(m \times n)$

- 空间复杂度: $O(n)$

## 代码
```cpp
class Solution {
public:
    int minDistance(string word1, string word2) {
        // LCS 最长公共子序列
        int m = word1.size();
        int n = word2.size();
        vector<int> dp(n + 1, 0);
        // 初始化就是全部都是 0
        for (int i = 1; i <= m; i++) {
            int pre = 0;
            for (int j = 1; j <= n; j++) {
                int tmp = dp[j]; // 改动之前拿到
                if (word1[i - 1] == word2[j - 1]) {
                    dp[j] = pre + 1;
                } else {
                    dp[j] = max(dp[j], dp[j - 1]);
                }
                // cout << dp[i][j] << ' ';
                pre = tmp; // 改动之前的, dp[i - 1][j - 1], 给下一个用
            }
            // cout << endl;
        }
        return  m + n - 2 * dp[n];
    }
};
```
