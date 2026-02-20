# 贪心算法

## 1 简介

贪⼼的本质是选择每⼀阶段的局部最优，从⽽达到全局最优。

和贪心像对应的是动态规划，例如经典的背包问题，会在下一次笔记中记录

什么时候用贪心，什么时候用动态规划呢？

- 通过局部最优实现整体最优的情况
- 一般来说很难证明这一点，只能通过经验判断

## 2 解题步骤

- 将问题分解为若⼲个⼦问题
- 找出适合的贪⼼策略
- 求解每⼀个⼦问题的最优解
- 将局部最优解堆叠成全局最优解

但是实际上只要想清楚局部最优和全局最优，就已经足够了

## 3 经典题目

### 3.1 序列变化相关题目

- 0376 - 摆动序列 ｜ [LeetCode 链接](https://leetcode.cn/problems/wiggle-subsequence/) ｜ [题解笔记](../solutions/0301-0400/0376-wiggle-subsequence.md)

### 3.2 可达范围相关题目

- 0045 - 跳跃游戏 II ｜ [LeetCode 链接](https://leetcode.cn/problems/jump-game-ii/) ｜ [题解笔记](../solutions/0001-0100/0045-jump-game-ii.md)

### 3.3 邻接约束相关题目

- 0135 - 分发糖果 ｜ [LeetCode 链接](https://leetcode.cn/problems/candy/) ｜ [题解笔记](../solutions/0101-0200/0135-candy.md)

### 3.4 排序重建相关题目

- 0406 - 根据身高重建队列 ｜ [LeetCode 链接](https://leetcode.cn/problems/queue-reconstruction-by-height/) ｜ [题解笔记](../solutions/0401-0500/0406-queue-reconstruction-by-height.md)

### 3.5 数位构造相关题目

- 0738 - 单调递增的数字 ｜ [LeetCode 链接](https://leetcode.cn/problems/monotone-increasing-digits/) ｜ [题解笔记](../solutions/0701-0800/0738-monotone-increasing-digits.md)

### 3.6 树上状态相关题目

- 0968 - 监控二叉树 ｜ [LeetCode 链接](https://leetcode.cn/problems/binary-tree-cameras/) ｜ [题解笔记](../solutions/0901-1000/0968-binary-tree-cameras.md)

## 4 总结

贪心没有什么特定的套路，倒不如说更加考验问题抽象建模的能力。

想清楚当前选择如何服务于全局目标，是贪心题最核心的一步。
