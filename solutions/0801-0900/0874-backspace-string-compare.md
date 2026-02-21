---
id: 874
title: Backspace String Compare
difficulty: Easy
tags: [stack, two-pointers, string, simulation]
created: 2026-02-21
---

# 874. 比较含退格的字符串

## 题目链接
https://leetcode.cn/problems/backspace-string-compare/

## 题目描述
<p>给定 <code>s</code> 和 <code>t</code> 两个字符串，当它们分别被输入到空白的文本编辑器后，如果两者相等，返回 <code>true</code> 。<code>#</code> 代表退格字符。</p>

<p><strong>注意：</strong>如果对空文本输入退格字符，文本继续为空。</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>s = "ab#c", t = "ad#c"
<strong>输出：</strong>true
<strong>解释：</strong>s 和 t 都会变成 "ac"。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>s = "ab##", t = "c#d#"
<strong>输出：</strong>true
<strong>解释：</strong>s 和 t 都会变成 ""。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>s = "a#c", t = "b"
<strong>输出：</strong>false
<strong>解释：</strong>s 会变成 "c"，但 t 仍然是 "b"。</pre>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length, t.length &lt;= 200</code></li>
	<li><code>s</code> 和 <code>t</code> 只含有小写字母以及字符 <code>'#'</code></li>
</ul>

<p><strong>进阶：</strong></p>

<ul>
	<li>你可以用 <code>O(n)</code> 的时间复杂度和 <code>O(1)</code> 的空间复杂度解决该问题吗？</li>
</ul>


## 解题思路

分别对两个字符串做一次原地“退格模拟”：`fast` 读入字符，`slow` 写回有效字符。
读到普通字符就写入并前进，读到 `#` 就让 `slow` 回退一位（若可退）。
处理完后截断到有效长度，再比较两个结果串是否相同。
- 时间复杂度: $O(m+n)$
- 空间复杂度: $O(1)$

## 代码
```cpp
class Solution {
public:
    bool backspaceCompare(string s, string t) {
        get_str(s);
        get_str(t);
        return s == t;
    }


private:
    void get_str(string& s) {
        int slow = 0;
        int fast = 0;
        
        while (fast < s.length()) {
            s[slow] = s[fast];
            if (s[fast] == '#') {
                if (slow > 0)
                    slow--;
                fast++;
            } else {
                slow++;
                fast++;
            }   
        }
        s.resize(slow);  // 截断处理后的有效长度
    }
};
```
