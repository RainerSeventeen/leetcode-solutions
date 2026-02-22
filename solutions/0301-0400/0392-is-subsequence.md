---
id: 392
title: Is Subsequence
difficulty: Easy
tags: [two-pointers, string, dynamic-programming]
created: 2026-02-21
---

# 392. 判断子序列

## 题目链接
https://leetcode.cn/problems/is-subsequence/

## 题目描述
<p>给定字符串 <strong>s</strong> 和 <strong>t</strong> ，判断 <strong>s</strong> 是否为 <strong>t</strong> 的子序列。</p>

<p>字符串的一个子序列是原始字符串删除一些（也可以不删除）字符而不改变剩余字符相对位置形成的新字符串。（例如，<code>"ace"</code>是<code>"abcde"</code>的一个子序列，而<code>"aec"</code>不是）。</p>

<p><strong>进阶：</strong></p>

<p>如果有大量输入的 S，称作 S1, S2, ... , Sk 其中 k >= 10亿，你需要依次检查它们是否为 T 的子序列。在这种情况下，你会怎样改变代码？</p>

<p><strong>致谢：</strong></p>

<p>特别感谢<strong> </strong><a href="https://leetcode.com/pbrother/">@pbrother </a>添加此问题并且创建所有测试用例。</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>s = "abc", t = "ahbgdc"
<strong>输出：</strong>true
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>s = "axc", t = "ahbgdc"
<strong>输出：</strong>false
</pre>

<p><strong>提示：</strong></p>

<ul>
	<li><code>0 <= s.length <= 100</code></li>
	<li><code>0 <= t.length <= 10^4</code></li>
	<li>两个字符串都只由小写字符组成。</li>
</ul>


## 解题思路

- 用二维 DP 模拟匹配过程，`dp[i][j]` 表示 `s` 前 `i` 和 `t` 前 `j` 的可匹配长度。
- 相等时来自左上角加一，不等时继承左侧（等价于删除 `t` 的当前字符）。

- 时间复杂度: $O(m \times n)$

- 空间复杂度: $O(m \times n)$

## 相关专题
- [动态规划](../../topics/dynamic-programming.md)

## 代码
```cpp
#include <stdio.h>
class Solution {
public:
    bool isSubsequence(string s, string t) {
        // 动态规划， dp 代表 s[i - 1] 和 t[j - 1] 最长相等子序列长度
        // 这道题只能删 t，s 不可以改，所以有很多是 0
        int m = s.size();
        int n = t.size();
        vector<vector<int>> dp(m + 1, vector<int>(n + 1, 0));
        for (int i = 1; i <= m; i++) {
            // cout << "i = " << i << ": ";
            for (int j = 1; j <=n; j++) {
                if (s[i - 1] == t[j - 1]) {
                    dp[i][j] = dp[i - 1][j - 1] + 1;
                } else {
                    // 不相等，等于把 t 中删除一个字母的结果
                    // 不够长直接就是0，也是合理的
                    dp[i][j] = dp[i][j - 1];
                }
                // cout << dp[i][j] << ' '; 
            }
            // cout << endl;
        }
        return bool (dp[m][n] == s.size());
    }
};
```
