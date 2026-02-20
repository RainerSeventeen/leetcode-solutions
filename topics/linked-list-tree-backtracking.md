# 链表、树与回溯

## 1 概览
本专题覆盖链表原地操作、二叉树递归/迭代、以及组合搜索回溯三大类高频模板。

## 2 核心思想
- 链表：靠指针重连与哑节点降低边界复杂度。
- 树：先定义递归返回语义，再做合并。
- 回溯：路径试探、约束剪枝、现场恢复。

## 3 解题流程
1. 判断是链表指针问题、树形递归问题还是回溯搜索问题。
2. 先写模板骨架（哑节点/DFS 返回值/回溯框架）。
3. 加上题目特有约束（去重、剪枝、边界）。
4. 用最小结构验证：空链表、单节点树、空路径。

## 4 模板与子方法
### 4.1 链表指针重连
方法说明：
适用于合并、反转、删除等原地操作，哑节点可统一头结点分支。

模板代码：
```python
def reverse_list(head):
    prev, cur = None, head
    while cur:
        nxt = cur.next
        cur.next = prev
        prev, cur = cur, nxt
    return prev
```

#### 4.1.1 模板题目
- 0002 - Add Two Numbers ｜ [LeetCode 链接](https://leetcode.cn/problems/add-two-numbers/) ｜ [题解笔记](../solutions/0001-0100/0002-add-two-numbers.md)
- 0019 - 删除链表的倒数第 N 个结点 ｜ [LeetCode 链接](https://leetcode.cn/problems/remove-nth-node-from-end-of-list/) ｜ [题解笔记](../solutions/0001-0100/0019-remove-nth-node-from-end-of-list.md)
- 0021 - 合并两个有序链表 ｜ [LeetCode 链接](https://leetcode.cn/problems/merge-two-sorted-lists/) ｜ [题解笔记](../solutions/0001-0100/0021-merge-two-sorted-lists.md)
- 0148 - 排序链表 ｜ [LeetCode 链接](https://leetcode.cn/problems/sort-list/) ｜ [题解笔记](../solutions/0101-0200/0148-sort-list.md)
- 0206 - Reverse Linked List ｜ [LeetCode 链接](https://leetcode.cn/problems/reverse-linked-list/) ｜ [题解笔记](../solutions/0201-0300/0206-reverse-linked-list.md)
- 0234 - Palindrome Linked List ｜ [LeetCode 链接](https://leetcode.cn/problems/palindrome-linked-list/) ｜ [题解笔记](../solutions/0201-0300/0234-palindrome-linked-list.md)
- 0023 - 合并 K 个升序链表 ｜ [LeetCode 链接](https://leetcode.cn/problems/merge-k-sorted-lists/) ｜ [题解笔记](../solutions/0001-0100/0023-merge-k-sorted-lists.md)
### 4.2 链表快慢指针
方法说明：
用于判环、找环入口、找相交点。该模板与双指针专题交叉。

模板代码：
```python
def has_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True
    return False
```

#### 4.2.1 模板题目
- 0141 - 环形链表 ｜ [LeetCode 链接](https://leetcode.cn/problems/linked-list-cycle/) ｜ [题解笔记](../solutions/0101-0200/0141-linked-list-cycle.md)
- 0142 - 环形链表 II ｜ [LeetCode 链接](https://leetcode.cn/problems/linked-list-cycle-ii/) ｜ [题解笔记](../solutions/0101-0200/0142-linked-list-cycle-ii.md)
- 0160 - 相交链表 ｜ [LeetCode 链接](https://leetcode.cn/problems/intersection-of-two-linked-lists/) ｜ [题解笔记](../solutions/0101-0200/0160-intersection-of-two-linked-lists.md)
### 4.3 树的基础 DFS 递归
方法说明：
适用于高度、镜像、合并、翻转等局部独立递归。先确定返回值语义再写递归。

模板代码：
```python
def max_depth(root):
    if not root:
        return 0
    return max(max_depth(root.left), max_depth(root.right)) + 1
```

#### 4.3.1 模板题目
- 0101 - 对称二叉树 ｜ [LeetCode 链接](https://leetcode.cn/problems/symmetric-tree/) ｜ [题解笔记](../solutions/0101-0200/0101-symmetric-tree.md)
- 0110 - 平衡二叉树 ｜ [LeetCode 链接](https://leetcode.cn/problems/balanced-binary-tree/) ｜ [题解笔记](../solutions/0101-0200/0110-balanced-binary-tree.md)
- 0226 - Invert Binary Tree ｜ [LeetCode 链接](https://leetcode.cn/problems/invert-binary-tree/) ｜ [题解笔记](../solutions/0201-0300/0226-invert-binary-tree.md)
- 0617 - Merge Two Binary Trees ｜ [LeetCode 链接](https://leetcode.cn/problems/merge-two-binary-trees/) ｜ [题解笔记](../solutions/0601-0700/0617-merge-two-binary-trees.md)
- 0543 - 二叉树的直径 ｜ [LeetCode 链接](https://leetcode.cn/problems/diameter-of-binary-tree/) ｜ [题解笔记](../solutions/0501-0600/0543-diameter-of-binary-tree.md)
### 4.4 BST 定位与中序性质
方法说明：
利用 BST 左小右大的结构性质做验证、插入、删除、修剪与有序累加。

模板代码：
```python
def is_valid_bst(root):
    st = []
    prev = float('-inf')
    cur = root
    while st or cur:
        while cur:
            st.append(cur)
            cur = cur.left
        cur = st.pop()
        if cur.val <= prev:
            return False
        prev = cur.val
        cur = cur.right
    return True
```

#### 4.4.1 模板题目
- 0098 - 验证二叉搜索树 ｜ [LeetCode 链接](https://leetcode.cn/problems/validate-binary-search-tree/) ｜ [题解笔记](../solutions/0001-0100/0098-validate-binary-search-tree.md)
- 0450 - 删除二叉搜索树中的节点 ｜ [LeetCode 链接](https://leetcode.cn/problems/delete-node-in-a-bst/) ｜ [题解笔记](../solutions/0401-0500/0450-delete-node-in-a-bst.md)
- 0538 - 把二叉搜索树转换为累加树 ｜ [LeetCode 链接](https://leetcode.cn/problems/convert-bst-to-greater-tree/) ｜ [题解笔记](../solutions/0501-0600/0538-convert-bst-to-greater-tree.md)
- 0669 - 修剪二叉搜索树 ｜ [LeetCode 链接](https://leetcode.cn/problems/trim-a-binary-search-tree/) ｜ [题解笔记](../solutions/0601-0700/0669-trim-a-binary-search-tree.md)
- 0701 - 二叉搜索树中的插入操作 ｜ [LeetCode 链接](https://leetcode.cn/problems/insert-into-a-binary-search-tree/) ｜ [题解笔记](../solutions/0701-0800/0701-insert-into-a-binary-search-tree.md)
- 0108 - 将有序数组转换为二叉搜索树 ｜ [LeetCode 链接](https://leetcode.cn/problems/convert-sorted-array-to-binary-search-tree/) ｜ [题解笔记](../solutions/0101-0200/0108-convert-sorted-array-to-binary-search-tree.md)
### 4.5 树的构造与序列化
方法说明：
通过遍历序列划分子树，或用 BFS/DFS 完成编码解码。核心是边界一致性。

模板代码：
```python
def build(preorder, inorder):
    pos = {v: i for i, v in enumerate(inorder)}

    def dfs(pl, pr, il, ir):
        if pl > pr:
            return None
        root_val = preorder[pl]
        k = pos[root_val]
        left_size = k - il
        root = TreeNode(root_val)
        root.left = dfs(pl + 1, pl + left_size, il, k - 1)
        root.right = dfs(pl + left_size + 1, pr, k + 1, ir)
        return root
```

#### 4.5.1 模板题目
- 0105 - 从前序与中序遍历序列构造二叉树 ｜ [LeetCode 链接](https://leetcode.cn/problems/construct-binary-tree-from-preorder-and-inorder-traversal/) ｜ [题解笔记](../solutions/0101-0200/0105-construct-binary-tree-from-preorder-and-inorder-traversal.md)
- 0106 - 从中序与后序遍历序列构造二叉树 ｜ [LeetCode 链接](https://leetcode.cn/problems/construct-binary-tree-from-inorder-and-postorder-traversal/) ｜ [题解笔记](../solutions/0101-0200/0106-construct-binary-tree-from-inorder-and-postorder-traversal.md)
- 0114 - 二叉树展开为链表 ｜ [LeetCode 链接](https://leetcode.cn/problems/flatten-binary-tree-to-linked-list/) ｜ [题解笔记](../solutions/0101-0200/0114-flatten-binary-tree-to-linked-list.md)
- 0297 - 二叉树的序列化与反序列化 ｜ [LeetCode 链接](https://leetcode.cn/problems/serialize-and-deserialize-binary-tree/) ｜ [题解笔记](../solutions/0201-0300/0297-serialize-and-deserialize-binary-tree.md)
### 4.6 树上路径与决策
方法说明：
后序汇总子树信息，解决路径和、最大路径、最近公共祖先与摄像头布置。`0968` 是树上贪心的交叉题。

模板代码：
```python
def max_path_sum(root):
    ans = -10**15

    def dfs(node):
        nonlocal ans
        if not node:
            return 0
        l = max(dfs(node.left), 0)
        r = max(dfs(node.right), 0)
        ans = max(ans, node.val + l + r)
        return node.val + max(l, r)

    dfs(root)
    return ans
```

#### 4.6.1 模板题目
- 0124 - 二叉树中的最大路径和 ｜ [LeetCode 链接](https://leetcode.cn/problems/binary-tree-maximum-path-sum/) ｜ [题解笔记](../solutions/0101-0200/0124-binary-tree-maximum-path-sum.md)
- 0236 - 二叉树的最近公共祖先 ｜ [LeetCode 链接](https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-tree/) ｜ [题解笔记](../solutions/0201-0300/0236-lowest-common-ancestor-of-a-binary-tree.md)
- 0437 - 路径总和 III ｜ [LeetCode 链接](https://leetcode.cn/problems/path-sum-iii/) ｜ [题解笔记](../solutions/0401-0500/0437-path-sum-iii.md)
- 0968 - 监控二叉树 ｜ [LeetCode 链接](https://leetcode.cn/problems/binary-tree-cameras/) ｜ [题解笔记](../solutions/0901-1000/0968-binary-tree-cameras.md)
### 4.7 组合型回溯（子集/组合）
方法说明：
用 `startIndex` 控制可选范围，适合子集、组合与组合去重。

模板代码：
```python
def backtrack(cands):
    ans, path = [], []

    def dfs(start):
        ans.append(path[:])
        for i in range(start, len(cands)):
            path.append(cands[i])
            dfs(i + 1)
            path.pop()
```

#### 4.7.1 模板题目
- 0039 - 组合总和 ｜ [LeetCode 链接](https://leetcode.cn/problems/combination-sum/) ｜ [题解笔记](../solutions/0001-0100/0039-combination-sum.md)
- 0040 - 组合总和 II ｜ [LeetCode 链接](https://leetcode.cn/problems/combination-sum-ii/) ｜ [题解笔记](../solutions/0001-0100/0040-combination-sum-ii.md)
- 0078 - Subsets ｜ [LeetCode 链接](https://leetcode.cn/problems/subsets/) ｜ [题解笔记](../solutions/0001-0100/0078-subsets.md)
- 0491 - 非递减子序列 ｜ [LeetCode 链接](https://leetcode.cn/problems/non-decreasing-subsequences/) ｜ [题解笔记](../solutions/0401-0500/0491-non-decreasing-subsequences.md)
### 4.8 排列与去重回溯
方法说明：
使用 `used` 数组控制选择状态，重复元素需配合排序和同层去重。

模板代码：
```python
def permute(nums):
    nums.sort()
    ans, path = [], []
    used = [False] * len(nums)

    def dfs():
        if len(path) == len(nums):
            ans.append(path[:])
            return
        for i in range(len(nums)):
            if used[i]:
                continue
            if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                continue
            used[i] = True
            path.append(nums[i])
            dfs()
            path.pop()
            used[i] = False
```

#### 4.8.1 模板题目
- 0046 - 全排列 ｜ [LeetCode 链接](https://leetcode.cn/problems/permutations/) ｜ [题解笔记](../solutions/0001-0100/0046-permutations.md)
- 0047 - 全排列 II ｜ [LeetCode 链接](https://leetcode.cn/problems/permutations-ii/) ｜ [题解笔记](../solutions/0001-0100/0047-permutations-ii.md)
- 0017 - 电话号码的字母组合 ｜ [LeetCode 链接](https://leetcode.cn/problems/letter-combinations-of-a-phone-number/) ｜ [题解笔记](../solutions/0001-0100/0017-letter-combinations-of-a-phone-number.md)
- 0022 - 括号生成 ｜ [LeetCode 链接](https://leetcode.cn/problems/generate-parentheses/) ｜ [题解笔记](../solutions/0001-0100/0022-generate-parentheses.md)
### 4.9 约束搜索与切分回溯
方法说明：
处理网格单词搜索、括号删减、回文切分等约束型搜索。可与字符串、网格专题交叉。

模板代码：
```python
def partition_palindrome(s):
    ans, path = [], []

    def is_pal(l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True

    def dfs(start):
        if start == len(s):
            ans.append(path[:])
            return
        for end in range(start, len(s)):
            if is_pal(start, end):
                path.append(s[start:end + 1])
                dfs(end + 1)
                path.pop()
```

#### 4.9.1 模板题目
- 0131 - 分割回文串 ｜ [LeetCode 链接](https://leetcode.cn/problems/palindrome-partitioning/) ｜ [题解笔记](../solutions/0101-0200/0131-palindrome-partitioning.md)
- 0301 - 删除无效的括号 ｜ [LeetCode 链接](https://leetcode.cn/problems/remove-invalid-parentheses/) ｜ [题解笔记](../solutions/0301-0400/0301-remove-invalid-parentheses.md)
- 0079 - Word Search ｜ [LeetCode 链接](https://leetcode.cn/problems/word-search/) ｜ [题解笔记](../solutions/0001-0100/0079-word-search.md)
## 5 易错点
- 链表丢失后继指针或头结点。
- 树递归返回语义不统一。
- 回溯剪枝与去重层级混淆。

## 6 总结
链表重在指针一致性，树重在递归语义，回溯重在状态恢复；模板先行可显著降低实现风险。
