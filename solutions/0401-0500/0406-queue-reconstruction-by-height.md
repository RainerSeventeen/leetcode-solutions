---
id: 406
title: Queue Reconstruction by Height
difficulty: Medium
tags: [binary-indexed-tree, segment-tree, array, sorting]
created: 2026-02-20
---

# 406. 根据身高重建队列

## 题目链接
https://leetcode.cn/problems/queue-reconstruction-by-height/

## 题目描述
<p>假设有打乱顺序的一群人站成一个队列，数组 <code>people</code> 表示队列中一些人的属性（不一定按顺序）。每个 <code>people[i] = [h<sub>i</sub>, k<sub>i</sub>]</code> 表示第 <code>i</code> 个人的身高为 <code>h<sub>i</sub></code> ，前面 <strong>正好</strong> 有 <code>k<sub>i</sub></code><sub> </sub>个身高大于或等于 <code>h<sub>i</sub></code> 的人。</p>

<p>请你重新构造并返回输入数组 <code>people</code> 所表示的队列。返回的队列应该格式化为数组 <code>queue</code> ，其中 <code>queue[j] = [h<sub>j</sub>, k<sub>j</sub>]</code> 是队列中第 <code>j</code> 个人的属性（<code>queue[0]</code> 是排在队列前面的人）。</p>

<ul>
</ul>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
<strong>输出：</strong>[[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]]
<strong>解释：</strong>
编号为 0 的人身高为 5 ，没有身高更高或者相同的人排在他前面。
编号为 1 的人身高为 7 ，没有身高更高或者相同的人排在他前面。
编号为 2 的人身高为 5 ，有 2 个身高更高或者相同的人排在他前面，即编号为 0 和 1 的人。
编号为 3 的人身高为 6 ，有 1 个身高更高或者相同的人排在他前面，即编号为 1 的人。
编号为 4 的人身高为 4 ，有 4 个身高更高或者相同的人排在他前面，即编号为 0、1、2、3 的人。
编号为 5 的人身高为 7 ，有 1 个身高更高或者相同的人排在他前面，即编号为 1 的人。
因此 [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]] 是重新构造后的队列。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>people = [[6,0],[5,0],[4,0],[3,2],[2,2],[1,4]]
<strong>输出：</strong>[[4,0],[5,0],[2,2],[3,2],[1,4],[6,0]]
</pre>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 <= people.length <= 2000</code></li>
	<li><code>0 <= h<sub>i</sub> <= 10<sup>6</sup></code></li>
	<li><code>0 <= k<sub>i</sub> < people.length</code></li>
	<li>题目数据确保队列可以被重建</li>
</ul>


## 解题思路

先按身高从高到低排序，身高相同按 `k` 从小到大排序。这样处理时，已经放入队列的人都不矮于当前人；把当前人插入到下标 `k` 的位置，就能保证其前面恰好有 `k` 个身高不小于他的人。

排序后按顺序插入，最终得到满足条件的重建队列。

- 时间复杂度: $O(n^2)$
- 空间复杂度: $O(n)$

顺序插入会产生元素位移，因此整体为平方级时间。

## 相关专题
- [贪心与思维](../../topics/greedy-and-thinking.md)

## 代码
```cpp
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    static bool cmp(const vector<int>& a, const vector<int>& b) {
        if (a[0] != b[0]) return a[0] > b[0];
        return a[1] < b[1];
    }

    vector<vector<int>> reconstructQueue(vector<vector<int>>& people) {
        sort(people.begin(), people.end(), cmp);
        vector<vector<int>> que;
        for (const auto& p : people) {
            que.insert(que.begin() + p[1], p);
        }
        return que;
    }
};
```
