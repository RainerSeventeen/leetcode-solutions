# 动态规划（入门/背包/划分/状态机/区间/状压/数位/数据结构优化/树形/博弈/概率期望）

## 1 概览
动态规划通过状态定义与转移关系复用子问题结果，适合最值、计数、可行性问题。
核心不是“套公式”，而是先找到一个稳定不变的状态语义，让递推关系在每一层都成立。

## 2 核心思想
- 明确状态：`dp[i]`、`dp[i][j]` 或状态机维度。
- 写出转移：当前状态由哪些已知状态推来。
- 确定遍历顺序：保证依赖项先被计算。
- 做空间优化：滚动数组或一维压缩。

补充判断：
- 先看状态图是否可做无环递推。若存在环依赖，通常不适合直接做 DP。
- 数据规模过大且状态数爆炸时，DP 可能不可行，需要先做状态压缩或换思路。

## 3 解题流程

1. DP 数组中每一个值，或者索引的意义
2. 递推公式
3. DP 数组的如何初始化
4. 遍历顺序
5. 打印 DP 数组（主要用于分析错误）

## 4 模板与子方法
### 4.1 线性序列 DP
方法说明：
适用于一维最值与计数问题，可滚动优化到 O(1) 或 O(n) 空间。

模板代码：
```python
def max_subarray(nums):
    best = cur = nums[0]
    for x in nums[1:]:
        cur = max(x, cur + x)
        best = max(best, cur)
    return best
```

#### 4.1.1 模板题目
- 0053 - 最大子数组和 ｜ [LeetCode 链接](https://leetcode.cn/problems/maximum-subarray/) ｜ [题解笔记](../solutions/0001-0100/0053-maximum-subarray.md)
- 0198 - 打家劫舍 ｜ [LeetCode 链接](https://leetcode.cn/problems/house-robber/) ｜ [题解笔记](../solutions/0101-0200/0198-house-robber.md)
- 0152 - 乘积最大子数组 ｜ [LeetCode 链接](https://leetcode.cn/problems/maximum-product-subarray/) ｜ [题解笔记](../solutions/0101-0200/0152-maximum-product-subarray.md)
- 0300 - 最长递增子序列 ｜ [LeetCode 链接](https://leetcode.cn/problems/longest-increasing-subsequence/) ｜ [题解笔记](../solutions/0201-0300/0300-longest-increasing-subsequence.md)
- 0718 - 最长重复子数组 ｜ [LeetCode 链接](https://leetcode.cn/problems/maximum-length-of-repeated-subarray/) ｜ [题解笔记](../solutions/0701-0800/0718-maximum-length-of-repeated-subarray.md)
- 0213 - 打家劫舍 II ｜ [LeetCode 链接](https://leetcode.cn/problems/house-robber-ii/) ｜ [题解笔记](../solutions/0201-0300/0213-house-robber-ii.md)
- 0343 - 整数拆分 ｜ [LeetCode 链接](https://leetcode.cn/problems/integer-break/) ｜ [题解笔记](../solutions/0301-0400/0343-integer-break.md)
- 0435 - 无重叠区间 ｜ [LeetCode 链接](https://leetcode.cn/problems/non-overlapping-intervals/) ｜ [题解笔记](../solutions/0401-0500/0435-non-overlapping-intervals.md)
- 0747 - 使用最小花费爬楼梯 ｜ [LeetCode 链接](https://leetcode.cn/problems/min-cost-climbing-stairs/) ｜ [题解笔记](../solutions/0701-0800/0746-min-cost-climbing-stairs.md)
- 509 - 斐波那契数 ｜ [LeetCode 链接](https://leetcode.cn/problems/fibonacci-number/) ｜ [题解笔记](../solutions/0501-0600/0509-fibonacci-number.md)
- 3840 - 打家劫舍 V ｜ [LeetCode 链接](https://leetcode.cn/problems/house-robber-v/) ｜ [题解笔记](../solutions/3801-3900/3840-house-robber-v.md)
### 4.2 0-1 背包 DP
方法说明：
定义 `dp[j]` 为容量为 `j` 时的最优值/可行性。每个物品只能使用一次，因此容量必须倒序遍历，避免同一轮次重复使用当前物品。

讲解要点：
- 二维定义常写为：`dp[i][j]` 表示下标 `[0..i]` 物品里任选，容量 `j` 下的最优结果。
- 二维转移是：
  - 不选第 `i` 件：`dp[i - 1][j]`
  - 选第 `i` 件：`dp[i - 1][j - w[i]] + v[i]`（需 `j >= w[i]`）
- 压缩到一维后，`dp[j]` 仍然隐含“第 i 轮物品”的语义。倒序遍历是为了保证 `dp[j - w[i]]` 读取到的是上一轮状态，而不是本轮刚更新出的状态。
- 初始化要围绕转移前置条件来想：`dp[0]` 通常是天然边界；其余位置按题目语义设为 0、`-inf` 或 `False`。

模板代码：
```python
def knapsack_01(nums, target):
    dp = [False] * (target + 1)
    dp[0] = True
    for x in nums:
        for j in range(target, x - 1, -1):
            dp[j] = dp[j] or dp[j - x]
    return dp[target]
```

#### 4.2.1 模板题目
- 0416 - 分割等和子集 ｜ [LeetCode 链接](https://leetcode.cn/problems/partition-equal-subset-sum/) ｜ [题解笔记](../solutions/0401-0500/0416-partition-equal-subset-sum.md)
- 0494 - 目标和 ｜ [LeetCode 链接](https://leetcode.cn/problems/target-sum/) ｜ [题解笔记](../solutions/0401-0500/0494-target-sum.md)
- 0474 - 一和零 ｜ [LeetCode 链接](https://leetcode.cn/problems/ones-and-zeroes/) ｜ [题解笔记](../solutions/0401-0500/0474-ones-and-zeroes.md)
- 1049 - 最后一块石头的重量 II ｜ [LeetCode 链接](https://leetcode.cn/problems/last-stone-weight-ii/) ｜ [题解笔记](../solutions/1001-1100/1049-last-stone-weight-ii.md)

### 4.3 完全背包 DP（最值/可行性）
方法说明：
定义 `dp[j]` 为容量为 `j` 的最优值/可行性。每个物品可重复使用，因此容量需要正序遍历，使 `dp[j - x]` 可以来自当前物品已更新过的状态。纯完全背包最值模型下，“先物品后容量”与“先容量后物品”都可成立。

讲解要点：
- 二维写法中，选当前物品的分支来自当前行：`dp[i][j - w[i]] + v[i]`，这正是“可重复选取”的来源。
- 一维压缩时改为容量正序，含义是：当前轮次中 `dp[j - x]` 允许已经包含当前物品，从而可以继续叠加当前物品。
- 如果题目是“纯最值/可行性”且不关心序列顺序，则物品和容量的双层循环有时可交换；但在计数题中不能随意交换。

模板代码：
```python
def complete_knapsack_min(coins, amount):
    INF = 10**9
    dp = [0] + [INF] * amount
    for x in coins:
        for j in range(x, amount + 1):
            dp[j] = min(dp[j], dp[j - x] + 1)
    return -1 if dp[amount] == INF else dp[amount]
```

#### 4.3.1 模板题目
- 0279 - 完全平方数 ｜ [LeetCode 链接](https://leetcode.cn/problems/perfect-squares/) ｜ [题解笔记](../solutions/0201-0300/0279-perfect-squares.md)
- 0322 - 零钱兑换 ｜ [LeetCode 链接](https://leetcode.cn/problems/coin-change/) ｜ [题解笔记](../solutions/0301-0400/0322-coin-change.md)

### 4.4 完全背包计数（组合/排列）
方法说明：
计数型完全背包的核心差异在循环顺序：
- 先物品、后容量：统计组合数（顺序不敏感）。
- 先容量、后物品：统计排列数（顺序敏感）。

讲解要点：
- 通用计数转移常写作：`dp[j] += dp[j - x]`，关键不在公式本身，而在 `dp[j - x]` 当时“代表了哪些方案”。
- 先物品后容量：每轮先固定可用物品集合，天然避免同一组元素因顺序不同被重复计数，因此是组合。
- 先容量后物品：同一容量位会反复吸收不同“最后一个物品”，顺序不同会形成不同路径，因此是排列。
- 用 `nums = [1, 2]`、`target = 3` 手推可快速校验语义：
  - 组合语义只统计 `{1, 2}` 一次。
  - 排列语义会把 `[1, 2]` 与 `[2, 1]` 视作两种路径。
- 一旦题目问“方案数”，先明确题意是“顺序是否区分”，再反推循环顺序；不要先写循环再赌语义。

模板代码：
```python
def count_complete_knapsack(nums, target, order_matters):
    dp = [0] * (target + 1)
    dp[0] = 1
    if order_matters:
        for j in range(1, target + 1):
            for x in nums:
                if j >= x:
                    dp[j] += dp[j - x]
    else:
        for x in nums:
            for j in range(x, target + 1):
                dp[j] += dp[j - x]
    return dp[target]
```

#### 4.4.1 模板题目
- 0070 - 爬楼梯 ｜ [LeetCode 链接](https://leetcode.cn/problems/climbing-stairs/) ｜ [题解笔记](../solutions/0001-0100/0070-climbing-stairs.md)
- 0377 - 组合总和 Ⅳ ｜ [LeetCode 链接](https://leetcode.cn/problems/combination-sum-iv/) ｜ [题解笔记](../solutions/0301-0400/0377-combination-sum-iv.md)
- 0518 - 零钱兑换 II ｜ [LeetCode 链接](https://leetcode.cn/problems/coin-change-ii/) ｜ [题解笔记](../solutions/0501-0600/0518-coin-change-ii.md)
### 4.5 状态机 DP
方法说明：
把“持有/不持有/冷冻”等阶段建模为有限状态并转移。

讲解要点：
- 股票类题最关键的是状态定义：通常把 `dp[i][0/1/2...]` 定义为“第 i 天处于某种持仓状态的最优收益”，而不是简单统计“买/卖次数”。
- 一旦状态语义清晰，手续费、冷冻期、最多交易次数都只是新增状态或修改转移边。
- 以“只允许一次交易”的 121 为例，`dp[i][1]` 表示第 `i` 天持有股票的最大现金，其转移是 `max(dp[i-1][1], -prices[i])`，而不是 `dp[i-1][0] - prices[i]`；后者会引入“多次买卖”的语义。

模板代码：
```python
def max_profit_cooldown(prices):
    hold, sold, rest = -10**15, 0, 0
    for p in prices:
        pre_hold, pre_sold, pre_rest = hold, sold, rest
        hold = max(pre_hold, pre_rest - p)
        sold = pre_hold + p
        rest = max(pre_rest, pre_sold)
    return max(sold, rest)
```

#### 4.5.1 模板题目
- 0121 - 买卖股票的最佳时机 ｜ [LeetCode 链接](https://leetcode.cn/problems/best-time-to-buy-and-sell-stock/) ｜ [题解笔记](../solutions/0101-0200/0121-best-time-to-buy-and-sell-stock.md)
- 0309 - 买卖股票的最佳时机含冷冻期 ｜ [LeetCode 链接](https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-with-cooldown/) ｜ [题解笔记](../solutions/0301-0400/0309-best-time-to-buy-and-sell-stock-with-cooldown.md)
- 0122 - 买卖股票的最佳时机 II ｜ [LeetCode 链接](https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-ii/) ｜ [题解笔记](../solutions/0101-0200/0122-best-time-to-buy-and-sell-stock-ii.md)
- 0123 - 买卖股票的最佳时机 III ｜ [LeetCode 链接](https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-iii/) ｜ [题解笔记](../solutions/0101-0200/0123-best-time-to-buy-and-sell-stock-iii.md)
- 0188 - 买卖股票的最佳时机 IV ｜ [LeetCode 链接](https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-iv/) ｜ [题解笔记](../solutions/0101-0200/0188-best-time-to-buy-and-sell-stock-iv.md)
- 0714 - 买卖股票的最佳时机含手续费 ｜ [LeetCode 链接](https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/) ｜ [题解笔记](../solutions/0701-0800/0714-best-time-to-buy-and-sell-stock-with-transaction-fee.md)
### 4.6 区间 DP
方法说明：
以区间长度递增推进，常见于“戳气球、回文子序列、合并代价”这类依赖子区间的问题。

讲解要点：
- 典型状态是 `dp[l][r]`，表示闭区间或半开区间上的最优值，必须先统一边界语义再写转移。
- 常见依赖是把大区间拆成两个小区间，或从两端向内收缩，因此遍历顺序通常是“按区间长度从小到大”。
- 若顺序写反，会在计算 `dp[l][r]` 时访问到尚未计算的 `dp[l][k]` / `dp[k+1][r]`。

模板代码：
```python
def interval_dp(n):
    dp = [[0] * n for _ in range(n)]
    for length in range(2, n + 1):
        for l in range(0, n - length + 1):
            r = l + length - 1
            dp[l][r] = min(dp[l][k] + dp[k + 1][r] for k in range(l, r))
    return dp
```

#### 4.6.1 模板题目
- 0516 - 最长回文子序列 ｜ [LeetCode 链接](https://leetcode.cn/problems/longest-palindromic-subsequence/) ｜ [题解笔记](../solutions/0501-0600/0516-longest-palindromic-subsequence.md)
- 0312 - 戳气球 ｜ [LeetCode 链接](https://leetcode.cn/problems/burst-balloons/) ｜ [题解笔记](../solutions/0301-0400/0312-burst-balloons.md)

### 4.7 树形与结构化 DP
方法说明：
把节点当作状态单元，通过后序遍历（子树先于父节点）聚合子问题，常见于树上选点、树上路径、Catalan 结构计数。

讲解要点：
- 树形 DP 的核心不是“树”本身，而是每个节点要定义稳定状态语义，如“偷/不偷”或“作为根时的结构数”。
- 以打家劫舍 III 为例，节点返回二维状态：`dp[0]` 不偷当前节点、`dp[1]` 偷当前节点；父节点只组合左右子树返回值，不重复遍历。
- 以不同二叉搜索树为例，`dp[n]` 是由所有根划分累加得到：`dp[n] += dp[left] * dp[right]`，本质是结构化划分计数。

模板代码：
```python
def rob_tree(root):
    def dfs(node):
        if not node:
            return 0, 0
        l0, l1 = dfs(node.left)
        r0, r1 = dfs(node.right)
        not_take = max(l0, l1) + max(r0, r1)
        take = l0 + r0 + node.val
        return not_take, take
    return max(dfs(root))
```

#### 4.7.1 模板题目
- 0096 - 不同的二叉搜索树 ｜ [LeetCode 链接](https://leetcode.cn/problems/unique-binary-search-trees/) ｜ [题解笔记](../solutions/0001-0100/0096-unique-binary-search-trees.md)
- 0337 - 打家劫舍 III ｜ [LeetCode 链接](https://leetcode.cn/problems/house-robber-iii/) ｜ [题解笔记](../solutions/0301-0400/0337-house-robber-iii.md)

### 4.8 网格 DP
方法说明：
固定方向网格最值与计数，关注首行首列初始化。与网格专题交叉。

模板代码：
```python
def min_path_sum(grid):
    m, n = len(grid), len(grid[0])
    dp = [[0] * n for _ in range(m)]
    dp[0][0] = grid[0][0]
    for i in range(1, m):
        dp[i][0] = dp[i - 1][0] + grid[i][0]
    for j in range(1, n):
        dp[0][j] = dp[0][j - 1] + grid[0][j]
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
    return dp[-1][-1]
```

#### 4.8.1 模板题目
- 0062 - 不同路径 ｜ [LeetCode 链接](https://leetcode.cn/problems/unique-paths/) ｜ [题解笔记](../solutions/0001-0100/0062-unique-paths.md)
- 0064 - 最小路径和 ｜ [LeetCode 链接](https://leetcode.cn/problems/minimum-path-sum/) ｜ [题解笔记](../solutions/0001-0100/0064-minimum-path-sum.md)
- 0221 - 最大正方形 ｜ [LeetCode 链接](https://leetcode.cn/problems/maximal-square/) ｜ [题解笔记](../solutions/0201-0300/0221-maximal-square.md)
### 4.9 交叉字符串 DP 模板
方法说明：
以下题目主归属通常在字符串专题，此处作为 DP 视角交叉索引，模板是二维匹配转移。

讲解要点：
- 双串比较类问题通常可用二维状态网格覆盖全部对齐关系。
- 子序列问题常用定义：`dp[i][j]` 对应前缀 `[0..i)` 与 `[0..j)`，这样初始化和边界处理更统一。
- 回文类区间 DP 的典型依赖是“向内收缩”：`dp[i][j]` 依赖 `dp[i + 1][j - 1]`，因此遍历顺序必须保证内层区间先算完。
- 编辑距离做一维优化时，`dp[0]` 每轮都要更新为当前 `i`，并额外保存左上角旧值（常记作 `pre`），否则会把“上一行”状态覆盖掉导致转移失真。

模板代码：
```python
def lcs(a, b):
    m, n = len(a), len(b)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[m][n]
```

#### 4.9.1 模板题目
- 0072 - 编辑距离 ｜ [LeetCode 链接](https://leetcode.cn/problems/edit-distance/) ｜ [题解笔记](../solutions/0001-0100/0072-edit-distance.md)
- 0139 - 单词拆分 ｜ [LeetCode 链接](https://leetcode.cn/problems/word-break/) ｜ [题解笔记](../solutions/0101-0200/0139-word-break.md)
- 0010 - 正则表达式匹配 ｜ [LeetCode 链接](https://leetcode.cn/problems/regular-expression-matching/) ｜ [题解笔记](../solutions/0001-0100/0010-regular-expression-matching.md)
- 0032 - 最长有效括号 ｜ [LeetCode 链接](https://leetcode.cn/problems/longest-valid-parentheses/) ｜ [题解笔记](../solutions/0001-0100/0032-longest-valid-parentheses.md)
- 0115 - 不同的子序列 ｜ [LeetCode 链接](https://leetcode.cn/problems/distinct-subsequences/) ｜ [题解笔记](../solutions/0101-0200/0115-distinct-subsequences.md)
- 0392 - 判断子序列 ｜ [LeetCode 链接](https://leetcode.cn/problems/is-subsequence/) ｜ [题解笔记](../solutions/0301-0400/0392-is-subsequence.md)
- 0583 - 两个字符串的删除操作 ｜ [LeetCode 链接](https://leetcode.cn/problems/delete-operation-for-two-strings/) ｜ [题解笔记](../solutions/0501-0600/0583-delete-operation-for-two-strings.md)
- 1035 - 不相交的线 ｜ [LeetCode 链接](https://leetcode.cn/problems/uncrossed-lines/) ｜ [题解笔记](../solutions/1001-1100/1035-uncrossed-lines.md)
- 1143 - 最长公共子序列 ｜ [LeetCode 链接](https://leetcode.cn/problems/longest-common-subsequence/) ｜ [题解笔记](../solutions/1101-1200/1143-longest-common-subsequence.md)

### 4.10 网格 DP 路径转移
#### 4.10.1 模板题目
- 0063 - 不同路径 II ｜ [LeetCode 链接](https://leetcode.cn/problems/unique-paths-ii/) ｜ [题解笔记](../solutions/0001-0100/0063-unique-paths-ii.md)

### 4.11 分层扩散 DP
方法说明：
按层推进状态并把“超额”向下一层相邻位置分发，常用于金字塔/三角结构中的流量或概率传递问题。

#### 4.11.1 模板题目
- 0815 - 香槟塔 ｜ [LeetCode 链接](https://leetcode.cn/problems/champagne-tower/) ｜ [题解笔记](../solutions/0701-0800/0799-champagne-tower.md)

### 4.12 状态压缩计数 DP
方法说明：
把多维状态压缩成可哈希表示，通过逐元素做计数转移，适合“每步有固定分支”的方案数问题。

#### 4.12.1 模板题目
- 3850 - 统计结果等于 K 的序列数目 ｜ [LeetCode 链接](https://leetcode.cn/problems/count-sequences-to-k/) ｜ [题解笔记](../solutions/3801-3900/3850-count-sequences-to-k.md)
## 5 易错点
- 状态定义含糊，导致初始化和转移全错。
- 背包遍历顺序错误。
- 区间 DP 未按长度递增。

## 6 总结
动态规划先定状态语义，再定转移与遍历顺序；一旦不变量清晰，复杂题可拆成稳定模板。
