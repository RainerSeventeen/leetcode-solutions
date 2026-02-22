---
id: 93
title: Restore IP Addresses
difficulty: Medium
tags: [string, backtracking]
created: 2026-02-21
---

# 93. 复原 IP 地址

## 题目链接
https://leetcode.cn/problems/restore-ip-addresses/

## 题目描述
<p><strong>有效 IP 地址</strong> 正好由四个整数（每个整数位于 <code>0</code> 到 <code>255</code> 之间组成，且不能含有前导 <code>0</code>），整数之间用 <code>'.'</code> 分隔。</p>

<ul>
	<li>例如：<code>"0.1.2.201"</code> 和<code> "192.168.1.1"</code> 是 <strong>有效</strong> IP 地址，但是 <code>"0.011.255.245"</code>、<code>"192.168.1.312"</code> 和 <code>"192.168@1.1"</code> 是 <strong>无效</strong> IP 地址。</li>
</ul>

<p>给定一个只包含数字的字符串 <code>s</code> ，用以表示一个 IP 地址，返回所有可能的<strong>有效 IP 地址</strong>，这些地址可以通过在 <code>s</code> 中插入&nbsp;<code>'.'</code> 来形成。你 <strong>不能</strong>&nbsp;重新排序或删除 <code>s</code> 中的任何数字。你可以按 <strong>任何</strong> 顺序返回答案。</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>s = "25525511135"
<strong>输出：</strong>["255.255.11.135","255.255.111.35"]
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>s = "0000"
<strong>输出：</strong>["0.0.0.0"]
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>s = "101023"
<strong>输出：</strong>["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]
</pre>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 20</code></li>
	<li><code>s</code> 仅由数字组成</li>
</ul>


## 解题思路

用回溯切分字符串，路径里保存当前已经选择的 IP 段，段数超过 4 直接剪枝。
每次只接受合法段（长度不超过 3、无前导 0、数值在 `0~255`），凑满 4 段且恰好用完字符就加入答案。
- 时间复杂度: $O(3^4)$
- 空间复杂度: $O(4)$

## 相关专题
- [链表、树与回溯](../../topics/linked-list-tree-backtracking.md)

## 代码
```cpp
class Solution {
public:
    vector<string> restoreIpAddresses(string s) {
        auto start = s.begin();
        ret.clear();
        path.clear();
        traceback(s, start);
        return ret;
    }

    vector<string> ret;
    vector<int> path;
    void traceback(const string& s, string::iterator start) {
        if (path.size() > 4) return;
        if (path.size() == 4) {
            if (start >= s.end()) {
                string ip;
                for (int num : path) {
                    string str_num = to_string(num);
                    ip.append(str_num);
                    ip.append(".");
                }
                // 删除末尾
                ip.erase(ip.size() - 1);
                ret.push_back(ip);
            }
            return;
        }
        for (auto i = start + 1; i <= s.end(); i++) {
            if (isAddress(string(start, i))) {
                path.push_back(stoi(string(start, i)));
                traceback(s, i);
                path.pop_back();
            } else {
                continue;
            }
        }
    }
    bool isAddress (string s) {
        if (s.size() > 3) return false;
        if (s.size() != 1 && s[0] == '0') {
            // 前缀 0 
            return false;
        }
        int num = stoi(s);
        if (num < 256 && num >= 0)
            return true;
        return false;
    }
};
```
