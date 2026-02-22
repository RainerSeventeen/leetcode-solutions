---
id: 51
title: N-Queens
difficulty: Hard
tags: [array, backtracking]
created: 2026-02-21
---

# 51. N 皇后

## 题目链接
https://leetcode.cn/problems/n-queens/

## 题目描述
<p>按照国际象棋的规则，皇后可以攻击与之处在同一行或同一列或同一斜线上的棋子。</p>

<p><strong>n&nbsp;皇后问题</strong> 研究的是如何将 <code>n</code>&nbsp;个皇后放置在 <code>n×n</code> 的棋盘上，并且使皇后彼此之间不能相互攻击。</p>

<p>给你一个整数 <code>n</code> ，返回所有不同的&nbsp;<strong>n<em>&nbsp;</em>皇后问题</strong> 的解决方案。</p>

<div class="original__bRMd">
<div>
<p>每一种解法包含一个不同的&nbsp;<strong>n 皇后问题</strong> 的棋子放置方案，该方案中 <code>'Q'</code> 和 <code>'.'</code> 分别代表了皇后和空位。</p>

<p><strong>示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/11/13/queens.jpg" style="width: 600px; height: 268px;" />
<pre>
<strong>输入：</strong>n = 4
<strong>输出：</strong>[[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
<strong>解释：</strong>如上图所示，4 皇后问题存在两个不同的解法。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>n = 1
<strong>输出：</strong>[["Q"]]
</pre>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 9</code></li>
</ul>
</div>
</div>


## 解题思路

按行回溯放皇后，每行枚举一个列位置，构造当前棋盘状态。
放置后检查同列、左上、右上是否冲突，合法则继续下一行，到第 `n` 行收集一个解。
- 时间复杂度: $O(n!)$
- 空间复杂度: $O(n^2)$

## 相关专题
- [链表、树与回溯](../../topics/linked-list-tree-backtracking.md)

## 代码
```cpp
class Solution {
public:
    vector<vector<string>> solveNQueens(int n) {
        path.clear();
        ret.clear();
        traceback(0, n);
        return ret;;
    }
    vector<vector<string>> ret;
    vector<string> path;

    void traceback(int count, const int total) {
        // count 表示已经放了几个
        if (count == total) {
            ret.push_back(path);
            return;
        }
        for (int i = 0; i < total; i++) {
            string line(total, '.');
            line[i] = 'Q';
            path.push_back(line);
            if (checkValid(i))
                traceback(count + 1, total);
            path.pop_back();
        }
    }
    bool checkValid(int q) {
        int collum = path.size() - 1;      // 当前行
        int n = path[0].size();            // 棋盘大小

        // 1) 纵向检查（只看之前的行）
        for (int i = 0; i < collum; i++) {
            if (path[i][q] == 'Q') return false;
        }

        // 2) 斜向检查：从当前行往上扫左上、右上
        for (int row = collum - 1, l = q - 1, r = q + 1;
            row >= 0;
            --row, --l, ++r) {

            if (l >= 0 && path[row][l] == 'Q') return false;      // 左上
            if (r < n && path[row][r] == 'Q') return false;     // 右上
        }
        return true;
    }
};
```
