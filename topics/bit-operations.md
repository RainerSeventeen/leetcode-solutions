# 位运算（基础/性质/拆位/试填/恒等式/思维）

## 概览
位运算专题覆盖按位操作、异或性质、AND/OR 单调性、拆位贡献、逐位试填、恒等式、线性基与思维构造。核心目标是把二进制性质转化为可实现的模板。

## 核心思想
- 异或满足交换律、结合律，且有自反消去性质。
- `x & (x - 1)` 可消去最低位的 `1`，常用于位计数与状态跳转。
- AND 随参与元素增多不增，OR 随参与元素增多不减，可用于按位贪心与区间收缩。
- 按位拆分后可把全局问题转为独立 bit 贡献求和。

## 解题流程
1. 识别问题是否可按位独立处理，或存在异或抵消类不变量。
2. 选择模型：位统计、异或前缀、LogTrick、拆位贡献、逐位试填、线性基。
3. 明确位宽、移位规则与边界值（`0`、全 `1`、最高位单点）。
4. 通过模板题验证复杂度，再按题意替换状态转移或判定逻辑。

## 模板与子方法
### 基础题
#### 通用位运算基础
模板：

```python
def bit_count(x: int) -> int:
    cnt = 0
    while x:
        x &= x - 1
        cnt += 1
    return cnt


def hamming_distance(x: int, y: int) -> int:
    return bit_count(x ^ y)
```

模板题目：
- 0461 - 汉明距离 ｜ [LeetCode 链接](https://leetcode.cn/problems/hamming-distance/) ｜ [题解笔记](../solutions/0401-0500/0461-hamming-distance.md)
- 0067 - 二进制求和 ｜ [LeetCode 链接](https://leetcode.cn/problems/add-binary/) ｜ [题解笔记](../solutions/0001-0100/0067-add-binary.md)
- 0338 - 比特位计数 ｜ [LeetCode 链接](https://leetcode.cn/problems/counting-bits/) ｜ [题解笔记](../solutions/0301-0400/0338-counting-bits.md)
- 0693 - 交替位二进制数 ｜ [LeetCode 链接](https://leetcode.cn/problems/binary-number-with-alternating-bits/) ｜ [题解笔记](../solutions/0601-0700/0693-binary-number-with-alternating-bits.md)
- 0762 - 二进制表示中质数个计算置位 ｜ [LeetCode 链接](https://leetcode.cn/problems/prime-number-of-set-bits-in-binary-representation/) ｜ [题解笔记](../solutions/0701-0800/0762-prime-number-of-set-bits-in-binary-representation.md)
- 0868 - 二进制间距 ｜ [LeetCode 链接](https://leetcode.cn/problems/binary-gap/) ｜ [题解笔记](../solutions/0801-0900/0868-binary-gap.md)
- 1009 - 十进制整数的反码 ｜ [LeetCode 链接](https://leetcode.cn/problems/complement-of-base-10-integer/) ｜ [题解笔记](../solutions/1001-1100/1009-complement-of-base-10-integer.md)
- 1356 - 根据数字二进制下 1 的数目排序 ｜ [LeetCode 链接](https://leetcode.cn/problems/sort-integers-by-the-number-of-1-bits/) ｜ [题解笔记](../solutions/1301-1400/1356-sort-integers-by-the-number-of-1-bits.md)
- 3827 - 统计单比特整数 ｜ [LeetCode 链接](https://leetcode.cn/problems/count-monobit-integers/) ｜ [题解笔记](../solutions/3801-3900/3827-count-monobit-integers.md)

#### 用位运算代替数组操作
待补充...

#### 反转二进制数
模板：

```python
def reverse_bits(n: int) -> int:
    ans = 0
    for _ in range(32):
        ans = (ans << 1) | (n & 1)
        n >>= 1
    return ans
```

模板题目：
- 0190 - 颠倒二进制位 ｜ [LeetCode 链接](https://leetcode.cn/problems/reverse-bits/) ｜ [题解笔记](../solutions/0101-0200/0190-reverse-bits.md)

### 异或（XOR）的性质
#### 异或抵消
模板：

```python
def single_number(nums):
    x = 0
    for v in nums:
        x ^= v
    return x
```

模板题目：
待补充...

### 与或（AND/OR）的性质
#### AND/OR 基础性质
模板：

```python
def minimum_flips(a: int, b: int, c: int) -> int:
    ans = 0
    while a or b or c:
        x, y, z = a & 1, b & 1, c & 1
        if z == 0:
            ans += x + y
        elif x == 0 and y == 0:
            ans += 1
        a >>= 1
        b >>= 1
        c >>= 1
    return ans
```

模板题目：
待补充...

#### AND/OR LogTrick
模板：

```python
from typing import List


def log_trick_or(nums: List[int]) -> None:
    or_left = []
    for i, x in enumerate(nums):
        for p in or_left:
            p[0] |= x
        or_left.append([x, i])

        idx = 1
        for j in range(1, len(or_left)):
            if or_left[j][0] != or_left[j - 1][0]:
                or_left[idx] = or_left[j]
                idx += 1
        del or_left[idx:]
```

模板题目：
待补充...

#### GCD LogTrick
模板：

```python
import math
from typing import List


def log_trick_gcd(nums: List[int]) -> None:
    gcd_left = []
    for i, x in enumerate(nums):
        for p in gcd_left:
            p[0] = math.gcd(p[0], x)
        gcd_left.append([x, i])

        idx = 1
        for j in range(1, len(gcd_left)):
            if gcd_left[j][0] != gcd_left[j - 1][0]:
                gcd_left[idx] = gcd_left[j]
                idx += 1
        del gcd_left[idx:]
```

模板题目：
待补充...

### 拆位 / 贡献法
#### 二进制拆位
模板：

```python
def count_bits(n):
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        dp[i] = dp[i >> 1] + (i & 1)
    return dp
```

模板题目：
待补充...

#### 十进制拆位
模板：
待补充...

模板题目：
待补充...

### 试填法
#### 逐位试填
模板：
待补充...

模板题目：
待补充...

### 恒等式
#### 位运算恒等式
模板：
待补充...

模板题目：
待补充...

### 线性基
#### 最大异或和线性基
模板：

```python
class XorBasis:
    def __init__(self, n: int):
        self.b = [0] * n

    def insert(self, x: int) -> None:
        for i in range(len(self.b) - 1, -1, -1):
            if x >> i:
                if self.b[i] == 0:
                    self.b[i] = x
                    return
                x ^= self.b[i]

    def max_xor(self) -> int:
        res = 0
        for i in range(len(self.b) - 1, -1, -1):
            if res ^ self.b[i] > res:
                res ^= self.b[i]
        return res
```

模板题目：
待补充...

### 思维题
#### 贪心与脑筋急转弯
模板：
待补充...

模板题目：
待补充...

### 其他
#### 杂项
模板：

```python
def concatenated_binary(n: int) -> int:
    mod = 10**9 + 7
    ans = 0
    for x in range(1, n + 1):
        ans = ((ans << x.bit_length()) | x) % mod
    return ans
```

模板题目：
- 1680 - 连接连续二进制数字 ｜ [LeetCode 链接](https://leetcode.cn/problems/concatenation-of-consecutive-binary-numbers/) ｜ [题解笔记](../solutions/1601-1700/1680-concatenation-of-consecutive-binary-numbers.md)
- 0136 - 只出现一次的数字 ｜ [LeetCode 链接](https://leetcode.cn/problems/single-number/) ｜ [题解笔记](../solutions/0101-0200/0136-single-number.md)

### 关联题单
#### 外部题单索引
模板：
待补充...

模板题目：
待补充...

### 算法题单
#### 总题单索引
模板：
待补充...

模板题目：
待补充...

## 易错点
- 把 `x & (x - 1)` 误当作“提取最低位 1”，它实际是“清除最低位 1”。
- Python 负数是无限符号位语义，跨语言移位时需显式控制位宽。
- 位运算模板常见错误在边界处理：`0`、最高位、固定位宽循环次数。

## 总结
位运算题的关键是识别按位不变量，并选择匹配模板。对可拆位问题优先做 bit 级贡献分析，对区间按位运算优先考虑单调性与去重优化。
