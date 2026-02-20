---
id: 738
title: Monotone Increasing Digits
difficulty: Medium
tags: [greedy, math]
created: 2026-02-20
---

# 738. 单调递增的数字

## 题目链接
https://leetcode.cn/problems/monotone-increasing-digits/

## 题目描述
<p>当且仅当每个相邻位数上的数字&nbsp;<code>x</code>&nbsp;和&nbsp;<code>y</code>&nbsp;满足&nbsp;<code>x &lt;= y</code>&nbsp;时，我们称这个整数是<strong>单调递增</strong>的。</p>

<p>给定一个整数 <code>n</code> ，返回 <em>小于或等于 <code>n</code> 的最大数字，且数字呈 <strong>单调递增</strong></em> 。</p>

<p><strong>示例 1:</strong></p>

<pre>
<strong>输入:</strong> n = 10
<strong>输出:</strong> 9
</pre>

<p><strong>示例 2:</strong></p>

<pre>
<strong>输入:</strong> n = 1234
<strong>输出:</strong> 1234
</pre>

<p><strong>示例 3:</strong></p>

<pre>
<strong>输入:</strong> n = 332
<strong>输出:</strong> 299
</pre>

<p><strong>提示:</strong></p>

<ul>
	<li><code>0 &lt;= n &lt;= 10<sup>9</sup></code></li>
</ul>


## 解题思路

把数字转成字符串，从右向左扫描。一旦发现 `s[i-1] > s[i]`，说明从 `i-1` 开始不再单调，需要把 `s[i-1]` 减一，并记录位置 `mark=i`。继续向左扫描是为了处理连锁借位。

扫描完成后，把 `mark` 及其右侧全部改成 `'9'`，就得到不超过原数且尽可能大的单调递增数字。

- 时间复杂度: $O(m)$，`m` 是数字位数。
- 空间复杂度: $O(m)$，字符串存储。

## 代码
```cpp
#include <string>
using namespace std;

class Solution {
public:
    int monotoneIncreasingDigits(int n) {
        string s = to_string(n);
        int mark = static_cast<int>(s.size());
        for (int i = static_cast<int>(s.size()) - 1; i > 0; i--) {
            if (s[i - 1] > s[i]) {
                s[i - 1]--;
                mark = i;
            }
        }
        for (int i = mark; i < static_cast<int>(s.size()); i++) {
            s[i] = '9';
        }
        return stoi(s);
    }
};
```
