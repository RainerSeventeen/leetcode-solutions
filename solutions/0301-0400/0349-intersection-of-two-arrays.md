---
id: 349
title: Intersection of Two Arrays
difficulty: Easy
tags: [array, hash-table, two-pointers, binary-search, sorting]
created: 2026-02-21
---

# 349. 两个数组的交集

## 题目链接
https://leetcode.cn/problems/intersection-of-two-arrays/

## 题目描述
<p>给定两个数组&nbsp;<code>nums1</code>&nbsp;和&nbsp;<code>nums2</code> ，返回 <em>它们的 <span data-keyword="array-intersection">交集</span></em>&nbsp;。输出结果中的每个元素一定是 <strong>唯一</strong> 的。我们可以 <strong>不考虑输出结果的顺序</strong> 。</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums1 = [1,2,2,1], nums2 = [2,2]
<strong>输出：</strong>[2]
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums1 = [4,9,5], nums2 = [9,4,9,8,4]
<strong>输出：</strong>[9,4]
<strong>解释：</strong>[4,9] 也是可通过的
</pre>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums1.length, nums2.length &lt;= 1000</code></li>
	<li><code>0 &lt;= nums1[i], nums2[i] &lt;= 1000</code></li>
</ul>


## 解题思路

先把 `nums1` 放入哈希集合，便于 `O(1)` 判断元素是否存在。
遍历 `nums2`，若元素在集合中就加入答案集合，自动去重。
最后把答案集合转成数组返回即可。
- 时间复杂度: $O(m+n)$
- 空间复杂度: $O(m+n)$

## 代码
```cpp
#include <unordered_set>
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
        unordered_set<int> s(nums1.begin(), nums1.end());
        unordered_set<int> ans;
        for (int y : nums2) {
            if (s.count(y)) ans.insert(y);
        }
        return vector<int>(ans.begin(), ans.end());
    }
};
```
