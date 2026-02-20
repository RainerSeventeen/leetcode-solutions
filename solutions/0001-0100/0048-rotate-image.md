---
id: 48
title: 旋转图像
difficulty: Medium
tags: [array, math, matrix]
created: 2026-02-20
---

# 48. 旋转图像

## 题目链接
https://leetcode.cn/problems/rotate-image/

## 题目描述
暂无（需要从LeetCode获取）

## 解题思路
要求原地旋转 90°，可以按“分层 + 四点循环置换”做。

把矩阵看成若干层（外圈到内圈）。对每一层的每个位置 `(i, j)`，它会与另外三个位置形成一个 4 环：

`(i, j) -> (n-1-j, i) -> (n-1-i, n-1-j) -> (j, n-1-i) -> (i, j)`

按这个顺序做四点交换即可完成旋转。循环边界的写法（代码中 `i <= n/2-1`、`j <= (n-1)/2`）确保每个 4 环只处理一次，且奇偶 `n` 都覆盖到位。

- 时间复杂度: $O(n^2)$
- 空间复杂度: $O(1)$

## 代码
```cpp
class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        int n = matrix.size();
        for (int i = 0; i <= n / 2 - 1; i++) {
            for (int j = 0; j <= (n - 1) / 2; j++) {
                // 四点变换
                int tmp = matrix[i][j];
                matrix[i][j] = matrix[n - j - 1][i];
                matrix[n - j - 1][i] = matrix[n - i -1][n - j -1];
                matrix[n - i -1][n - j -1] = matrix[j][n - i -1];
                matrix[j][n - i -1] = tmp;
            }
        }
    }
};
```
