---
id: 503
title: Next Greater Element II
difficulty: Medium
tags: [stack, array, monotonic-stack]
created: 2026-02-20
---

# 503. 下一个更大元素 II

## 题目链接
https://leetcode.cn/problems/next-greater-element-ii/

## 题目描述
<p>给定一个循环数组&nbsp;<code>nums</code>&nbsp;（&nbsp;<code>nums[nums.length - 1]</code>&nbsp;的下一个元素是&nbsp;<code>nums[0]</code>&nbsp;），返回&nbsp;<em><code>nums</code>&nbsp;中每个元素的 <strong>下一个更大元素</strong></em> 。</p>

<p>数字 <code>x</code>&nbsp;的 <strong>下一个更大的元素</strong> 是按数组遍历顺序，这个数字之后的第一个比它更大的数，这意味着你应该循环地搜索它的下一个更大的数。如果不存在，则输出 <code>-1</code>&nbsp;。</p>

<p><strong>示例 1:</strong></p>

<pre>
<strong>输入:</strong> nums = [1,2,1]
<strong>输出:</strong> [2,-1,2]
<strong>解释:</strong> 第一个 1 的下一个更大的数是 2；
数字 2 找不到下一个更大的数； 
第二个 1 的下一个最大的数需要循环搜索，结果也是 2。
</pre>

<p><strong>示例 2:</strong></p>

<pre>
<strong>输入:</strong> nums = [1,2,3,4,3]
<strong>输出:</strong> [2,3,4,-1,4]
</pre>

<p><strong>提示:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>4</sup></code></li>
	<li><code>-10<sup>9</sup>&nbsp;&lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
</ul>


## 解题思路

循环数组可以通过遍历 `2n` 次并用 `i % n` 映射到真实下标来模拟。维护单调递减栈（存下标），当当前值比栈顶下标对应值大时，说明找到了栈顶元素的下一个更大值，弹栈并赋值。

只在第一轮（`i < n`）把下标入栈，第二轮只负责触发补答案，避免重复入栈。

- 时间复杂度: $O(n)$

- 空间复杂度: $O(n)$

## 相关专题
- [单调栈](../../topics/monotonic-stack.md)

## 代码
```cpp
class Solution {
public:
    vector<int> nextGreaterElements(vector<int>& nums) {
        int n = nums.size();
        vector<int> ans(n, -1);
        vector<int> stk;
        stk.reserve(n);

        for (int i = 0; i < 2 * n; ++i) {
            int j = i % n;
            while (!stk.empty() && nums[j] > nums[stk.back()]) {
                ans[stk.back()] = nums[j];
                stk.pop_back();
            }
            if (i < n) {
                stk.push_back(j);
            }
        }
        return ans;
    }
};
```
