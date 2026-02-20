# 回溯算法

回溯算法是暴力搜索的一种实现方式，本质是通过递归在解空间树中做”试探 - 撤销 - 再试探”。

## 1 概览

回溯算法可以抽象成**递归** + **`for` 循环**。集合大小决定树的宽度，递归层数决定树的深度。

## 2 核心思想

回溯算法三部曲：

1. 设计递归函数参数：通常围绕路径、起点、剩余目标等状态展开。
2. 写终止条件：达到目标或无法继续时，收集结果或直接返回。
3. 写单层搜索：在当前层通过 `for` 循环枚举选择，进入下一层后再撤销状态。

## 3 解题流程

```cpp
void backtracking(参数) {
    if (终止条件) {
        存放结果;
        return;
    }
    for (选择 : 本层集合中的元素) {
        处理节点;
        backtracking(路径, 选择列表); // 递归
        回溯，撤销处理结果;
    }
}
```

## 4 模板与子方法

### 4.1 子方法 A：使用 startIndex（组合/子集问题）

#### 4.1.1 方法说明

当问题是”组合 / 子集”这类只允许向后选择元素的场景时，使用 `startIndex` 控制下一层的起点，避免重复使用前面的元素。同时利用**横向去重**（先排序，再在同层跳过重复值）来去除重复组合。

#### 4.1.2 模板代码

```cpp
void backtracking(int startIndex) {
    if (终止条件) {
        存放结果;
        return;
    }
    for (int i = startIndex; i < value.size(); i++) {
        // 横向去重
        if (i > startIndex && value[i] == value[i-1]) continue;
        处理节点;
        backtracking(i + 1);
        回溯，撤销处理结果;
    }
}
```

#### 4.1.3 模板题目

- 0039 - 组合总和 ｜ [LeetCode 链接](https://leetcode.cn/problems/combination-sum/) ｜ [题解笔记](../solutions/0001-0100/0039-combination-sum.md)
- 0040 - 组合总和 II ｜ [LeetCode 链接](https://leetcode.cn/problems/combination-sum-ii/) ｜ [题解笔记](../solutions/0001-0100/0040-combination-sum-ii.md)
- 0078 - Subsets ｜ [LeetCode 链接](https://leetcode.cn/problems/subsets/) ｜ [题解笔记](../solutions/0001-0100/0078-subsets.md)
- 0131 - 分割回文串 ｜ [LeetCode 链接](https://leetcode.cn/problems/palindrome-partitioning/) ｜ [题解笔记](../solutions/0101-0200/0131-palindrome-partitioning.md)

### 4.2 子方法 B：使用 used 数组（全排列/去重问题）

#### 4.2.1 方法说明

当问题是”全排列”这类允许循环选择元素但需要避免同一路径重复的场景时，使用 `used` 数组记录当前路径上已选择的下标。同时利用**纵向去重**（排序后检查前一个元素是否使用过）来去除重复排列。

#### 4.2.2 模板代码

```cpp
vector<bool> used;

void backtracking() {
    if (终止条件) {
        存放结果;
        return;
    }
    for (int i = 0; i < value.size(); i++) {
        // 纵向去重
        if (i > 0 && value[i] == value[i-1] && !used[i-1]) continue;
        if (used[i]) continue;
        used[i] = true;
        处理节点;
        backtracking();
        回溯，撤销处理结果;
        used[i] = false;
    }
}
```

#### 4.2.3 模板题目

- 0046 - 全排列 ｜ [LeetCode 链接](https://leetcode.cn/problems/permutations/) ｜ [题解笔记](../solutions/0001-0100/0046-permutations.md)
- 0047 - 全排列 II ｜ [LeetCode 链接](https://leetcode.cn/problems/permutations-ii/) ｜ [题解笔记](../solutions/0001-0100/0047-permutations-ii.md)
- 0491 - 非递减子序列 ｜ [LeetCode 链接](https://leetcode.cn/problems/non-decreasing-subsequences/) ｜ [题解笔记](../solutions/0401-0500/0491-non-decreasing-subsequences.md)

### 4.3 子方法 C：最少删除与合法性约束

#### 4.3.1 方法说明

当问题要求在最少操作次数下生成所有合法结果时，可以先计算必须删除的数量，再通过回溯枚举删除位置，并结合去重与合法性校验剪枝。

#### 4.3.2 模板题目

- 0301 - 删除无效的括号 ｜ [LeetCode 链接](https://leetcode.cn/problems/remove-invalid-parentheses/) ｜ [题解笔记](../solutions/0301-0400/0301-remove-invalid-parentheses.md)


### 4.4 字符串回溯相关题目

- 0017 - 电话号码的字母组合 ｜ [LeetCode 链接](https://leetcode.cn/problems/letter-combinations-of-a-phone-number/) ｜ [题解笔记](../solutions/0001-0100/0017-letter-combinations-of-a-phone-number.md)
- 0022 - 括号生成 ｜ [LeetCode 链接](https://leetcode.cn/problems/generate-parentheses/) ｜ [题解笔记](../solutions/0001-0100/0022-generate-parentheses.md)
- 0079 - Word Search ｜ [LeetCode 链接](https://leetcode.cn/problems/word-search/) ｜ [题解笔记](../solutions/0001-0100/0079-word-search.md)
## 5 易错点

1. **横向去重 vs 纵向去重混淆**：横向去重在同一层跳过重复值（组合问题），纵向去重在同一路径不同层检查前驱节点（排列问题）
2. **startIndex 的作用边界**：使用 startIndex 时，下一层应该传 `i + 1`，不能从 0 开始重新遍历
3. **去重前必须排序**：无论横向还是纵向去重，都需要先对输入数组排序才能生效
4. **撤销状态易忘记**：回溯时需要恢复路径、used 数组等所有被修改的状态

## 6 总结

- 使用 **startIndex** 解决组合/子集问题，配合**横向去重**
- 使用 **used 数组**解决全排列问题，配合**纵向去重**
- 始终记住”试探 - 递归 - 撤销”的完整节奏
