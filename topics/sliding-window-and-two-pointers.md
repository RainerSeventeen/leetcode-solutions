# 滑动窗口与双指针（定长/不定长/单序列/双序列/三指针/分组循环）

## 1 概览
滑动窗口与双指针用于线性扫描中维护区间或边界，常见于子串覆盖、计数统计、数组原地修改、对撞求最值。

## 2 核心思想
- 滑动窗口：用左右边界维护动态区间，通过扩张与收缩维持约束。
- 双指针：利用有序性、单调性或结构性质，移动指针排除不可能解空间。
- 三指针/分组循环：通过额外边界或分段遍历，统一处理“恰好型”与“连续段”问题。

## 3 解题流程
1. 先判断属于定长窗口、不定长窗口、单序列/双序列指针、三指针还是分组循环。
2. 定义不变量：窗口计数、合法条件、指针移动规则、分组边界。
3. 明确移动与终止条件，保证每一步至少有一个指针前进。
4. 用极小样例检查边界：空串、单元素、全重复、无解、全合法。

## 4 模板与子方法
### 4.1 定长滑动窗口
方法说明：

窗口长度固定，重点是进入/离开窗口时的增量维护。常见目标是窗口最值、固定长度统计、固定长度匹配。

#### 4.1.1 基础
模板：

```python
from collections import deque


def max_sliding_window(nums, k):
    q = deque()
    ans = []
    for i, x in enumerate(nums):
        while q and nums[q[-1]] <= x:
            q.pop()
        q.append(i)
        if q[0] <= i - k:
            q.popleft()
        if i >= k - 1:
            ans.append(nums[q[0]])
    return ans
```

模板题目：

待补充...

#### 4.1.2 进阶（选做）
模板：

```python
# 待补充...
```

模板题目：

- 0438 - 找到字符串中所有字母异位词 ｜ [LeetCode 链接](https://leetcode.cn/problems/find-all-anagrams-in-a-string/) ｜ [题解笔记](../solutions/0401-0500/0438-find-all-anagrams-in-a-string.md)

#### 4.1.3 其他（选做）
模板：

```python
# 待补充...
```

模板题目：

待补充...

### 4.2 不定长滑动窗口
方法说明：

不定长滑动窗口常见三类目标：求最长、求最短、求子数组个数。可将右指针视为入队、左指针视为出队，维护区间合法性。

#### 4.2.1 越短越合法/求最长/最大
模板：

```python
from collections import Counter


def min_window(s: str, t: str) -> str:
    need = Counter(t)
    miss = len(t)
    l = 0
    best = (10**9, 0, 0)
    for r, ch in enumerate(s):
        if need[ch] > 0:
            miss -= 1
        need[ch] -= 1
        while miss == 0:
            if r - l + 1 < best[0]:
                best = (r - l + 1, l, r + 1)
            need[s[l]] += 1
            if need[s[l]] > 0:
                miss += 1
            l += 1
    return "" if best[0] == 10**9 else s[best[1]:best[2]]
```

模板题目：

- 0003 - 无重复字符的最长子串 ｜ [LeetCode 链接](https://leetcode.cn/problems/longest-substring-without-repeating-characters/) ｜ [题解笔记](../solutions/0001-0100/0003-longest-substring-without-repeating-characters.md)
- 0904 - 水果成篮 ｜ [LeetCode 链接](https://leetcode.cn/problems/fruit-into-baskets/) ｜ [题解笔记](../solutions/0901-1000/0904-fruit-into-baskets.md)

#### 4.2.2 越长越合法/求最短/最小
模板：

```python
def min_subarray_len(target, nums):
    ans = 10**9
    total = 0
    left = 0
    for right, x in enumerate(nums):
        total += x
        while total >= target:
            ans = min(ans, right - left + 1)
            total -= nums[left]
            left += 1
    return 0 if ans == 10**9 else ans
```

模板题目：

- 0209 - 长度最小的子数组 ｜ [LeetCode 链接](https://leetcode.cn/problems/minimum-size-subarray-sum/) ｜ [题解笔记](../solutions/0201-0300/0209-minimum-size-subarray-sum.md)
- 0076 - 最小覆盖子串 ｜ [LeetCode 链接](https://leetcode.cn/problems/minimum-window-substring/) ｜ [题解笔记](../solutions/0001-0100/0076-minimum-window-substring.md)

#### 4.2.3 求子数组个数
模板：

```python
def count_at_most(nums, k):
    left = 0
    ans = 0
    # 按题目定义维护窗口合法性；合法后累计 right-left+1
    for right, _ in enumerate(nums):
        while False:
            left += 1
        ans += right - left + 1
    return ans
```

模板题目：

待补充...

#### 4.2.4 其他（选做）
模板：

```python
# 待补充...
```

模板题目：

待补充...

### 4.3 单序列双指针
方法说明：

单序列双指针包含相向、同向、背向与原地修改。核心是定义两个指针各自语义，并保证移动后不变量仍成立。

#### 4.3.1 反转字符串
模板：

```python
def reverse_string(s):
    l, r = 0, len(s) - 1
    while l < r:
        s[l], s[r] = s[r], s[l]
        l += 1
        r -= 1
```

模板题目：

- 0344 - 反转字符串 ｜ [LeetCode 链接](https://leetcode.cn/problems/reverse-string/) ｜ [题解笔记](../solutions/0301-0400/0344-reverse-string.md)
- 0541 - 反转字符串 II ｜ [LeetCode 链接](https://leetcode.cn/problems/reverse-string-ii/) ｜ [题解笔记](../solutions/0501-0600/0541-reverse-string-ii.md)
- 0151 - 反转字符串中的单词 ｜ [LeetCode 链接](https://leetcode.cn/problems/reverse-words-in-a-string/) ｜ [题解笔记](../solutions/0101-0200/0151-reverse-words-in-a-string.md)

#### 4.3.2 相向双指针
模板：

```python
def two_pointer(nums):
    nums.sort()
    l, r = 0, len(nums) - 1
    while l < r:
        s = nums[l] + nums[r]
        if s == 0:
            l += 1
            r -= 1
        elif s < 0:
            l += 1
        else:
            r -= 1
```

模板题目：

- 0977 - 有序数组的平方 ｜ [LeetCode 链接](https://leetcode.cn/problems/squares-of-a-sorted-array/) ｜ [题解笔记](../solutions/0901-1000/0977-squares-of-a-sorted-array.md)
- 0015 - 三数之和 ｜ [LeetCode 链接](https://leetcode.cn/problems/3sum/) ｜ [题解笔记](../solutions/0001-0100/0015-3sum.md)
- 0018 - 四数之和 ｜ [LeetCode 链接](https://leetcode.cn/problems/4sum/) ｜ [题解笔记](../solutions/0001-0100/0018-4sum.md)
- 0011 - 盛最多水的容器 ｜ [LeetCode 链接](https://leetcode.cn/problems/container-with-most-water/) ｜ [题解笔记](../solutions/0001-0100/0011-container-with-most-water.md)

#### 4.3.3 同向双指针
模板：

```python
def forward_two_pointers(nums):
    slow = 0
    for fast in range(len(nums)):
        if True:
            nums[slow] = nums[fast]
            slow += 1
    return slow
```

模板题目：

待补充...

#### 4.3.4 背向双指针
模板：

```python
# 待补充...
```

模板题目：

待补充...

#### 4.3.5 原地修改
模板：

```python
def remove_element(nums, val):
    slow = 0
    for fast in range(len(nums)):
        if nums[fast] != val:
            nums[slow] = nums[fast]
            slow += 1
    return slow
```

模板题目：

- 0027 - 移除元素 ｜ [LeetCode 链接](https://leetcode.cn/problems/remove-element/) ｜ [题解笔记](../solutions/0001-0100/0027-remove-element.md)
- 0026 - 删除有序数组中的重复项 ｜ [LeetCode 链接](https://leetcode.cn/problems/remove-duplicates-from-sorted-array/) ｜ [题解笔记](../solutions/0001-0100/0026-remove-duplicates-from-sorted-array.md)
- 0283 - 移动零 ｜ [LeetCode 链接](https://leetcode.cn/problems/move-zeroes/) ｜ [题解笔记](../solutions/0201-0300/0283-move-zeroes.md)
- 0075 - 颜色分类 ｜ [LeetCode 链接](https://leetcode.cn/problems/sort-colors/) ｜ [题解笔记](../solutions/0001-0100/0075-sort-colors.md)

#### 4.3.6 矩阵上的双指针
模板：

```python
def search_matrix(matrix, target):
    if not matrix or not matrix[0]:
        return False
    r, c = 0, len(matrix[0]) - 1
    while r < len(matrix) and c >= 0:
        x = matrix[r][c]
        if x == target:
            return True
        if x > target:
            c -= 1
        else:
            r += 1
    return False
```

模板题目：

- 0240 - 搜索二维矩阵 II ｜ [LeetCode 链接](https://leetcode.cn/problems/search-a-2d-matrix-ii/) ｜ [题解笔记](../solutions/0201-0300/0240-search-a-2d-matrix-ii.md)

### 4.4 双序列双指针
方法说明：

两个序列同步推进，常见于匹配、合并、比较与子序列判断，时间复杂度通常为 $O(n+m)$。

#### 4.4.1 双指针
模板：

```python
def merge_like(a, b):
    i = j = 0
    ans = []
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            ans.append(a[i])
            i += 1
        else:
            ans.append(b[j])
            j += 1
    ans.extend(a[i:])
    ans.extend(b[j:])
    return ans
```

模板题目：

- 0844 - 比较含退格的字符串 ｜ [LeetCode 链接](https://leetcode.cn/problems/backspace-string-compare/) ｜ [题解笔记](../solutions/0801-0900/0844-backspace-string-compare.md)

#### 4.4.2 判断子序列
模板：

```python
def is_subsequence(s, t):
    i = j = 0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
        j += 1
    return i == len(s)
```

模板题目：

待补充...

### 4.5 三指针
方法说明：

三指针常用于“恰好型”计数或双窗口同右端点同步推进。

#### 4.5.1 基础
模板：

```python
def exact_k_by_at_most(nums, k):
    return at_most(nums, k) - at_most(nums, k - 1)
```

模板题目：

待补充...

### 4.6 分组循环
方法说明：

按连续段分组处理，外层定位组起点，内层推进到当前组终点，适合同规则分段统计。

#### 4.6.1 基础
模板：

```python
def grouped_scan(nums):
    n = len(nums)
    i = 0
    ans = 0
    while i < n:
        start = i
        while i + 1 < n and nums[i + 1] >= nums[i]:
            i += 1
        ans = max(ans, i - start + 1)
        i += 1
    return ans
```

模板题目：

- 1784 - 检查二进制字符串字段 ｜ [LeetCode 链接](https://leetcode.cn/problems/check-if-binary-string-has-at-most-one-segment-of-ones/) ｜ [题解笔记](../solutions/1701-1800/1784-check-if-binary-string-has-at-most-one-segment-of-ones.md)

## 5 易错点
- 窗口收缩时忘记回滚计数，导致漏解或死循环。
- 对撞前未排序，或去重位置错误。
- 指针移动条件缺少“严格前进”，导致卡死在同一状态。
- 分组循环忘记处理最后一组，或组边界更新顺序错误。

## 6 总结
滑动窗口解决区间约束，双指针解决边界收缩与匹配，三指针与分组循环解决计数拆分与分段统计。先定不变量，再写移动规则，最后补边界验证。
