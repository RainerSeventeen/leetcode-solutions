---
id: 45
title: Jump Game II
difficulty: Medium
tags: [greedy, array, dynamic-programming]
created: 2026-02-20
---

# 45. 跳跃游戏 II

## 题目链接
https://leetcode.cn/problems/jump-game-ii/

## 题目描述
<p>给定一个长度为 <code>n</code> 的 <strong>0 索引</strong>整数数组 <code>nums</code>。初始位置在下标 0。</p>

<p>每个元素 <code>nums[i]</code> 表示从索引 <code>i</code> 向后跳转的最大长度。换句话说，如果你在索引&nbsp;<code>i</code>&nbsp;处，你可以跳转到任意 <code>(i + j)</code> 处：</p>

<ul>
	<li><code>0 &lt;= j &lt;= nums[i]</code>&nbsp;且</li>
	<li><code>i + j &lt; n</code></li>
</ul>

<p>返回到达&nbsp;<code>n - 1</code>&nbsp;的最小跳跃次数。测试用例保证可以到达 <code>n - 1</code>。</p>

<p><strong>示例 1:</strong></p>

<pre>
<strong>输入:</strong> nums = [2,3,1,1,4]
<strong>输出:</strong> 2
<strong>解释:</strong> 跳到最后一个位置的最小跳跃数是 <code>2</code>。
&nbsp;    从下标为 0 跳到下标为 1 的位置，跳&nbsp;<code>1</code>&nbsp;步，然后跳&nbsp;<code>3</code>&nbsp;步到达数组的最后一个位置。
</pre>

<p><strong>示例 2:</strong></p>

<pre>
<strong>输入:</strong> nums = [2,3,0,1,4]
<strong>输出:</strong> 2
</pre>

<p><strong>提示:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>4</sup></code></li>
	<li><code>0 &lt;= nums[i] &lt;= 1000</code></li>
	<li>题目保证可以到达&nbsp;<code>n - 1</code></li>
</ul>


## 解题思路

贪心地按“层”推进。把一次跳跃能覆盖到的位置区间视作一层，遍历当前层内所有下标，计算下一层最远能到哪里。当下标走到当前层右边界时，说明这一跳已经用完，步数加一，并把边界更新为下一层最远位置。

这个过程和 BFS 按层扩展的思想一致，但不需要显式队列，只用两个边界变量即可。

- 时间复杂度: $O(n)$
- 空间复杂度: $O(1)$

每个位置只会被扫描一次。

## 代码
```cpp
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    int jump(vector<int>& nums) {
        if (nums.size() == 1) return 0;
        int currdis = 0;
        int nextdis = 0;
        int ans = 0;
        for (int i = 0; i < static_cast<int>(nums.size()); i++) {
            nextdis = max(nextdis, i + nums[i]);
            if (i == currdis) {
                ans++;
                currdis = nextdis;
                if (currdis >= static_cast<int>(nums.size()) - 1) {
                    return ans;
                }
            }
        }
        return ans;
    }
};
```
