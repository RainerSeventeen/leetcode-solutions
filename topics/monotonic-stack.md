# 单调栈（基础/矩形面积/贡献法/最小字典序）

## 概览

单调栈用于在线性扫描中维护候选下标，常见目标是定位当前元素左侧或右侧第一个更大/更小元素。

该结构的关键收益是：每个元素最多入栈和出栈一次，因此多数问题可以在 $O(n)$ 时间内完成边界定位或贡献结算。

## 核心思想

- 栈内元素按值保持单调，当前元素触发一批元素出栈。
- 出栈瞬间通常能确定被弹出元素的最近边界。
- 多数题应存下标而非值，以便同时计算值、距离与区间宽度。
- 面积类、雨水类与贡献法本质都是先定边界，再做贡献计算。
- 比较符号（`<`、`<=`、`>`、`>=`）决定相等元素归属，需要和题意一致。

## 解题流程

1. 确认栈里存下标还是值（通常存下标）。
2. 明确要找的边界（更大/更小、左/右）并确定单调方向。
3. 在出栈时计算答案或记录边界。
4. 处理残留元素（补哨兵或手动清栈），统一无边界默认值。

## 模板与子方法

### 单调栈

#### 基础

模板：

```python
def nearest_greater(nums):
    n = len(nums)
    left = [-1] * n
    st = []
    for i, x in enumerate(nums):
        while st and nums[st[-1]] <= x:
            st.pop()
        if st:
            left[i] = st[-1]
        st.append(i)

    right = [n] * n
    st = []
    for i in range(n - 1, -1, -1):
        while st and nums[st[-1]] <= nums[i]:
            st.pop()
        if st:
            right[i] = st[-1]
        st.append(i)

    return left, right
```

模板题目：

- 0496 - 下一个更大元素 I ｜ [LeetCode 链接](https://leetcode.cn/problems/next-greater-element-i/) ｜ [题解笔记](../solutions/0401-0500/0496-next-greater-element-i.md)
- 0503 - 下一个更大元素 II ｜ [LeetCode 链接](https://leetcode.cn/problems/next-greater-element-ii/) ｜ [题解笔记](../solutions/0501-0600/0503-next-greater-element-ii.md)
- 0739 - 每日温度 ｜ [LeetCode 链接](https://leetcode.cn/problems/daily-temperatures/) ｜ [题解笔记](../solutions/0701-0800/0739-daily-temperatures.md)

#### 进阶

模板：

```python
def construct_maximum_binary_tree(nums):
    st = []
    for x in nums:
        node = TreeNode(x)
        while st and st[-1].val < x:
            node.left = st.pop()
        if st:
            st[-1].right = node
        st.append(node)
    return st[0] if st else None
```

模板题目：
待补充...

### 矩形

#### 柱状图与矩阵转化

模板：

```python
def largest_rectangle_area(heights):
    a = [0] + heights + [0]
    st = []
    ans = 0
    for i, h in enumerate(a):
        while st and a[st[-1]] > h:
            mid = st.pop()
            left = st[-1]
            ans = max(ans, a[mid] * (i - left - 1))
        st.append(i)
    return ans
```

模板题目：

- 0084 - 柱状图中最大的矩形 ｜ [LeetCode 链接](https://leetcode.cn/problems/largest-rectangle-in-histogram/) ｜ [题解笔记](../solutions/0001-0100/0084-largest-rectangle-in-histogram.md)
- 0085 - 最大矩形 ｜ [LeetCode 链接](https://leetcode.cn/problems/maximal-rectangle/) ｜ [题解笔记](../solutions/0001-0100/0085-maximal-rectangle.md)

#### 接雨水

模板：

```python
def trap(height):
    st = []
    ans = 0
    for i, h in enumerate(height):
        while st and h > height[st[-1]]:
            bottom = st.pop()
            if not st:
                break
            left = st[-1]
            w = i - left - 1
            hi = min(height[left], h) - height[bottom]
            ans += w * hi
        st.append(i)
    return ans
```

模板题目：

- 0042 - 接雨水 ｜ [LeetCode 链接](https://leetcode.cn/problems/trapping-rain-water/) ｜ [题解笔记](../solutions/0001-0100/0042-trapping-rain-water.md)

### 贡献法

#### 贡献分解

待补充...

#### 思维扩展

待补充...

### 最小字典序

待补充...

## 易错点

- 存值而非下标会丢失宽度信息，面积题和距离题容易出错。
- 忘记补哨兵或清栈，导致尾部元素未结算。
- 相等元素的比较符号选错，会让边界归属不一致。
- 接雨水中弹栈后若栈空，说明缺左边界，不能直接结算。

## 总结

单调栈的核心是用一次线性扫描维护“可成为边界的候选集合”，并在出栈时完成边界确认与答案计算。
