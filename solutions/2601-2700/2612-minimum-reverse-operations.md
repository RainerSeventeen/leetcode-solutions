---
id: 2612
title: Minimum Reverse Operations
difficulty: Hard
tags: [breadth-first-search, union-find, array, hash-table, ordered-set]
created: 2026-02-27
---

# 2612. 最少翻转操作数

## 题目链接
https://leetcode.cn/problems/minimum-reverse-operations/

## 题目描述
<p>给定一个整数&nbsp;<code>n</code>&nbsp;和一个整数&nbsp;<code>p</code>，它们表示一个长度为 <code>n</code> 且除了下标为&nbsp;<code>p</code>&nbsp;处是 <code>1</code>&nbsp;以外，其他所有数都是 <code>0</code>&nbsp;的数组&nbsp;<code>arr</code>。同时给定一个整数数组&nbsp;<code>banned</code>&nbsp;，它包含数组中的一些限制位置。在&nbsp;<code>arr</code>&nbsp;上进行下列操作：</p>

<ul>
	<li>如果单个 1 不在&nbsp;<code>banned</code>&nbsp;中的位置上，反转大小为 <code>k</code> 的 <strong><span data-keyword="subarray-nonempty">子数组</span></strong>。</li>
</ul>

<p>返回一个包含&nbsp;<code>n</code>&nbsp;个结果的整数数组&nbsp;<code>answer</code>，其中第&nbsp;<code>i</code>&nbsp;个结果是将&nbsp;<code>1</code>&nbsp;放到位置&nbsp;<code>i</code>&nbsp;处所需的&nbsp;<strong>最少</strong>&nbsp;翻转操作次数，如果无法放到位置&nbsp;<code>i</code>&nbsp;处，此数为&nbsp;<code>-1</code>&nbsp;。</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>n = 4, p = 0, banned = [1,2], k = 4</span></p>

<p><span class="example-io"><b>输出：</b>[0,-1,-1,1]</span></p>

<p><strong>解释：</strong></p>

<ul>
	<li>一开始 1 位于位置 0，因此我们需要在位置 0 上的操作数是 0。</li>
	<li>我们不能将 1 放置在被禁止的位置上，所以位置 1 和 2 的答案是 -1。</li>
	<li>执行大小为 4 的操作以反转整个数组。</li>
	<li>在一次操作后，1 位于位置 3，因此位置 3 的答案是 1。</li>
</ul>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>n = 5, p = 0, banned = [2,4], k = 3</span></p>

<p><span class="example-io"><b>输出：</b>[0,-1,-1,-1,-1]</span></p>

<p><b>解释：</b></p>

<ul>
	<li>一开始 1 位于位置 0，因此我们需要在位置 0 上的操作数是 0。</li>
	<li>我们不能在&nbsp;<code>[0, 2]</code>&nbsp;的子数组位置上执行操作，因为位置 2 在 banned 中。</li>
	<li>由于 1 不能够放置在位置 2 上，使用更多操作将 1 放置在其它位置上是不可能的。</li>
</ul>
</div>

<p><strong class="example">示例 3：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>n = 4, p = 2, banned = [0,1,3], k = 1</span></p>

<p><span class="example-io"><b>输出：</b>[-1,-1,0,-1]</span></p>

<p><strong>解释：</strong></p>

<p>执行大小为 1 的操作，且 1 永远不会改变位置。</p>
</div>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= p &lt;= n - 1</code></li>
	<li><code>0 &lt;= banned.length &lt;= n - 1</code></li>
	<li><code>0 &lt;= banned[i] &lt;= n - 1</code></li>
	<li><code>1 &lt;= k &lt;= n&nbsp;</code></li>
	<li><code>banned[i] != p</code></li>
	<li><code>banned</code>&nbsp;中的值 <strong>互不相同</strong>&nbsp;。</li>
</ul>


## 解题思路

这是一道 2824 分的题目，比较难，另外题目本身的意思也比较难懂

题目的意思是每一次都可以执行一个 `k` 长度的子数组的反转，但是如果 `banned` 的下标上出现了 1 就不允许操作了，如果把他当成一张图，这就是一个没有出度的节点

1. 将下标看作为不同的节点，将两个可以直接翻转换位的节点之间视为有权为 1 的路径，此时问题变成计算 `p` 每一个点的最短路径，由于权全都是 1，就可以使用 BFS 计算
2. 翻转 `[L, R]`数组的操作中，下标 `i` 经过翻转后得到的是`L + R - i`，我们滑动 LR 窗口，`L + R` 的变化步长是 2， 因此 i 的可到达位置是一个 公差为 2 的等差数列
3. 当 `i`  可以成为窗口边界值`(L, R)`的时候，他们的最小最大值分别是: `i - k + 1 / i + k - 1`, 但是需要处理边界情况，有的点是无法成为窗口 `[L, R]` 的边界值的，例如：

`k = 3` 时候 `i = 0, 1, 2` 都无法成为窗口的最右边，因为他们的边界不可以使用上面的那个值

- 对于 `i < k - 1`, 窗口 `L = 0, R = k - 1` ， `i` 翻转的最小值是 `k - i - 1`
- 对于 `i > n - k`, 窗口 `L = n - k, R = n - 1`, ` i` 翻转的最大值 `2 * n - k - i - 1`

最后`i` 的翻转范围是:`max(i - k + 1, k - i - 1) <= i <= min(i + k - 1, 2 * n - k -i - 1)`

- 时间复杂度: $O(n \log n)$

- 空间复杂度: $O(n)$

## 相关专题
- [图论算法](../../topics/graph-algorithms.md)

## 代码
```python
import sortedcontainers
class Solution:
    def minReverseOperations(self, n: int, p: int, banned: List[int], k: int) -> List[int]:
        ban = set(banned) | {p} # 构建ban + p 的集合
        indices = [SortedList(), SortedList()] # 某个下标可到达的点一定是 2 的公差
        for i in range(n):
            if i not in ban:
                indices[i % 2].add(i)
        # 哨兵
        indices[0].add(n)
        indices[1].add(n)
    
        ans = [-1] * n
        ans[p] = 0 # 起点次数 0
        q = deque([p])
        
        while q:
            i = q.popleft()
            mn = max(i - k + 1, k - i - 1)
            mx = min(i + k - 1, 2 * n - k -i - 1)
            # 确定奇偶数后，一定能访问对应奇偶区间内的所有值
            sl = indices[mn % 2]
            idx = sl.bisect_left(mn) # 二分查找左下限
            while sl[idx] <= mx:    # 拿走区间内所有尚未被访问的节点
                j = sl.pop(idx)
                ans[j] = ans[i] + 1
                q.append(j) # 放入下一轮需要访问的节点
        return ans # 起点是0, ban 是 -1, 其他都是对应数值
```
