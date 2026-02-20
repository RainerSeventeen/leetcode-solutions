# 贪心与思维题

## 1 概览
贪心与思维题通过局部最优策略推进到全局解，重点是证明而非状态枚举。

## 2 核心思想
- 贪心：每步做当前最优且不破坏后续可行性。
- 思维构造：用排序、不变量、上下界或交换论证化简问题。
- 区间类常结合排序和最小结构维护。

## 3 解题流程
1. 提出候选贪心策略与比较标准。
2. 给出交换论证或反证证明正确。
3. 写线性/排序后扫描实现。
4. 检查反例：局部最优是否会阻断全局。

## 4 模板与子方法
### 4.1 可达范围贪心
方法说明：
维护当前步可覆盖最远位置，范围耗尽时增加一步并更新下一层边界。

模板代码：
```python
def jump(nums):
    end = far = steps = 0
    for i in range(len(nums) - 1):
        far = max(far, i + nums[i])
        if i == end:
            steps += 1
            end = far
    return steps
```

#### 4.1.1 模板题目
- 0045 - 跳跃游戏 II ｜ [LeetCode 链接](https://leetcode.cn/problems/jump-game-ii/) ｜ [题解笔记](../solutions/0001-0100/0045-jump-game-ii.md)
- 0055 - Jump Game ｜ [LeetCode 链接](https://leetcode.cn/problems/jump-game/) ｜ [题解笔记](../solutions/0001-0100/0055-jump-game.md)
### 4.2 序列与邻接约束贪心
方法说明：
通过双向扫描或状态压缩处理相邻约束；摆动序列可用符号变化贪心。

模板代码：
```python
def candy(ratings):
    n = len(ratings)
    left = [1] * n
    for i in range(1, n):
        if ratings[i] > ratings[i - 1]:
            left[i] = left[i - 1] + 1
    right = ans = 1
    for i in range(n - 1, -1, -1):
        if i < n - 1 and ratings[i] > ratings[i + 1]:
            right += 1
        else:
            right = 1
        ans += max(left[i], right) if i < n - 1 else left[i]
    return ans
```

#### 4.2.1 模板题目
- 0376 - 摆动序列 ｜ [LeetCode 链接](https://leetcode.cn/problems/wiggle-subsequence/) ｜ [题解笔记](../solutions/0301-0400/0376-wiggle-subsequence.md)
- 0135 - 分发糖果 ｜ [LeetCode 链接](https://leetcode.cn/problems/candy/) ｜ [题解笔记](../solutions/0101-0200/0135-candy.md)
- 0581 - 最短无序连续子数组 ｜ [LeetCode 链接](https://leetcode.cn/problems/shortest-unsorted-continuous-subarray/) ｜ [题解笔记](../solutions/0501-0600/0581-shortest-unsorted-continuous-subarray.md)
### 4.3 排序重建与区间贪心
方法说明：
先排序建立处理顺序，再线性合并或放置。会议室 II 常配合最小堆实现，可交叉到数据结构专题。

模板代码：
```python
def merge(intervals):
    intervals.sort(key=lambda x: x[0])
    ans = []
    for l, r in intervals:
        if not ans or ans[-1][1] < l:
            ans.append([l, r])
        else:
            ans[-1][1] = max(ans[-1][1], r)
    return ans
```

#### 4.3.1 模板题目
- 0056 - Merge Intervals ｜ [LeetCode 链接](https://leetcode.cn/problems/merge-intervals/) ｜ [题解笔记](../solutions/0001-0100/0056-merge-intervals.md)
- 0406 - 根据身高重建队列 ｜ [LeetCode 链接](https://leetcode.cn/problems/queue-reconstruction-by-height/) ｜ [题解笔记](../solutions/0401-0500/0406-queue-reconstruction-by-height.md)
- 0253 - 会议室 II ｜ [LeetCode 链接](https://leetcode.cn/problems/meeting-rooms-ii/) ｜ [题解笔记](../solutions/0201-0300/0253-meeting-rooms-ii.md)
### 4.4 频次下界与构造思维
方法说明：
利用频次上界、空位模型或投票机制构造答案。树上贪心题可交叉到树专题。

模板代码：
```python
def majority_element(nums):
    cand, cnt = None, 0
    for x in nums:
        if cnt == 0:
            cand = x
        cnt += 1 if x == cand else -1
    return cand
```

#### 4.4.1 模板题目
- 0621 - Task Scheduler ｜ [LeetCode 链接](https://leetcode.cn/problems/task-scheduler/) ｜ [题解笔记](../solutions/0601-0700/0621-task-scheduler.md)
- 0169 - 多数元素 ｜ [LeetCode 链接](https://leetcode.cn/problems/majority-element/) ｜ [题解笔记](../solutions/0101-0200/0169-majority-element.md)
- 0031 - 下一个排列 ｜ [LeetCode 链接](https://leetcode.cn/problems/next-permutation/) ｜ [题解笔记](../solutions/0001-0100/0031-next-permutation.md)
- 0738 - 单调递增的数字 ｜ [LeetCode 链接](https://leetcode.cn/problems/monotone-increasing-digits/) ｜ [题解笔记](../solutions/0701-0800/0738-monotone-increasing-digits.md)
- 0968 - 监控二叉树 ｜ [LeetCode 链接](https://leetcode.cn/problems/binary-tree-cameras/) ｜ [题解笔记](../solutions/0901-1000/0968-binary-tree-cameras.md)
## 5 易错点
- 只给策略不证明正确性。
- 排序键选错导致局部决策失效。
- 区间题忽略端点闭开语义。

## 6 总结
贪心题关键不在代码，而在“为什么这一步不会后悔”；先给证明再落实现。
