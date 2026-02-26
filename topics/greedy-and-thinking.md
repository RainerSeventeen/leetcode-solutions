# 贪心与思维（基本贪心策略/反悔/区间/字典序/数学/思维/脑筋急转弯/构造）

## 1 概览
贪心与思维题通过局部最优策略推进到全局解，重点是证明而非状态枚举。

## 2 核心思想
- 贪心：每步做当前最优且不破坏后续可行性。
- 思维构造：用排序、不变量、上下界或交换论证化简问题。
- 区间类常结合排序和最小结构维护。
- 证明主线：先给出“当前决策不吃亏”的局部论证，再说明该决策可迭代堆叠到全局最优。
- 多维问题通常先固定一个维度的顺序，再在另一个维度做插入/扫描；两个维度同时贪心往往会互相破坏。

## 3 解题流程
1. 提出候选贪心策略与比较标准。
2. 给出交换论证或反证证明正确。
3. 写线性/排序后扫描实现。
4. 检查反例：局部最优是否会阻断全局。

## 4 模板与子方法
### 4.1 可达范围贪心
方法说明：

维护当前步可覆盖最远位置，范围耗尽时增加一步并更新下一层边界。
把当前位置 `i` 能扩展到的最远点记为 `next_end`，当前步的边界记为 `cur_end`。当扫描到 `i == cur_end` 时，说明这一层可达位置已经用尽，必须迈出下一步并把边界推进到 `next_end`。这个“按层推进”的过程与 BFS 分层一致，能保证步数最小。

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
- 0055 - 跳跃游戏 ｜ [LeetCode 链接](https://leetcode.cn/problems/jump-game/) ｜ [题解笔记](../solutions/0001-0100/0055-jump-game.md)
### 4.2 序列与邻接约束贪心
方法说明：

通过双向扫描或状态压缩处理相邻约束；摆动序列可用符号变化贪心。
摆动序列要同时覆盖三类场景：正常上下坡、夹杂平坡的摆动、单调段中的平坡。实现上只在“坡度符号发生变化”时计数，并用 `<= / >=` 包住平坡，避免漏记转折点。
分发糖果采用两次局部最优叠加：从左到右保证“右边更高分则糖更多”，从右到左补齐“左边更高分则糖更多”。第二次更新必须取 `max`，否则会破坏第一次已经满足的约束。

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
- 0134 - 加油站 ｜ [LeetCode 链接](https://leetcode.cn/problems/gas-station/) ｜ [题解笔记](../solutions/0101-0200/0134-gas-station.md)
- 0455 - 分发饼干 ｜ [LeetCode 链接](https://leetcode.cn/problems/assign-cookies/) ｜ [题解笔记](../solutions/0401-0500/0455-assign-cookies.md)
- 0768 - 划分字母区间 ｜ [LeetCode 链接](https://leetcode.cn/problems/partition-labels/) ｜ [题解笔记](../solutions/0701-0800/0763-partition-labels.md)
- 0890 - 柠檬水找零 ｜ [LeetCode 链接](https://leetcode.cn/problems/lemonade-change/) ｜ [题解笔记](../solutions/0801-0900/0860-lemonade-change.md)
- 1005 - K 次取反后最大化的数组和 ｜ [LeetCode 链接](https://leetcode.cn/problems/maximize-sum-of-array-after-k-negations/) ｜ [题解笔记](../solutions/1001-1100/1005-maximize-sum-of-array-after-k-negations.md)
### 4.3 多维排序与重建
方法说明：

涉及多个约束维度时，先找“可一次性固定”的主维度，再处理次维度。
以身高重建队列为例：先按身高降序、`k` 升序排序，先放高个子可让后续矮个插入不影响已满足的计数条件；再按 `k` 插入即可保证每个人前面恰有 `k` 个不矮于他的人。

模板代码：

```python
def reconstruct_queue(people):
    people.sort(key=lambda p: (-p[0], p[1]))
    q = []
    for p in people:
        q.insert(p[1], p)
    return q
```

#### 4.3.1 模板题目
- 0406 - 根据身高重建队列 ｜ [LeetCode 链接](https://leetcode.cn/problems/queue-reconstruction-by-height/) ｜ [题解笔记](../solutions/0401-0500/0406-queue-reconstruction-by-height.md)

### 4.4 区间排序与合并
方法说明：

先按左端点排序建立“最早开始”的处理顺序，再维护当前合并区间右端点。若新区间左端点超过当前右端点则开启新区间，否则更新右端点。
这类题的关键坑在端点语义和排序键：排序键错误或闭开区间判断错位，都会直接导致错误合并。

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

#### 4.4.1 模板题目
- 0056 - 合并区间 ｜ [LeetCode 链接](https://leetcode.cn/problems/merge-intervals/) ｜ [题解笔记](../solutions/0001-0100/0056-merge-intervals.md)
- 0452 - 用最少数量的箭引爆气球 ｜ [LeetCode 链接](https://leetcode.cn/problems/minimum-number-of-arrows-to-burst-balloons/) ｜ [题解笔记](../solutions/0401-0500/0452-minimum-number-of-arrows-to-burst-balloons.md)

### 4.5 频次下界与构造思维
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

#### 4.5.1 模板题目
- 0621 - 任务调度器 ｜ [LeetCode 链接](https://leetcode.cn/problems/task-scheduler/) ｜ [题解笔记](../solutions/0601-0700/0621-task-scheduler.md)
- 0169 - 多数元素 ｜ [LeetCode 链接](https://leetcode.cn/problems/majority-element/) ｜ [题解笔记](../solutions/0101-0200/0169-majority-element.md)

### 4.6 数位与排列构造贪心
方法说明：

这类题关注“从高位/高优先级位置回退后，如何一次性把低位修成最优形态”。
单调递增数字中，一旦出现 `nums[i-1] > nums[i]`，就把高位减一并把该位之后全部置为 `9`；这是因为高位一旦下调，低位取最大值才能保证不超过原数且尽量大。
下一个排列则反向找下降点、交换后缀最小更大值、再反转后缀，本质也是局部调整后缀到字典序最优。

模板代码：

```python
def monotone_increasing_digits(n):
    s = list(str(n))
    flag = len(s)
    for i in range(len(s) - 1, 0, -1):
        if s[i - 1] > s[i]:
            s[i - 1] = str(int(s[i - 1]) - 1)
            flag = i
    for i in range(flag, len(s)):
        s[i] = "9"
    return int("".join(s))
```

#### 4.6.1 模板题目
- 0031 - 下一个排列 ｜ [LeetCode 链接](https://leetcode.cn/problems/next-permutation/) ｜ [题解笔记](../solutions/0001-0100/0031-next-permutation.md)
- 0738 - 单调递增的数字 ｜ [LeetCode 链接](https://leetcode.cn/problems/monotone-increasing-digits/) ｜ [题解笔记](../solutions/0701-0800/0738-monotone-increasing-digits.md)

### 4.7 树上状态贪心
方法说明：

把节点状态离散化后，用后序遍历自底向上决策。监控二叉树常用三态：`0=未覆盖`、`1=有摄像头`、`2=已覆盖`。
决策顺序不能乱：若任一子节点未覆盖，当前节点必须放摄像头；否则若任一子节点有摄像头，当前节点已覆盖；最后才是“两个子节点都已覆盖但无摄像头”，当前节点返回未覆盖并交给父节点处理。`null` 视作已覆盖可避免叶子节点被误装摄像头。

模板代码：

```python
def min_camera_cover(root):
    ans = 0

    def dfs(node):
        nonlocal ans
        if not node:
            return 2
        l, r = dfs(node.left), dfs(node.right)
        if l == 0 or r == 0:
            ans += 1
            return 1
        if l == 1 or r == 1:
            return 2
        return 0

    if dfs(root) == 0:
        ans += 1
    return ans
```

#### 4.7.1 模板题目

### 4.8 规则模拟
方法说明：

这种题没有很好的办法, 直接模拟题目的运行顺序即可

#### 4.8.1 模板题目
- 1404 - 将二进制表示减到 1 的步骤数 ｜ [LeetCode 链接](https://leetcode.cn/problems/number-of-steps-to-reduce-a-number-in-binary-representation-to-one/) ｜ [题解笔记](../solutions/1401-1500/1404-number-of-steps-to-reduce-a-number-in-binary-representation-to-one.md)
- 3847 - 计算比赛分数差 ｜ [LeetCode 链接](https://leetcode.cn/problems/find-the-score-difference-in-a-game/) ｜ [题解笔记](../solutions/3801-3900/3847-find-the-score-difference-in-a-game.md)
- 3849 - 重新排列后的最大按位异或值 ｜ [LeetCode 链接](https://leetcode.cn/problems/maximum-bitwise-xor-after-rearrangement/) ｜ [题解笔记](../solutions/3801-3900/3849-maximum-bitwise-xor-after-rearrangement.md)
## 5 易错点
- 只给策略不证明正确性。
- 排序键选错导致局部决策失效。
- 区间题忽略端点闭开语义。
- 双向扫描第二遍直接覆盖第一遍结果，导致前置约束失效（如糖果分配未取 `max`）。
- 认为多维约束可同时贪心，未先固定主维度（如队列重建）。
- 树上贪心状态转移顺序写反，导致摄像头数偏大或漏覆盖。

## 6 总结
贪心题关键不在代码，而在“为什么这一步不会后悔”；先给证明再落实现。
