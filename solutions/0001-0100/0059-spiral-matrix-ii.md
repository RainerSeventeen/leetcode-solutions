---
id: 59
title: Spiral Matrix II
difficulty: Medium
tags: [array, matrix, simulation]
created: 2026-02-21
---

# 59. 螺旋矩阵 II

## 题目链接
https://leetcode.cn/problems/spiral-matrix-ii/

## 题目描述
<p>给你一个正整数 <code>n</code> ，生成一个包含 <code>1</code> 到 <code>n<sup>2</sup></code> 所有元素，且元素按顺时针顺序螺旋排列的 <code>n x n</code> 正方形矩阵 <code>matrix</code> 。</p>

<p><strong>示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/11/13/spiraln.jpg" style="width: 242px; height: 242px;" />
<pre>
<strong>输入：</strong>n = 3
<strong>输出：</strong>[[1,2,3],[8,9,4],[7,6,5]]
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>n = 1
<strong>输出：</strong>[[1]]
</pre>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 <= n <= 20</code></li>
</ul>


## 解题思路

维护上、下、左、右四个边界，按“上行、右列、下行、左列”四个方向一圈圈填数。
每完成一个方向就收缩对应边界，并在进入下一方向前判断边界是否仍有效。
直到边界交错时结束，矩阵恰好填满 `1..n^2`。
- 时间复杂度: $O(n^2)$
- 空间复杂度: $O(1)$

## 代码
```cpp
class Solution {
public:
    vector<vector<int>> generateMatrix(int n) {
        vector<vector<int>> ret(n, vector<int>(n,0));
        int top = 0, bottom = n - 1;
        int left = 0, right = n - 1;
        int num = 1;    // 填充数字
        while (left <= right && top <= bottom) {

            for (int j = left; j <= right; j++) {
                ret[top][j] = num++;
            }
            top++;

            for (int i = top; i <= bottom; i++) {
                ret[i][right] = num++;
            }
            right--;

            if (top <= bottom) {
                for (int j = right; j >= left; j--) {
                    ret[bottom][j] = num++;
                }
                bottom--;
            }

            if (left <= right) {
                for (int i = bottom; i >= top; i--) {
                    ret[i][left] = num++;
                }
                left++;
            }                

        }
        return ret;

    }
};
```
