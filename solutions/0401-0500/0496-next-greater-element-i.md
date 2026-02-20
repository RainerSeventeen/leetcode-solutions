---
id: 496
title: Next Greater Element I
difficulty: Easy
tags: [stack, array, hash-table, monotonic-stack]
created: 2026-02-20
---

# 496. 下一个更大元素 I

## 题目链接
https://leetcode.cn/problems/next-greater-element-i/

## 题目描述
<p><code>nums1</code>&nbsp;中数字&nbsp;<code>x</code>&nbsp;的 <strong>下一个更大元素</strong> 是指&nbsp;<code>x</code>&nbsp;在&nbsp;<code>nums2</code> 中对应位置 <strong>右侧</strong> 的 <strong>第一个</strong> 比&nbsp;<code>x</code><strong>&nbsp;</strong>大的元素。</p>

<p>给你两个<strong> 没有重复元素</strong> 的数组&nbsp;<code>nums1</code> 和&nbsp;<code>nums2</code> ，下标从 <strong>0</strong> 开始计数，其中<code>nums1</code>&nbsp;是&nbsp;<code>nums2</code>&nbsp;的子集。</p>

<p>对于每个 <code>0 &lt;= i &lt; nums1.length</code> ，找出满足 <code>nums1[i] == nums2[j]</code> 的下标 <code>j</code> ，并且在 <code>nums2</code> 确定 <code>nums2[j]</code> 的 <strong>下一个更大元素</strong> 。如果不存在下一个更大元素，那么本次查询的答案是 <code>-1</code> 。</p>

<p>返回一个长度为&nbsp;<code>nums1.length</code> 的数组<em> </em><code>ans</code><em> </em>作为答案，满足<em> </em><code>ans[i]</code><em> </em>是如上所述的 <strong>下一个更大元素</strong> 。</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums1 = [4,1,2], nums2 = [1,3,4,2].
<strong>输出：</strong>[-1,3,-1]
<strong>解释：</strong>nums1 中每个值的下一个更大元素如下所述：
- 4 ，用加粗斜体标识，nums2 = [1,3,<strong>4</strong>,2]。不存在下一个更大元素，所以答案是 -1 。
- 1 ，用加粗斜体标识，nums2 = [<em><strong>1</strong></em>,3,4,2]。下一个更大元素是 3 。
- 2 ，用加粗斜体标识，nums2 = [1,3,4,<em><strong>2</strong></em>]。不存在下一个更大元素，所以答案是 -1 。</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums1 = [2,4], nums2 = [1,2,3,4].
<strong>输出：</strong>[3,-1]
<strong>解释：</strong>nums1 中每个值的下一个更大元素如下所述：
- 2 ，用加粗斜体标识，nums2 = [1,<em><strong>2</strong></em>,3,4]。下一个更大元素是 3 。
- 4 ，用加粗斜体标识，nums2 = [1,2,3,<em><strong>4</strong></em>]。不存在下一个更大元素，所以答案是 -1 。
</pre>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums1.length &lt;= nums2.length &lt;= 1000</code></li>
	<li><code>0 &lt;= nums1[i], nums2[i] &lt;= 10<sup>4</sup></code></li>
	<li><code>nums1</code>和<code>nums2</code>中所有整数 <strong>互不相同</strong></li>
	<li><code>nums1</code> 中的所有整数同样出现在 <code>nums2</code> 中</li>
</ul>

<p><strong>进阶：</strong>你可以设计一个时间复杂度为 <code>O(nums1.length + nums2.length)</code> 的解决方案吗？</p>


## 解题思路

先把 `nums1` 的值映射到答案下标，方便后续 O(1) 回填。然后扫描 `nums2`，维护一个单调递减栈（存值）。当当前值 `x` 大于栈顶值时，说明找到了栈顶元素的下一个更大值，持续弹栈并更新对应答案。

因为 `nums2` 每个元素只会入栈出栈一次，所以总复杂度是线性的。

- 时间复杂度: $O(|nums1| + |nums2|)$

- 空间复杂度: $O(|nums1| + |nums2|)$

## 代码
```cpp
class Solution {
public:
    vector<int> nextGreaterElement(vector<int>& nums1, vector<int>& nums2) {
        unordered_map<int, int> pos;
        pos.reserve(nums1.size());
        for (int i = 0; i < (int)nums1.size(); ++i) {
            pos[nums1[i]] = i;
        }

        vector<int> ans(nums1.size(), -1);
        vector<int> stk;
        stk.reserve(nums2.size());

        for (int x : nums2) {
            while (!stk.empty() && x > stk.back()) {
                int v = stk.back();
                stk.pop_back();
                auto it = pos.find(v);
                if (it != pos.end()) {
                    ans[it->second] = x;
                }
            }
            stk.push_back(x);
        }

        return ans;
    }
};
```
