---
id: 621
title: Task Scheduler
difficulty: Medium
tags: [greedy, array, hash-table, counting, sorting, heap-priority-queue]
created: 2026-02-20
---

# 621. Task Scheduler

## 题目链接
https://leetcode.cn/problems/task-scheduler/

## 题目描述
<p>给你一个用字符数组&nbsp;<code>tasks</code> 表示的 CPU 需要执行的任务列表，用字母 A 到 Z 表示，以及一个冷却时间 <code>n</code>。每个周期或时间间隔允许完成一项任务。任务可以按任何顺序完成，但有一个限制：两个<strong> 相同种类</strong> 的任务之间必须有长度为<strong>&nbsp;</strong><code>n</code><strong> </strong>的冷却时间。</p>

<p>返回完成所有任务所需要的<strong> 最短时间间隔</strong>&nbsp;。</p>

<p><strong>示例 1：</strong></p>

<div class="example-block"><strong>输入：</strong>tasks = ["A","A","A","B","B","B"], n = 2</div>

<div class="example-block"><strong>输出：</strong>8</div>

<div class="example-block"><strong>解释：</strong></div>

<div class="example-block">在完成任务 A 之后，你必须等待两个间隔。对任务 B 来说也是一样。在第 3 个间隔，A 和 B 都不能完成，所以你需要待命。在第 4 个间隔，由于已经经过了 2 个间隔，你可以再次执行 A 任务。</div>

<div class="example-block">&nbsp;</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><b>输入：</b>tasks = ["A","C","A","B","D","B"], n = 1</p>

<p><b>输出：</b>6</p>

<p><b>解释：</b>一种可能的序列是：A -&gt; B -&gt; C -&gt; D -&gt; A -&gt; B。</p>

<p>由于冷却间隔为 1，你可以在完成另一个任务后重复执行这个任务。</p>
</div>

<p><strong>示例 3：</strong></p>

<div class="example-block"><strong>输入：</strong>tasks = ["A","A","A","B","B","B"], n = 3</div>

<div class="example-block"><strong>输出：</strong>10</div>

<div class="example-block"><strong>解释：</strong>一种可能的序列为：A -&gt; B -&gt; idle -&gt; idle -&gt; A -&gt; B -&gt; idle -&gt; idle -&gt; A -&gt; B。</div>

<div class="example-block">只有两种任务类型，A 和 B，需要被 3 个间隔分割。这导致重复执行这些任务的间隔当中有两次待命状态。</div>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= tasks.length &lt;= 10<sup>4</sup></code></li>
	<li><code>tasks[i]</code> 是大写英文字母</li>
	<li><code>0 &lt;= n &lt;= 100</code></li>
</ul>



## 解题思路

贪心/数学化推导：决定总长度的关键在于**出现次数最多的任务**，因为相同任务之间必须至少间隔 `n`。

设：

- `tmax` = 最高频次（某个字母出现了多少次）
- `cmax` = 有多少个任务并列达到 `tmax`
- `m` = 任务总数

把最高频次任务先排出来：可以看成有 `tmax - 1` 个“完整空槽段”，每段长度为 `n + 1`（一个任务 + n 个冷却位）：

- 先放 `tmax - 1` 段：`(tmax - 1) * (n + 1)`
- 最后一段只需要放完所有最高频次的任务尾巴，共 `cmax` 个：再加 `cmax`

得到一个理论下界：

`min_len = (tmax - 1) * (n + 1) + cmax`

如果其他任务足够多，可以把冷却位全部填满，此时答案就是任务总数 `m`；否则需要插入 idle，答案就是 `min_len`。因此最终：

`ans = max(m, min_len)`

边界：

- `n == 0` 时不需要冷却，公式自然退化为 `ans = m`。
- 多个任务并列最高频次时，用 `cmax` 修正最后一段长度，避免低估。

- 时间复杂度: $O(n)$
- 空间复杂度: $O(1)$

## 代码
```python
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        m = len(tasks)
        count = [0] * 26
        tmax = 0 # 最多的任务的数量
        cmax = 1 # 有几个并列最多的
        for t in tasks:
            idx = ord(t) - ord('A')
            count[idx] += 1
            if count[idx] > tmax:
                cmax = 1
                tmax = count[idx]
            elif count[idx] == tmax:
                cmax += 1
        return max(m, (tmax - 1) * (n + 1) + cmax)
```
