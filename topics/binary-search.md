# 二分查找

## 1 概览
二分查找用于有序数据或满足单调性的判定函数，目标是把线性试探降到对数复杂度。

## 2 核心思想
- 区间二分：在有序区间内定位边界或目标。
- 答案二分：在解空间上二分可行性。
- 结构二分：如旋转数组、分割二分等特殊有序结构。

## 3 解题流程
1. 明确二分对象：索引区间还是答案区间。
2. 选定区间语义 `[l, r)` 或 `[l, r]`，全程保持一致。
3. 写单调谓词并证明“真区间/假区间”单调。
4. 用极小数据验证边界收敛与返回值。

## 4 模板与子方法
### 4.1 边界二分（lower_bound / upper_bound）
方法说明：
适用于“第一个大于等于”“最后一个小于等于”等边界查询。

模板代码：
```python
def lower_bound(nums, target):
    l, r = 0, len(nums)
    while l < r:
        m = (l + r) // 2
        if nums[m] < target:
            l = m + 1
        else:
            r = m
    return l
```

#### 4.1.1 模板题目
- 0034 - 在排序数组中查找元素的第一个和最后一个位置 ｜ [LeetCode 链接](https://leetcode.cn/problems/find-first-and-last-position-of-element-in-sorted-array/) ｜ [题解笔记](../solutions/0001-0100/0034-find-first-and-last-position-of-element-in-sorted-array.md)
- 0035 - 搜索插入位置 ｜ [LeetCode 链接](https://leetcode.cn/problems/search-insert-position/) ｜ [题解笔记](../solutions/0001-0100/0035-search-insert-position.md)
- 0069 - x 的平方根 ｜ [LeetCode 链接](https://leetcode.cn/problems/sqrtx/) ｜ [题解笔记](../solutions/0001-0100/0069-sqrtx.md)
- 0209 - 长度最小的子数组 ｜ [LeetCode 链接](https://leetcode.cn/problems/minimum-size-subarray-sum/) ｜ [题解笔记](../solutions/0201-0300/0209-minimum-size-subarray-sum.md)
- 0349 - 两个数组的交集 ｜ [LeetCode 链接](https://leetcode.cn/problems/intersection-of-two-arrays/) ｜ [题解笔记](../solutions/0301-0400/0349-intersection-of-two-arrays.md)
- 0367 - 有效的完全平方数 ｜ [LeetCode 链接](https://leetcode.cn/problems/valid-perfect-square/) ｜ [题解笔记](../solutions/0301-0400/0367-valid-perfect-square.md)
- 0792 - 二分查找 ｜ [LeetCode 链接](https://leetcode.cn/problems/binary-search/) ｜ [题解笔记](../solutions/0701-0800/0792-binary-search.md)
### 4.2 旋转数组二分
方法说明：
适用于局部有序的旋转数组，先判断哪半边有序，再判目标是否落在有序半边。

模板代码：
```python
def search_rotated(nums, target):
    l, r = 0, len(nums) - 1
    while l <= r:
        m = (l + r) // 2
        if nums[m] == target:
            return m
        if nums[l] <= nums[m]:
            if nums[l] <= target < nums[m]:
                r = m - 1
            else:
                l = m + 1
        else:
            if nums[m] < target <= nums[r]:
                l = m + 1
            else:
                r = m - 1
    return -1
```

#### 4.2.1 模板题目
- 0033 - 搜索旋转排序数组 ｜ [LeetCode 链接](https://leetcode.cn/problems/search-in-rotated-sorted-array/) ｜ [题解笔记](../solutions/0001-0100/0033-search-in-rotated-sorted-array.md)
### 4.3 分割二分
方法说明：
适用于在两个有序结构上找分割点。实现要点是让左半部分长度固定并检查边界关系。

模板代码：
```python
def find_median_sorted_arrays(a, b):
    if len(a) > len(b):
        a, b = b, a
    m, n = len(a), len(b)
    l, r = 0, m
    while l <= r:
        i = (l + r) // 2
        j = (m + n + 1) // 2 - i
        al = float('-inf') if i == 0 else a[i - 1]
        ar = float('inf') if i == m else a[i]
        bl = float('-inf') if j == 0 else b[j - 1]
        br = float('inf') if j == n else b[j]
        if al <= br and bl <= ar:
            if (m + n) % 2:
                return max(al, bl)
            return (max(al, bl) + min(ar, br)) / 2
        if al > br:
            r = i - 1
        else:
            l = i + 1
```

#### 4.3.1 模板题目
- 0004 - Median of Two Sorted Arrays ｜ [LeetCode 链接](https://leetcode.cn/problems/median-of-two-sorted-arrays/) ｜ [题解笔记](../solutions/0001-0100/0004-median-of-two-sorted-arrays.md)
### 4.4 答案二分（可行性判定）
方法说明：
把“求最小/最大满足值”转成判定函数。`0287` 在本专题是交叉做法，主模板也可用快慢指针。

模板代码：
```python
def binary_search_answer(lo, hi, ok):
    while lo < hi:
        mid = (lo + hi) // 2
        if ok(mid):
            hi = mid
        else:
            lo = mid + 1
    return lo
```

#### 4.4.1 模板题目
- 0287 - 寻找重复数 ｜ [LeetCode 链接](https://leetcode.cn/problems/find-the-duplicate-number/) ｜ [题解笔记](../solutions/0201-0300/0287-find-the-duplicate-number.md)
- 0240 - 搜索二维矩阵 II ｜ [LeetCode 链接](https://leetcode.cn/problems/search-a-2d-matrix-ii/) ｜ [题解笔记](../solutions/0201-0300/0240-search-a-2d-matrix-ii.md)
## 5 易错点
- 区间语义混用导致死循环或越界。
- 返回值错位（返回 `l` 还是 `l-1`）与题意不一致。
- 答案二分未证明单调性。

## 6 总结
二分的本质是维护单调区间并不断缩小搜索空间，先确定区间语义与单调谓词，再编码。
