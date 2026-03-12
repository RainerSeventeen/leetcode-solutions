# 二分算法（二分答案/最小化最大值/最大化最小值/第 K 小）

## 概览
二分算法通过维护单调区间，把线性试探降为对数复杂度，常用于有序数组定位边界、答案空间可行性判定，以及若干结构化变形问题。

## 核心思想
- 区间二分：在索引区间里持续缩小搜索范围，定位第一个/最后一个满足条件的位置。
- 答案二分：把“求最优值”转成 `check(mid)` 的单调判定问题。
- 二分前提：必须先明确单调性，再确定区间语义与循环不变量。

## 解题流程
1. 明确二分对象是“数组下标”还是“答案值域”。
2. 确定区间语义（开区间或闭区间），并在循环内保持一致。
3. 设计 `check` 并证明其单调性。
4. 用边界样例验证收敛与返回值是否对应题意。

## 模板与子方法
### 二分查找
#### 基础
模板：

```python
def lower_bound(nums, target):
    left, right = 0, len(nums)
    while left < right:
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left
```

模板题目：
- 0034 - 在排序数组中查找元素的第一个和最后一个位置 ｜ [LeetCode 链接](https://leetcode.cn/problems/find-first-and-last-position-of-element-in-sorted-array/) ｜ [题解笔记](../solutions/0001-0100/0034-find-first-and-last-position-of-element-in-sorted-array.md)
- 0035 - 搜索插入位置 ｜ [LeetCode 链接](https://leetcode.cn/problems/search-insert-position/) ｜ [题解笔记](../solutions/0001-0100/0035-search-insert-position.md)
- 0704 - 二分查找 ｜ [LeetCode 链接](https://leetcode.cn/problems/binary-search/) ｜ [题解笔记](../solutions/0701-0800/0704-binary-search.md)

#### 进阶
模板：

```python
# 常见做法：先排序，再在有序结构上做 lower_bound / upper_bound。
def binary_search_after_sort(nums, target):
    nums = sorted(nums)
    i = lower_bound(nums, target)
    return i if i < len(nums) and nums[i] == target else -1
```

模板题目：
待补充...

### 二分答案
#### 求最小
模板：

```python
def binary_search_min(left, right, check):
    # 循环不变量：check(left) == False, check(right) == True
    while left + 1 < right:
        mid = (left + right) // 2
        if check(mid):
            right = mid
        else:
            left = mid
    return right
```

模板题目：
待补充...

#### 求最大
模板：

```python
def binary_search_max(left, right, check):
    # 循环不变量：check(left) == True, check(right) == False
    while left + 1 < right:
        mid = (left + right) // 2
        if check(mid):
            left = mid
        else:
            right = mid
    return left
```

模板题目：
待补充...

#### 二分间接值
模板：

```python
# 通过把目标函数转写为单调判定，再做二分。
def binary_search_indirect(left, right, check):
    while left + 1 < right:
        mid = (left + right) // 2
        if check(mid):
            right = mid
        else:
            left = mid
    return right
```

模板题目：
待补充...

#### 最小化最大值
模板：

```python
def minimize_maximum(left, right, check):
    while left + 1 < right:
        mid = (left + right) // 2
        if check(mid):
            right = mid
        else:
            left = mid
    return right
```

模板题目：
待补充...

#### 最大化最小值
模板：

```python
def maximize_minimum(left, right, check):
    while left + 1 < right:
        mid = (left + right) // 2
        if check(mid):
            left = mid
        else:
            right = mid
    return left
```

模板题目：
- 3600 - 升级后最大生成树稳定性 ｜ [LeetCode 链接](https://leetcode.cn/problems/maximize-spanning-tree-stability-with-upgrades/) ｜ [题解笔记](../solutions/3501-3600/3600-maximize-spanning-tree-stability-with-upgrades.md)

#### 第 K 小/大
模板：

```python
# 典型写法：二分值域，统计 <= mid 的元素个数。
def kth_by_binary_search(left, right, count_leq, k):
    while left + 1 < right:
        mid = (left + right) // 2
        if count_leq(mid) >= k:
            right = mid
        else:
            left = mid
    return right
```

模板题目：
待补充...

### 三分法
待补充...

### 其他
#### 常见二分变形
模板：

```python
# 旋转数组、峰值、矩阵等问题，核心仍是维护可判定区间。
def binary_search_variant(left, right, decide):
    while left <= right:
        mid = (left + right) // 2
        step = decide(mid)
        if step == 0:
            return mid
        if step < 0:
            right = mid - 1
        else:
            left = mid + 1
    return -1
```

模板题目：
- 0004 - 寻找两个正序数组的中位数 ｜ [LeetCode 链接](https://leetcode.cn/problems/median-of-two-sorted-arrays/) ｜ [题解笔记](../solutions/0001-0100/0004-median-of-two-sorted-arrays.md)
- 0033 - 搜索旋转排序数组 ｜ [LeetCode 链接](https://leetcode.cn/problems/search-in-rotated-sorted-array/) ｜ [题解笔记](../solutions/0001-0100/0033-search-in-rotated-sorted-array.md)
- 0069 - x 的平方根 ｜ [LeetCode 链接](https://leetcode.cn/problems/sqrtx/) ｜ [题解笔记](../solutions/0001-0100/0069-sqrtx.md)

### 关联题单
待补充...

### 算法题单
待补充...

## 易错点
- 区间语义混用会导致死循环或漏解。
- 二分答案未证明单调性时，`check` 可能不可用。
- 返回值与“第一个满足/最后一个满足”方向不一致时，结果会偏一位。

## 总结
二分题的关键不是模板记忆，而是先建立单调性与循环不变量，再选择与题意一致的返回边界。
