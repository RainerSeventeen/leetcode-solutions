---
id: 1047
title: Maximize Sum Of Array After K Negations
difficulty: Easy
tags: [greedy, array, sorting]
created: 2026-02-21
---

# 1047. K 次取反后最大化的数组和

## 题目链接
https://leetcode.cn/problems/maximize-sum-of-array-after-k-negations/

## 题目描述
<p>给你一个整数数组 <code>nums</code> 和一个整数 <code>k</code> ，按以下方法修改该数组：</p>

<ul>
	<li>选择某个下标 <code>i</code>&nbsp;并将 <code>nums[i]</code> 替换为 <code>-nums[i]</code> 。</li>
</ul>

<p>重复这个过程恰好 <code>k</code> 次。可以多次选择同一个下标 <code>i</code> 。</p>

<p>以这种方式修改数组后，返回数组 <strong>可能的最大和</strong> 。</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [4,2,3], k = 1
<strong>输出：</strong>5
<strong>解释：</strong>选择下标 1 ，nums 变为 [4,-2,3] 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [3,-1,0,2], k = 3
<strong>输出：</strong>6
<strong>解释：</strong>选择下标 (1, 2, 2) ，nums 变为 [3,1,0,2] 。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>nums = [2,-3,-1,5,-4], k = 2
<strong>输出：</strong>13
<strong>解释：</strong>选择下标 (1, 4) ，nums 变为 [2,3,-1,5,4] 。
</pre>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>4</sup></code></li>
	<li><code>-100 &lt;= nums[i] &lt;= 100</code></li>
	<li><code>1 &lt;= k &lt;= 10<sup>4</sup></code></li>
</ul>


## 解题思路

先按绝对值从小到大排序，再从后往前优先把负数翻转为正数，尽量提升总和。
若 `k` 还有剩余且为奇数，只需再翻转一次绝对值最小的元素（即排序后首元素）。
- 时间复杂度: $O(n \log n)$
- 空间复杂度: $O(\log n)$

## 代码
```cpp
class Solution {
public:
    static bool _cmp(int a, int b) {
        return abs(a) < abs(b);
    }
    int largestSumAfterKNegations(vector<int>& nums, int k) {
        // 贪心算法，第一次选择最大的数值进行反转
        sort(nums.begin(), nums.end(), _cmp);
        for (int i = nums.size() - 1; i >= 0; i--) {
            if (nums[i] < 0 && k > 0) {
                nums[i] *= -1;
                k--;
            }
        }
        if (k > 0 && k % 2 == 1) {
            nums[0] *= -1;           
        }
        int ret = 0;
        for (int a : nums) ret += a;
        return ret; 
    }
};
```
