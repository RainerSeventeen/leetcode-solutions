---
id: 202
title: Happy Number
difficulty: Easy
tags: [hash-table, math, two-pointers]
created: 2026-02-21
---

# 202. 快乐数

## 题目链接
https://leetcode.cn/problems/happy-number/

## 题目描述
<p>编写一个算法来判断一个数 <code>n</code> 是不是快乐数。</p>

<p><strong>「快乐数」</strong>&nbsp;定义为：</p>

<ul>
	<li>对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和。</li>
	<li>然后重复这个过程直到这个数变为 1，也可能是 <strong>无限循环</strong> 但始终变不到 1。</li>
	<li>如果这个过程 <strong>结果为</strong>&nbsp;1，那么这个数就是快乐数。</li>
</ul>

<p>如果 <code>n</code> 是 <em>快乐数</em> 就返回 <code>true</code> ；不是，则返回 <code>false</code> 。</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>n = 19
<strong>输出：</strong>true
<strong>解释：
</strong>1<sup>2</sup> + 9<sup>2</sup> = 82
8<sup>2</sup> + 2<sup>2</sup> = 68
6<sup>2</sup> + 8<sup>2</sup> = 100
1<sup>2</sup> + 0<sup>2</sup> + 0<sup>2</sup> = 1
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>n = 2
<strong>输出：</strong>false
</pre>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 2<sup>31</sup> - 1</code></li>
</ul>


## 解题思路

把数字反复替换为“各位平方和”，该过程要么进入 1，要么进入循环。
代码用快慢指针做判环：慢指针走一步，快指针走两步。
若最终相遇在 1 则是快乐数，否则说明落入非 1 的循环。
- 时间复杂度: $O(\log n)$
- 空间复杂度: $O(1)$

## 相关专题
- [滑动窗口与双指针](../../topics/sliding-window-and-two-pointers.md)

## 代码
```cpp
#include <unordered_set>
using namespace std;

class Solution {
public:
    bool isHappy(int n) {
        int slow = n, fast = n;
        do {
            slow = digitSquareSum(slow);                   // 走一步
            fast = digitSquareSum(digitSquareSum(fast));   // 走两步
        } while (slow != fast);
        return slow == 1;                                  // 相遇于1则快乐
    }

private:
    static int digitSquareSum(int x) {
        int s = 0;
        while (x > 0) {
            int d = x % 10;
            s += d * d;
            x /= 10;
        }
        return s;
    }
};
```
