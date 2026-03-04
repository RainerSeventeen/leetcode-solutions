# 常用数据结构（枚举技巧/前缀和/差分/栈/队列/堆/字典树/并查集/树状数组/线段树）

## 概览
本专题聚焦哈希、栈、堆、Trie、前缀和等高频结构，目标是以结构换时间。

## 核心思想
- 哈希：O(1) 平均查询与去重。
- 栈/堆：分别维护最近约束与 Top-K。
- Trie：前缀匹配与字典树检索。
- 前缀和：区间信息前缀化，配合哈希计数。

## 解题流程
1. 明确操作需求：查找、维护最值、前缀统计或结构设计。
2. 选择主结构并定义其不变量。
3. 处理更新与查询的一致性。
4. 用复杂度校验是否达到题目要求。

## 模板与子方法
### 常用枚举技巧
#### 枚举右，维护左
模板：适用于查找补数、分组、去重与连续性判断。与图并查集思路可交叉，但实现更轻量。

```python
def two_sum(nums, target):
    pos = {}
    for i, x in enumerate(nums):
        if target - x in pos:
            return [pos[target - x], i]
        pos[x] = i
    return []
```

模板题目：
- 0001 - 两数之和 ｜ [LeetCode 链接](https://leetcode.cn/problems/two-sum/) ｜ [题解笔记](../solutions/0001-0100/0001-two-sum.md)
- 0454 - 四数相加 II ｜ [LeetCode 链接](https://leetcode.cn/problems/4sum-ii/) ｜ [题解笔记](../solutions/0401-0500/0454-4sum-ii.md)
- 3713 - 最长的平衡子串 I ｜ [LeetCode 链接](https://leetcode.cn/problems/longest-balanced-substring-i/) ｜ [题解笔记](../solutions/3701-3800/3713-longest-balanced-substring-i.md)

#### 枚举中间
模板：

```python
# 待补充
```

模板题目：
待补充...

#### 遍历对角线
模板：

```python
# 待补充
```

模板题目：
待补充...

### 前缀和
#### 基础
模板：

```python
# 待补充
```

模板题目：
待补充...

#### 前缀和与哈希表
模板：将区间和问题转成前缀差，配合哈希统计历史前缀出现次数。树路径前缀和可交叉到树专题。

```python
from collections import defaultdict


def subarray_sum(nums, k):
    cnt = defaultdict(int)
    cnt[0] = 1
    s = ans = 0
    for x in nums:
        s += x
        ans += cnt[s - k]
        cnt[s] += 1
    return ans
```

模板题目：
- 0560 - 和为 K 的子数组 ｜ [LeetCode 链接](https://leetcode.cn/problems/subarray-sum-equals-k/) ｜ [题解笔记](../solutions/0501-0600/0560-subarray-sum-equals-k.md)
- 3714 - 最长的平衡子串 II ｜ [LeetCode 链接](https://leetcode.cn/problems/longest-balanced-substring-ii/) ｜ [题解笔记](../solutions/3701-3800/3714-longest-balanced-substring-ii.md)

#### 距离和
模板：

```python
# 待补充
```

模板题目：
待补充...

#### 状态压缩前缀和
模板：

```python
# 待补充
```

模板题目：
待补充...

#### 进阶
模板：

```python
# 待补充
```

模板题目：
待补充...

#### 二维前缀和
模板：

```python
# 待补充
```

模板题目：
待补充...

#### 二维计数（行列统计）
模板：

```python
def num_special(mat):
    rows = [sum(r) for r in mat]
    cols = [sum(c) for c in zip(*mat)]
    ans = 0
    for i, row in enumerate(mat):
        for j, x in enumerate(row):
            if x == 1 and rows[i] == 1 and cols[j] == 1:
                ans += 1
    return ans
```

模板题目：
- 1582 - 二进制矩阵中的特殊位置 ｜ [LeetCode 链接](https://leetcode.cn/problems/special-positions-in-a-binary-matrix/) ｜ [题解笔记](../solutions/1501-1600/1582-special-positions-in-a-binary-matrix.md)

### 差分
#### 一维差分
模板：

```python
# 待补充
```

模板题目：
待补充...

#### 二维差分
模板：

```python
# 待补充
```

模板题目：
待补充...

### 栈
#### 基础
模板：适用于括号匹配、最小值维护等“后进先出”约束。

```python
class MinStack:
    def __init__(self):
        self.st = []
        self.mn = []

    def push(self, x):
        self.st.append(x)
        self.mn.append(x if not self.mn else min(x, self.mn[-1]))

    def pop(self):
        self.st.pop()
        self.mn.pop()
```

模板题目：
待补充...

#### 进阶
模板：

```python
# 待补充
```

模板题目：
- 0155 - 最小栈 ｜ [LeetCode 链接](https://leetcode.cn/problems/min-stack/) ｜ [题解笔记](../solutions/0101-0200/0155-min-stack.md)

#### 邻项消除
模板：

```python
# 待补充
```

模板题目：
- 1047 - 删除字符串中的所有相邻重复项 ｜ [LeetCode 链接](https://leetcode.cn/problems/remove-all-adjacent-duplicates-in-string/) ｜ [题解笔记](../solutions/1001-1100/1047-remove-all-adjacent-duplicates-in-string.md)

#### 合法括号字符串（RBS）
模板：

```python
# 待补充
```

模板题目：
- 0020 - 有效的括号 ｜ [LeetCode 链接](https://leetcode.cn/problems/valid-parentheses/) ｜ [题解笔记](../solutions/0001-0100/0020-valid-parentheses.md)

#### 表达式解析
模板：

```python
# 待补充
```

模板题目：
- 0150 - 逆波兰表达式求值 ｜ [LeetCode 链接](https://leetcode.cn/problems/evaluate-reverse-polish-notation/) ｜ [题解笔记](../solutions/0101-0200/0150-evaluate-reverse-polish-notation.md)

#### 对顶栈
模板：

```python
# 待补充
```

模板题目：
待补充...

#### 单调栈
模板：

```python
# 待补充
```

模板题目：
待补充...

### 队列
#### 基础
模板：

```python
# 待补充
```

模板题目：
待补充...

#### 设计
模板：设计题核心是保证每个操作复杂度满足要求，常见是 O(1) 的访问与淘汰。

```python
class LRUCache:
    def __init__(self, capacity):
        self.cap = capacity
        self.mp = {}
```

模板题目：
- 0225 - 用队列实现栈 ｜ [LeetCode 链接](https://leetcode.cn/problems/implement-stack-using-queues/) ｜ [题解笔记](../solutions/0201-0300/0225-implement-stack-using-queues.md)
- 0232 - 用栈实现队列 ｜ [LeetCode 链接](https://leetcode.cn/problems/implement-queue-using-stacks/) ｜ [题解笔记](../solutions/0201-0300/0232-implement-queue-using-stacks.md)

#### 双端队列
模板：

```python
# 待补充
```

模板题目：
待补充...

#### 单调队列
模板：

```python
# 待补充
```

模板题目：
- 0239 - 滑动窗口最大值 ｜ [LeetCode 链接](https://leetcode.cn/problems/sliding-window-maximum/) ｜ [题解笔记](../solutions/0201-0300/0239-sliding-window-maximum.md)

### 堆（优先队列）
#### 基础
模板：适用于动态维护前 K 大、小根堆调度与多路归并。链表多路合并可交叉到链表专题。

```python
import heapq


def top_k(nums, k):
    h = []
    for x in nums:
        if len(h) < k:
            heapq.heappush(h, x)
        elif x > h[0]:
            heapq.heapreplace(h, x)
    return h
```

模板题目：
待补充...

#### 进阶
模板：

```python
# 待补充
```

模板题目：
- 0023 - 合并 K 个升序链表 ｜ [LeetCode 链接](https://leetcode.cn/problems/merge-k-sorted-lists/) ｜ [题解笔记](../solutions/0001-0100/0023-merge-k-sorted-lists.md)

#### 第 K 小/大
模板：

```python
# 待补充
```

模板题目：
待补充...

#### 重排元素
模板：

```python
# 待补充
```

模板题目：
待补充...

#### 反悔堆
模板：

```python
# 待补充
```

模板题目：
待补充...

#### 懒删除堆
模板：

```python
# 待补充
```

模板题目：
待补充...

#### 对顶堆（滑动窗口第 K 小/大）
模板：

```python
# 待补充
```

模板题目：
待补充...

### 字典树（trie）
#### 基础
模板：适用于前缀查询、单词插入与字典匹配。

```python
class TrieNode:
    def __init__(self):
        self.next = {}
        self.end = False
```

模板题目：
- 0208 - 实现 Trie (前缀树) ｜ [LeetCode 链接](https://leetcode.cn/problems/implement-trie-prefix-tree/) ｜ [题解笔记](../solutions/0201-0300/0208-implement-trie-prefix-tree.md)

#### 进阶
模板：

```python
# 待补充
```

模板题目：
待补充...

#### 字典树优化 DP
模板：

```python
# 待补充
```

模板题目：
待补充...

#### 0-1 字典树（异或字典树）
模板：

```python
# 待补充
```

模板题目：
待补充...

### 并查集
#### 基础
模板：

```python
# 待补充
```

模板题目：
待补充...

#### 进阶
模板：

```python
# 待补充
```

模板题目：
待补充...

#### GCD 并查集
模板：

```python
# 待补充
```

模板题目：
待补充...

#### 数组上的并查集
模板：

```python
# 待补充
```

模板题目：
待补充...

#### 区间并查集
模板：

```python
# 待补充
```

模板题目：
待补充...

#### 带权并查集（边权并查集）
模板：

```python
# 待补充
```

模板题目：
- 0399 - 除法求值 ｜ [LeetCode 链接](https://leetcode.cn/problems/evaluate-division/) ｜ [题解笔记](../solutions/0301-0400/0399-evaluate-division.md)

### 树状数组和线段树
#### 树状数组
模板：

```python
# 待补充
```

模板题目：
待补充...

#### 逆序对
模板：

```python
# 待补充
```

模板题目：
待补充...

#### 线段树（无区间更新）
模板：

```python
# 待补充
```

模板题目：
待补充...

#### Lazy 线段树（有区间更新）
模板：

```python
# 待补充
```

模板题目：
待补充...

#### 动态开点线段树
模板：

```python
# 待补充
```

模板题目：
待补充...

#### 可持久化线段树
模板：

```python
# 待补充
```

模板题目：
待补充...

#### ST 表（Sparse Table）
模板：

```python
# 待补充
```

模板题目：
待补充...

### 伸展树（Splay 树）
待补充...

### 根号算法
#### 根号分解（Sqrt Decomposition）
模板：

```python
# 待补充
```

模板题目：
待补充...

#### 莫队算法
模板：

```python
# 待补充
```

模板题目：
待补充...

#### 其他
模板：

```python
# 待补充
```

模板题目：
待补充...

### 专题：离线算法
待补充...

### 编程能力强化训练
#### Part A
模板：

```python
# 待补充
```

模板题目：
- 0012 - 整数转罗马数字 ｜ [LeetCode 链接](https://leetcode.cn/problems/integer-to-roman/) ｜ [题解笔记](../solutions/0001-0100/0012-integer-to-roman.md)

#### Part B
模板：

```python
# 待补充
```

模板题目：
- 0146 - LRU 缓存 ｜ [LeetCode 链接](https://leetcode.cn/problems/lru-cache/) ｜ [题解笔记](../solutions/0101-0200/0146-lru-cache.md)

#### Part C
模板：

```python
# 待补充
```

模板题目：
待补充...

### 关联题单
待补充...

### 算法题单
待补充...

## 易错点
- 前缀和计数更新顺序错位。
- 堆里放值还是放键值对不清晰。
- 设计题忽略边界容量与重复操作。

## 总结
数据结构题本质是为操作目标选最匹配的结构组合，先写不变量，再实现更新与查询。
