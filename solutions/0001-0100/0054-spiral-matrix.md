---
id: 54
title: Spiral Matrix
difficulty: Medium
tags: [array, matrix, simulation]
created: 2026-02-21
---

# 54. 螺旋矩阵

## 题目链接
https://leetcode.cn/problems/spiral-matrix/

## 题目描述
<p>给你一个 <code>m</code> 行 <code>n</code> 列的矩阵 <code>matrix</code> ，请按照 <strong>顺时针螺旋顺序</strong> ，返回矩阵中的所有元素。</p>

<p><strong>示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/11/13/spiral1.jpg" style="width: 242px; height: 242px;" />
<pre>
<strong>输入：</strong>matrix = [[1,2,3],[4,5,6],[7,8,9]]
<strong>输出：</strong>[1,2,3,6,9,8,7,4,5]
</pre>

<p><strong>示例 2：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/11/13/spiral.jpg" style="width: 322px; height: 242px;" />
<pre>
<strong>输入：</strong>matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
<strong>输出：</strong>[1,2,3,4,8,12,11,10,9,5,6,7]
</pre>

<p><strong>提示：</strong></p>

<ul>
	<li><code>m == matrix.length</code></li>
	<li><code>n == matrix[i].length</code></li>
	<li><code>1 <= m, n <= 10</code></li>
	<li><code>-100 <= matrix[i][j] <= 100</code></li>
</ul>


## 解题思路

维护当前方向 `(dx, dy)` 与当前位置 `(x, y)`，每次先取值再把当前位置标记为已访问。
若下一步越界或碰到已访问位置，就按顺时针规则旋转方向后再前进。
总共执行 `m*n` 次即可按螺旋顺序收集完整矩阵。
- 时间复杂度: $O(mn)$
- 空间复杂度: $O(1)$

## 相关专题
- [数学算法](../../topics/math-algorithms.md)

## 代码
```cpp
class Solution {
public:
    int dx = 0,dy = 1;
    int x = 0, y = 0;// 当前指针
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        int hei = matrix.size(); // 高度 
        int len = matrix[0].size(); // 宽度 
        vector<int> ret; 
        for (int k = 0; k < hei * len; k++){
            ret.push_back(matrix[x][y]);
            matrix[x][y] = -101;
            if (!check(matrix, len, hei)){
                turn(); // 转弯
            }
            x += dx;
            y += dy;
        }
        return ret;
    }
private:
    void turn(){
        int tmp = dy;
        dy = 0 - dx;
        dx = tmp;
    }
    bool check(vector<vector<int>>& matrix, int len, int hei){
        if (dx + x >= hei || dx + x < 0)
            return false;
        if (dy + y >= len || dy + y < 0)
            return false;
        if (matrix[x + dx][y + dy] == -101)
            return false;
        return true;
    }
};
```
