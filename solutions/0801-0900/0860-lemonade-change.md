---
id: 860
title: Lemonade Change
difficulty: Easy
tags: [greedy, array]
created: 2026-02-21
---

# 860. 柠檬水找零

## 题目链接
https://leetcode.cn/problems/lemonade-change/

## 题目描述
<p>在柠檬水摊上，每一杯柠檬水的售价为&nbsp;<code>5</code>&nbsp;美元。顾客排队购买你的产品，（按账单 <code>bills</code> 支付的顺序）一次购买一杯。</p>

<p>每位顾客只买一杯柠檬水，然后向你付 <code>5</code> 美元、<code>10</code> 美元或 <code>20</code> 美元。你必须给每个顾客正确找零，也就是说净交易是每位顾客向你支付 <code>5</code> 美元。</p>

<p>注意，一开始你手头没有任何零钱。</p>

<p>给你一个整数数组 <code>bills</code> ，其中 <code>bills[i]</code> 是第 <code>i</code> 位顾客付的账。如果你能给每位顾客正确找零，返回&nbsp;<code>true</code>&nbsp;，否则返回 <code>false</code>&nbsp;。</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>bills = [5,5,5,10,20]
<strong>输出：</strong>true
<strong>解释：
</strong>前 3 位顾客那里，我们按顺序收取 3 张 5 美元的钞票。
第 4 位顾客那里，我们收取一张 10 美元的钞票，并返还 5 美元。
第 5 位顾客那里，我们找还一张 10 美元的钞票和一张 5 美元的钞票。
由于所有客户都得到了正确的找零，所以我们输出 true。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>bills = [5,5,10,10,20]
<strong>输出：</strong>false
<strong>解释：</strong>
前 2 位顾客那里，我们按顺序收取 2 张 5 美元的钞票。
对于接下来的 2 位顾客，我们收取一张 10 美元的钞票，然后返还 5 美元。
对于最后一位顾客，我们无法退回 15 美元，因为我们现在只有两张 10 美元的钞票。
由于不是每位顾客都得到了正确的找零，所以答案是 false。
</pre>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= bills.length &lt;= 10<sup>5</sup></code></li>
	<li><code>bills[i]</code>&nbsp;不是&nbsp;<code>5</code>&nbsp;就是&nbsp;<code>10</code>&nbsp;或是&nbsp;<code>20</code>&nbsp;</li>
</ul>


## 解题思路

维护手里 5 元和 10 元的数量，按顾客顺序模拟找零过程。
遇到 20 元时优先使用 `10+5`，否则尝试 `5+5+5`，任一步无法找零则直接返回 `false`。
- 时间复杂度: $O(n)$
- 空间复杂度: $O(1)$

## 相关专题
- [贪心与思维](../../topics/greedy-and-thinking.md)

## 代码
```cpp
class Solution {
public:
    bool lemonadeChange(vector<int>& bills) {
        // 分析所有的情况
        // 1. 5 不用找
        // 2. 10 至少之前要有个 5
        // 3. 20 至少前面要有个 10 + 5 或者 3 个 5
        vector<int> now(2, 0);
        for (int i = 0; i < bills.size(); i++) {
            switch (bills[i]) {
            case 5:
                now[0]++;
                break;
            case 10:
                now[0]--;
                now[1]++;
                if (now[0] < 0) return false;
                break;
            case 20:
                if (now[0] > 0 && now[1] > 0) {
                    now[0]--;
                    now[1]--;
                } else if (now[0] > 2) {
                    now[0] -= 3;
                } else {
                    return false;
                }
                break;
            }
        
        }
        return true;
    }


};
```
