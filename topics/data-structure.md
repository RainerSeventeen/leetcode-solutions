# 单调栈

## 1 概览

单调栈是一种特殊的栈数据结构，其中元素保持单调性（递增或递减）。它是解决特定区间问题的高效工具，特别是求解元素左右两边边界相关的问题。

## 2 核心思想

单调栈的核心思想是利用栈的性质和元素的单调性，在一次遍历中高效地找到每个元素的相关信息（如左/右边的第一个更大/小的元素）。通过维护栈中元素的单调性，可以确保不会遗漏任何关键的元素关系。

## 3 解题流程

1. 选择栈的单调方向（递增或递减）
2. 从左到右遍历数组
3. 对于每个元素，与栈顶元素比较：
   - 如果满足单调性条件，直接入栈
   - 如果不满足，弹出栈顶并处理（记录答案或进行计算）
   - 重复直到满足条件或栈为空
4. 将当前元素入栈
5. 处理遍历结束后栈中剩余的元素

## 4 模板与子方法

### 4.1 递增单调栈 - 求右侧第一个更大元素

#### 4.1.1 方法说明

使用递增单调栈（从栈顶向栈底看元素递增），适合求解右侧第一个更大元素的问题。当遇到比栈顶更大的元素时，栈顶元素的"右侧第一个更大元素"就被找到了。

#### 4.1.2 模板代码

```python
def nextGreaterElement(nums):
    stack = []
    result = [-1] * len(nums)

    for i in range(len(nums)):
        while stack and nums[stack[-1]] < nums[i]:
            idx = stack.pop()
            result[idx] = nums[i]
        stack.append(i)

    return result
```

#### 4.1.3 模板题目

- 0496 - 下一个更大元素 I ｜ [LeetCode 链接](https://leetcode.cn/problems/next-greater-element-i/) ｜ [题解笔记](../solutions/0401-0500/0496-next-greater-element-i.md)
- 0503 - 下一个更大元素 II ｜ [LeetCode 链接](https://leetcode.cn/problems/next-greater-element-ii/) ｜ [题解笔记](../solutions/0501-0600/0503-next-greater-element-ii.md)
- 0739 - 每日温度 ｜ [LeetCode 链接](https://leetcode.cn/problems/daily-temperatures/) ｜ [题解笔记](../solutions/0701-0800/0739-daily-temperatures.md)

### 4.2 递减单调栈 - 求区间最大矩形面积

#### 4.2.1 方法说明

使用递减单调栈（从栈顶向栈底看元素递减），适合求解矩形面积、接雨水等区间计算问题。当遇到比栈顶更小的元素时，可以计算以栈顶元素为高的矩形面积。

#### 4.2.2 模板代码

```python
def largestRectangleArea(heights):
    stack = []
    max_area = 0

    for i in range(len(heights)):
        while stack and heights[stack[-1]] > heights[i]:
            h_idx = stack.pop()
            h = heights[h_idx]
            w = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, h * w)
        stack.append(i)

    return max_area
```

#### 4.2.3 模板题目

- 0042 - 接雨水 ｜ [LeetCode 链接](https://leetcode.cn/problems/trapping-rain-water/) ｜ [题解笔记](../solutions/0001-0100/0042-trapping-rain-water.md)
- 0084 - 柱状图中最大的矩形 ｜ [LeetCode 链接](https://leetcode.cn/problems/largest-rectangle-in-histogram/) ｜ [题解笔记](../solutions/0001-0100/0084-largest-rectangle-in-histogram.md)

### 4.3 矩阵相关题目

- 0048 - 旋转图像 ｜ [LeetCode 链接](https://leetcode.cn/problems/rotate-image/) ｜ [题解笔记](../solutions/0001-0100/0048-rotate-image.md)
- 0240 - 搜索二维矩阵 II ｜ [LeetCode 链接](https://leetcode.cn/problems/search-a-2d-matrix-ii/) ｜ [题解笔记](../solutions/0201-0300/0240-search-a-2d-matrix-ii.md)

### 4.4 单调队列相关题目

- 0239 - 滑动窗口最大值 ｜ [LeetCode 链接](https://leetcode.cn/problems/sliding-window-maximum/) ｜ [题解笔记](../solutions/0201-0300/0239-sliding-window-maximum.md)
- 0438 - 找到字符串中所有字母异位词 ｜ [LeetCode 链接](https://leetcode.cn/problems/find-all-anagrams-in-a-string/) ｜ [题解笔记](../solutions/0401-0500/0438-find-all-anagrams-in-a-string.md)

### 4.5 链表相关题目

- 0002 - Add Two Numbers ｜ [LeetCode 链接](https://leetcode.cn/problems/add-two-numbers/) ｜ [题解笔记](../solutions/0001-0100/0002-add-two-numbers.md)
- 0019 - 删除链表的倒数第 N 个结点 ｜ [LeetCode 链接](https://leetcode.cn/problems/remove-nth-node-from-end-of-list/) ｜ [题解笔记](../solutions/0001-0100/0019-remove-nth-node-from-end-of-list.md)
- 0021 - 合并两个有序链表 ｜ [LeetCode 链接](https://leetcode.cn/problems/merge-two-sorted-lists/) ｜ [题解笔记](../solutions/0001-0100/0021-merge-two-sorted-lists.md)
- 0023 - 合并 K 个升序链表 ｜ [LeetCode 链接](https://leetcode.cn/problems/merge-k-sorted-lists/) ｜ [题解笔记](../solutions/0001-0100/0023-merge-k-sorted-lists.md)
- 0141 - 环形链表 ｜ [LeetCode 链接](https://leetcode.cn/problems/linked-list-cycle/) ｜ [题解笔记](../solutions/0101-0200/0141-linked-list-cycle.md)
- 0142 - 环形链表 II ｜ [LeetCode 链接](https://leetcode.cn/problems/linked-list-cycle-ii/) ｜ [题解笔记](../solutions/0101-0200/0142-linked-list-cycle-ii.md)
- 0146 - LRU 缓存 ｜ [LeetCode 链接](https://leetcode.cn/problems/lru-cache/) ｜ [题解笔记](../solutions/0101-0200/0146-lru-cache.md)
- 0148 - 排序链表 ｜ [LeetCode 链接](https://leetcode.cn/problems/sort-list/) ｜ [题解笔记](../solutions/0101-0200/0148-sort-list.md)
- 0160 - 相交链表 ｜ [LeetCode 链接](https://leetcode.cn/problems/intersection-of-two-linked-lists/) ｜ [题解笔记](../solutions/0101-0200/0160-intersection-of-two-linked-lists.md)
- 0206 - Reverse Linked List ｜ [LeetCode 链接](https://leetcode.cn/problems/reverse-linked-list/) ｜ [题解笔记](../solutions/0201-0300/0206-reverse-linked-list.md)
- 0234 - Palindrome Linked List ｜ [LeetCode 链接](https://leetcode.cn/problems/palindrome-linked-list/) ｜ [题解笔记](../solutions/0201-0300/0234-palindrome-linked-list.md)

### 4.6 字典树相关题目

- 0208 - Implement Trie (Prefix Tree) ｜ [LeetCode 链接](https://leetcode.cn/problems/implement-trie-prefix-tree/) ｜ [题解笔记](../solutions/0201-0300/0208-implement-trie-prefix-tree.md)

### 4.7 堆与优先队列相关题目

- 0215 - Kth Largest Element in an Array ｜ [LeetCode 链接](https://leetcode.cn/problems/kth-largest-element-in-an-array/) ｜ [题解笔记](../solutions/0201-0300/0215-kth-largest-element-in-an-array.md)
- 0347 - 前 K 个高频元素 ｜ [LeetCode 链接](https://leetcode.cn/problems/top-k-frequent-elements/) ｜ [题解笔记](../solutions/0301-0400/0347-top-k-frequent-elements.md)

### 4.8 前缀和相关题目

- 0238 - Product of Array Except Self ｜ [LeetCode 链接](https://leetcode.cn/problems/product-of-array-except-self/) ｜ [题解笔记](../solutions/0201-0300/0238-product-of-array-except-self.md)
- 0560 - 和为 K 的子数组 ｜ [LeetCode 链接](https://leetcode.cn/problems/subarray-sum-equals-k/) ｜ [题解笔记](../solutions/0501-0600/0560-subarray-sum-equals-k.md)

### 4.9 双指针相关题目

- 0283 - 移动零 ｜ [LeetCode 链接](https://leetcode.cn/problems/move-zeroes/) ｜ [题解笔记](../solutions/0201-0300/0283-move-zeroes.md)
- 0287 - 寻找重复数 ｜ [LeetCode 链接](https://leetcode.cn/problems/find-the-duplicate-number/) ｜ [题解笔记](../solutions/0201-0300/0287-find-the-duplicate-number.md)

### 4.10 原地哈希相关题目

- 0448 - 找到所有数组中消失的数字 ｜ [LeetCode 链接](https://leetcode.cn/problems/find-all-numbers-disappeared-in-an-array/) ｜ [题解笔记](../solutions/0401-0500/0448-find-all-numbers-disappeared-in-an-array.md)

### 4.11 位运算相关题目

- 0136 - 只出现一次的数字 ｜ [LeetCode 链接](https://leetcode.cn/problems/single-number/) ｜ [题解笔记](../solutions/0101-0200/0136-single-number.md)
- 0461 - 汉明距离 ｜ [LeetCode 链接](https://leetcode.cn/problems/hamming-distance/) ｜ [题解笔记](../solutions/0401-0500/0461-hamming-distance.md)


### 4.12 哈希表相关题目


- 0001 - Two Sum ｜ [LeetCode 链接](https://leetcode.cn/problems/two-sum/) ｜ [题解笔记](../solutions/0001-0100/0001-two-sum.md)
- 0049 - 字母异位词分组 ｜ [LeetCode 链接](https://leetcode.cn/problems/group-anagrams/) ｜ [题解笔记](../solutions/0001-0100/0049-group-anagrams.md)
- 0169 - 多数元素 ｜ [LeetCode 链接](https://leetcode.cn/problems/majority-element/) ｜ [题解笔记](../solutions/0101-0200/0169-majority-element.md)
### 4.13 滑动窗口相关题目


- 0003 - Longest Substring Without Repeating Characters ｜ [LeetCode 链接](https://leetcode.cn/problems/longest-substring-without-repeating-characters/) ｜ [题解笔记](../solutions/0001-0100/0003-longest-substring-without-repeating-characters.md)
- 0076 - Minimum Window Substring ｜ [LeetCode 链接](https://leetcode.cn/problems/minimum-window-substring/) ｜ [题解笔记](../solutions/0001-0100/0076-minimum-window-substring.md)
### 4.14 二分查找相关题目


- 0004 - Median of Two Sorted Arrays ｜ [LeetCode 链接](https://leetcode.cn/problems/median-of-two-sorted-arrays/) ｜ [题解笔记](../solutions/0001-0100/0004-median-of-two-sorted-arrays.md)
- 0033 - 搜索旋转排序数组 ｜ [LeetCode 链接](https://leetcode.cn/problems/search-in-rotated-sorted-array/) ｜ [题解笔记](../solutions/0001-0100/0033-search-in-rotated-sorted-array.md)
- 0034 - 在排序数组中查找元素的第一个和最后一个位置 ｜ [LeetCode 链接](https://leetcode.cn/problems/find-first-and-last-position-of-element-in-sorted-array/) ｜ [题解笔记](../solutions/0001-0100/0034-find-first-and-last-position-of-element-in-sorted-array.md)
### 4.15 双指针相关题目


- 0011 - Container With Most Water ｜ [LeetCode 链接](https://leetcode.cn/problems/container-with-most-water/) ｜ [题解笔记](../solutions/0001-0100/0011-container-with-most-water.md)
- 0015 - 3Sum ｜ [LeetCode 链接](https://leetcode.cn/problems/3sum/) ｜ [题解笔记](../solutions/0001-0100/0015-3sum.md)
- 0075 - Sort Colors ｜ [LeetCode 链接](https://leetcode.cn/problems/sort-colors/) ｜ [题解笔记](../solutions/0001-0100/0075-sort-colors.md)
### 4.16 栈相关题目


- 0020 - 有效的括号 ｜ [LeetCode 链接](https://leetcode.cn/problems/valid-parentheses/) ｜ [题解笔记](../solutions/0001-0100/0020-valid-parentheses.md)
- 0155 - 最小栈 ｜ [LeetCode 链接](https://leetcode.cn/problems/min-stack/) ｜ [题解笔记](../solutions/0101-0200/0155-min-stack.md)
- 0394 - 字符串解码 ｜ [LeetCode 链接](https://leetcode.cn/problems/decode-string/) ｜ [题解笔记](../solutions/0301-0400/0394-decode-string.md)
### 4.17 数组与区间相关题目

- 0031 - 下一个排列 ｜ [LeetCode 链接](https://leetcode.cn/problems/next-permutation/) ｜ [题解笔记](../solutions/0001-0100/0031-next-permutation.md)
- 0056 - Merge Intervals ｜ [LeetCode 链接](https://leetcode.cn/problems/merge-intervals/) ｜ [题解笔记](../solutions/0001-0100/0056-merge-intervals.md)
## 5 易错点

1. **栈的单调方向混淆**：递增栈求的是第一个更大的元素，递减栈求的是第一个更小的元素，容易写反。
2. **边界处理**：需要在循环结束后处理栈中剩余的元素，它们可能代表没有找到答案或需要特殊处理。
3. **索引vs值**：注意栈中存放的是索引还是值，不同的问题可能需要不同的选择。
4. **循环数组处理**：对于循环数组问题，需要遍历两遍或使用模运算处理索引。
5. **宽度计算**：在计算面积时，宽度的计算容易出错，要明确是包含当前位置还是不包含。

## 6 总结

单调栈是一种时间复杂度为 O(n) 的高效算法，虽然看起来代码简洁，但实现中细节众多。掌握单调栈的关键在于：
- 清楚理解题目要求的是什么边界信息
- 选择合适的单调方向
- 正确处理栈的弹出和入栈逻辑
- 谨慎处理边界和特殊情况
