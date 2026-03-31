# 字符串（KMP/Z函数/Manacher/字符串哈希/AC自动机/后缀数组/子序列自动机）

## 概览
本专题聚焦字符串匹配、回文处理、哈希比较、自动机与后缀结构等高频方法，用于子串/子序列判断、计数与构造问题。

## 核心思想
- 匹配问题优先考虑线性状态转移（KMP、Z 函数、AC 自动机）。
- 回文问题优先考虑中心扩展或 Manacher 的半径数组。
- 多子串比较与去重可使用滚动哈希、后缀数组/后缀自动机。
- 子序列问题可转化为“下一个出现位置”自动机查询。

## 解题流程
1. 先判断问题属于子串、子序列、回文或字典序比较。
2. 根据目标复杂度选择线性或近线性字符串工具。
3. 明确下标语义与边界后再实现模板。
4. 用最短反例验证失败跳转与窗口更新。

## 模板与子方法
### KMP（前缀的后缀）
#### 前缀函数匹配
模板：

```python
def kmp(text: str, pattern: str) -> list[int]:
    m = len(pattern)
    pi = [0] * m
    j = 0
    for i in range(1, m):
        while j and pattern[j] != pattern[i]:
            j = pi[j - 1]
        if pattern[j] == pattern[i]:
            j += 1
        pi[i] = j

    ans = []
    j = 0
    for i, ch in enumerate(text):
        while j and pattern[j] != ch:
            j = pi[j - 1]
        if pattern[j] == ch:
            j += 1
        if j == m:
            ans.append(i - m + 1)
            j = pi[j - 1]
    return ans
```

模板题目：

- 0028 - 找出字符串中第一个匹配项的下标 ｜ [LeetCode 链接](https://leetcode.cn/problems/find-the-index-of-the-first-occurrence-in-a-string/) ｜ [题解笔记](../solutions/0001-0100/0028-find-the-index-of-the-first-occurrence-in-a-string.md)

### Z 函数（后缀的前缀）
#### Z 数组匹配
模板：

```python
def calc_z(s: str) -> list[int]:
    n = len(s)
    z = [0] * n
    l = r = 0
    for i in range(1, n):
        if i <= r:
            z[i] = min(z[i - l], r - i + 1)
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            l, r = i, i + z[i]
            z[i] += 1
    z[0] = n
    return z
```

模板题目：

待补充...

#### LCP 数组应用
模板：

```python
def lcp_by_z(s: str) -> list[int]:
    # 待补充：按具体题意构造并复用 Z 数组
    return calc_z(s)
```

模板题目：

待补充...

#### 字符串构造
模板：

```python
# 待补充
```

模板题目：

- 3474 - 字典序最小的生成字符串 ｜ [LeetCode 链接](https://leetcode.cn/problems/lexicographically-smallest-generated-string/) ｜ [题解笔记](../solutions/3401-3500/3474-lexicographically-smallest-generated-string.md)

### Manacher 算法（回文串）
#### Manacher 模板
模板：

```python
def manacher(s: str) -> list[int]:
    t = "#" + "#".join(s) + "#"
    n = len(t)
    p = [0] * n
    c = r = 0
    for i in range(n):
        if i < r:
            p[i] = min(r - i, p[2 * c - i])
        while 0 <= i - p[i] - 1 and i + p[i] + 1 < n and t[i - p[i] - 1] == t[i + p[i] + 1]:
            p[i] += 1
        if i + p[i] > r:
            c, r = i, i + p[i]
    return p
```

模板题目：

- 0005 - 最长回文子串 ｜ [LeetCode 链接](https://leetcode.cn/problems/longest-palindromic-substring/) ｜ [题解笔记](../solutions/0001-0100/0005-longest-palindromic-substring.md)
- 0647 - 回文子串 ｜ [LeetCode 链接](https://leetcode.cn/problems/palindromic-substrings/) ｜ [题解笔记](../solutions/0601-0700/0647-palindromic-substrings.md)

#### 中心扩展法
模板：

```python
def count_substrings(s: str) -> int:
    n = len(s)
    ans = 0
    for c in range(2 * n - 1):
        l = c // 2
        r = l + c % 2
        while l >= 0 and r < n and s[l] == s[r]:
            ans += 1
            l -= 1
            r += 1
    return ans
```

模板题目：

待补充...

### 字符串哈希
#### 多项式哈希
模板：

```python
def build_hash(s: str, base: int = 911382323, mod: int = 1_000_000_007):
    n = len(s)
    p = [1] * (n + 1)
    h = [0] * (n + 1)
    for i, ch in enumerate(s, 1):
        p[i] = p[i - 1] * base % mod
        h[i] = (h[i - 1] * base + ord(ch)) % mod
    return p, h
```

模板题目：

待补充...

### 最小表示法
#### 最小循环同构串
模板：

```python
def smallest_representation(s: str) -> str:
    t = s + s
    n = len(s)
    i, j = 0, 1
    while i < n and j < n:
        k = 0
        while k < n and t[i + k] == t[j + k]:
            k += 1
        if k == n:
            break
        if t[i + k] <= t[j + k]:
            j = j + k + 1
        else:
            i = max(i + k + 1, j)
            j = i + 1
    return t[min(i, j):min(i, j) + n]
```

模板题目：

待补充...

### 字典树
#### Trie 基础
模板：

```python
class Trie:
    def __init__(self):
        self.son = {}
        self.end = False
```

模板题目：

待补充...

### AC 自动机
#### Trie + 失配指针
模板：

```python
from collections import deque


def build_fail(trie):
    q = deque()
    for node in trie[0]["next"].values():
        trie[node]["fail"] = 0
        q.append(node)
    while q:
        u = q.popleft()
        for ch, v in trie[u]["next"].items():
            f = trie[u]["fail"]
            while f and ch not in trie[f]["next"]:
                f = trie[f]["fail"]
            trie[v]["fail"] = trie[f]["next"].get(ch, 0)
            q.append(v)
```

模板题目：

待补充...

### 后缀数组/后缀自动机
#### 后缀结构基础
模板：

```python
def suffix_array(s: str) -> list[int]:
    # 待补充：按倍增或 SA-IS 实现
    return sorted(range(len(s)), key=lambda i: s[i:])
```

模板题目：

待补充...

### 子序列自动机
#### next 数组跳转
模板：

```python
def build_next(s: str):
    n = len(s)
    nxt = [[n] * 26 for _ in range(n + 1)]
    for i in range(n - 1, -1, -1):
        nxt[i] = nxt[i + 1][:]
        nxt[i][ord(s[i]) - 97] = i
    return nxt
```

模板题目：

待补充...

### 其他
#### 综合应用
模板：

```python
def solve():
    # 待补充：按题目组合字符串工具
    pass
```

模板题目：

待补充...

## 易错点
- KMP 与 Z 函数实现中最容易错在边界回退与下标偏移。
- Manacher 需要统一变换串与原串的下标映射。
- 哈希比较子串时要注意负值取模与碰撞风险。

## 总结
字符串题目的关键是先选对模型，再写对边界。以线性模板为主，按题意组合即可覆盖多数场景。
