# 常见数据结构

## 1 概览
本专题聚焦哈希、栈、堆、Trie、前缀和等高频结构，目标是以结构换时间。

## 2 核心思想
- 哈希：O(1) 平均查询与去重。
- 栈/堆：分别维护最近约束与 Top-K。
- Trie：前缀匹配与字典树检索。
- 前缀和：区间信息前缀化，配合哈希计数。

## 3 解题流程
1. 明确操作需求：查找、维护最值、前缀统计或结构设计。
2. 选择主结构并定义其不变量。
3. 处理更新与查询的一致性。
4. 用复杂度校验是否达到题目要求。

## 4 模板与子方法
### 4.1 哈希映射与集合
方法说明：
适用于查找补数、分组、去重与连续性判断。与图并查集思路可交叉，但实现更轻量。

模板代码：
```python
def two_sum(nums, target):
    pos = {}
    for i, x in enumerate(nums):
        if target - x in pos:
            return [pos[target - x], i]
        pos[x] = i
    return []
```

#### 4.1.1 模板题目
- 0001 - Two Sum ｜ [LeetCode 链接](https://leetcode.cn/problems/two-sum/) ｜ [题解笔记](../solutions/0001-0100/0001-two-sum.md)
- 0049 - 字母异位词分组 ｜ [LeetCode 链接](https://leetcode.cn/problems/group-anagrams/) ｜ [题解笔记](../solutions/0001-0100/0049-group-anagrams.md)
- 0128 - 最长连续序列 ｜ [LeetCode 链接](https://leetcode.cn/problems/longest-consecutive-sequence/) ｜ [题解笔记](../solutions/0101-0200/0128-longest-consecutive-sequence.md)
- 0448 - 找到所有数组中消失的数字 ｜ [LeetCode 链接](https://leetcode.cn/problems/find-all-numbers-disappeared-in-an-array/) ｜ [题解笔记](../solutions/0401-0500/0448-find-all-numbers-disappeared-in-an-array.md)
### 4.2 栈结构
方法说明：
适用于括号匹配、最小值维护等“后进先出”约束。

模板代码：
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

#### 4.2.1 模板题目
- 0020 - 有效的括号 ｜ [LeetCode 链接](https://leetcode.cn/problems/valid-parentheses/) ｜ [题解笔记](../solutions/0001-0100/0020-valid-parentheses.md)
- 0155 - 最小栈 ｜ [LeetCode 链接](https://leetcode.cn/problems/min-stack/) ｜ [题解笔记](../solutions/0101-0200/0155-min-stack.md)
### 4.3 堆与 Top-K
方法说明：
适用于动态维护前 K 大、小根堆调度与多路归并。链表多路合并可交叉到链表专题。

模板代码：
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

#### 4.3.1 模板题目
- 0215 - Kth Largest Element in an Array ｜ [LeetCode 链接](https://leetcode.cn/problems/kth-largest-element-in-an-array/) ｜ [题解笔记](../solutions/0201-0300/0215-kth-largest-element-in-an-array.md)
- 0347 - 前 K 个高频元素 ｜ [LeetCode 链接](https://leetcode.cn/problems/top-k-frequent-elements/) ｜ [题解笔记](../solutions/0301-0400/0347-top-k-frequent-elements.md)
- 0023 - 合并 K 个升序链表 ｜ [LeetCode 链接](https://leetcode.cn/problems/merge-k-sorted-lists/) ｜ [题解笔记](../solutions/0001-0100/0023-merge-k-sorted-lists.md)
- 0253 - 会议室 II ｜ [LeetCode 链接](https://leetcode.cn/problems/meeting-rooms-ii/) ｜ [题解笔记](../solutions/0201-0300/0253-meeting-rooms-ii.md)
### 4.4 Trie 与前缀树
方法说明：
适用于前缀查询、单词插入与字典匹配。

模板代码：
```python
class TrieNode:
    def __init__(self):
        self.next = {}
        self.end = False
```

#### 4.4.1 模板题目
- 0208 - Implement Trie (Prefix Tree) ｜ [LeetCode 链接](https://leetcode.cn/problems/implement-trie-prefix-tree/) ｜ [题解笔记](../solutions/0201-0300/0208-implement-trie-prefix-tree.md)
### 4.5 前缀和与哈希计数
方法说明：
将区间和问题转成前缀差，配合哈希统计历史前缀出现次数。树路径前缀和可交叉到树专题。

模板代码：
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

#### 4.5.1 模板题目
- 0560 - 和为 K 的子数组 ｜ [LeetCode 链接](https://leetcode.cn/problems/subarray-sum-equals-k/) ｜ [题解笔记](../solutions/0501-0600/0560-subarray-sum-equals-k.md)
- 0238 - Product of Array Except Self ｜ [LeetCode 链接](https://leetcode.cn/problems/product-of-array-except-self/) ｜ [题解笔记](../solutions/0201-0300/0238-product-of-array-except-self.md)
- 0437 - 路径总和 III ｜ [LeetCode 链接](https://leetcode.cn/problems/path-sum-iii/) ｜ [题解笔记](../solutions/0401-0500/0437-path-sum-iii.md)
### 4.6 结构设计（哈希 + 双链表）
方法说明：
设计题核心是保证每个操作复杂度满足要求，常见是 O(1) 的访问与淘汰。

模板代码：
```python
class LRUCache:
    def __init__(self, capacity):
        self.cap = capacity
        self.mp = {}
```

#### 4.6.1 模板题目
- 0146 - LRU 缓存 ｜ [LeetCode 链接](https://leetcode.cn/problems/lru-cache/) ｜ [题解笔记](../solutions/0101-0200/0146-lru-cache.md)
## 5 易错点
- 前缀和计数更新顺序错位。
- 堆里放值还是放键值对不清晰。
- 设计题忽略边界容量与重复操作。

## 6 总结
数据结构题本质是为操作目标选最匹配的结构组合，先写不变量，再实现更新与查询。
