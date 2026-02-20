# 贪心算法

## 1 概览

贪心的本质是选择每一阶段的局部最优，从而达到全局最优。与贪心对应的是动态规划，例如经典的背包问题。

贪心算法的应用场景：
- 通过局部最优实现整体最优的情况
- 一般来说很难证明这一点，只能通过经验判断

## 2 核心思想

贪心算法的核心在于：想清楚当前选择如何服务于全局目标。

关键判断标准：
- 能否将问题的最优解通过局部的贪心选择来构造？
- 当前决策是否会影响后续的最优性？

## 3 解题流程

- 将问题分解为若干个子问题
- 找出适合的贪心策略
- 求解每一个子问题的最优解
- 将局部最优解堆叠成全局最优解

## 4 模板与子方法

### 4.1 子方法 A：序列变化相关

**方法说明**

通过观察序列的变化趋势，选择符合条件的局部最优点，构造满足约束的子序列或序列。

**模板代码**

```python
# 序列变化相关问题的通用思路
def greedy_sequence(nums):
    # 1. 确定贪心策略：选择哪些元素或如何修改序列
    # 2. 遍历数组，按照策略选择或跳过元素
    # 3. 返回构造的结果
    pass
```

**模板题目**

- 0376 - 摆动序列 ｜ [LeetCode 链接](https://leetcode.cn/problems/wiggle-subsequence/) ｜ [题解笔记](../solutions/0301-0400/0376-wiggle-subsequence.md)
- 0581 - 最短无序连续子数组 ｜ [LeetCode 链接](https://leetcode.cn/problems/shortest-unsorted-continuous-subarray/) ｜ [题解笔记](../solutions/0501-0600/0581-shortest-unsorted-continuous-subarray.md)

### 4.2 子方法 B：可达范围相关

**方法说明**

通过维护当前能够到达的最远距离，每次跳跃选择能使覆盖范围最大化的位置，实现最少跳跃次数。

**模板代码**

```python
# 可达范围问题的通用思路
def greedy_reach(nums):
    # 1. 维护当前范围和下一范围的边界
    # 2. 遍历当前范围内的元素，找出下一范围的最远位置
    # 3. 更新范围，重复直到到达目标
    pass
```

**模板题目**

- 0045 - 跳跃游戏 II ｜ [LeetCode 链接](https://leetcode.cn/problems/jump-game-ii/) ｜ [题解笔记](../solutions/0001-0100/0045-jump-game-ii.md)
- 0055 - Jump Game ｜ [LeetCode 链接](https://leetcode.cn/problems/jump-game/) ｜ [题解笔记](../solutions/0001-0100/0055-jump-game.md)

### 4.3 子方法 C：邻接约束相关

**方法说明**

处理相邻元素间存在约束关系的问题。通过多次遍历，从不同方向应用贪心策略，确保所有约束条件都被满足。

**模板代码**

```python
# 邻接约束问题的通用思路
def greedy_adjacent(arr):
    # 1. 首次遍历：从左到右应用一个贪心策略
    # 2. 二次遍历：从右到左应用另一个贪心策略
    # 3. 两次遍历的结果取最大值，保证所有约束满足
    pass
```

**模板题目**

- 0135 - 分发糖果 ｜ [LeetCode 链接](https://leetcode.cn/problems/candy/) ｜ [题解笔记](../solutions/0101-0200/0135-candy.md)

### 4.4 子方法 D：排序重建相关

**方法说明**

根据某些属性对元素进行排序，然后按照排序结果按贪心策略插入或构造新的数据结构。

**模板代码**

```python
# 排序重建问题的通用思路
def greedy_reconstruct(items):
    # 1. 按照某个关键属性排序元素
    # 2. 根据另一个属性作为贪心策略进行插入或构造
    # 3. 返回重建后的结果
    pass
```

**模板题目**

- 0406 - 根据身高重建队列 ｜ [LeetCode 链接](https://leetcode.cn/problems/queue-reconstruction-by-height/) ｜ [题解笔记](../solutions/0401-0500/0406-queue-reconstruction-by-height.md)

### 4.5 子方法 E：数位构造相关

**方法说明**

通过从高位到低位的贪心选择，构造满足约束条件的最大或最小数字。

**模板代码**

```python
# 数位构造问题的通用思路
def greedy_digit(num):
    # 1. 将数字转换为数字序列
    # 2. 从高位开始，贪心地选择最优的数字
    # 3. 如果不满足约束，回退调整
    # 4. 返回构造的数字
    pass
```

**模板题目**

- 0738 - 单调递增的数字 ｜ [LeetCode 链接](https://leetcode.cn/problems/monotone-increasing-digits/) ｜ [题解笔记](../solutions/0701-0800/0738-monotone-increasing-digits.md)

### 4.6 子方法 F：树上状态相关

**方法说明**

在树上使用贪心策略，通常从叶子节点向上进行状态转移，每个节点的决策考虑子树的最优性。

**模板代码**

```python
# 树上贪心问题的通用思路
def greedy_tree(root):
    # 1. 从叶子节点开始，自下而上遍历
    # 2. 对于每个节点，根据子节点的状态进行贪心决策
    # 3. 返回以当前节点为根的最优解
    pass
```

**模板题目**

- 0968 - 监控二叉树 ｜ [LeetCode 链接](https://leetcode.cn/problems/binary-tree-cameras/) ｜ [题解笔记](../solutions/0901-1000/0968-binary-tree-cameras.md)

### 4.7 子方法 G：区间调度相关

**方法说明**

按开始时间排序，并用最小堆维护当前正在占用的会议室结束时间；当最早结束时间不晚于新会议开始时复用会议室。遍历过程中的堆大小峰值即最少会议室数量。

**模板题目**

- 0253 - 会议室 II ｜ [LeetCode 链接](https://leetcode.cn/problems/meeting-rooms-ii/) ｜ [题解笔记](../solutions/0201-0300/0253-meeting-rooms-ii.md)

### 4.8 子方法 H：频次约束调度相关

**方法说明**

统计任务频次，抓住最高频任务对总时长的下界约束，再与任务总数取最大值，得到最短执行时间。

**模板题目**

- 0621 - Task Scheduler ｜ [LeetCode 链接](https://leetcode.cn/problems/task-scheduler/) ｜ [题解笔记](../solutions/0601-0700/0621-task-scheduler.md)

## 5 易错点

- 贪心策略的正确性难以证明，容易遗漏反例
- 多个约束条件时，需要明确约束的优先级和冲突处理方式
- 未考虑边界情况或特殊输入的处理

## 6 总结

贪心没有什么特定的套路，倒不如说更加考验问题抽象建模的能力。想清楚当前选择如何服务于全局目标，是贪心题最核心的一步。
