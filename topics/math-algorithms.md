# 数学算法（数论/组合/概率期望/博弈/计算几何/随机算法）

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
- 0054 - 螺旋矩阵 ｜ [LeetCode 链接](https://leetcode.cn/problems/spiral-matrix/) ｜ [题解笔记](../solutions/0001-0100/0054-spiral-matrix.md)
- 0059 - 螺旋矩阵 II ｜ [LeetCode 链接](https://leetcode.cn/problems/spiral-matrix-ii/) ｜ [题解笔记](../solutions/0001-0100/0059-spiral-matrix-ii.md)
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
- 1925 - 统计平方和三元组的数目 ｜ [LeetCode 链接](https://leetcode.cn/problems/count-square-sum-triples/) ｜ [题解笔记](../solutions/1901-2000/1925-count-square-sum-triples.md)
- 3512 - 使数组和能被 K 整除的最少操作次数 ｜ [LeetCode 链接](https://leetcode.cn/problems/minimum-operations-to-make-array-sum-divisible-by-k/) ｜ [题解笔记](../solutions/3501-3600/3512-minimum-operations-to-make-array-sum-divisible-by-k.md)

### 4.3 数位频次不变量
方法说明：

先对原数做数位统计并计算不变量，再把候选值映射到同一统计维度进行一致性校验。

#### 4.3.1 模板题目
- 3848 - 阶数数字排列 ｜ [LeetCode 链接](https://leetcode.cn/problems/check-digitorial-permutation/) ｜ [题解笔记](../solutions/3801-3900/3848-check-digitorial-permutation.md)

### 4.4 数位回文判断
方法说明：

通过反转整数后半段与前半段比较，可在不转字符串的前提下完成回文判断。

#### 4.4.1 模板题目
- 0009 - 回文数 ｜ [LeetCode 链接](https://leetcode.cn/problems/palindrome-number/) ｜ [题解笔记](../solutions/0001-0100/0009-palindrome-number.md)
## 5 易错点
- 原地旋转顺序写反会得到错误结果。
- 数位回退后未统一填 9 导致非最优。

## 6 总结
数学题重点在变换不变量和构造正确性，模板虽然短，但证明必须先行。
