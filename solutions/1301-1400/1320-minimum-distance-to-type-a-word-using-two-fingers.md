---
id: 1320
title: Minimum Distance to Type a Word Using Two Fingers
difficulty: Hard
tags: [string, dynamic-programming]
created: 2026-04-13
---

# 1320. 二指输入的的最小距离

## 题目链接
https://leetcode.cn/problems/minimum-distance-to-type-a-word-using-two-fingers/

## 题目描述
<p><img alt="" src="https://assets.leetcode.cn/aliyun-lc-upload/uploads/2020/01/11/leetcode_keyboard.png" /></p>

<p>二指输入法定制键盘在 <strong>X-Y</strong> 平面上的布局如上图所示，其中每个大写英文字母都位于某个坐标处。</p>

<ul>
	<li>例如字母&nbsp;<strong>A</strong>&nbsp;位于坐标&nbsp;<strong>(0,0)</strong>，字母&nbsp;<strong>B</strong>&nbsp;位于坐标&nbsp;<strong>(0,1)</strong>，字母&nbsp;<strong>P</strong>&nbsp;位于坐标&nbsp;<strong>(2,3)</strong>&nbsp;且字母 <strong>Z</strong>&nbsp;位于坐标&nbsp;<strong>(4,1)</strong>。</li>
</ul>

<p>给你一个待输入字符串&nbsp;<code>word</code>，请你计算并返回在仅使用两根手指的情况下，键入该字符串需要的最小移动总距离。</p>

<p>坐标<code>&nbsp;<strong>(x<sub>1</sub>,y<sub>1</sub>)</strong> </code>和 <code><strong>(x<sub>2</sub>,y<sub>2</sub>)</strong></code> 之间的 <strong>距离</strong> 是&nbsp;<code><strong>|x<sub>1</sub> - x<sub>2</sub>| + |y<sub>1</sub> - y<sub>2</sub>|</strong></code>。&nbsp;</p>

<p><strong>注意</strong>，两根手指的起始位置是零代价的，不计入移动总距离。你的两根手指的起始位置也不必从首字母或者前两个字母开始。</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>word = "CAKE"
<strong>输出：</strong>3
<strong>解释： 
</strong>使用两根手指输入 "CAKE" 的最佳方案之一是： 
手指 1 在字母 'C' 上 -&gt; 移动距离 = 0 
手指 1 在字母 'A' 上 -&gt; 移动距离 = 从字母 'C' 到字母 'A' 的距离 = 2 
手指 2 在字母 'K' 上 -&gt; 移动距离 = 0 
手指 2 在字母 'E' 上 -&gt; 移动距离 = 从字母 'K' 到字母 'E' 的距离  = 1 
总距离 = 3
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>word = "HAPPY"
<strong>输出：</strong>6
<strong>解释： </strong>
使用两根手指输入 "HAPPY" 的最佳方案之一是：
手指 1 在字母 'H' 上 -&gt; 移动距离 = 0
手指 1 在字母 'A' 上 -&gt; 移动距离 = 从字母 'H' 到字母 'A' 的距离 = 2
手指 2 在字母 'P' 上 -&gt; 移动距离 = 0
手指 2 在字母 'P' 上 -&gt; 移动距离 = 从字母 'P' 到字母 'P' 的距离 = 0
手指 1 在字母 'Y' 上 -&gt; 移动距离 = 从字母 'A' 到字母 'Y' 的距离 = 4
总距离 = 6
</pre>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 &lt;= word.length &lt;= 300</code></li>
	<li>每个 <code>word[i]</code>&nbsp;都是一个大写英文字母。</li>
</ul>


## 解题思路

- 把字母映射成 0 到 25 的编号后，用 DFS + 记忆化搜索枚举“当前处理到第几个字符、两根手指分别停在哪”。
- 每次输入当前字符时，只需要让其中一根手指移动过去，取两种方案的最小值。
- 最后枚举另一根手指的初始落点，取全局最优。

- 时间复杂度: $O(n \times 26^2)$

- 空间复杂度: $O(n \times 26^2)$

## 相关专题

- [动态规划](../../topics/dynamic-programming.md)

## 代码
```python
# 预处理两个字母的距离
COLUMN = 6
get_dis = lambda a, b: abs(a // COLUMN - b // COLUMN) + abs(a % COLUMN - b % COLUMN)
dis = [[get_dis(i, j) for j in range(26)] for i in range(26)]

class Solution:
    # CV
    def minimumDistance(self, word: str) -> int:
        word = [ord(ch) - ord('A') for ch in word]  # 避免在 dfs 中频繁调用 ord

        @cache  # 缓存装饰器，避免重复计算 dfs（一行代码实现记忆化）
        def dfs(i: int, finger1: int, finger2: int) -> int:
            if i < 0:
                return 0

            # 手指 1 移到 word[i]
            res1 = dfs(i - 1, word[i], finger2) + dis[finger1][word[i]]

            # 手指 2 移到 word[i]
            res2 = dfs(i - 1, finger1, word[i]) + dis[finger2][word[i]]

            return min(res1, res2)

        n = len(word)
        # 最后一定有一根手指在 word[-1]，另一根手指的位置不确定，枚举
        return min(dfs(n - 2, word[-1], finger2) for finger2 in range(26))
```
