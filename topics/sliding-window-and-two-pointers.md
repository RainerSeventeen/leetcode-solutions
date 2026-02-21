# 滑动窗口与双指针

## 1 概览
滑动窗口与双指针用于线性扫描中维护区间或边界，常见于子串覆盖、去重、对撞求最值、快慢指针链表判环。

## 2 核心思想
- 滑动窗口：用左右边界维护一个动态区间，通过扩张与收缩维持约束。
- 对撞双指针：利用有序性或单调性，每次排除一段不可能解空间。
- 快慢双指针：利用速度差或步数差实现定位、判环和相遇。

## 3 解题流程
1. 判断是窗口约束问题、对撞问题，还是快慢指针问题。
2. 定义不变量（窗口计数、边界条件、指针移动规则）。
3. 写出移动条件与终止条件，确保每步都有进展。
4. 用最小样例验证边界：空串、单元素、全重复、无解。

## 4 模板与子方法
### 4.1 可变滑动窗口（覆盖/计数）
方法说明：
适用于“最短覆盖”“固定条件下最长/最短子串”。若题目核心对象是字符串，可与字符串专题交叉，但模板仍是窗口计数。

模板代码：
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

#### 4.1.1 模板题目
- 0003 - 无重复字符的最长子串 ｜ [LeetCode 链接](https://leetcode.cn/problems/longest-substring-without-repeating-characters/) ｜ [题解笔记](../solutions/0001-0100/0003-longest-substring-without-repeating-characters.md)
- 0076 - 最小覆盖子串 ｜ [LeetCode 链接](https://leetcode.cn/problems/minimum-window-substring/) ｜ [题解笔记](../solutions/0001-0100/0076-minimum-window-substring.md)
- 0438 - 找到字符串中所有字母异位词 ｜ [LeetCode 链接](https://leetcode.cn/problems/find-all-anagrams-in-a-string/) ｜ [题解笔记](../solutions/0401-0500/0438-find-all-anagrams-in-a-string.md)
- 0940 - 水果成篮 ｜ [LeetCode 链接](https://leetcode.cn/problems/fruit-into-baskets/) ｜ [题解笔记](../solutions/0901-1000/0940-fruit-into-baskets.md)
### 4.2 双指针对撞（有序数组）
方法说明：
适用于两端收缩与去重扫描。通常先排序再对撞，三数之和等题可在外层枚举后套对撞模板。

模板代码：
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

#### 4.2.1 模板题目
- 0011 - 盛最多水的容器 ｜ [LeetCode 链接](https://leetcode.cn/problems/container-with-most-water/) ｜ [题解笔记](../solutions/0001-0100/0011-container-with-most-water.md)
- 0015 - 三数之和 ｜ [LeetCode 链接](https://leetcode.cn/problems/3sum/) ｜ [题解笔记](../solutions/0001-0100/0015-3sum.md)
- 0283 - 移动零 ｜ [LeetCode 链接](https://leetcode.cn/problems/move-zeroes/) ｜ [题解笔记](../solutions/0201-0300/0283-move-zeroes.md)
- 0075 - 颜色分类 ｜ [LeetCode 链接](https://leetcode.cn/problems/sort-colors/) ｜ [题解笔记](../solutions/0001-0100/0075-sort-colors.md)
- 0018 - 四数之和 ｜ [LeetCode 链接](https://leetcode.cn/problems/4sum/) ｜ [题解笔记](../solutions/0001-0100/0018-4sum.md)
- 0026 - 删除有序数组中的重复项 ｜ [LeetCode 链接](https://leetcode.cn/problems/remove-duplicates-from-sorted-array/) ｜ [题解笔记](../solutions/0001-0100/0026-remove-duplicates-from-sorted-array.md)
- 0027 - 移除元素 ｜ [LeetCode 链接](https://leetcode.cn/problems/remove-element/) ｜ [题解笔记](../solutions/0001-0100/0027-remove-element.md)
- 0028 - 找出字符串中第一个匹配项的下标 ｜ [LeetCode 链接](https://leetcode.cn/problems/find-the-index-of-the-first-occurrence-in-a-string/) ｜ [题解笔记](../solutions/0001-0100/0028-find-the-index-of-the-first-occurrence-in-a-string.md)
- 0151 - 反转字符串中的单词 ｜ [LeetCode 链接](https://leetcode.cn/problems/reverse-words-in-a-string/) ｜ [题解笔记](../solutions/0101-0200/0151-reverse-words-in-a-string.md)
- 0202 - 快乐数 ｜ [LeetCode 链接](https://leetcode.cn/problems/happy-number/) ｜ [题解笔记](../solutions/0201-0300/0202-happy-number.md)
- 0344 - 反转字符串 ｜ [LeetCode 链接](https://leetcode.cn/problems/reverse-string/) ｜ [题解笔记](../solutions/0301-0400/0344-reverse-string.md)
- 0454 - 四数相加 II ｜ [LeetCode 链接](https://leetcode.cn/problems/4sum-ii/) ｜ [题解笔记](../solutions/0401-0500/0454-4sum-ii.md)
- 0541 - 反转字符串 II ｜ [LeetCode 链接](https://leetcode.cn/problems/reverse-string-ii/) ｜ [题解笔记](../solutions/0501-0600/0541-reverse-string-ii.md)
- 0874 - 比较含退格的字符串 ｜ [LeetCode 链接](https://leetcode.cn/problems/backspace-string-compare/) ｜ [题解笔记](../solutions/0801-0900/0874-backspace-string-compare.md)
- 1019 - 有序数组的平方 ｜ [LeetCode 链接](https://leetcode.cn/problems/squares-of-a-sorted-array/) ｜ [题解笔记](../solutions/1001-1100/1019-squares-of-a-sorted-array.md)
### 4.3 单调队列窗口最值
方法说明：
适用于滑动窗口内最大值/最小值维护。与单调栈相似但作用在动态窗口，核心是队头始终有效、队列单调。

模板代码：
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

#### 4.3.1 模板题目
- 0239 - 滑动窗口最大值 ｜ [LeetCode 链接](https://leetcode.cn/problems/sliding-window-maximum/) ｜ [题解笔记](../solutions/0201-0300/0239-sliding-window-maximum.md)
### 4.4 快慢指针与环检测
方法说明：
适用于链表环、入口定位、相交等问题；题目主归属常在链表专题，这里保留交叉模板。`0287` 也可做答案二分（交叉到二分专题）。

模板代码：
```python
def has_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True
    return False
```

#### 4.4.1 模板题目
- 0141 - 环形链表 ｜ [LeetCode 链接](https://leetcode.cn/problems/linked-list-cycle/) ｜ [题解笔记](../solutions/0101-0200/0141-linked-list-cycle.md)
- 0142 - 环形链表 II ｜ [LeetCode 链接](https://leetcode.cn/problems/linked-list-cycle-ii/) ｜ [题解笔记](../solutions/0101-0200/0142-linked-list-cycle-ii.md)
- 0160 - 相交链表 ｜ [LeetCode 链接](https://leetcode.cn/problems/intersection-of-two-linked-lists/) ｜ [题解笔记](../solutions/0101-0200/0160-intersection-of-two-linked-lists.md)
- 0287 - 寻找重复数 ｜ [LeetCode 链接](https://leetcode.cn/problems/find-the-duplicate-number/) ｜ [题解笔记](../solutions/0201-0300/0287-find-the-duplicate-number.md)
## 5 易错点
- 窗口收缩时忘记回滚计数，导致漏解或死循环。
- 对撞前未排序，或去重位置错误。
- 快慢指针判空顺序不当导致空指针访问。

## 6 总结
窗口模板解决“区间约束”，对撞模板解决“有序收缩”，快慢模板解决“链表定位与判环”；先定不变量再写移动规则最稳。
