# 贪心与思维（基本贪心策略/反悔/区间/字典序/数学/思维/脑筋急转弯/构造）

## 概览
贪心与思维题重在局部选择的正确性证明，以及对特殊结构的构造与转化。

## 核心思想
- 先定义局部决策标准，再证明该决策不会破坏全局最优。
- 常见证明方式包括交换论证、反证、归纳与不变量。
- 思维题通常通过等价转换、逆向分析和分类讨论降低复杂度。

## 解题流程
1. 识别题目是排序贪心、区间贪心、构造还是思维转化。
2. 写出候选策略并用反例自测。
3. 给出正确性证明，再实现线性或排序扫描算法。
4. 复查边界条件与不可行情形。

## 模板与子方法
### 贪心策略

#### 从最小/最大开始贪心
模板：

```python
# 待补充
```

模板题目：

- 1005 - K 次取反后最大化的数组和 ｜ [LeetCode 链接](https://leetcode.cn/problems/maximize-sum-of-array-after-k-negations/) ｜ [题解笔记](../solutions/1001-1100/1005-maximize-sum-of-array-after-k-negations.md)

#### 单序列配对
模板：

```python
# 待补充
```

模板题目：

待补充...

#### 双序列配对
模板：

```python
# 待补充
```

模板题目：

- 0455 - 分发饼干 ｜ [LeetCode 链接](https://leetcode.cn/problems/assign-cookies/) ｜ [题解笔记](../solutions/0401-0500/0455-assign-cookies.md)

#### 从最左/最右开始贪心
模板：

```python
# 待补充
```

模板题目：

- 1536 - 排布二进制网格的最少交换次数 ｜ [LeetCode 链接](https://leetcode.cn/problems/minimum-swaps-to-arrange-a-binary-grid/) ｜ [题解笔记](../solutions/1501-1600/1536-minimum-swaps-to-arrange-a-binary-grid.md)

#### 划分型贪心
模板：

```python
# 待补充
```

模板题目：

待补充...

#### 先枚举，再贪心
模板：

```python
# 待补充
```

模板题目：

- 1727 - 重新排列后的最大子矩阵 ｜ [LeetCode 链接](https://leetcode.cn/problems/largest-submatrix-with-rearrangements/) ｜ [题解笔记](../solutions/1701-1800/1727-largest-submatrix-with-rearrangements.md)

#### 交换论证法
模板：

```python
# 待补充
```

模板题目：

待补充...

#### 相邻不同
模板：

```python
from typing import Iterable, Callable


def min_changes_to_alternate(states: Iterable[int], start: int = 0) -> int:
    """
    二元状态交替最少修改次数模板。
    - states: 每个元素应为 0/1（可由字符/数字映射得到）
    - start: 期望第 0 位状态（0 或 1）
    """
    diff = 0
    for i, x in enumerate(states):
        expected = start ^ (i & 1)
        if x != expected:
            diff += 1
    return diff
```

模板题目：

- 0621 - 任务调度器 ｜ [LeetCode 链接](https://leetcode.cn/problems/task-scheduler/) ｜ [题解笔记](../solutions/0601-0700/0621-task-scheduler.md)
- 1758 - 生成交替二进制字符串的最少操作数 ｜ [LeetCode 链接](https://leetcode.cn/problems/minimum-changes-to-make-alternating-binary-string/) ｜ [题解笔记](../solutions/1701-1800/1758-minimum-changes-to-make-alternating-binary-string.md)
- 3854 - 使数组奇偶交替的最少操作 ｜ [LeetCode 链接](https://leetcode.cn/problems/minimum-operations-to-make-array-parity-alternating/) ｜ [题解笔记](../solutions/3801-3900/3854-minimum-operations-to-make-array-parity-alternating.md)

#### 反悔贪心
模板：

```python
# 待补充
```

模板题目：

待补充...

### 区间贪心

#### 不相交区间
模板：

```python
# 待补充
```

模板题目：

待补充...

#### 区间分组
模板：

```python
# 待补充
```

模板题目：

- 0253 - 会议室 II ｜ [LeetCode 链接](https://leetcode.cn/problems/meeting-rooms-ii/) ｜ [题解笔记](../solutions/0201-0300/0253-meeting-rooms-ii.md)

#### 区间选点
模板：

```python
# 待补充
```

模板题目：

- 0452 - 用最少数量的箭引爆气球 ｜ [LeetCode 链接](https://leetcode.cn/problems/minimum-number-of-arrows-to-burst-balloons/) ｜ [题解笔记](../solutions/0401-0500/0452-minimum-number-of-arrows-to-burst-balloons.md)

#### 区间覆盖
模板：

```python
# 待补充
```

模板题目：

- 0045 - 跳跃游戏 II ｜ [LeetCode 链接](https://leetcode.cn/problems/jump-game-ii/) ｜ [题解笔记](../solutions/0001-0100/0045-jump-game-ii.md)

#### 合并区间
模板：

```python
# 待补充
```

模板题目：

- 0056 - 合并区间 ｜ [LeetCode 链接](https://leetcode.cn/problems/merge-intervals/) ｜ [题解笔记](../solutions/0001-0100/0056-merge-intervals.md)
- 0055 - 跳跃游戏 ｜ [LeetCode 链接](https://leetcode.cn/problems/jump-game/) ｜ [题解笔记](../solutions/0001-0100/0055-jump-game.md)
- 0763 - 划分字母区间 ｜ [LeetCode 链接](https://leetcode.cn/problems/partition-labels/) ｜ [题解笔记](../solutions/0701-0800/0763-partition-labels.md)

#### 其他区间贪心
模板：

```python
# 待补充
```

模板题目：

待补充...

### 字符串贪心

#### 字典序最小/最大
模板：

```python
# 待补充
```

模板题目：

- 0738 - 单调递增的数字 ｜ [LeetCode 链接](https://leetcode.cn/problems/monotone-increasing-digits/) ｜ [题解笔记](../solutions/0701-0800/0738-monotone-increasing-digits.md)

#### 回文串贪心
模板：

```python
# 待补充
```

模板题目：

待补充...

#### 合法括号字符串
模板：

```python
# 待补充
```

模板题目：

待补充...

### 数学贪心

#### 基础
模板：

```python
# 待补充
```

模板题目：

待补充...

#### 乘积贪心
模板：

```python
# 待补充
```

模板题目：

待补充...

#### 排序不等式
模板：

```python
# 待补充
```

模板题目：

待补充...

#### 均值不等式
模板：

```python
# 待补充
```

模板题目：

待补充...

#### 中位数贪心
模板：

```python
# 待补充
```

模板题目：

待补充...

#### 归纳法
模板：

```python
# 待补充
```

模板题目：

待补充...

#### 其他数学贪心
模板：

```python
# 待补充
```

模板题目：

待补充...

### 思维题

#### 从特殊到一般
模板：

```python
# 待补充
```

模板题目：

待补充...

#### 脑筋急转弯
模板：

```python
# 待补充
```

模板题目：

- 1689 - 十-二进制数的最少数目 ｜ [LeetCode 链接](https://leetcode.cn/problems/partitioning-into-minimum-number-of-deci-binary-numbers/) ｜ [题解笔记](../solutions/1601-1700/1689-partitioning-into-minimum-number-of-deci-binary-numbers.md)

#### 等价转换
模板：

```python
# 待补充
```

模板题目：

- 0049 - 字母异位词分组 ｜ [LeetCode 链接](https://leetcode.cn/problems/group-anagrams/) ｜ [题解笔记](../solutions/0001-0100/0049-group-anagrams.md)

#### 逆向思维
模板：

```python
# 待补充
```

模板题目：

待补充...

#### 贡献法
模板：

```python
# 待补充
```

模板题目：

待补充...

#### 两次扫描
模板：

```python
# 待补充
```

模板题目：

- 0135 - 分发糖果 ｜ [LeetCode 链接](https://leetcode.cn/problems/candy/) ｜ [题解笔记](../solutions/0101-0200/0135-candy.md)

#### 分类讨论
模板：

```python
# 待补充
```

模板题目：

- 0860 - 柠檬水找零 ｜ [LeetCode 链接](https://leetcode.cn/problems/lemonade-change/) ｜ [题解笔记](../solutions/0801-0900/0860-lemonade-change.md)
- 3863 - 将一个字符串排序的最小操作次数 ｜ [LeetCode 链接](https://leetcode.cn/problems/minimum-operations-to-sort-a-string/) ｜ [题解笔记](../solutions/3801-3900/3863-minimum-operations-to-sort-a-string.md)

### 构造题
#### 对角线构造
模板：

```python
# 待补充
```

模板题目：

- 1980 - 找出不同的二进制字符串 ｜ [LeetCode 链接](https://leetcode.cn/problems/find-unique-binary-string/) ｜ [题解笔记](../solutions/1901-2000/1980-find-unique-binary-string.md)

### 交互题
待补充...

### 其他
待补充...
