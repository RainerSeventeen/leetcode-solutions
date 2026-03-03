# 数学算法（数论/组合/概率期望/博弈/计算几何/随机算法）

## 概览
数学算法专题聚焦数论、组合计数、概率期望、博弈、计算几何与随机化方法，核心在于建模与证明。

## 核心思想
- 先识别数学结构：同余、因子、组合模型、几何关系或随机过程。
- 用不变量、构造法、反证法或计数拆分建立正确性。
- 将公式化思路落地为可复用模板，并严格处理边界与取模。

## 解题流程
1. 抽象问题中的数学对象与约束。
2. 选择对应工具并给出关键结论或证明。
3. 编写模板并用小样例验证正确性与边界。
4. 回查复杂度、溢出风险、取模与特殊值处理。

## 模板与子方法
### 数论

#### 判断质数
模板：

```python
# 时间复杂度 O(sqrt(n))
def is_prime(n: int) -> bool:
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return n >= 2  # 1 不是质数
```

模板题目：


#### 预处理质数（筛质数）
模板：

```python
# 时间复杂度 O(MX * log log MX)
MX = 1_000_001
is_prime = [False] * 2 + [True] * (MX - 2)  # 0 和 1 不是质数
primes = []
for i in range(2, MX):
    if is_prime[i]:
        primes.append(i)
        for j in range(i * i, MX, i):
            is_prime[j] = False  # j 是质数 i 的倍数
```

模板题目：


#### 质因数分解
模板：

```python
MX = 1_000_001
prime_factors = [[] for _ in range(MX)]
for i in range(2, MX):
    if not prime_factors[i]:  # i 是质数
        for j in range(i, MX, i):  # i 的倍数 j 有质因子 i
            prime_factors[j].append(i)
```

模板题目：


#### 阶乘分解
模板：

```python
# 待补充
```

模板题目：


#### 因子
模板：

```python
# 预处理每个数的因子
MX = 1_000_001  # **根据题目调整**
divisors = [[] for _ in range(MX)]
for i in range(1, MX):
    for j in range(i, MX, i):  # 枚举 i 的倍数 j
        divisors[j].append(i)  # i 是 j 的因子
```

模板题目：


#### 最大公约数（GCD）
模板：

```python
# 待补充
```

模板题目：


#### 最小公倍数（LCM）
模板：

```python
# 待补充
```

模板题目：


#### 互质
模板：

```python
# 待补充
```

模板题目：


#### 同余
模板：

```python
# 待补充
```

模板题目：


#### 数论分块
模板：

```python
# 待补充
```

模板题目：

- 1925 - 统计平方和三元组的数目 ｜ [LeetCode 链接](https://leetcode.cn/problems/count-square-sum-triples/) ｜ [题解笔记](../solutions/1901-2000/1925-count-square-sum-triples.md)

#### 其他
模板：

```python
# 待补充
```

模板题目：


### 组合数学

#### 乘法原理
模板：

```python
# 待补充
```

模板题目：


#### 组合计数
模板：

```python
# 待补充
```

模板题目：


#### 放球问题
模板：

```python
# 待补充
```

模板题目：


#### 容斥原理
模板：

```python
# 待补充
```

模板题目：


#### 生成函数（母函数）
模板：

```python
# 待补充
```

模板题目：


### 概率期望

待补充...

### 博弈论

待补充...

### 计算几何

#### 点、线
模板：

```python
# 待补充
```

模板题目：


#### 圆
模板：

```python
# 待补充
```

模板题目：


#### 矩形、多边形
模板：

```python
# 待补充
```

模板题目：


#### 凸包
模板：

```python
class Vec:
    __slots__ = 'x', 'y'

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __sub__(self, b: "Vec") -> "Vec":
        return Vec(self.x - b.x, self.y - b.y)

    def det(self, b: "Vec") -> int:
        return self.x * b.y - self.y * b.x


# Andrew 算法，计算 points 的凸包（逆时针顺序）
# 时间复杂度 O(n log n)，其中 n = len(points)
def convexHull(points: List[Vec]) -> List[Vec]:
    if len(points) <= 1:
        return points

    points.sort(key=lambda p: (p.x, p.y))

    q = []

    # 计算下凸包（从左到右）
    for p in points:
        # 新来的点 p，能否让旧的点变成在凸包内的点？ ->  需要判断向量左右关系  ->  det
        while len(q) > 1 and (q[-1] - q[-2]).det(p - q[-1]) <= 0:
            q.pop()
        q.append(p)

    # 计算上凸包（从右到左）
    # 注意下凸包的最后一个点，已经是上凸包的（右边）第一个点了，所以从 n-2 开始遍历
    lower_size = len(q)
    for i in range(len(points) - 2, -1, -1):
        p = points[i]
        while len(q) > lower_size and (q[-1] - q[-2]).det(p - q[-1]) <= 0:
            q.pop()
        q.append(p)

    # 此时首尾是同一个点 points[0]，需要去掉
    q.pop()

    return q
```

模板题目：


### 随机算法

#### 随机数
模板：

```python
# 待补充
```

模板题目：


#### 随机化技巧
模板：

```python
# 待补充
```

模板题目：


### 杂项

#### 回文数
模板：

```python
def gen_palindrome() -> Iterator[int]:
    base = 1
    while True:
        # 生成奇数长度回文数，例如 base = 10，生成的范围是 101 ~ 999
        for i in range(base, base * 10):
            s = str(i)
            x = int(s + s[::-1][1:])
            yield x

        # 生成偶数长度回文数，例如 base = 10，生成的范围是 1001 ~ 9999
        for i in range(base, base * 10):
            s = str(i)
            x = int(s + s[::-1])
            yield x

        base *= 10


for x in gen_palindrome():
    if x > 10 ** 9:  # 根据题目调整
        break
    # 处理 x 的逻辑写下面
    print(x)
```

模板题目：

- 0009 - 回文数 ｜ [LeetCode 链接](https://leetcode.cn/problems/palindrome-number/) ｜ [题解笔记](../solutions/0001-0100/0009-palindrome-number.md)

#### 整数拆分
模板：

```python
# 待补充
```

模板题目：


#### 曼哈顿距离与切比雪夫距离
模板：

```python
# 待补充
```

模板题目：


#### 多项式
模板：

```python
# 待补充
```

模板题目：


#### 快速沃尔什变换（FWT）
模板：

```python
# 待补充
```

模板题目：


#### 线性基
模板：

```python
# 待补充
```

模板题目：


#### 摩尔投票法
模板：

```python
# 待补充
```

模板题目：

- 0169 - 多数元素 ｜ [LeetCode 链接](https://leetcode.cn/problems/majority-element/) ｜ [题解笔记](../solutions/0101-0200/0169-majority-element.md)

#### 其他
模板：

```python
# 待补充
```

模板题目：
