---
id: 79
title: Word Search
difficulty: Medium
tags: [depth-first-search, array, string, backtracking, matrix]
created: 2026-02-20
---

# 79. 单词搜索

## 题目链接
https://leetcode.cn/problems/word-search/

## 题目描述
<p>给定一个&nbsp;<code>m x n</code> 二维字符网格&nbsp;<code>board</code> 和一个字符串单词&nbsp;<code>word</code> 。如果&nbsp;<code>word</code> 存在于网格中，返回 <code>true</code> ；否则，返回 <code>false</code> 。</p>

<p>单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。</p>

<p><strong>示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/11/04/word2.jpg" style="width: 322px; height: 242px;" />
<pre>
<strong>输入：</strong>board = [['A','B','C','E'],['S','F','C','S'],['A','D','E','E']], word = "ABCCED"
<strong>输出：</strong>true
</pre>

<p><strong>示例 2：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/11/04/word-1.jpg" style="width: 322px; height: 242px;" />
<pre>
<strong>输入：</strong>board = [['A','B','C','E'],['S','F','C','S'],['A','D','E','E']], word = "SEE"
<strong>输出：</strong>true
</pre>

<p><strong>示例 3：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/10/15/word3.jpg" style="width: 322px; height: 242px;" />
<pre>
<strong>输入：</strong>board = [['A','B','C','E'],['S','F','C','S'],['A','D','E','E']], word = "ABCB"
<strong>输出：</strong>false
</pre>

<p><strong>提示：</strong></p>

<ul>
	<li><code>m == board.length</code></li>
	<li><code>n = board[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 6</code></li>
	<li><code>1 &lt;= word.length &lt;= 15</code></li>
	<li><code>board</code> 和 <code>word</code> 仅由大小写英文字母组成</li>
</ul>

<p><strong>进阶：</strong>你可以使用搜索剪枝的技术来优化解决方案，使其在 <code>board</code> 更大的情况下可以更快解决问题？</p>



## 解题思路

DFS 回溯在网格中找路径。

对每个起点 `(i, j)`，尝试匹配 `word[0]`，若相等则从该点做深度优先搜索，递归匹配下一个字符。

状态与约束：

- 当前位置 `(x, y)` 对应要匹配 `word[k]`
- 每个格子在同一条路径中只能使用一次，因此需要 `visited`（或原地修改 `board[x][y]` 为哨兵字符）来避免重复

转移：

- 若 `board[x][y] != word[k]`：失败返回
- 若 `k == len(word) - 1` 且字符相等：成功返回
- 否则向 4 个方向扩展到未越界且未访问的邻格，递归匹配 `k+1`
- 回溯时撤销 `visited` 标记（或恢复原字符），保证不影响其他分支/其他起点

剪枝与边界：

- 先判断 `len(word) > m*n` 可直接返回 `False`
- 访问边界检查必须在读格子前完成
- `visited` 的设置/撤销必须成对，否则会把合法路径错误剪掉

- 时间复杂度: $O(mn\cdot 4^L)$
- 空间复杂度: $O(L)$

其中 $L$ 为 `word` 长度；本解法用原地标记代替 `visited` 数组。

## 代码
```python
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        direction = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        start = word[0]
        m = len(board)   # m * n 矩形
        n = len(board[0])
        l = len(word)
        def dfs(x, y, idx): # [0, idx) 匹配成功
            if idx == l:
                return True
            for dir in direction:
                xn = x + dir[0]
                yn = y + dir[1]
                if not (0 <= xn < m and 0 <= yn < n):
                    continue
                if board[xn][yn] != word[idx]:
                    continue
                board[xn][yn] = '#'
                if (dfs(xn, yn, idx + 1)):
                    return True # 上报直接返回
                board[xn][yn] = word[idx]
            return False    # 4 个边界都不对
        for i in range(m):
            for j in range(n):
                if board[i][j] == start:
                    board[i][j] = '#'
                    if dfs(i, j, 1):
                        return True
                    board[i][j] = start
        return False
```
