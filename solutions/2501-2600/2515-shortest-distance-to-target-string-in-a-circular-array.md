---
id: 2515
title: Shortest Distance to Target String in a Circular Array
difficulty: Easy
tags: [array, string]
created: 2026-04-25
---

# 2515. 到目标字符串的最短距离

## 题目链接
https://leetcode.cn/problems/shortest-distance-to-target-string-in-a-circular-array/

## 题目描述
<p>给你一个下标从 <strong>0</strong> 开始的 <strong>环形</strong> 字符串数组 <code>words</code> 和一个字符串 <code>target</code> 。<strong>环形数组</strong> 意味着数组首尾相连。</p>

<ul>
	<li>形式上， <code>words[i]</code> 的下一个元素是 <code>words[(i + 1) % n]</code> ，而 <code>words[i]</code> 的前一个元素是 <code>words[(i - 1 + n) % n]</code> ，其中 <code>n</code> 是 <code>words</code> 的长度。</li>
</ul>

<p>从 <code>startIndex</code> 开始，你一次可以用 <code>1</code> 步移动到下一个或者前一个单词。</p>

<p>返回到达目标字符串 <code>target</code> 所需的最短距离。如果 <code>words</code> 中不存在字符串 <code>target</code> ，返回 <code>-1</code> 。</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>words = ["hello","i","am","leetcode","hello"], target = "hello", startIndex = 1
<strong>输出：</strong>1
<strong>解释：</strong>从下标 1 开始，可以经由以下步骤到达 "hello" ：
- 向右移动 3 个单位，到达下标 4 。
- 向左移动 2 个单位，到达下标 4 。
- 向右移动 4 个单位，到达下标 0 。
- 向左移动 1 个单位，到达下标 0 。
到达 "hello" 的最短距离是 1 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>words = ["a","b","leetcode"], target = "leetcode", startIndex = 0
<strong>输出：</strong>1
<strong>解释：</strong>从下标 0 开始，可以经由以下步骤到达 "leetcode" ：
- 向右移动 2 个单位，到达下标 2 。
- 向左移动 1 个单位，到达下标 2 。
到达 "leetcode" 的最短距离是 1 。</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>words = ["i","eat","leetcode"], target = "ate", startIndex = 0
<strong>输出：</strong>-1
<strong>解释：</strong>因为 words 中不存在字符串 "ate" ，所以返回 -1 。
</pre>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= words.length &lt;= 100</code></li>
	<li><code>1 &lt;= words[i].length &lt;= 100</code></li>
	<li><code>words[i]</code> 和 <code>target</code> 仅由小写英文字母组成</li>
	<li><code>0 &lt;= startIndex &lt; words.length</code></li>
</ul>


## 解题思路

从 `startIndex` 同时向左、向右扩展，每次步数加一并检查两个方向当前位置是否为 `target`。因为是环形数组，左右指针都用取模移动；第一次找到目标时的步数就是最短距离，若两边相遇仍未找到则返回 `-1`。

- 时间复杂度: $O(n)$，其中 `n` 为 `words` 长度。

- 空间复杂度: $O(1)$

## 相关专题

- [滑动窗口与双指针](../../topics/sliding-window-and-two-pointers.md)

## 代码
```python
class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        # 双向搜索
        if words[startIndex] == target:
            return 0
        n = len(words)
        l = (startIndex + n - 1) % n
        r = (startIndex + 1) % n
        step = 1
        while True:
            if l == r:
                if words[l] == target or words[r] == target:
                    return step
                else:
                    break
            if words[l] == target or words[r] == target:
                return step
            l = (l + n - 1) % n
            r = (r + 1) % n
            step += 1
        return -1
```
