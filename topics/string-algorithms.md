# 字符串算法

## 1 概览
字符串算法涵盖匹配、回文、括号、解码与字符串动态规划，常与窗口、栈、DP、回溯交叉。

## 2 核心思想
- 匹配类依赖状态转移和边界处理。
- 回文类常用中心扩展或区间 DP。
- 括号类可用栈或 DP 维护有效区间。
- 扫描类常结合滑动窗口与计数器。

## 3 解题流程
1. 确认目标：匹配、计数、最值或构造。
2. 选择模型：DP、栈、窗口、回溯。
3. 统一下标语义与初始化。
4. 用短串样例验证转移与边界。

## 4 模板与子方法
### 4.1 编辑距离与二维匹配 DP
方法说明：
适用于插删改代价最小化与字符匹配问题。与动态规划专题交叉但核心对象是字符串。

模板代码：
```python
def edit_distance(a, b):
    m, n = len(a), len(b)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
    return dp[m][n]
```

#### 4.1.1 模板题目
- 0072 - 编辑距离 ｜ [LeetCode 链接](https://leetcode.cn/problems/edit-distance/) ｜ [题解笔记](../solutions/0001-0100/0072-edit-distance.md)
- 0010 - Regular Expression Matching ｜ [LeetCode 链接](https://leetcode.cn/problems/regular-expression-matching/) ｜ [题解笔记](../solutions/0001-0100/0010-regular-expression-matching.md)
- 0139 - 单词拆分 ｜ [LeetCode 链接](https://leetcode.cn/problems/word-break/) ｜ [题解笔记](../solutions/0101-0200/0139-word-break.md)
### 4.2 回文字符串
方法说明：
可用中心扩展或区间 DP 统计/求最长回文。回文切分类题可交叉回溯专题。

模板代码：
```python
def count_substrings(s):
    n = len(s)
    ans = 0
    for c in range(2 * n - 1):
        l = c // 2
        r = l + c % 2
        while l >= 0 and r < n and s[l] == s[r]:
            ans += 1
            l -= 1
            r += 1
    return ans
```

#### 4.2.1 模板题目
- 0005 - Longest Palindromic Substring ｜ [LeetCode 链接](https://leetcode.cn/problems/longest-palindromic-substring/) ｜ [题解笔记](../solutions/0001-0100/0005-longest-palindromic-substring.md)
- 0647 - 回文子串 ｜ [LeetCode 链接](https://leetcode.cn/problems/palindromic-substrings/) ｜ [题解笔记](../solutions/0601-0700/0647-palindromic-substrings.md)
- 0131 - 分割回文串 ｜ [LeetCode 链接](https://leetcode.cn/problems/palindrome-partitioning/) ｜ [题解笔记](../solutions/0101-0200/0131-palindrome-partitioning.md)
### 4.3 括号与栈/DP
方法说明：
括号合法性与最长有效区间可用栈或 DP。删除无效括号常转为回溯/BFS 搜索。

模板代码：
```python
def longest_valid_parentheses(s):
    st = [-1]
    ans = 0
    for i, ch in enumerate(s):
        if ch == '(':
            st.append(i)
        else:
            st.pop()
            if not st:
                st.append(i)
            else:
                ans = max(ans, i - st[-1])
    return ans
```

#### 4.3.1 模板题目
- 0022 - 括号生成 ｜ [LeetCode 链接](https://leetcode.cn/problems/generate-parentheses/) ｜ [题解笔记](../solutions/0001-0100/0022-generate-parentheses.md)
- 0032 - 最长有效括号 ｜ [LeetCode 链接](https://leetcode.cn/problems/longest-valid-parentheses/) ｜ [题解笔记](../solutions/0001-0100/0032-longest-valid-parentheses.md)
- 0301 - 删除无效的括号 ｜ [LeetCode 链接](https://leetcode.cn/problems/remove-invalid-parentheses/) ｜ [题解笔记](../solutions/0301-0400/0301-remove-invalid-parentheses.md)
- 0761 - 特殊的二进制字符串 ｜ [LeetCode 链接](https://leetcode.cn/problems/special-binary-string/) ｜ [题解笔记](../solutions/0701-0800/0761-special-binary-string.md)
### 4.4 字符串栈与解码
方法说明：
分层结构可用双栈或递归下降解析，遇到 `]` 回收一层。

模板代码：
```python
def decode_string(s):
    num_st, str_st = [], []
    cur_num, cur = 0, ""
    for ch in s:
        if ch.isdigit():
            cur_num = cur_num * 10 + int(ch)
        elif ch == '[':
            num_st.append(cur_num)
            str_st.append(cur)
            cur_num, cur = 0, ""
        elif ch == ']':
            k = num_st.pop()
            cur = str_st.pop() + cur * k
        else:
            cur += ch
    return cur
```

#### 4.4.1 模板题目
- 0394 - 字符串解码 ｜ [LeetCode 链接](https://leetcode.cn/problems/decode-string/) ｜ [题解笔记](../solutions/0301-0400/0394-decode-string.md)
### 4.5 滑动窗口字符串匹配
方法说明：
以字符频次为约束维护窗口，主方法在双指针专题，这里作为字符串视角交叉模板。

模板代码：
```python
from collections import Counter


def find_anagrams(s, p):
    need = Counter(p)
    miss = len(p)
    l = 0
    ans = []
    for r, ch in enumerate(s):
        if need[ch] > 0:
            miss -= 1
        need[ch] -= 1
        if r - l + 1 > len(p):
            need[s[l]] += 1
            if need[s[l]] > 0:
                miss += 1
            l += 1
        if miss == 0:
            ans.append(l)
    return ans
```

#### 4.5.1 模板题目
- 0003 - Longest Substring Without Repeating Characters ｜ [LeetCode 链接](https://leetcode.cn/problems/longest-substring-without-repeating-characters/) ｜ [题解笔记](../solutions/0001-0100/0003-longest-substring-without-repeating-characters.md)
- 0076 - Minimum Window Substring ｜ [LeetCode 链接](https://leetcode.cn/problems/minimum-window-substring/) ｜ [题解笔记](../solutions/0001-0100/0076-minimum-window-substring.md)
- 0438 - 找到字符串中所有字母异位词 ｜ [LeetCode 链接](https://leetcode.cn/problems/find-all-anagrams-in-a-string/) ｜ [题解笔记](../solutions/0401-0500/0438-find-all-anagrams-in-a-string.md)
- 4137 - 前缀连接组的数目 ｜ [LeetCode 链接](https://leetcode.cn/problems/number-of-prefix-connected-groups/) ｜ [题解笔记](../solutions/4101-4200/4137-number-of-prefix-connected-groups.md)
- 4216 - 带权单词映射 ｜ [LeetCode 链接](https://leetcode.cn/problems/weighted-word-mapping/) ｜ [题解笔记](../solutions/4201-4300/4216-weighted-word-mapping.md)
### 4.6 回溯生成字符串组合
方法说明：
字符串枚举类题常用 DFS 构造路径，适合组合生成与约束搜索。

模板代码：
```python
def letter_combinations(digits, mp):
    if not digits:
        return []
    ans, path = [], []

    def dfs(i):
        if i == len(digits):
            ans.append(''.join(path))
            return
        for ch in mp[digits[i]]:
            path.append(ch)
            dfs(i + 1)
            path.pop()
```

#### 4.6.1 模板题目
- 0017 - 电话号码的字母组合 ｜ [LeetCode 链接](https://leetcode.cn/problems/letter-combinations-of-a-phone-number/) ｜ [题解笔记](../solutions/0001-0100/0017-letter-combinations-of-a-phone-number.md)
## 5 易错点
- 字符串下标与 DP 下标错位。
- 回文 DP 遍历方向错误。
- 窗口计数更新先后顺序颠倒。

## 6 总结
字符串题先选模型再统一下标语义，DP、栈、窗口、回溯四类模板能覆盖大多数场景。
