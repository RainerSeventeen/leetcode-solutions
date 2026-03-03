# 链表、树与回溯（前后指针/快慢指针/DFS/BFS/直径/LCA）

## 概览
本专题覆盖链表原地操作、二叉树递归/迭代、一般树 DFS、以及回溯搜索的核心模板。

## 核心思想
- 链表：围绕指针重连与哑节点统一边界处理。
- 树：先定义递归返回语义，再做子树合并。
- 回溯：路径试探、约束剪枝、现场恢复。

## 解题流程
1. 先判断题型：链表指针、二叉树/一般树递归，还是回溯搜索。
2. 先写模板骨架（哑节点/DFS 返回值/回溯框架）。
3. 再补题目特有约束（去重、剪枝、边界条件）。
4. 用极小样例验证：空链表、单节点树、空路径。

## 模板与子方法
### 链表
#### 遍历链表
模板：

```python
# 待补充
```

模板题目：
待补充...

#### 删除节点
模板：

```python
# 待补充
```

模板题目：
- 0203 - 移除链表元素 ｜ [LeetCode 链接](https://leetcode.cn/problems/remove-linked-list-elements/) ｜ [题解笔记](../solutions/0201-0300/0203-remove-linked-list-elements.md)

#### 插入节点
模板：

```python
# 待补充
```

模板题目：
待补充...

#### 反转链表
模板：

```python
def reverse_list(head):
    prev, cur = None, head
    while cur:
        nxt = cur.next
        cur.next = prev
        prev, cur = cur, nxt
    return prev
```

模板题目：
- 0024 - 两两交换链表中的节点 ｜ [LeetCode 链接](https://leetcode.cn/problems/swap-nodes-in-pairs/) ｜ [题解笔记](../solutions/0001-0100/0024-swap-nodes-in-pairs.md)
- 0206 - 反转链表 ｜ [LeetCode 链接](https://leetcode.cn/problems/reverse-linked-list/) ｜ [题解笔记](../solutions/0201-0300/0206-reverse-linked-list.md)

#### 前后指针
模板：

```python
def remove_nth_from_end(head, n):
    dummy = ListNode(0, head)
    fast = slow = dummy
    for _ in range(n):
        fast = fast.next
    while fast.next:
        fast = fast.next
        slow = slow.next
    slow.next = slow.next.next
    return dummy.next
```

模板题目：
- 0019 - 删除链表的倒数第 N 个结点 ｜ [LeetCode 链接](https://leetcode.cn/problems/remove-nth-node-from-end-of-list/) ｜ [题解笔记](../solutions/0001-0100/0019-remove-nth-node-from-end-of-list.md)

#### 快慢指针
模板：

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

模板题目：
- 0141 - 环形链表 ｜ [LeetCode 链接](https://leetcode.cn/problems/linked-list-cycle/) ｜ [题解笔记](../solutions/0101-0200/0141-linked-list-cycle.md)
- 0142 - 环形链表 II ｜ [LeetCode 链接](https://leetcode.cn/problems/linked-list-cycle-ii/) ｜ [题解笔记](../solutions/0101-0200/0142-linked-list-cycle-ii.md)
- 0234 - 回文链表 ｜ [LeetCode 链接](https://leetcode.cn/problems/palindrome-linked-list/) ｜ [题解笔记](../solutions/0201-0300/0234-palindrome-linked-list.md)

#### 双指针
模板：

```python
def get_intersection_node(head_a, head_b):
    pa, pb = head_a, head_b
    while pa is not pb:
        pa = pa.next if pa else head_b
        pb = pb.next if pb else head_a
    return pa
```

模板题目：
- 0160 - 相交链表 ｜ [LeetCode 链接](https://leetcode.cn/problems/intersection-of-two-linked-lists/) ｜ [题解笔记](../solutions/0101-0200/0160-intersection-of-two-linked-lists.md)

#### 合并链表
模板：

```python
def merge_two_lists(l1, l2):
    dummy = ListNode(0)
    cur = dummy
    while l1 and l2:
        if l1.val <= l2.val:
            cur.next, l1 = l1, l1.next
        else:
            cur.next, l2 = l2, l2.next
        cur = cur.next
    cur.next = l1 or l2
    return dummy.next
```

模板题目：
- 0002 - 两数相加 ｜ [LeetCode 链接](https://leetcode.cn/problems/add-two-numbers/) ｜ [题解笔记](../solutions/0001-0100/0002-add-two-numbers.md)
- 0021 - 合并两个有序链表 ｜ [LeetCode 链接](https://leetcode.cn/problems/merge-two-sorted-lists/) ｜ [题解笔记](../solutions/0001-0100/0021-merge-two-sorted-lists.md)

#### 分治
模板：

```python
def sort_list(head):
    if not head or not head.next:
        return head
    slow, fast = head, head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    mid = slow.next
    slow.next = None
    left = sort_list(head)
    right = sort_list(mid)
    return merge_two_lists(left, right)
```

模板题目：
- 0148 - 排序链表 ｜ [LeetCode 链接](https://leetcode.cn/problems/sort-list/) ｜ [题解笔记](../solutions/0101-0200/0148-sort-list.md)

#### 综合应用
模板：

```python
# 待补充
```

模板题目：
- 0707 - 设计链表 ｜ [LeetCode 链接](https://leetcode.cn/problems/design-linked-list/) ｜ [题解笔记](../solutions/0701-0800/0707-design-linked-list.md)

#### 其他
模板：

```python
# 待补充
```

模板题目：
待补充...

### 二叉树
#### 遍历二叉树
模板：

```python
def preorder(root):
    if not root:
        return []
    return [root.val] + preorder(root.left) + preorder(root.right)
```

模板题目：
待补充...

#### 自顶向下 DFS（先序遍历）
模板：

```python
def max_depth(root):
    if not root:
        return 0
    return max(max_depth(root.left), max_depth(root.right)) + 1
```

模板题目：
- 1022 - 从根到叶的二进制数之和 ｜ [LeetCode 链接](https://leetcode.cn/problems/sum-of-root-to-leaf-binary-numbers/) ｜ [题解笔记](../solutions/1001-1100/1022-sum-of-root-to-leaf-binary-numbers.md)

#### 自底向上 DFS（后序遍历）
模板：

```python
def is_balanced(root):
    def height(node):
        if not node:
            return 0
        l = height(node.left)
        if l == -1:
            return -1
        r = height(node.right)
        if r == -1 or abs(l - r) > 1:
            return -1
        return max(l, r) + 1

    return height(root) != -1
```

模板题目：
- 0101 - 对称二叉树 ｜ [LeetCode 链接](https://leetcode.cn/problems/symmetric-tree/) ｜ [题解笔记](../solutions/0101-0200/0101-symmetric-tree.md)
- 0110 - 平衡二叉树 ｜ [LeetCode 链接](https://leetcode.cn/problems/balanced-binary-tree/) ｜ [题解笔记](../solutions/0101-0200/0110-balanced-binary-tree.md)
- 0226 - 翻转二叉树 ｜ [LeetCode 链接](https://leetcode.cn/problems/invert-binary-tree/) ｜ [题解笔记](../solutions/0201-0300/0226-invert-binary-tree.md)
- 0617 - 合并二叉树 ｜ [LeetCode 链接](https://leetcode.cn/problems/merge-two-binary-trees/) ｜ [题解笔记](../solutions/0601-0700/0617-merge-two-binary-trees.md)

#### 自底向上 DFS：删点
模板：

```python
# 待补充
```

模板题目：
待补充...

#### 有递有归
模板：

```python
# 待补充
```

模板题目：
- 0538 - 把二叉搜索树转换为累加树 ｜ [LeetCode 链接](https://leetcode.cn/problems/convert-bst-to-greater-tree/) ｜ [题解笔记](../solutions/0501-0600/0538-convert-bst-to-greater-tree.md)

#### 二叉树的直径
模板：

```python
def diameter_of_binary_tree(root):
    ans = 0

    def dfs(node):
        nonlocal ans
        if not node:
            return 0
        l = dfs(node.left)
        r = dfs(node.right)
        ans = max(ans, l + r)
        return max(l, r) + 1

    dfs(root)
    return ans
```

模板题目：
- 0124 - 二叉树中的最大路径和 ｜ [LeetCode 链接](https://leetcode.cn/problems/binary-tree-maximum-path-sum/) ｜ [题解笔记](../solutions/0101-0200/0124-binary-tree-maximum-path-sum.md)
- 0543 - 二叉树的直径 ｜ [LeetCode 链接](https://leetcode.cn/problems/diameter-of-binary-tree/) ｜ [题解笔记](../solutions/0501-0600/0543-diameter-of-binary-tree.md)

#### 回溯
模板：

```python
def binary_tree_paths(root):
    ans, path = [], []

    def dfs(node):
        if not node:
            return
        path.append(str(node.val))
        if not node.left and not node.right:
            ans.append("->".join(path))
        else:
            dfs(node.left)
            dfs(node.right)
        path.pop()

    dfs(root)
    return ans
```

模板题目：
- 0437 - 路径总和 III ｜ [LeetCode 链接](https://leetcode.cn/problems/path-sum-iii/) ｜ [题解笔记](../solutions/0401-0500/0437-path-sum-iii.md)

#### 最近公共祖先
模板：

```python
def lowest_common_ancestor(root, p, q):
    if not root or root == p or root == q:
        return root
    l = lowest_common_ancestor(root.left, p, q)
    r = lowest_common_ancestor(root.right, p, q)
    if l and r:
        return root
    return l or r
```

模板题目：
- 0236 - 二叉树的最近公共祖先 ｜ [LeetCode 链接](https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-tree/) ｜ [题解笔记](../solutions/0201-0300/0236-lowest-common-ancestor-of-a-binary-tree.md)

#### 二叉搜索树
模板：

```python
def is_valid_bst(root):
    st = []
    prev = float("-inf")
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

模板题目：
- 0098 - 验证二叉搜索树 ｜ [LeetCode 链接](https://leetcode.cn/problems/validate-binary-search-tree/) ｜ [题解笔记](../solutions/0001-0100/0098-validate-binary-search-tree.md)
- 0700 - 二叉搜索树中的搜索 ｜ [LeetCode 链接](https://leetcode.cn/problems/search-in-a-binary-search-tree/) ｜ [题解笔记](../solutions/0601-0700/0700-search-in-a-binary-search-tree.md)

#### 创建二叉树
模板：

```python
def build_tree(preorder, inorder):
    idx = {v: i for i, v in enumerate(inorder)}

    def dfs(pl, pr, il, ir):
        if pl > pr:
            return None
        root_val = preorder[pl]
        k = idx[root_val]
        left_size = k - il
        root = TreeNode(root_val)
        root.left = dfs(pl + 1, pl + left_size, il, k - 1)
        root.right = dfs(pl + left_size + 1, pr, k + 1, ir)
        return root

    return dfs(0, len(preorder) - 1, 0, len(inorder) - 1)
```

模板题目：
- 0108 - 将有序数组转换为二叉搜索树 ｜ [LeetCode 链接](https://leetcode.cn/problems/convert-sorted-array-to-binary-search-tree/) ｜ [题解笔记](../solutions/0101-0200/0108-convert-sorted-array-to-binary-search-tree.md)
- 0105 - 从前序与中序遍历序列构造二叉树 ｜ [LeetCode 链接](https://leetcode.cn/problems/construct-binary-tree-from-preorder-and-inorder-traversal/) ｜ [题解笔记](../solutions/0101-0200/0105-construct-binary-tree-from-preorder-and-inorder-traversal.md)
- 0106 - 从中序与后序遍历序列构造二叉树 ｜ [LeetCode 链接](https://leetcode.cn/problems/construct-binary-tree-from-inorder-and-postorder-traversal/) ｜ [题解笔记](../solutions/0101-0200/0106-construct-binary-tree-from-inorder-and-postorder-traversal.md)
- 0654 - 最大二叉树 ｜ [LeetCode 链接](https://leetcode.cn/problems/maximum-binary-tree/) ｜ [题解笔记](../solutions/0601-0700/0654-maximum-binary-tree.md)

#### 插入/删除节点
模板：

```python
# 待补充
```

模板题目：
- 0450 - 删除二叉搜索树中的节点 ｜ [LeetCode 链接](https://leetcode.cn/problems/delete-node-in-a-bst/) ｜ [题解笔记](../solutions/0401-0500/0450-delete-node-in-a-bst.md)
- 0669 - 修剪二叉搜索树 ｜ [LeetCode 链接](https://leetcode.cn/problems/trim-a-binary-search-tree/) ｜ [题解笔记](../solutions/0601-0700/0669-trim-a-binary-search-tree.md)
- 0701 - 二叉搜索树中的插入操作 ｜ [LeetCode 链接](https://leetcode.cn/problems/insert-into-a-binary-search-tree/) ｜ [题解笔记](../solutions/0701-0800/0701-insert-into-a-binary-search-tree.md)

#### 树形 DP
模板：

```python
# 待补充
```

模板题目：
- 0968 - 监控二叉树 ｜ [LeetCode 链接](https://leetcode.cn/problems/binary-tree-cameras/) ｜ [题解笔记](../solutions/0901-1000/0968-binary-tree-cameras.md)

#### 二叉树 BFS
模板：

```python
from collections import deque

def level_order(root):
    if not root:
        return []
    ans = []
    q = deque([root])
    while q:
        level = []
        for _ in range(len(q)):
            node = q.popleft()
            level.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        ans.append(level)
    return ans
```

模板题目：
待补充...

#### 链表+二叉树
模板：

```python
# 待补充
```

模板题目：
- 0114 - 二叉树展开为链表 ｜ [LeetCode 链接](https://leetcode.cn/problems/flatten-binary-tree-to-linked-list/) ｜ [题解笔记](../solutions/0101-0200/0114-flatten-binary-tree-to-linked-list.md)

#### N 叉树
模板：

```python
# 待补充
```

模板题目：
待补充...

#### 其他
模板：

```python
# 待补充
```

模板题目：
- 0222 - 完全二叉树的节点个数 ｜ [LeetCode 链接](https://leetcode.cn/problems/count-complete-tree-nodes/) ｜ [题解笔记](../solutions/0201-0300/0222-count-complete-tree-nodes.md)
- 0297 - 二叉树的序列化与反序列化 ｜ [LeetCode 链接](https://leetcode.cn/problems/serialize-and-deserialize-binary-tree/) ｜ [题解笔记](../solutions/0201-0300/0297-serialize-and-deserialize-binary-tree.md)

### 一般树
#### 遍历
模板：

```python
# 待补充
```

模板题目：
待补充...

#### 自顶向下 DFS
模板：

```python
# 待补充
```

模板题目：
待补充...

#### 自底向上 DFS
模板：

```python
# 待补充
```

模板题目：
待补充...

#### 有递有归
模板：

```python
# 待补充
```

模板题目：
待补充...

#### 树的直径
模板：

```python
# 待补充
```

模板题目：
待补充...

#### 树的拓扑排序
模板：

```python
# 待补充
```

模板题目：
待补充...

#### DFS 时间戳
模板：

```python
# 待补充
```

模板题目：
待补充...

#### 最近公共祖先（LCA）、倍增算法
模板：

```python
# 待补充
```

模板题目：
待补充...

#### 虚树
模板：

```python
# 待补充
```

模板题目：
待补充...

#### 树上启发式合并
模板：

```python
# 待补充
```

模板题目：
待补充...

#### 点分治
模板：

```python
# 待补充
```

模板题目：
待补充...

#### 树上滑动窗口
模板：

```python
# 待补充
```

模板题目：
待补充...

#### 其他
模板：

```python
# 待补充
```

模板题目：
待补充...

### 回溯
#### 入门回溯
模板：

```python
def backtrack(nums):
    ans, path = [], []

    def dfs(i):
        if i == len(nums):
            ans.append(path[:])
            return
        dfs(i + 1)
        path.append(nums[i])
        dfs(i + 1)
        path.pop()

    dfs(0)
    return ans
```

模板题目：
- 0017 - 电话号码的字母组合 ｜ [LeetCode 链接](https://leetcode.cn/problems/letter-combinations-of-a-phone-number/) ｜ [题解笔记](../solutions/0001-0100/0017-letter-combinations-of-a-phone-number.md)

#### 子集型回溯
模板：

```python
def subsets(nums):
    ans, path = [], []

    def dfs(i):
        if i == len(nums):
            ans.append(path[:])
            return
        dfs(i + 1)
        path.append(nums[i])
        dfs(i + 1)
        path.pop()

    dfs(0)
    return ans
```

模板题目：
- 0078 - 子集 ｜ [LeetCode 链接](https://leetcode.cn/problems/subsets/) ｜ [题解笔记](../solutions/0001-0100/0078-subsets.md)
- 0039 - 组合总和 ｜ [LeetCode 链接](https://leetcode.cn/problems/combination-sum/) ｜ [题解笔记](../solutions/0001-0100/0039-combination-sum.md)

#### 划分型回溯
模板：

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
            if not is_pal(start, end):
                continue
            path.append(s[start:end + 1])
            dfs(end + 1)
            path.pop()

    dfs(0)
    return ans
```

模板题目：
- 0093 - 复原 IP 地址 ｜ [LeetCode 链接](https://leetcode.cn/problems/restore-ip-addresses/) ｜ [题解笔记](../solutions/0001-0100/0093-restore-ip-addresses.md)
- 0131 - 分割回文串 ｜ [LeetCode 链接](https://leetcode.cn/problems/palindrome-partitioning/) ｜ [题解笔记](../solutions/0101-0200/0131-palindrome-partitioning.md)

#### 组合型回溯
模板：

```python
def combination_backtrack(cands, target):
    ans, path = [], []
    cands.sort()

    def dfs(start, remain):
        if remain == 0:
            ans.append(path[:])
            return
        if remain < 0:
            return
        for i in range(start, len(cands)):
            if cands[i] > remain:
                break
            path.append(cands[i])
            dfs(i, remain - cands[i])
            path.pop()

    dfs(0, target)
    return ans
```

模板题目：
- 0022 - 括号生成 ｜ [LeetCode 链接](https://leetcode.cn/problems/generate-parentheses/) ｜ [题解笔记](../solutions/0001-0100/0022-generate-parentheses.md)
- 0077 - 组合 ｜ [LeetCode 链接](https://leetcode.cn/problems/combinations/) ｜ [题解笔记](../solutions/0001-0100/0077-combinations.md)
- 0216 - 组合总和 III ｜ [LeetCode 链接](https://leetcode.cn/problems/combination-sum-iii/) ｜ [题解笔记](../solutions/0201-0300/0216-combination-sum-iii.md)
- 0301 - 删除无效的括号 ｜ [LeetCode 链接](https://leetcode.cn/problems/remove-invalid-parentheses/) ｜ [题解笔记](../solutions/0301-0400/0301-remove-invalid-parentheses.md)

#### 排列型回溯
模板：

```python
def permute(nums):
    ans, path = [], []
    used = [False] * len(nums)

    def dfs():
        if len(path) == len(nums):
            ans.append(path[:])
            return
        for i, x in enumerate(nums):
            if used[i]:
                continue
            used[i] = True
            path.append(x)
            dfs()
            path.pop()
            used[i] = False

    dfs()
    return ans
```

模板题目：
- 0046 - 全排列 ｜ [LeetCode 链接](https://leetcode.cn/problems/permutations/) ｜ [题解笔记](../solutions/0001-0100/0046-permutations.md)
- 0037 - 解数独 ｜ [LeetCode 链接](https://leetcode.cn/problems/sudoku-solver/) ｜ [题解笔记](../solutions/0001-0100/0037-sudoku-solver.md)
- 0051 - N 皇后 ｜ [LeetCode 链接](https://leetcode.cn/problems/n-queens/) ｜ [题解笔记](../solutions/0001-0100/0051-n-queens.md)

#### 有重复元素的回溯
模板：

```python
def find_subsequences(nums):
    ans, path = [], []

    def dfs(start):
        if len(path) >= 2:
            ans.append(path[:])
        used = set()
        for i in range(start, len(nums)):
            if nums[i] in used:
                continue
            if path and nums[i] < path[-1]:
                continue
            used.add(nums[i])
            path.append(nums[i])
            dfs(i + 1)
            path.pop()

    dfs(0)
    return ans
```

模板题目：
- 0040 - 组合总和 II ｜ [LeetCode 链接](https://leetcode.cn/problems/combination-sum-ii/) ｜ [题解笔记](../solutions/0001-0100/0040-combination-sum-ii.md)
- 0047 - 全排列 II ｜ [LeetCode 链接](https://leetcode.cn/problems/permutations-ii/) ｜ [题解笔记](../solutions/0001-0100/0047-permutations-ii.md)
- 0491 - 非递减子序列 ｜ [LeetCode 链接](https://leetcode.cn/problems/non-decreasing-subsequences/) ｜ [题解笔记](../solutions/0401-0500/0491-non-decreasing-subsequences.md)

#### 搜索
模板：

```python
# 待补充
```

模板题目：
待补充...

#### 折半枚举
模板：

```python
# 待补充
```

模板题目：
待补充...

### 其他递归/分治
- 1545 - 找出第 N 个二进制字符串中的第 K 位 ｜ [LeetCode 链接](https://leetcode.cn/problems/find-kth-bit-in-nth-binary-string/) ｜ [题解笔记](../solutions/1501-1600/1545-find-kth-bit-in-nth-binary-string.md)

### 算法题单
待补充...

## 易错点
- 链表中先改指针再取后继，容易导致链断。
- 树递归返回语义不一致，会造成合并逻辑错位。
- 回溯把“树层去重”和“树枝占用”混用，容易漏解或重复。
- 剪枝位置错误会提前截断整层搜索。

## 总结
链表重在指针一致性，树重在递归语义，回溯重在状态恢复；先稳定模板，再按题意局部变形。
