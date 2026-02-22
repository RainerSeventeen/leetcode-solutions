# 单调栈（基础/矩形面积/贡献法/最小字典序）

## 1 概览

单调栈就是一个栈中元素保持单调性

单调栈适合解决：求当前元素左或者右边**第一个**更大/小的元素

重点需要确定栈是递增（从栈顶向栈底看）还是递减的属性：递增求的是第一个比他**大**的元素

单调栈的作用是存放之前遍历过的数据，而数据的单调性有保证了一定不会漏掉之前已经放进来过的元素，这个过程比较巧妙，通过模拟一遍流程应该能能够理解这个步骤

## 2 核心思想
- 栈内维护单调性，当前元素触发一批元素出栈。
- 出栈时通常能确定该元素的最近边界。
- 面积/雨水类题把“边界定位”转成“贡献计算”。
- 单调方向要和问题目标一一对应：若要找“右侧第一个更大”，左到右扫描时维护“从栈底到栈顶递减”的栈（等价于从栈顶看递增）；若要找“右侧第一个更小”则反过来。
- 多数题应存下标而不是值：下标可同时拿到值、距离（`i - idx`）和区间宽度（`right - left - 1`），这是每日温度、柱状图、接雨水三类题的统一前提。
- 清栈策略有两类：补哨兵触发自然出栈，或遍历结束后手动清栈；两种做法本质一致，都是把“右边界不存在”转成可计算场景。

## 3 解题流程
1. 先确定栈存“下标”还是“值”，多数题存下标。
2. 定义单调方向与触发出栈条件（`<`、`<=`、`>`、`>=` 会决定相等元素归属）。
3. 在出栈瞬间计算答案或边界。
4. 处理尾部残留：补哨兵或手动清栈，并核对“无右边界”时的默认值（如 `-1` 或 `n`）。

## 4 模板与子方法
### 4.1 右侧第一个更大元素
方法说明：
典型“下一个更大元素”模板，维护递减栈，遇到更大值时回填答案。这里存下标的核心原因是：既要比较 `nums[stk[-1]]` 和当前值，也要在出栈时根据题意写回“值”或“距离”。

模板代码：
```python
def next_greater(nums):
    n = len(nums)
    ans = [-1] * n
    st = []
    for i, x in enumerate(nums):
        while st and nums[st[-1]] < x:
            ans[st.pop()] = x
        st.append(i)
    return ans
```

#### 4.1.1 模板题目
- 0496 - 下一个更大元素 I ｜ [LeetCode 链接](https://leetcode.cn/problems/next-greater-element-i/) ｜ [题解笔记](../solutions/0401-0500/0496-next-greater-element-i.md)
- 0739 - 每日温度 ｜ [LeetCode 链接](https://leetcode.cn/problems/daily-temperatures/) ｜ [题解笔记](../solutions/0701-0800/0739-daily-temperatures.md)
### 4.2 循环数组单调栈
方法说明：
对循环数组做两轮扫描（下标取模），保证每个元素都能看到“右侧环形部分”。关键是“元素只入栈一次”：第一轮入栈建立候选，第二轮只负责触发出栈并回填，避免重复覆盖。

模板代码：
```python
def next_greater_circular(nums):
    n = len(nums)
    ans = [-1] * n
    st = []
    for i in range(2 * n):
        idx = i % n
        while st and nums[st[-1]] < nums[idx]:
            ans[st.pop()] = nums[idx]
        if i < n:
            st.append(idx)
    return ans
```

#### 4.2.1 模板题目
- 0503 - 下一个更大元素 II ｜ [LeetCode 链接](https://leetcode.cn/problems/next-greater-element-ii/) ｜ [题解笔记](../solutions/0501-0600/0503-next-greater-element-ii.md)
### 4.3 柱状图最大矩形（左右第一个更小）
方法说明：
结果一定对应某根柱子的高度。扫描到更小柱子时，弹出的 `mid` 立即确定了“右侧第一个更小”为当前 `i`；弹出后新的栈顶就是“左侧第一个更小”。因此可直接用
`width = i - left - 1`，`area = heights[mid] * width`。

清栈策略可选：
1. 在数组首尾补 `0` 哨兵，统一在主循环里算完。
2. 不补哨兵，主循环结束后手动清栈，等价地把右边界视为 `n`。

模板代码：
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

#### 4.3.1 模板题目
- 0084 - 柱状图中最大的矩形 ｜ [LeetCode 链接](https://leetcode.cn/problems/largest-rectangle-in-histogram/) ｜ [题解笔记](../solutions/0001-0100/0084-largest-rectangle-in-histogram.md)
### 4.4 二维矩阵降维为柱状图
方法说明：
`0085` 的单调栈本体是 `0084` 的复用：逐行累积高度，把每一行当作一幅柱状图求最大矩形。方法边界在于“先做状态建模（矩阵 -> 高度数组）”，再调用柱状图子方法，适合单独成节。

#### 4.4.1 模板题目
- 0085 - 最大矩形 ｜ [LeetCode 链接](https://leetcode.cn/problems/maximal-rectangle/) ｜ [题解笔记](../solutions/0001-0100/0085-maximal-rectangle.md)
### 4.5 凹槽积水
方法说明：
出栈元素作为“凹槽底”，当前元素与新栈顶形成左右边界计算积水；该题也可用双指针，双指针做法可交叉到双指针专题。

推导统一为三步：
1. `bottom` 是刚弹出的低点。
2. `left` 是弹出后新的栈顶，`right` 是当前下标 `i`。
3. 当前可接水量 `w * h`，其中 `w = right - left - 1`，`h = min(height[left], height[right]) - height[bottom]`。

当弹出后栈空，表示不存在左边界，无法形成凹槽，必须直接 `break`。

模板代码：
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

#### 4.5.1 模板题目
- 0042 - 接雨水 ｜ [LeetCode 链接](https://leetcode.cn/problems/trapping-rain-water/) ｜ [题解笔记](../solutions/0001-0100/0042-trapping-rain-water.md)
## 5 易错点
- 存值导致无法计算宽度，面积题应存下标。
- 忘记哨兵或清栈导致尾部结果丢失。
- 相等元素的比较符号选择会影响边界归属。
- 把“栈空”当成可计算边界：接雨水里栈空意味着左挡板缺失，不能结算该 `bottom`。

## 6 总结
单调栈本质是把“最近更大/更小”边界问题转成线性可维护结构，关键在于出栈时机与边界定义。
