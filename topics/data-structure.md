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
