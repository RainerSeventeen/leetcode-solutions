---
id: 1306
title: Jump Game III
difficulty: Medium
tags: [depth-first-search, breadth-first-search, array]
created: 2026-02-21
---

# 1306. 跳跃游戏 III

## 题目链接
https://leetcode.cn/problems/jump-game-iii/

## 题目描述
<p>这里有一个非负整数数组&nbsp;<code>arr</code>，你最开始位于该数组的起始下标&nbsp;<code>start</code>&nbsp;处。当你位于下标&nbsp;<code>i</code>&nbsp;处时，你可以跳到&nbsp;<code>i + arr[i]</code> 或者 <code>i - arr[i]</code>。</p>

<p>请你判断自己是否能够跳到对应元素值为 0 的 <strong>任一</strong> 下标处。</p>

<p>注意，不管是什么情况下，你都无法跳到数组之外。</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>arr = [4,2,3,0,3,1,2], start = 5
<strong>输出：</strong>true
<strong>解释：</strong>
到达值为 0 的下标 3 有以下可能方案： 
下标 5 -&gt; 下标 4 -&gt; 下标 1 -&gt; 下标 3 
下标 5 -&gt; 下标 6 -&gt; 下标 4 -&gt; 下标 1 -&gt; 下标 3 
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>arr = [4,2,3,0,3,1,2], start = 0
<strong>输出：</strong>true 
<strong>解释：
</strong>到达值为 0 的下标 3 有以下可能方案： 
下标 0 -&gt; 下标 4 -&gt; 下标 1 -&gt; 下标 3
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>arr = [3,0,2,1,2], start = 2
<strong>输出：</strong>false
<strong>解释：</strong>无法到达值为 0 的下标 1 处。 
</pre>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= arr.length &lt;= 5 * 10^4</code></li>
	<li><code>0 &lt;= arr[i] &lt;&nbsp;arr.length</code></li>
	<li><code>0 &lt;= start &lt; arr.length</code></li>
</ul>


## 解题思路

从 `start` 做 DFS，当前位置可跳到 `i-arr[i]` 和 `i+arr[i]`。
用 `visited` 防止重复访问和递归死循环。
搜索过程中只要到达值为 `0` 的下标即可返回 `True`。
- 时间复杂度: $O(n)$
- 空间复杂度: $O(n)$

## 相关专题
- [图论算法](../../topics/graph-algorithms.md)

## 代码
```python
class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)
        visited = [False] * n
        
        def dfs(curr):
            if arr[curr] == 0:
                return True
            visited[curr] = True
            l = curr - arr[curr]
            r = curr + arr[curr]
            ret_l, ret_r = False, False
            if l >= 0:
                ret_l = dfs(l) if visited[l] == False else False
            if r < n:
                ret_r = dfs(r) if visited[r] == False else False
            return ret_l or ret_r
        return dfs(start)
```
