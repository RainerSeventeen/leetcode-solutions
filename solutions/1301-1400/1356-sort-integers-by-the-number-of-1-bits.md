---
id: 1356
title: Sort Integers by The Number of 1 Bits
difficulty: Easy
tags: [bit-manipulation, array, counting, sorting]
created: 2026-02-25
---

# 1356. 根据数字二进制下 1 的数目排序

## 题目链接
https://leetcode.cn/problems/sort-integers-by-the-number-of-1-bits/

## 题目描述
<p>给你一个整数数组&nbsp;<code>arr</code>&nbsp;。请你将数组中的元素按照其二进制表示中数字 <strong>1</strong> 的数目升序排序。</p>

<p>如果存在多个数字二进制中&nbsp;<strong>1</strong>&nbsp;的数目相同，则必须将它们按照数值大小升序排列。</p>

<p>请你返回排序后的数组。</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>arr = [0,1,2,3,4,5,6,7,8]
<strong>输出：</strong>[0,1,2,4,8,3,5,6,7]
<strong>解释：</strong>[0] 是唯一一个有 0 个 1 的数。
[1,2,4,8] 都有 1 个 1 。
[3,5,6] 有 2 个 1 。
[7] 有 3 个 1 。
按照 1 的个数排序得到的结果数组为 [0,1,2,4,8,3,5,6,7]
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>arr = [1024,512,256,128,64,32,16,8,4,2,1]
<strong>输出：</strong>[1,2,4,8,16,32,64,128,256,512,1024]
<strong>解释：</strong>数组中所有整数二进制下都只有 1 个 1 ，所以你需要按照数值大小将它们排序。
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>arr = [10000,10000]
<strong>输出：</strong>[10000,10000]
</pre>

<p><strong>示例 4：</strong></p>

<pre><strong>输入：</strong>arr = [2,3,5,7,11,13,17,19]
<strong>输出：</strong>[2,3,5,17,7,11,13,19]
</pre>

<p><strong>示例 5：</strong></p>

<pre><strong>输入：</strong>arr = [10,100,1000,10000]
<strong>输出：</strong>[10,100,10000,1000]
</pre>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= arr.length &lt;= 500</code></li>
	<li><code>0 &lt;= arr[i] &lt;= 10^4</code></li>
</ul>


## 解题思路
按题意可直接自定义排序键：先按 `x.bit_count()`（二进制 1 的个数）升序，再按数值 `x` 升序。Python 的 `sorted` 支持元组键，正好对应这两个排序条件。

- 时间复杂度: $O(n\log n)$，其中 `n` 代表数组长度
- 空间复杂度: $O(n)$，其中 `n` 代表数组长度

## 相关专题
- [位运算](../../topics/bit-operations.md)

## 代码
```python
class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        return sorted(arr, key=lambda x : (x.bit_count(), x))
```

```python
from collections import defaultdict
class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        # 哈希表
        mp = defaultdict(list)
        for x in arr:
            cnt = x.bit_count()
            mp[cnt].append(x)
        count_list = sorted(mp.items()) # 字典按照 key 排序
        ret = []
        for _, lst in count_list:
            ret.extend(sorted(lst)) # 解列表然后放在后面
        return ret
```
