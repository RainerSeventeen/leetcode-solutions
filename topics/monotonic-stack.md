# 单调栈

## 1 概览
单调栈用于一次遍历内定位“左/右第一个更大或更小元素”，并可进一步计算区间贡献。

## 2 核心思想
- 栈内维护单调性，当前元素触发一批元素出栈。
- 出栈时通常能确定该元素的最近边界。
- 面积/雨水类题把“边界定位”转成“贡献计算”。

## 3 解题流程
1. 先确定栈存“下标”还是“值”，多数题存下标。
2. 定义单调方向与触发出栈条件。
3. 在出栈瞬间计算答案或边界。
4. 处理尾部残留：补哨兵或手动清栈。

## 4 模板与子方法
### 4.1 右侧第一个更大元素
方法说明：
典型“下一个更大元素”模板，维护递减栈，遇到更大值时回填答案。

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
对循环数组做两轮扫描（下标取模），保证每个元素都能看到“右侧环形部分”。

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
### 4.3 边界贡献（柱状图/矩形）
方法说明：
通过单调栈确定每根柱子的左右第一个更小位置，再计算以该柱为高的最大矩形。

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
- 0085 - Maximal Rectangle ｜ [LeetCode 链接](https://leetcode.cn/problems/maximal-rectangle/) ｜ [题解笔记](../solutions/0001-0100/0085-maximal-rectangle.md)
### 4.4 凹槽积水
方法说明：
出栈元素作为“凹槽底”，当前元素与新栈顶形成左右边界计算积水；该题也可用双指针，双指针做法可交叉到双指针专题。

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

#### 4.4.1 模板题目
- 0042 - 接雨水 ｜ [LeetCode 链接](https://leetcode.cn/problems/trapping-rain-water/) ｜ [题解笔记](../solutions/0001-0100/0042-trapping-rain-water.md)
## 5 易错点
- 存值导致无法计算宽度，面积题应存下标。
- 忘记哨兵或清栈导致尾部结果丢失。
- 相等元素的比较符号选择会影响边界归属。

## 6 总结
单调栈本质是把“最近更大/更小”边界问题转成线性可维护结构，关键在于出栈时机与边界定义。
