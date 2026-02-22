---
id: 216
title: Combination Sum III
difficulty: Medium
tags: [array, backtracking]
created: 2026-02-21
---

# 216. 组合总和 III

## 题目链接
https://leetcode.cn/problems/combination-sum-iii/

## 题目描述
<p>找出所有相加之和为&nbsp;<code>n</code><em> </em>的&nbsp;<code>k</code><strong>&nbsp;</strong>个数的组合，且满足下列条件：</p>

<ul>
	<li>只使用数字1到9</li>
	<li>每个数字&nbsp;<strong>最多使用一次</strong>&nbsp;</li>
</ul>

<p>返回 <em>所有可能的有效组合的列表</em> 。该列表不能包含相同的组合两次，组合可以以任何顺序返回。</p>

<p><strong>示例 1:</strong></p>

<pre>
<strong>输入:</strong> <em><strong>k</strong></em> = 3, <em><strong>n</strong></em> = 7
<strong>输出:</strong> [[1,2,4]]
<strong>解释:</strong>
1 + 2 + 4 = 7
没有其他符合的组合了。</pre>

<p><strong>示例 2:</strong></p>

<pre>
<strong>输入:</strong> <em><strong>k</strong></em> = 3, <em><strong>n</strong></em> = 9
<strong>输出:</strong> [[1,2,6], [1,3,5], [2,3,4]]
<strong>解释:
</strong>1 + 2 + 6 = 9
1 + 3 + 5 = 9
2 + 3 + 4 = 9
没有其他符合的组合了。</pre>

<p><strong>示例 3:</strong></p>

<pre>
<strong>输入:</strong> k = 4, n = 1
<strong>输出:</strong> []
<strong>解释:</strong> 不存在有效的组合。
在[1,9]范围内使用4个不同的数字，我们可以得到的最小和是1+2+3+4 = 10，因为10 &gt; 1，没有有效的组合。
</pre>

<p><strong>提示:</strong></p>

<ul>
	<li><code>2 &lt;= k &lt;= 9</code></li>
	<li><code>1 &lt;= n &lt;= 60</code></li>
</ul>


## 解题思路

回溯枚举 `1~9` 的组合，路径长度到 `k` 时检查当前和是否等于 `n`。
利用 `start` 保证数字不重复递增选择，并在循环上界做剪枝减少无效分支。
- 时间复杂度: $O(C(9,k))$
- 空间复杂度: $O(k)$

## 相关专题
- [链表、树与回溯](../../topics/linked-list-tree-backtracking.md)

## 代码
```cpp
class Solution {
public:
    int sum;
    vector<int> path;
    vector<vector<int>> ret;
    vector<vector<int>> combinationSum3(int k, int n) {
        sum = 0;
        int start = 1;
        path.clear();
        ret.clear();
        backtrace(k, n, start);
        return ret;
    }

    void backtrace(int k, int n, int start) {
        // 终止条件，k 个数字就停止了
        if (path.size() == k) {
            if (sum == n) ret.push_back(path);
            return;
        }
        if (sum > n) return;
        for (int i = start; i <= 9 - (k - path.size()) + 1; i++) {
            path.push_back(i);
            sum += i;
            backtrace(k, n, i + 1);
            // 回溯对称流程
            sum -= i;
            path.pop_back();
        }
    }
};
```
