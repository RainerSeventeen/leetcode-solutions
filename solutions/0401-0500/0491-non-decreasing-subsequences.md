---
id: 491
title: Non-decreasing Subsequences
difficulty: Medium
tags: [bit-manipulation, array, hash-table, backtracking]
created: 2026-02-20
---

# 491. 非递减子序列

## 题目链接
https://leetcode.cn/problems/non-decreasing-subsequences/

## 题目描述
<p>给你一个整数数组 <code>nums</code> ，找出并返回所有该数组中不同的递增子序列，递增子序列中 <strong>至少有两个元素</strong> 。你可以按 <strong>任意顺序</strong> 返回答案。</p>

<p>数组中可能含有重复元素，如出现两个整数相等，也可以视作递增序列的一种特殊情况。</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [4,6,7,7]
<strong>输出：</strong>[[4,6],[4,6,7],[4,6,7,7],[4,7],[4,7,7],[6,7],[6,7,7],[7,7]]
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [4,4,3,2,1]
<strong>输出：</strong>[[4,4]]
</pre>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 15</code></li>
	<li><code>-100 &lt;= nums[i] &lt;= 100</code></li>
</ul>


## 解题思路

这题同时要求“子序列递增”和“结果去重”。回溯时维护 `path` 与当前起点 `start`，并记录上一位已选值 `pre`，只有 `nums[i] >= pre` 才能继续向下扩展，保证序列非递减。只要 `path` 长度至少为 2，就把它加入答案。

难点是同一层去重：每层递归内部用一个局部 `unordered_set<int> used`，避免当前层重复选择同值元素产生等价分支。注意这个 `used` 必须是“层内变量”，不能复用全局状态。

- 时间复杂度: $O(n \cdot 2^n)$
- 空间复杂度: $O(n)$

不计答案存储。

## 代码
```cpp
#include <unordered_set>
#include <vector>
using namespace std;

class Solution {
public:
    vector<vector<int>> findSubsequences(vector<int>& nums) {
        ret.clear();
        path.clear();
        backtrack(0, INT_MIN, nums);
        return ret;
    }

private:
    vector<vector<int>> ret;
    vector<int> path;

    void backtrack(int start, int pre, vector<int>& nums) {
        if (path.size() > 1) ret.push_back(path);

        unordered_set<int> used;
        for (int i = start; i < static_cast<int>(nums.size()); i++) {
            if (used.count(nums[i])) continue;
            if (pre > nums[i]) continue;

            used.insert(nums[i]);
            path.push_back(nums[i]);
            backtrack(i + 1, nums[i], nums);
            path.pop_back();
        }
    }
};
```
