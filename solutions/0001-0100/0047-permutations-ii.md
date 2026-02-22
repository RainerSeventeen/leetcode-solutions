---
id: 47
title: Permutations II
difficulty: Medium
tags: [array, backtracking, sorting]
created: 2026-02-20
---

# 47. 全排列 II

## 题目链接
https://leetcode.cn/problems/permutations-ii/

## 题目描述
<p>给定一个可包含重复数字的序列 <code>nums</code> ，<em><strong>按任意顺序</strong></em> 返回所有不重复的全排列。</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,1,2]
<strong>输出：</strong>
[[1,1,2],
 [1,2,1],
 [2,1,1]]
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,2,3]
<strong>输出：</strong>[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
</pre>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 8</code></li>
	<li><code>-10 &lt;= nums[i] &lt;= 10</code></li>
</ul>


## 解题思路

全排列问题没有 `startIndex` 的概念，每一层都要尝试所有还没用过的位置，所以用 `used[i]` 控制纵向（同一条路径）不能重复使用同一下标。为了去掉重复排列，先排序，再做同层去重：当 `nums[i] == nums[i-1]` 且 `used[i-1] == false` 时跳过当前元素。

这个条件的含义是：同一层里，如果前一个相同值还没被选，当前值也不应作为该层起点，否则会产生重复排列；但如果前一个值已在当前路径中使用，就允许选择当前值继续构造不同分支。路径长度等于 `nums.size()` 时收集答案并返回。

- 时间复杂度: $O(n \cdot n!)$
- 空间复杂度: $O(n)$

不计答案存储。

## 相关专题
- [链表、树与回溯](../../topics/linked-list-tree-backtracking.md)

## 代码
```cpp
class Solution {
public:
    vector<vector<int>> permuteUnique(vector<int>& nums) {
        ret.clear();
        path.clear();
        sort(nums.begin(), nums.end());
        vector<bool> used(nums.size(), false);
        traceback(used, nums);
        return ret;
    }

private:
    vector<vector<int>> ret;
    vector<int> path;

    void traceback(vector<bool>& used, const vector<int>& nums) {
        if (path.size() == nums.size()) {
            ret.push_back(path);
            return;
        }

        for (int i = 0; i < static_cast<int>(nums.size()); i++) {
            if (i > 0 && nums[i] == nums[i - 1] && used[i - 1] == false) continue;
            if (used[i]) continue;

            path.push_back(nums[i]);
            used[i] = true;
            traceback(used, nums);
            used[i] = false;
            path.pop_back();
        }
    }
};
```
