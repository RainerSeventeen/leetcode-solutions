---
id: 455
title: Assign Cookies
difficulty: Easy
tags: [greedy, array, two-pointers, sorting]
created: 2026-02-21
---

# 455. 分发饼干

## 题目链接
https://leetcode.cn/problems/assign-cookies/

## 题目描述
<p>假设你是一位很棒的家长，想要给你的孩子们一些小饼干。但是，每个孩子最多只能给一块饼干。</p>

<p>对每个孩子 <code>i</code>，都有一个胃口值&nbsp;<code>g[i]</code><sub>，</sub>这是能让孩子们满足胃口的饼干的最小尺寸；并且每块饼干 <code>j</code>，都有一个尺寸 <code>s[j]</code><sub>&nbsp;</sub>。如果 <code>s[j]&nbsp;&gt;= g[i]</code>，我们可以将这个饼干 <code>j</code> 分配给孩子 <code>i</code> ，这个孩子会得到满足。你的目标是满足尽可能多的孩子，并输出这个最大数值。</p>
&nbsp;

<p><strong>示例&nbsp;1:</strong></p>

<pre>
<strong>输入:</strong> g = [1,2,3], s = [1,1]
<strong>输出:</strong> 1
<strong>解释:</strong> 
你有三个孩子和两块小饼干，3 个孩子的胃口值分别是：1,2,3。
虽然你有两块小饼干，由于他们的尺寸都是 1，你只能让胃口值是 1 的孩子满足。
所以你应该输出 1。
</pre>

<p><strong>示例&nbsp;2:</strong></p>

<pre>
<strong>输入:</strong> g = [1,2], s = [1,2,3]
<strong>输出:</strong> 2
<strong>解释:</strong> 
你有两个孩子和三块小饼干，2 个孩子的胃口值分别是 1,2。
你拥有的饼干数量和尺寸都足以让所有孩子满足。
所以你应该输出 2。
</pre>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= g.length &lt;= 3 * 10<sup>4</sup></code></li>
	<li><code>0 &lt;= s.length &lt;= 3 * 10<sup>4</sup></code></li>
	<li><code>1 &lt;= g[i], s[j] &lt;=&nbsp;2<sup>31</sup> - 1</code></li>
</ul>

<p><strong>注意：</strong>本题与&nbsp;<a href="https://leetcode.cn/problems/maximum-matching-of-players-with-trainers/">2410. 运动员和训练师的最大匹配数</a>&nbsp;题相同。</p>


## 解题思路

将孩子胃口和饼干尺寸都排序，用双指针从大到小匹配。
每次优先用当前最大饼干满足当前最大胃口，能满足就计数并同时左移，否则仅移动孩子指针。
- 时间复杂度: $O(n \log n + m \log m)$
- 空间复杂度: $O(\log n + \log m)$

## 代码
```cpp
class Solution {
public:
    int findContentChildren(vector<int>& g, vector<int>& s) {
        // 贪心算法，遍历饼干，并查找能满足的最大胃口的小孩子
        sort(g.begin(), g.end());
        sort(s.begin(), s.end());
        int result = 0;
        int j = s.size() - 1;
        for (int i = g.size() - 1; i >= 0; i--) {
            if (j >= 0 && g[i] <= s[j]) {
                result++;
                j--;
            }
        }
        return result;
    }
};
```
