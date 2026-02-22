---
id: 739
title: Daily Temperatures
difficulty: Medium
tags: [stack, array, monotonic-stack]
created: 2026-02-20
---

# 739. 每日温度

## 题目链接
https://leetcode.cn/problems/daily-temperatures/

## 题目描述
<p>给定一个整数数组&nbsp;<code>temperatures</code>&nbsp;，表示每天的温度，返回一个数组&nbsp;<code>answer</code>&nbsp;，其中&nbsp;<code>answer[i]</code>&nbsp;是指对于第 <code>i</code> 天，下一个更高温度出现在几天后。如果气温在这之后都不会升高，请在该位置用&nbsp;<code>0</code> 来代替。</p>

<p><strong>示例 1:</strong></p>

<pre>
<strong>输入:</strong> temperatures = [73,74,75,71,69,72,76,73]
<strong>输出:</strong>&nbsp;[1,1,4,2,1,1,0,0]
</pre>

<p><strong>示例 2:</strong></p>

<pre>
<strong>输入:</strong> temperatures = [30,40,50,60]
<strong>输出:</strong>&nbsp;[1,1,1,0]
</pre>

<p><strong>示例 3:</strong></p>

<pre>
<strong>输入:</strong> temperatures = [30,60,90]
<strong>输出: </strong>[1,1,0]</pre>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;=&nbsp;temperatures.length &lt;= 10<sup>5</sup></code></li>
	<li><code>30 &lt;=&nbsp;temperatures[i]&nbsp;&lt;= 100</code></li>
</ul>


## 解题思路

维护一个单调递减栈，栈里存放下标而不是温度值。遍历到 `i` 时，如果当前温度比栈顶下标对应的温度高，说明找到了栈顶那一天的下一个更高温度，持续弹栈并写答案 `i - idx`。

这样每个下标最多入栈一次、出栈一次，线性时间就能完成。

- 时间复杂度: $O(n)$

- 空间复杂度: $O(n)$

## 相关专题
- [单调栈](../../topics/monotonic-stack.md)

## 代码
```cpp
class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        int n = temperatures.size();
        vector<int> ans(n, 0);
        vector<int> stk;
        stk.reserve(n);

        for (int i = 0; i < n; ++i) {
            while (!stk.empty() && temperatures[i] > temperatures[stk.back()]) {
                int idx = stk.back();
                stk.pop_back();
                ans[idx] = i - idx;
            }
            stk.push_back(i);
        }
        return ans;
    }
};
```
