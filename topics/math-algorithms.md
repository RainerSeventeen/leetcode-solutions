# 数学算法

## 1 概览
数学算法题强调不变量、变换规则与数位构造，通常不依赖复杂结构。

## 2 核心思想
- 矩阵变换依赖操作顺序与对称性。
- 数位构造依赖从高位到低位维护约束。
- 证明常用不变量、反证或构造法。

## 3 解题流程
1. 确认数学对象：矩阵、数位、公式或不变量。
2. 给出变换规则并证明合法性。
3. 优先写可手算验证的小模板。
4. 检查边界：前导零、回退、原地修改。

## 4 模板与子方法
### 4.1 矩阵原地变换
方法说明：
适用于旋转、转置、镜像等原地矩阵操作。网格题视角可交叉到网格专题。

模板代码：
```python
def rotate_matrix_90(a):
    n = len(a)
    for i in range(n):
        for j in range(i + 1, n):
            a[i][j], a[j][i] = a[j][i], a[i][j]
    for row in a:
        row.reverse()
```

#### 4.1.1 模板题目
- 0048 - 旋转图像 ｜ [LeetCode 链接](https://leetcode.cn/problems/rotate-image/) ｜ [题解笔记](../solutions/0001-0100/0048-rotate-image.md)
### 4.2 数位贪心构造
方法说明：
按位扫描并在冲突处回退高位，再把低位置 9。该题也可归入贪心专题。

模板代码：
```python
def monotone_increasing_digits(n):
    s = list(str(n))
    mark = len(s)
    for i in range(len(s) - 1, 0, -1):
        if s[i - 1] > s[i]:
            s[i - 1] = str(int(s[i - 1]) - 1)
            mark = i
    for i in range(mark, len(s)):
        s[i] = '9'
    return int(''.join(s))
```

#### 4.2.1 模板题目
- 0738 - 单调递增的数字 ｜ [LeetCode 链接](https://leetcode.cn/problems/monotone-increasing-digits/) ｜ [题解笔记](../solutions/0701-0800/0738-monotone-increasing-digits.md)
## 5 易错点
- 原地旋转顺序写反会得到错误结果。
- 数位回退后未统一填 9 导致非最优。

## 6 总结
数学题重点在变换不变量和构造正确性，模板虽然短，但证明必须先行。
