---
id: 37
title: Sudoku Solver
difficulty: Hard
tags: [array, hash-table, backtracking, matrix]
created: 2026-02-21
---

# 37. 解数独

## 题目链接
https://leetcode.cn/problems/sudoku-solver/

## 题目描述
<p>编写一个程序，通过填充空格来解决数独问题。</p>

<p>数独的解法需<strong> 遵循如下规则</strong>：</p>

<ol>
	<li>数字&nbsp;<code>1-9</code>&nbsp;在每一行只能出现一次。</li>
	<li>数字&nbsp;<code>1-9</code>&nbsp;在每一列只能出现一次。</li>
	<li>数字&nbsp;<code>1-9</code>&nbsp;在每一个以粗实线分隔的&nbsp;<code>3x3</code>&nbsp;宫内只能出现一次。（请参考示例图）</li>
</ol>

<p>数独部分空格内已填入了数字，空白格用&nbsp;<code>'.'</code>&nbsp;表示。</p>

<div class="top-view__1vxA">
<div class="original__bRMd">
<div>
<p><strong>示例 1：</strong></p>
<img src="https://assets.leetcode.cn/aliyun-lc-upload/uploads/2021/04/12/250px-sudoku-by-l2g-20050714svg.png" style="height:250px; width:250px" />
<pre>
<strong>输入：</strong>board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
<strong>输出：</strong>[["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]
<strong>解释：</strong>输入的数独如上图所示，唯一有效的解决方案如下所示：

<img src=" https://assets.leetcode.cn/aliyun-lc-upload/uploads/2021/04/12/250px-sudoku-by-l2g-20050714_solutionsvg.png" style="height:250px; width:250px" />
</pre>

<p><strong>提示：</strong></p>

<ul>
	<li><code>board.length == 9</code></li>
	<li><code>board[i].length == 9</code></li>
	<li><code>board[i][j]</code> 是一位数字或者 <code>'.'</code></li>
	<li>题目数据 <strong>保证</strong> 输入数独仅有一个解</li>
</ul>
</div>
</div>
</div>


## 解题思路

使用回溯：按行列找到第一个空格，依次尝试填入 `1~9`。
每次填数后检查当前行、列和 3x3 宫是否合法，合法则递归下一个空格，不合法就撤销。
- 时间复杂度: $O(9^m)$（$m$ 为空格数）
- 空间复杂度: $O(m)$

## 相关专题
- [链表、树与回溯](../../topics/linked-list-tree-backtracking.md)

## 代码
```cpp
class Solution {
public:
    void solveSudoku(vector<vector<char>>& board) {
        traceback(board);
    }
    
    bool traceback(vector<vector<char>>& board) {
        // 二维遍历，遍历终止就表示填充完毕，直接终止
        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                if (board[i][j] != '.') continue;
                // 递归遍历
                for (char num = '1'; num <= '9'; num++) {
                    board[i][j] = num;
                    if (checkValid(board, i, j))
                        if (traceback(board)) return true;
                    board[i][j] = '.';
                }
                return false; //  9 个数字用完了
            }
        }
        return true;
    }

    bool checkValid(vector<vector<char>>& board, int i, int j) {
        // board[i][j] 是上个放入的数据
        
        for (int row = 0; row < 9; row++) {
            if (row != i && board[row][j] == board[i][j])
                return false; 
        }
        for (int col = 0; col < 9; col++) {
            if (col != j && board[i][col] == board[i][j])
                return false;
        }
        int row_s = i / 3 * 3;
        int col_s = j / 3 * 3;
        for (int r = row_s; r < row_s + 3; r++) {
            for (int c = col_s; c < col_s + 3; c++) {
                if (r == i && c == j) continue;
                if (board[r][c] == board[i][j])
                    return false;
            }
        }
        return true;
    }
};
```
