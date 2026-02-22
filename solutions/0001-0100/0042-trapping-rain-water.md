---
id: 42
title: Trapping Rain Water
difficulty: Hard
tags: [stack, array, two-pointers, dynamic-programming, monotonic-stack]
created: 2026-02-20
---

# 42. 接雨水

## 题目链接
https://leetcode.cn/problems/trapping-rain-water/

## 题目描述
<p>给定&nbsp;<code>n</code> 个非负整数表示每个宽度为 <code>1</code> 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。</p>

<p><strong>示例 1：</strong></p>

<p><img src="https://assets.leetcode.cn/aliyun-lc-upload/uploads/2018/10/22/rainwatertrap.png" style="height: 161px; width: 412px;" /></p>

<pre>
<strong>输入：</strong>height = [0,1,0,2,1,0,1,3,2,1,2,1]
<strong>输出：</strong>6
<strong>解释：</strong>上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。 
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>height = [4,2,0,3,2,5]
<strong>输出：</strong>9
</pre>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == height.length</code></li>
	<li><code>1 &lt;= n &lt;= 2 * 10<sup>4</sup></code></li>
	<li><code>0 &lt;= height[i] &lt;= 10<sup>5</sup></code></li>
</ul>


## 解题思路

使用单调递减栈存下标。遍历到 `i` 时，如果 `height[i]` 大于栈顶高度，说明出现了右边界；弹出的元素是“凹槽底部”，新的栈顶是左边界。三者确定后可以计算本次能接的水量：

`宽度 = i - left - 1`，`高度 = min(height[left], height[i]) - height[mid]`。

把每次贡献累加即可。每个下标最多入栈和出栈一次，因此是线性复杂度。

- 时间复杂度: $O(n)$

- 空间复杂度: $O(n)$

## 相关专题
- [单调栈](../../topics/monotonic-stack.md)

## 代码
```cpp
class Solution {
public:
    int trap(vector<int>& height) {
        int n = height.size();
        vector<int> stk;
        stk.reserve(n);
        int ans = 0;

        for (int i = 0; i < n; ++i) {
            while (!stk.empty() && height[i] > height[stk.back()]) {
                int mid = stk.back();
                stk.pop_back();
                if (stk.empty()) {
                    break;
                }
                int left = stk.back();
                int w = i - left - 1;
                int h = min(height[left], height[i]) - height[mid];
                if (h > 0) {
                    ans += w * h;
                }
            }
            stk.push_back(i);
        }

        return ans;
    }
};
```

```python
class Solution:
    def trap(self, height: List[int]) -> int:
        stk = []
        ret = 0
        n = len(height)
        for i in range(n):
            while stk and height[stk[-1]] <= height[i]:
                # 单调栈：非空且栈顶 <= 当前值，需要弹出
                mid_idx = stk.pop()
                if stk: # 表示 mid_idx 左边有比他大的, 可以接水
                    left_idx = stk[-1]
                    l = i - left_idx -1
                    h = min(height[left_idx], height[i]) - height[mid_idx]
                    ret += l * h
                    # print(f"{l} * {h}, {ret}, ({left_idx}, {mid_idx}, {i})")
            stk.append(i)
        return ret
```
