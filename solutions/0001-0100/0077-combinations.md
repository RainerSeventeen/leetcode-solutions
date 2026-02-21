---
id: 77
title: Combinations
difficulty: Medium
tags: [backtracking]
created: 2026-02-21
---

# 77. 组合

## 题目链接
https://leetcode.cn/problems/combinations/

## 题目描述
<p>给定两个整数 <code>n</code> 和 <code>k</code>，返回范围 <code>[1, n]</code> 中所有可能的 <code>k</code> 个数的组合。</p>

<p>你可以按 <strong>任何顺序</strong> 返回答案。</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>n = 4, k = 2
<strong>输出：</strong>
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>n = 1, k = 1
<strong>输出：</strong>[[1]]</pre>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 <= n <= 20</code></li>
	<li><code>1 <= k <= n</code></li>
</ul>


## 解题思路

标准回溯：从 `start` 开始枚举可选数字，加入路径后递归到下一层。
当路径长度达到 `k` 时记录当前组合，回溯时弹出末尾元素继续尝试。
- 时间复杂度: $O(C(n,k)\cdot k)$
- 空间复杂度: $O(k)$

## 代码
```cpp
class Solution {
public:
    vector<vector<int>> ret;
    vector<int> path;

    vector<vector<int>> combine(int n, int k) {
        ret.clear();
        path.clear();
        backtrace(n, k, 1);
        return ret;
    }
    void backtrace(int n, int k, int start) {
        if (path.size() == k) {
            // 满足数组的条件
            ret.push_back(path);
            return;
        }
        for (int i = start; i <= n; i++) {
            path.push_back(i);
            backtrace(n, k, i + 1);
            path.pop_back();
        } 
    }
};
```
