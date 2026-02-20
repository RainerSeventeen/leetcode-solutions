# 动态规划

## 1 概览
动态规划通过状态定义与转移关系复用子问题结果，适合最值、计数、可行性问题。

## 2 核心思想
- 明确状态：`dp[i]`、`dp[i][j]` 或状态机维度。
- 写出转移：当前状态由哪些已知状态推来。
- 确定遍历顺序：保证依赖项先被计算。
- 做空间优化：滚动数组或一维压缩。

## 3 解题流程
1. 写清状态语义与答案位置。
2. 给出初始化与非法状态处理。
3. 按依赖顺序转移并更新答案。
4. 用小样例手推验证转移正确性。

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
- 0053 - Maximum Subarray ｜ [LeetCode 链接](https://leetcode.cn/problems/maximum-subarray/) ｜ [题解笔记](../solutions/0001-0100/0053-maximum-subarray.md)
- 0070 - 爬楼梯 ｜ [LeetCode 链接](https://leetcode.cn/problems/climbing-stairs/) ｜ [题解笔记](../solutions/0001-0100/0070-climbing-stairs.md)
- 0198 - 打家劫舍 ｜ [LeetCode 链接](https://leetcode.cn/problems/house-robber/) ｜ [题解笔记](../solutions/0101-0200/0198-house-robber.md)
- 0152 - 乘积最大子数组 ｜ [LeetCode 链接](https://leetcode.cn/problems/maximum-product-subarray/) ｜ [题解笔记](../solutions/0101-0200/0152-maximum-product-subarray.md)
- 0300 - 最长递增子序列 ｜ [LeetCode 链接](https://leetcode.cn/problems/longest-increasing-subsequence/) ｜ [题解笔记](../solutions/0201-0300/0300-longest-increasing-subsequence.md)
- 0718 - 最长重复子数组 ｜ [LeetCode 链接](https://leetcode.cn/problems/maximum-length-of-repeated-subarray/) ｜ [题解笔记](../solutions/0701-0800/0718-maximum-length-of-repeated-subarray.md)
### 4.2 背包 DP（0-1/完全）
方法说明：
容量维度转移是核心。0-1 背包倒序，完全背包正序。也可表示计数型目标。

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
- 0279 - 完全平方数 ｜ [LeetCode 链接](https://leetcode.cn/problems/perfect-squares/) ｜ [题解笔记](../solutions/0201-0300/0279-perfect-squares.md)
- 0322 - 零钱兑换 ｜ [LeetCode 链接](https://leetcode.cn/problems/coin-change/) ｜ [题解笔记](../solutions/0301-0400/0322-coin-change.md)
### 4.3 状态机 DP
方法说明：
把“持有/不持有/冷冻”等阶段建模为有限状态并转移。

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

#### 4.3.1 模板题目
- 0121 - 买卖股票的最佳时机 ｜ [LeetCode 链接](https://leetcode.cn/problems/best-time-to-buy-and-sell-stock/) ｜ [题解笔记](../solutions/0101-0200/0121-best-time-to-buy-and-sell-stock.md)
- 0309 - 买卖股票的最佳时机含冷冻期 ｜ [LeetCode 链接](https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-with-cooldown/) ｜ [题解笔记](../solutions/0301-0400/0309-best-time-to-buy-and-sell-stock-with-cooldown.md)
### 4.4 区间与结构化 DP
方法说明：
以区间长度递增或结构节点递归推进。字符串区间类题可交叉到字符串专题。

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

#### 4.4.1 模板题目
- 0516 - 最长回文子序列 ｜ [LeetCode 链接](https://leetcode.cn/problems/longest-palindromic-subsequence/) ｜ [题解笔记](../solutions/0501-0600/0516-longest-palindromic-subsequence.md)
- 0312 - 戳气球 ｜ [LeetCode 链接](https://leetcode.cn/problems/burst-balloons/) ｜ [题解笔记](../solutions/0301-0400/0312-burst-balloons.md)
- 0096 - 不同的二叉搜索树 ｜ [LeetCode 链接](https://leetcode.cn/problems/unique-binary-search-trees/) ｜ [题解笔记](../solutions/0001-0100/0096-unique-binary-search-trees.md)
- 0337 - 打家劫舍 III ｜ [LeetCode 链接](https://leetcode.cn/problems/house-robber-iii/) ｜ [题解笔记](../solutions/0301-0400/0337-house-robber-iii.md)
### 4.5 网格 DP
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

#### 4.5.1 模板题目
- 0062 - Unique Paths ｜ [LeetCode 链接](https://leetcode.cn/problems/unique-paths/) ｜ [题解笔记](../solutions/0001-0100/0062-unique-paths.md)
- 0064 - Minimum Path Sum ｜ [LeetCode 链接](https://leetcode.cn/problems/minimum-path-sum/) ｜ [题解笔记](../solutions/0001-0100/0064-minimum-path-sum.md)
- 0221 - Maximal Square ｜ [LeetCode 链接](https://leetcode.cn/problems/maximal-square/) ｜ [题解笔记](../solutions/0201-0300/0221-maximal-square.md)
- 0085 - Maximal Rectangle ｜ [LeetCode 链接](https://leetcode.cn/problems/maximal-rectangle/) ｜ [题解笔记](../solutions/0001-0100/0085-maximal-rectangle.md)
### 4.6 交叉字符串 DP 模板
方法说明：
以下题目主归属通常在字符串专题，此处作为 DP 视角交叉索引，模板是二维匹配转移。

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

#### 4.6.1 模板题目
- 0072 - 编辑距离 ｜ [LeetCode 链接](https://leetcode.cn/problems/edit-distance/) ｜ [题解笔记](../solutions/0001-0100/0072-edit-distance.md)
- 0647 - 回文子串 ｜ [LeetCode 链接](https://leetcode.cn/problems/palindromic-substrings/) ｜ [题解笔记](../solutions/0601-0700/0647-palindromic-substrings.md)
- 0139 - 单词拆分 ｜ [LeetCode 链接](https://leetcode.cn/problems/word-break/) ｜ [题解笔记](../solutions/0101-0200/0139-word-break.md)
- 0005 - Longest Palindromic Substring ｜ [LeetCode 链接](https://leetcode.cn/problems/longest-palindromic-substring/) ｜ [题解笔记](../solutions/0001-0100/0005-longest-palindromic-substring.md)
- 0010 - Regular Expression Matching ｜ [LeetCode 链接](https://leetcode.cn/problems/regular-expression-matching/) ｜ [题解笔记](../solutions/0001-0100/0010-regular-expression-matching.md)
- 0032 - 最长有效括号 ｜ [LeetCode 链接](https://leetcode.cn/problems/longest-valid-parentheses/) ｜ [题解笔记](../solutions/0001-0100/0032-longest-valid-parentheses.md)
- 0338 - 比特位计数 ｜ [LeetCode 链接](https://leetcode.cn/problems/counting-bits/) ｜ [题解笔记](../solutions/0301-0400/0338-counting-bits.md)
## 5 易错点
- 状态定义含糊，导致初始化和转移全错。
- 背包遍历顺序错误。
- 区间 DP 未按长度递增。

## 6 总结
动态规划先定状态语义，再定转移与遍历顺序；一旦不变量清晰，复杂题可拆成稳定模板。
