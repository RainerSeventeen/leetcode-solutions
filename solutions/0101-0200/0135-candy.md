---
id: 135
title: Candy
difficulty: Hard
tags: [greedy, array]
created: 2026-02-20
---

# 135. 分发糖果

## 题目链接
https://leetcode.cn/problems/candy/

## 题目描述
<p><code>n</code> 个孩子站成一排。给你一个整数数组 <code>ratings</code> 表示每个孩子的评分。</p>

<p>你需要按照以下要求，给这些孩子分发糖果：</p>

<ul>
	<li>每个孩子至少分配到 <code>1</code> 个糖果。</li>
	<li>相邻两个孩子中，评分更高的那个会获得更多的糖果。</li>
</ul>

<p>请你给每个孩子分发糖果，计算并返回需要准备的 <strong>最少糖果数目</strong> 。</p>

<p><strong>示例&nbsp;1：</strong></p>

<pre>
<strong>输入：</strong>ratings = [1,0,2]
<strong>输出：</strong>5
<strong>解释：</strong>你可以分别给第一个、第二个、第三个孩子分发 2、1、2 颗糖果。
</pre>

<p><strong>示例&nbsp;2：</strong></p>

<pre>
<strong>输入：</strong>ratings = [1,2,2]
<strong>输出：</strong>4
<strong>解释：</strong>你可以分别给第一个、第二个、第三个孩子分发 1、2、1 颗糖果。
     第三个孩子只得到 1 颗糖果，这满足题面中的两个条件。</pre>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == ratings.length</code></li>
	<li><code>1 &lt;= n &lt;= 2 * 10<sup>4</sup></code></li>
	<li><code>0 &lt;= ratings[i] &lt;= 2 * 10<sup>4</sup></code></li>
</ul>


## 解题思路

相邻约束同时作用在左右两个方向，因此分两次贪心扫描：
第一次从左到右，满足“右边评分更高就比左边多一颗”；第二次从右到左，满足“左边评分更高就比右边多一颗”。第二次更新时要和第一次结果取 `max`，避免破坏已满足的另一侧约束。

最终把每个位置的糖果数求和即可。

- 时间复杂度: $O(n)$
- 空间复杂度: $O(n)$

需要一个长度为 `n` 的数组记录每个孩子的糖果数。

## 代码
```cpp
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    int candy(vector<int>& ratings) {
        int n = static_cast<int>(ratings.size());
        vector<int> candies(n, 1);
        for (int i = 1; i < n; i++) {
            if (ratings[i] > ratings[i - 1]) {
                candies[i] = candies[i - 1] + 1;
            }
        }
        for (int i = n - 2; i >= 0; i--) {
            if (ratings[i] > ratings[i + 1]) {
                candies[i] = max(candies[i], candies[i + 1] + 1);
            }
        }
        int sum = 0;
        for (int c : candies) sum += c;
        return sum;
    }
};
```
