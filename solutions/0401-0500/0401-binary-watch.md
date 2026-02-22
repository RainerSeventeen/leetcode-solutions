---
id: 401
title: Binary Watch
difficulty: Easy
tags: [bit-manipulation, backtracking]
created: 2026-02-21
---

# 401. 二进制手表

## 题目链接
https://leetcode.cn/problems/binary-watch/

## 题目描述
<p>二进制手表顶部有 4 个 LED 代表<strong> 小时（0-11）</strong>，底部的 6 个 LED 代表<strong> 分钟（0-59）</strong>。每个 LED 代表一个 0 或 1，最低位在右侧。</p>

<ul>
	<li>例如，下面的二进制手表读取 <code>"4:51"</code> 。</li>
</ul>

<p><img src="https://assets.leetcode.com/uploads/2021/04/08/binarywatch.jpg" style="height: 300px; width" /></p>

<p>给你一个整数 <code>turnedOn</code> ，表示当前亮着的 LED 的数量，返回二进制手表可以表示的所有可能时间。你可以 <strong>按任意顺序</strong> 返回答案。</p>

<p>小时不会以零开头：</p>

<ul>
	<li>例如，<code>"01:00"</code> 是无效的时间，正确的写法应该是 <code>"1:00"</code> 。</li>
</ul>

<p>分钟必须由两位数组成，可能会以零开头：</p>

<ul>
	<li>例如，<code>"10:2"</code> 是无效的时间，正确的写法应该是 <code>"10:02"</code> 。</li>
</ul>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>turnedOn = 1
<strong>输出：</strong>["0:01","0:02","0:04","0:08","0:16","0:32","1:00","2:00","4:00","8:00"]
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>turnedOn = 9
<strong>输出：</strong>[]
</pre>

<p><strong>提示：</strong></p>

<ul>
	<li><code>0 &lt;= turnedOn &lt;= 10</code></li>
</ul>


## 解题思路

直接枚举所有小时 `0~11` 和分钟 `0~59` 的组合。
用 `bit_count()` 统计小时和分钟二进制 1 的个数之和。
当总数等于 `turnedOn` 时按格式加入结果。
- 时间复杂度: $O(1)$
- 空间复杂度: $O(1)$

## 相关专题
- [链表、树与回溯](../../topics/linked-list-tree-backtracking.md)

## 代码
```python
class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        # 直接枚举 0 ~ 11 以及 0 ~ 59 的所有情况
        ret = []
        for h in range(12):
            count = h.bit_count()
            if count > turnedOn:
                continue
            for m in range(60):
                count += m.bit_count()
                if count == turnedOn:
                    # 格式化
                    ret.append(f"{h}:{m:0>2}")
                count -= m.bit_count()
        return ret
```
