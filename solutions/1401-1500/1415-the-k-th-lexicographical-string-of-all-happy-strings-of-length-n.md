---
id: 1415
title: The k-th Lexicographical String of All Happy Strings of Length n
difficulty: Medium
tags: [string, backtracking]
created: 2026-03-14
---

# 1415. 长度为 n 的开心字符串中字典序第 k 小的字符串

## 题目链接
https://leetcode.cn/problems/the-k-th-lexicographical-string-of-all-happy-strings-of-length-n/

## 题目描述
<p>一个 「开心字符串」定义为：</p>

<ul>
	<li>仅包含小写字母&nbsp;<code>[&#39;a&#39;, &#39;b&#39;, &#39;c&#39;]</code>.</li>
	<li>对所有在&nbsp;<code>1</code>&nbsp;到&nbsp;<code>s.length - 1</code>&nbsp;之间的&nbsp;<code>i</code>&nbsp;，满足&nbsp;<code>s[i] != s[i + 1]</code>&nbsp;（字符串的下标从 1 开始）。</li>
</ul>

<p>比方说，字符串&nbsp;<strong>&quot;abc&quot;</strong>，<strong>&quot;ac&quot;，&quot;b&quot;</strong> 和&nbsp;<strong>&quot;abcbabcbcb&quot;</strong>&nbsp;都是开心字符串，但是&nbsp;<strong>&quot;aa&quot;</strong>，<strong>&quot;baa&quot;</strong>&nbsp;和&nbsp;<strong>&quot;ababbc&quot;</strong>&nbsp;都不是开心字符串。</p>

<p>给你两个整数 <code>n</code>&nbsp;和 <code>k</code>&nbsp;，你需要将长度为 <code>n</code>&nbsp;的所有开心字符串按字典序排序。</p>

<p>请你返回排序后的第 k 个开心字符串，如果长度为 <code>n</code>&nbsp;的开心字符串少于 <code>k</code>&nbsp;个，那么请你返回 <strong>空字符串</strong>&nbsp;。</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>n = 1, k = 3
<strong>输出：</strong>&quot;c&quot;
<strong>解释：</strong>列表 [&quot;a&quot;, &quot;b&quot;, &quot;c&quot;] 包含了所有长度为 1 的开心字符串。按照字典序排序后第三个字符串为 &quot;c&quot; 。
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>n = 1, k = 4
<strong>输出：</strong>&quot;&quot;
<strong>解释：</strong>长度为 1 的开心字符串只有 3 个。
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>n = 3, k = 9
<strong>输出：</strong>&quot;cab&quot;
<strong>解释：</strong>长度为 3 的开心字符串总共有 12 个 [&quot;aba&quot;, &quot;abc&quot;, &quot;aca&quot;, &quot;acb&quot;, &quot;bab&quot;, &quot;bac&quot;, &quot;bca&quot;, &quot;bcb&quot;, &quot;cab&quot;, &quot;cac&quot;, &quot;cba&quot;, &quot;cbc&quot;] 。第 9 个字符串为 &quot;cab&quot;
</pre>

<p><strong>示例 4：</strong></p>

<pre><strong>输入：</strong>n = 2, k = 7
<strong>输出：</strong>&quot;&quot;
</pre>

<p><strong>示例 5：</strong></p>

<pre><strong>输入：</strong>n = 10, k = 100
<strong>输出：</strong>&quot;abacbabacb&quot;
</pre>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 10</code></li>
	<li><code>1 &lt;= k &lt;= 100</code></li>
</ul>



## 解题思路

- 先计算长度为 `n` 的开心字符串总数 `3 * 2 ** (n - 1)`，若总数小于 `k` 直接返回空串。
- 通过回溯在满足前一个字符不同的条件下逐步构造字符串，按字典序生成所有开心字符串，记录遍历顺序，当收集到第 `k` 个时即可停止。
- 最后取出生成的结果列表中的第 `k` 个字符串返回。
- 时间复杂度: $O(\min(k, 3 \times 2^{n - 1}) \times n)$
- 空间复杂度: $O(n)$

## 相关专题
- [链表、树与回溯](../../topics/linked-list-tree-backtracking.md)

## 代码
```python
class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        count = 3 * 2 ** (n - 1) # 总数
        if count < k:
            return ""

        ret, path = [], []
        def backtrack(pre, idx): # idx 当前下标
            nonlocal ret, path
            if idx == n:
                s = ''.join(path)
                ret.append(s)
                return len(ret)

            for ch in ('a', 'b', 'c'):
                if ch == pre:
                    continue
                tmp, pre = pre, ch # 暂存 tmp
                path.append(ch)
                # print(path)
                cnt = backtrack(pre, idx + 1)
                if cnt == k:
                    return cnt # 完成目标
                else:   # 恢复现场
                    pre = tmp
                    path.pop() 
        
        backtrack('#', 0)
        return ret[-1]
```
