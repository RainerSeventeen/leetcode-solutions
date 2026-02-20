# 数据结构

在本文件中存放各类数据结构类的题目

##  单调栈

单调栈就是一个栈中元素保持单调性

单调栈适合解决：求当前元素左或者右边**第一个**更大/小的元素

重点需要确定栈是递增（从栈顶向栈底看）还是递减的属性：递增求的是第一个比他**大**的元素

单调栈的作用是存放之前遍历过的数据，而数据的单调性有保证了一定不会漏掉之前已经放进来过的元素，这个过程比较巧妙，通过模拟一遍流程应该能能够理解这个步骤

### 单调栈相关题目

- 0042 - 接雨水 ｜ [LeetCode 链接](https://leetcode.cn/problems/trapping-rain-water/) ｜ [题解笔记](../solutions/0001-0100/0042-trapping-rain-water.md)
- 0084 - 柱状图中最大的矩形 ｜ [LeetCode 链接](https://leetcode.cn/problems/largest-rectangle-in-histogram/) ｜ [题解笔记](../solutions/0001-0100/0084-largest-rectangle-in-histogram.md)
- 0496 - 下一个更大元素 I ｜ [LeetCode 链接](https://leetcode.cn/problems/next-greater-element-i/) ｜ [题解笔记](../solutions/0401-0500/0496-next-greater-element-i.md)
- 0503 - 下一个更大元素 II ｜ [LeetCode 链接](https://leetcode.cn/problems/next-greater-element-ii/) ｜ [题解笔记](../solutions/0501-0600/0503-next-greater-element-ii.md)
- 0739 - 每日温度 ｜ [LeetCode 链接](https://leetcode.cn/problems/daily-temperatures/) ｜ [题解笔记](../solutions/0701-0800/0739-daily-temperatures.md)
