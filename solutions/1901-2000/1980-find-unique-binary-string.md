---
id: 1980
title: Find Unique Binary String
difficulty: Medium
tags: [array, hash-table, string, backtracking]
created: 2026-03-08
---

# 1980. 找出不同的二进制字符串

## 题目链接
https://leetcode.cn/problems/find-unique-binary-string/

## 题目描述
<p>给你一个字符串数组 <code>nums</code> ，该数组由 <code>n</code> 个 <strong>互不相同</strong> 的二进制字符串组成，且每个字符串长度都是 <code>n</code> 。请你找出并返回一个长度为&nbsp;<code>n</code>&nbsp;且&nbsp;<strong>没有出现</strong> 在 <code>nums</code> 中的二进制字符串<em>。</em>如果存在多种答案，只需返回 <strong>任意一个</strong> 即可。</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = ["01","10"]
<strong>输出：</strong>"11"
<strong>解释：</strong>"11" 没有出现在 nums 中。"00" 也是正确答案。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = ["00","01"]
<strong>输出：</strong>"11"
<strong>解释：</strong>"11" 没有出现在 nums 中。"10" 也是正确答案。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>nums = ["111","011","001"]
<strong>输出：</strong>"101"
<strong>解释：</strong>"101" 没有出现在 nums 中。"000"、"010"、"100"、"110" 也是正确答案。</pre>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == nums.length</code></li>
	<li><code>1 &lt;= n &lt;= 16</code></li>
	<li><code>nums[i].length == n</code></li>
	<li><code>nums[i] </code>为 <code>'0'</code> 或 <code>'1'</code></li>
	<li><code>nums</code> 中的所有字符串 <strong>互不相同</strong></li>
</ul>


## 解题思路

最优做法是直接利用康托对角线构造。

遍历第 `i` 个字符串时，只看它的第 `i` 位：如果这一位是 `'0'`，答案第 `i` 位就填 `'1'`；反之填 `'0'`。这样构造出的新串在第 `i` 位一定与 `nums[i]` 不同，因此它不可能和任意一个原字符串完全相同。

后面的两个代码块分别给出了整数枚举和回溯搜索，都是正确做法，但复杂度不如对角线构造，因此保留在后面。

- 时间复杂度: $O(n)$，其中 `n=len(nums)`，只需遍历一次对角线。

- 空间复杂度: $O(n)$，用于保存答案字符数组。

## 相关专题
- [贪心与思维](../../topics/greedy-and-thinking.md)

## 代码
```python
class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        # Cantor Diagonal Argument 数学原理
        # 在二进制下可以在对角线上构造出一个和所有数都有 “至少一位” 不同的数
        ans = [''] * len(nums)
        for i, s in enumerate(nums):
            ans[i] = '1' if s[i] == '0' else '0'
        return ''.join(ans)
```

```python
class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        # 整数 hash 表
        st = {int(s, 2) for s in nums}

        ans = 0
        while ans in st:
            ans += 1

        n = len(nums)
        return f"{ans:0{n}b}"
```

```python
class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        exist = set(nums)
        n = len(nums)
        # 回溯 + hash
        curr = ['0'] * n
        ans = None
        def backtrack(idx, curr):
            nonlocal ans
            if idx == n:
                s = ''.join(curr)
                if s not in exist:
                    ans = s
                    return True
                return False

            pre = curr[idx] 
            for ch in ('0', '1'):
                curr[idx] = ch
                if backtrack(idx + 1, curr):
                    return True # 立刻返回
            curr[idx] = pre # 恢复
            return False
        backtrack(0, curr)
        return ans
```
