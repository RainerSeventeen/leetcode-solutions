---
id: 40
title: Combination Sum II
difficulty: Medium
tags: [array, backtracking]
created: 2026-02-20
---

# 40. 组合总和 II

## 题目链接
https://leetcode.cn/problems/combination-sum-ii/

## 题目描述
<p>给定一个候选人编号的集合&nbsp;<code>candidates</code>&nbsp;和一个目标数&nbsp;<code>target</code>&nbsp;，找出&nbsp;<code>candidates</code>&nbsp;中所有可以使数字和为&nbsp;<code>target</code>&nbsp;的组合。</p>

<p><code>candidates</code>&nbsp;中的每个数字在每个组合中只能使用&nbsp;<strong>一次</strong>&nbsp;。</p>

<p><strong>注意：</strong>解集不能包含重复的组合。&nbsp;</p>

<p><strong>示例&nbsp;1:</strong></p>

<pre>
<strong>输入:</strong> candidates =&nbsp;<code>[10,1,2,7,6,1,5]</code>, target =&nbsp;<code>8</code>,
<strong>输出:</strong>
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]</pre>

<p><strong>示例&nbsp;2:</strong></p>

<pre>
<strong>输入:</strong> candidates =&nbsp;[2,5,2,1,2], target =&nbsp;5,
<strong>输出:</strong>
[
[1,2,2],
[5]
]</pre>

<p><strong>提示:</strong></p>

<ul>
	<li><code>1 &lt;=&nbsp;candidates.length &lt;= 100</code></li>
	<li><code>1 &lt;=&nbsp;candidates[i] &lt;= 50</code></li>
	<li><code>1 &lt;= target &lt;= 30</code></li>
</ul>


## 解题思路

先对数组排序，让相同元素相邻，这样就能在同一层搜索时通过 `i > start && candidates[i] == candidates[i-1]` 跳过重复分支，避免生成重复组合。递归参数里维护 `start` 和当前剩余和 `remain`，每次从 `start` 往后枚举，把当前数加入路径后递归到 `i + 1`，保证每个位置最多使用一次。

当当前候选值已经大于 `remain` 时，可以直接 `break`，因为后面的数只会更大，这是排序后最有效的剪枝。`remain == 0` 时收集当前路径，`remain < 0` 或枚举结束时回溯。

- 时间复杂度: $O(n \log n + n \cdot 2^n)$
- 空间复杂度: $O(n)$（不含答案存储）

## 代码
```cpp
class Solution {
public:
    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
        path.clear();
        ret.clear();
        sort(candidates.begin(), candidates.end());
        traceback(0, candidates, target);
        return ret;
    }

private:
    vector<int> path;
    vector<vector<int>> ret;

    void traceback(int start, const vector<int>& candidates, int remain) {
        if (remain < 0) return;
        if (remain == 0) {
            ret.push_back(path);
            return;
        }

        for (int i = start; i < static_cast<int>(candidates.size()); i++) {
            if (i > start && candidates[i - 1] == candidates[i]) continue;
            if (candidates[i] > remain) break;

            path.push_back(candidates[i]);
            traceback(i + 1, candidates, remain - candidates[i]);
            path.pop_back();
        }
    }
};
```
