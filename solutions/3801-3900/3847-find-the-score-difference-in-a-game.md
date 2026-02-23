---
id: 3847
title: Find the Score Difference in a Game
difficulty: Medium
tags: []
created: 2026-02-22
---

# 3847. 计算比赛分数差

## 题目链接
https://leetcode.cn/problems/find-the-score-difference-in-a-game/

## 题目描述
<p>给你一个整数数组 <code>nums</code>，其中 <code>nums[i]</code> 表示在第 <code>i</code>&nbsp;场比赛中获得的分数。</p>

<p><strong>恰好 </strong>有两位玩家。初始时，第一位玩家为<strong>&nbsp;主动玩家</strong>，第二位玩家为&nbsp;<strong>被动玩家</strong>。</p>

<p><strong>按顺序</strong>&nbsp;将下述规则应用于每场比赛 <code>i</code>：</p>

<ul>
	<li>如果 <code>nums[i]</code> 是奇数，主动玩家和被动玩家互换角色。</li>
	<li>在每第 6 场比赛（即比赛索引为 <code>5, 11, 17, ...</code> 的比赛中），主动玩家和被动玩家互换角色。</li>
	<li>主动玩家参与第 <code>i</code>&nbsp;场比赛，并获得 <code>nums[i]</code> 分。</li>
</ul>

<p>返回<strong>&nbsp;分数差</strong>，即第一位玩家的&nbsp;<strong>总分&nbsp;</strong>减去第二位玩家的&nbsp;<strong>总分&nbsp;</strong>。</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">nums = [1,2,3]</span></p>

<p><strong>输出：</strong> <span class="example-io">0</span></p>

<p><strong>解释：</strong>​​​​​​​</p>

<ul>
	<li>第 0 场比赛：分数为奇数，第二位玩家成为主动玩家，获得 <code>nums[0] = 1</code> 分。</li>
	<li>第 1 场比赛：没有交换角色。第二位玩家获得 <code>nums[1] = 2</code> 分。</li>
	<li>第 2 场比赛：分数为奇数，第一位玩家成为主动玩家，获得 <code>nums[2] = 3</code> 分。</li>
	<li>分数差为 <code>3 - 3 = 0</code>。</li>
</ul>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">nums = [2,4,2,1,2,1]</span></p>

<p><strong>输出：</strong> <span class="example-io">4</span></p>

<p><strong>解释：</strong></p>

<ul>
	<li>第 0 到第 2 场比赛：第一位玩家获得 <code>2 + 4 + 2 = 8</code> 分。</li>
	<li>第 3 场比赛：分数为奇数，第二位玩家成为主动玩家，获得 <code>nums[3] = 1</code> 分。</li>
	<li>第 4 场比赛：第二位玩家获得 <code>nums[4] = 2</code> 分。</li>
	<li>第 5 场比赛：分数为奇数，玩家互换角色。由于这是第 6 场比赛，玩家再次互换角色。第二位玩家获得 <code>nums[5] = 1</code> 分。</li>
	<li>分数差为 <code>8 - 4 = 4</code>。</li>
</ul>
</div>

<p><strong class="example">示例 3：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">nums = [1]</span></p>

<p><strong>输出：</strong> <span class="example-io">-1</span></p>

<p><strong>解释：</strong></p>

<ul>
	<li>第 0 场比赛：分数为奇数，第二位玩家成为主动玩家，获得 <code>nums[0] = 1</code> 分。</li>
	<li>分数差为 <code>0 - 1 = -1</code>。</li>
</ul>
</div>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 1000</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 1000</code></li>
</ul>


## 解题思路

- 按题意顺序模拟每一场比赛。
- 用 `p1`、`p2` 表示当前主动/被动玩家累计分数；当出现“分数是奇数”或“第 6 的倍数场次”时交换两者，最后把本场分数加给主动方。
- 变量 `r` 记录当前主动方是否已经从“玩家 1”切换为“玩家 2”，据此在结尾把主动/被动累计分还原成“玩家 1 - 玩家 2”的差值。

- 时间复杂度: $O(n)$

- 空间复杂度: $O(1)$

## 相关专题
- [贪心与思维](../../topics/greedy-and-thinking.md)

## 代码
```python
class Solution:
    def scoreDifference(self, nums: List[int]) -> int:
        p1, p2 = 0, 0 # p1 主动
        r = False
        for i, n in enumerate(nums):
            if n % 2 == 1:
                p1, p2 = p2, p1
                r = not r
            if (i + 1)% 6 == 0:
                p1, p2 = p2, p1
                r = not r
            p1 += n
        return p1 - p2 if not r else p2 - p1
```
