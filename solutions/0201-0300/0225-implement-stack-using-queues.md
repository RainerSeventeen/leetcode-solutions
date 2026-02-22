---
id: 225
title: Implement Stack using Queues
difficulty: Easy
tags: [stack, design, queue]
created: 2026-02-21
---

# 225. 用队列实现栈

## 题目链接
https://leetcode.cn/problems/implement-stack-using-queues/

## 题目描述
<p>请你仅使用两个队列实现一个后入先出（LIFO）的栈，并支持普通栈的全部四种操作（<code>push</code>、<code>top</code>、<code>pop</code> 和 <code>empty</code>）。</p>

<p>实现 <code>MyStack</code> 类：</p>

<ul>
	<li><code>void push(int x)</code> 将元素 x 压入栈顶。</li>
	<li><code>int pop()</code> 移除并返回栈顶元素。</li>
	<li><code>int top()</code> 返回栈顶元素。</li>
	<li><code>boolean empty()</code> 如果栈是空的，返回 <code>true</code> ；否则，返回 <code>false</code> 。</li>
</ul>

<p><strong>注意：</strong></p>

<ul>
	<li>你只能使用队列的标准操作 —— 也就是&nbsp;<code>push to back</code>、<code>peek/pop from front</code>、<code>size</code> 和&nbsp;<code>is empty</code>&nbsp;这些操作。</li>
	<li>你所使用的语言也许不支持队列。&nbsp;你可以使用 list （列表）或者 deque（双端队列）来模拟一个队列&nbsp;, 只要是标准的队列操作即可。</li>
</ul>

<p><strong>示例：</strong></p>

<pre>
<strong>输入：</strong>
["MyStack", "push", "push", "top", "pop", "empty"]
[[], [1], [2], [], [], []]
<strong>输出：</strong>
[null, null, null, 2, 2, false]

<strong>解释：</strong>
MyStack myStack = new MyStack();
myStack.push(1);
myStack.push(2);
myStack.top(); // 返回 2
myStack.pop(); // 返回 2
myStack.empty(); // 返回 False
</pre>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= x &lt;= 9</code></li>
	<li>最多调用<code>100</code> 次 <code>push</code>、<code>pop</code>、<code>top</code> 和 <code>empty</code></li>
	<li>每次调用 <code>pop</code> 和 <code>top</code> 都保证栈不为空</li>
</ul>

<p><strong>进阶：</strong>你能否仅用一个队列来实现栈。</p>


## 解题思路

维护两个队列：`q1` 存当前数据，`q2` 作为中转。
`pop/top` 时把 `q1` 前 `n-1` 个元素搬到 `q2`，最后一个即栈顶，再交换两个队列。
- 时间复杂度: $O(n)$
- 空间复杂度: $O(n)$

## 相关专题
- [常用数据结构](../../topics/common-data-structures.md)

## 代码
```cpp
#include <queue>
using namespace std;

class MyStack {
public:
    queue<int> q1, q2;

    void push(int x) {
        q1.push(x);
    }

    int pop() {
        while (q1.size() > 1) {
            q2.push(q1.front());
            q1.pop();
        }
        int ret = q1.front();
        q1.pop();
        // 全部移动后，直接使用 swap 交换指针
        swap(q1, q2);
        return ret;
    }

    int top() {
        while (q1.size() > 1) {
            q2.push(q1.front());
            q1.pop();
        }
        int ret = q1.front();
        q1.pop();
        q2.push(ret);
        swap(q1, q2);
        return ret;
    }

    bool empty() {
        return q1.empty();
    }
};
```
