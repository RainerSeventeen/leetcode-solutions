# 位运算

## 1 概览
位运算题关注按位性质、异或抵消、位掩码与低位操作，常用于线性时间和常数空间优化。

## 2 核心思想
- 异或：相同抵消、交换律结合律。
- 位计数：利用 `x & (x - 1)` 消去最低位 1。
- 位递推：通过右移或最低位关系写状态转移。

## 3 解题流程
1. 识别按位不变量（奇偶次出现、位和、掩码状态）。
2. 选异或、计数或位 DP 递推模型。
3. 注意语言差异（有符号移位、负数表示）。
4. 用边界值测试：0、全 1、单个高位。

## 4 模板与子方法
### 4.1 异或抵消
方法说明：
当除一个元素外其他都成对出现时，异或可线性求解。

模板代码：
```python
def single_number(nums):
    x = 0
    for v in nums:
        x ^= v
    return x
```

#### 4.1.1 模板题目
- 0136 - 只出现一次的数字 ｜ [LeetCode 链接](https://leetcode.cn/problems/single-number/) ｜ [题解笔记](../solutions/0101-0200/0136-single-number.md)
### 4.2 按位统计
方法说明：
统计两个数在二进制位上不同的数量，可用异或后统计 1 的个数。

模板代码：
```python
def bit_count(x):
    cnt = 0
    while x:
        x &= x - 1
        cnt += 1
    return cnt


def hamming_distance(x, y):
    return bit_count(x ^ y)
```

#### 4.2.1 模板题目
- 0461 - 汉明距离 ｜ [LeetCode 链接](https://leetcode.cn/problems/hamming-distance/) ｜ [题解笔记](../solutions/0401-0500/0461-hamming-distance.md)
### 4.3 位运算递推
方法说明：
通过 `i >> 1` 或 `i & (i - 1)` 构建从小到大的递推。该类也可交叉到动态规划专题。

模板代码：
```python
def count_bits(n):
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        dp[i] = dp[i >> 1] + (i & 1)
    return dp
```

#### 4.3.1 模板题目
- 0338 - 比特位计数 ｜ [LeetCode 链接](https://leetcode.cn/problems/counting-bits/) ｜ [题解笔记](../solutions/0301-0400/0338-counting-bits.md)
## 5 易错点
- 把 `x & (x - 1)` 误解为“取最低位 1”。
- Python 负数按位行为与固定宽度整型不同。
- 位递推初始化与下标边界易漏。

## 6 总结
位运算题重点是识别按位不变量，常见高频模板是异或抵消、清最低位
