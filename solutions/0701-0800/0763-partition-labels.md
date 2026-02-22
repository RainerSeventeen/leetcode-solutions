---
id: 763
title: Partition Labels
difficulty: Medium
tags: [greedy, hash-table, two-pointers, string]
created: 2026-02-21
---

# 763. 划分字母区间

## 题目链接
https://leetcode.cn/problems/partition-labels/

## 题目描述
<p>给你一个字符串 <code>s</code> 。我们要把这个字符串划分为尽可能多的片段，同一字母最多出现在一个片段中。例如，字符串&nbsp;<code>"ababcc"</code> 能够被分为 <code>["abab", "cc"]</code>，但类似&nbsp;<code>["aba", "bcc"]</code> 或&nbsp;<code>["ab", "ab", "cc"]</code> 的划分是非法的。</p>

<p>注意，划分结果需要满足：将所有划分结果按顺序连接，得到的字符串仍然是 <code>s</code> 。</p>

<p>返回一个表示每个字符串片段的长度的列表。</p>

<strong class="example">示例 1：</strong>

<pre>
<strong>输入：</strong>s = "ababcbacadefegdehijhklij"
<strong>输出：</strong>[9,7,8]
<strong>解释：</strong>
划分结果为 "ababcbaca"、"defegde"、"hijhklij" 。
每个字母最多出现在一个片段中。
像 "ababcbacadefegde", "hijhklij" 这样的划分是错误的，因为划分的片段数较少。 </pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<strong>输入：</strong>s = "eccbbbbdec"
<strong>输出：</strong>[10]
</pre>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 500</code></li>
	<li><code>s</code> 仅由小写英文字母组成</li>
</ul>


## 解题思路

- 先记录每个字符在字符串中的最后出现位置。
- 扫描时维护当前分段的最远右边界，遍历到边界就能切出一个合法分段。

- 时间复杂度: $O(n)$

- 空间复杂度: $O(1)$

## 代码
```cpp
#include <vector>
#include <utility>
class Solution {
public:
    vector<int> partitionLabels(string s) {
        // 统计字符出现的最远位置
        int far[26] = {0};
        for (int i = 0; i < s.size(); i++) {
            far[s[i] - 'a'] = i;
        }
        vector<int> ret;
        int max_dis = -1;
        int pre = -1;
        for (int i = 0; i < s.size(); i++) {
            // 获取当前区间内不字母的最远位置
            max_dis = max(far[s[i] - 'a'], max_dis);
            // 区间内所有最远距离已经到达
            if (i == max_dis) {
                ret.push_back(i - pre);
                pre = i;
                max_dis = -1;
            }
        }
        return ret;
    }
};
```
