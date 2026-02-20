# 回溯算法

回溯算法是暴力搜索的一种实现方式，本质是通过递归在解空间树中做“试探 - 撤销 - 再试探”。

## 1 解题步骤

回溯算法可以抽象成**递归** + **`for` 循环**。集合大小决定树的宽度，递归层数决定树的深度。

回溯算法三部曲：

1. 设计递归函数参数：通常围绕路径、起点、剩余目标等状态展开。
2. 写终止条件：达到目标或无法继续时，收集结果或直接返回。
3. 写单层搜索：在当前层通过 `for` 循环枚举选择，进入下一层后再撤销状态。

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

## 2 题目选取

### 2.1 组合与去重相关题目

- 0040 - 组合总和 II ｜ [LeetCode 链接](https://leetcode.cn/problems/combination-sum-ii/) ｜ [题解笔记](../solutions/0001-0100/0040-combination-sum-ii.md)

### 2.2 字符串分割相关题目

- 0131 - 分割回文串 ｜ [LeetCode 链接](https://leetcode.cn/problems/palindrome-partitioning/) ｜ [题解笔记](../solutions/0101-0200/0131-palindrome-partitioning.md)

### 2.3 子序列去重相关题目

- 0491 - 非递减子序列 ｜ [LeetCode 链接](https://leetcode.cn/problems/non-decreasing-subsequences/) ｜ [题解笔记](../solutions/0401-0500/0491-non-decreasing-subsequences.md)

### 2.4 全排列去重相关题目

- 0047 - 全排列 II ｜ [LeetCode 链接](https://leetcode.cn/problems/permutations-ii/) ｜ [题解笔记](../solutions/0001-0100/0047-permutations-ii.md)

## 3 总结

### 3.1 什么时候需要 `startIndex`？

当问题是“组合 / 子集”这类只允许向后选择元素的场景时，通常需要 `startIndex` 控制下一层的起点，避免重复使用前面的元素。

### 3.2 纵向横向去重分别怎么实现？

#### 3.2.1 纵向

纵向去重通常针对“同一路径上同一位置不能重复使用”的场景，常见做法是使用 `used` 记录当前路径上已选择的下标。

```cpp
vector<bool> used;

void backtrace() {
    if (...) {
        return;
    }
    for (int i = 0; i < value.size(); i++) {
        if (used[i]) continue;
        used[i] = true;
        backtrace();
        used[i] = false;
    }
}
```

#### 3.2.2 横向

横向去重针对“同一层不要重复起点”的场景，通常需要先排序，再在同层用条件跳过重复值。
