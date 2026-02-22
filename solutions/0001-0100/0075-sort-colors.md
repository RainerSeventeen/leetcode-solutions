---
id: 75
title: Sort Colors
difficulty: Medium
tags: [array, two-pointers, sorting]
created: 2026-02-20
---

# 75. 颜色分类

## 题目链接
https://leetcode.cn/problems/sort-colors/

## 题目描述
<p>给定一个包含红色、白色和蓝色、共&nbsp;<code>n</code><em> </em>个元素的数组<meta charset="UTF-8" />&nbsp;<code>nums</code>&nbsp;，<strong><a href="https://baike.baidu.com/item/%E5%8E%9F%E5%9C%B0%E7%AE%97%E6%B3%95" target="_blank">原地</a>&nbsp;</strong>对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。</p>

<p>我们使用整数 <code>0</code>、&nbsp;<code>1</code> 和 <code>2</code> 分别表示红色、白色和蓝色。</p>

<ul>
</ul>

<p>必须在不使用库内置的 sort 函数的情况下解决这个问题。</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [2,0,2,1,1,0]
<strong>输出：</strong>[0,0,1,1,2,2]
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [2,0,1]
<strong>输出：</strong>[0,1,2]
</pre>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == nums.length</code></li>
	<li><code>1 &lt;= n &lt;= 300</code></li>
	<li><code>nums[i]</code> 为 <code>0</code>、<code>1</code> 或 <code>2</code></li>
</ul>

<p><strong>进阶：</strong></p>

<ul>
	<li>你能想出一个仅使用常数空间的一趟扫描算法吗？</li>
</ul>



## 解题思路

荷兰国旗问题，三指针一次扫描原地排序。

维护三个区间（闭开更好理解）：

- `[0, low)`：已经放好的 0
- `[low, mid)`：已经放好的 1
- `(high, n-1]`：已经放好的 2（等价于 `[high+1, n)`）

指针含义：

- `mid`：当前正在处理的位置
- `low`：下一个 0 应该放的位置
- `high`：下一个 2 应该放的位置

转移规则（核心不变量：上述三个区间始终成立）：

- 若 `nums[mid] == 0`：把它交换到 `low`，`low += 1`，`mid += 1`
- 若 `nums[mid] == 1`：已经在中间区，`mid += 1`
- 若 `nums[mid] == 2`：把它交换到 `high`，`high -= 1`，但 `mid` 不动（因为换过来的元素还没检查）

边界：

- 循环条件通常为 `mid <= high`，保证未处理区间被完全扫描。

- 时间复杂度: $O(n)$
- 空间复杂度: $O(1)$

## 代码
```python
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        n = len(nums)
        l, r, i = 0, n - 1, 0
        while i <= r:
            if nums[i] == 0:
                nums[i], nums[l] = nums[l], nums[i]
                l += 1
                i += 1
            elif nums[i] == 1:
                i += 1
            elif nums[i] == 2:
                nums[i], nums[r] = nums[r], nums[i]
                r -= 1
```
