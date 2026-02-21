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
- 0024 - 两两交换链表中的节点 ｜ [LeetCode 链接](https://leetcode.cn/problems/swap-nodes-in-pairs/) ｜ [题解笔记](../solutions/0001-0100/0024-swap-nodes-in-pairs.md)
- 0203 - 移除链表元素 ｜ [LeetCode 链接](https://leetcode.cn/problems/remove-linked-list-elements/) ｜ [题解笔记](../solutions/0201-0300/0203-remove-linked-list-elements.md)
- 0838 - 设计链表 ｜ [LeetCode 链接](https://leetcode.cn/problems/design-linked-list/) ｜ [题解笔记](../solutions/0801-0900/0838-design-linked-list.md)
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
### 4.3 二叉树基础与遍历语义
方法说明：
树题先统一“访问节点时机”和“递归返回语义”，再落到模板代码。很多题做不稳不是代码细节问题，而是前中后序语义没有先定死。

基础理论：
- 树分类：满二叉树是“每层都满”；完全二叉树是“除底层外都满，底层从左到右连续”；BST 额外满足左小右大；平衡二叉树要求左右子树高度差不超过 1。
- 存储方式：链式存储（`left/right` 指针）是日常主力；顺序存储常见于堆，若父节点下标为 `i`，左右孩子下标分别是 `2 * i + 1`、`2 * i + 2`。

DFS/BFS 访问语义：
- DFS 本质是栈模型（递归隐式栈/显式栈）。前、中、后序差异只在“父节点何时处理”。
- 前序（中左右）：先处理父节点，适合“边遍历边建结果”的顺序任务，迭代写法通常最直接。
- 中序（左中右）：父节点夹在两棵子树中间，BST 上会得到递增序列，常用于 BST 合法性判断与有序性利用。
- 后序（左右中）：先拿到左右子树信息再处理父节点，天然适合“自底向上汇总”（高度、平衡性、直径、路径值、LCA 回传）。
- BFS（层序）本质是队列 FIFO；每轮先固定当前层节点数，再弹出这一层并扩展下一层。

递归三要素：
1. 参数与返回值：决定子问题边界和向上汇报的信息形态（`bool`/数值/节点指针等）。
2. 终止条件：空节点、命中目标、越界等必须先返回，避免语义漂移。
3. 单层递归逻辑：先递归子树，再按遍历时机在“中”位置做当前层合并或判定。

模板代码：
```python
def max_depth(root):
    if not root:
        return 0
    left_h = max_depth(root.left)
    right_h = max_depth(root.right)
    return max(left_h, right_h) + 1
```

#### 4.3.1 模板题目
- 0101 - 对称二叉树 ｜ [LeetCode 链接](https://leetcode.cn/problems/symmetric-tree/) ｜ [题解笔记](../solutions/0101-0200/0101-symmetric-tree.md)
- 0226 - Invert Binary Tree ｜ [LeetCode 链接](https://leetcode.cn/problems/invert-binary-tree/) ｜ [题解笔记](../solutions/0201-0300/0226-invert-binary-tree.md)
- 0617 - Merge Two Binary Trees ｜ [LeetCode 链接](https://leetcode.cn/problems/merge-two-binary-trees/) ｜ [题解笔记](../solutions/0601-0700/0617-merge-two-binary-trees.md)
- 0222 - 完全二叉树的节点个数 ｜ [LeetCode 链接](https://leetcode.cn/problems/count-complete-tree-nodes/) ｜ [题解笔记](../solutions/0201-0300/0222-count-complete-tree-nodes.md)
- 0654 - 最大二叉树 ｜ [LeetCode 链接](https://leetcode.cn/problems/maximum-binary-tree/) ｜ [题解笔记](../solutions/0601-0700/0654-maximum-binary-tree.md)
### 4.4 BST 定位与中序性质
方法说明：
利用 BST 左小右大的结构性质做验证、插入、删除、修剪与有序累加。

关键细节：
- 插入操作通常只改一条搜索路径，返回原根节点即可完成挂接。
- 删除操作要覆盖 5 类情况：未命中、叶子、仅左、仅右、左右都在（用右子树接班并把左子树挂到右子树最左侧）。
- 修剪操作不能粗暴把越界节点置空：当 `root.val < low` 时应递归到右子树；`root.val > high` 时递归到左子树，保留可能合法的后代。

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
- 0696 - 计数二进制子串 ｜ [LeetCode 链接](https://leetcode.cn/problems/count-binary-substrings/) ｜ [题解笔记](../solutions/0601-0700/0696-count-binary-substrings.md)
- 0783 - 二叉搜索树中的搜索 ｜ [LeetCode 链接](https://leetcode.cn/problems/search-in-a-binary-search-tree/) ｜ [题解笔记](../solutions/0701-0800/0783-search-in-a-binary-search-tree.md)
### 4.5 树的构造与序列化
方法说明：
通过遍历序列划分子树，或用 BFS/DFS 完成编码解码。核心是边界一致性。

构造题常用步骤（以中序 + 后序为例）：
1. 后序末尾元素是当前子树根节点。
2. 在中序中定位根节点位置，切出左/右子树区间。
3. 用左子树长度同步切分后序区间，再递归构造左右子树。
4. 优先传索引边界而不是复制子数组，避免不必要的额外开销。

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
### 4.6 树上后序汇总与回溯返回
方法说明：
后序汇总子树信息，解决路径和、最大路径、最近公共祖先与摄像头布置。`0968` 是树上贪心的交叉题。

返回值语义拆分：
- 返回 `void`：只做遍历/统计，结果写到外部变量。
- 返回 `bool`：做存在性判断，一旦某分支命中可提前终止。
- 返回数值（`int`/`long`）：向上汇报高度、贡献值、路径和等聚合信息。
- 返回 `TreeNode*`：需要改树结构或向上回传命中节点（如 LCA）时使用。

LCA 典型后序逻辑：
- 若左右子树都返回非空，当前节点就是最近公共祖先。
- 若仅一边非空，继续把该非空结果向上回传。
- 若都为空，返回空指针。

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
- 0110 - 平衡二叉树 ｜ [LeetCode 链接](https://leetcode.cn/problems/balanced-binary-tree/) ｜ [题解笔记](../solutions/0101-0200/0110-balanced-binary-tree.md)
- 0124 - 二叉树中的最大路径和 ｜ [LeetCode 链接](https://leetcode.cn/problems/binary-tree-maximum-path-sum/) ｜ [题解笔记](../solutions/0101-0200/0124-binary-tree-maximum-path-sum.md)
- 0236 - 二叉树的最近公共祖先 ｜ [LeetCode 链接](https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-tree/) ｜ [题解笔记](../solutions/0201-0300/0236-lowest-common-ancestor-of-a-binary-tree.md)
- 0437 - 路径总和 III ｜ [LeetCode 链接](https://leetcode.cn/problems/path-sum-iii/) ｜ [题解笔记](../solutions/0401-0500/0437-path-sum-iii.md)
- 0543 - 二叉树的直径 ｜ [LeetCode 链接](https://leetcode.cn/problems/diameter-of-binary-tree/) ｜ [题解笔记](../solutions/0501-0600/0543-diameter-of-binary-tree.md)
- 0968 - 监控二叉树 ｜ [LeetCode 链接](https://leetcode.cn/problems/binary-tree-cameras/) ｜ [题解笔记](../solutions/0901-1000/0968-binary-tree-cameras.md)
### 4.7 组合型回溯（子集/组合）
方法说明：
回溯本质是“递归 + `for` 循环”。`for` 负责同层横向枚举，递归负责沿路径纵向深入。
组合/子集问题通常用 `startIndex` 限定下一层起点，避免同一元素被重复选择到更前位置。

关键要点：
- 返回值通常用 `void` 风格（Python 中即不返回布尔），在终止条件命中时记录答案并 `return`。
- 终止条件按题意区分为“到达合法叶子就收集”（如子集）与“满足目标值就收集并停止当前分支”（如组合求和）。
- 若候选数组有序，可在 `for` 内结合 `break` 做单调剪枝；若只是当前分支不合法但兄弟分支仍可能合法，使用 `continue`。

模板代码：
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
            dfs(i, remain - cands[i])  # 元素可复用时传 i；不可复用时传 i + 1
            path.pop()
```

#### 4.7.1 模板题目
- 0039 - 组合总和 ｜ [LeetCode 链接](https://leetcode.cn/problems/combination-sum/) ｜ [题解笔记](../solutions/0001-0100/0039-combination-sum.md)
- 0078 - Subsets ｜ [LeetCode 链接](https://leetcode.cn/problems/subsets/) ｜ [题解笔记](../solutions/0001-0100/0078-subsets.md)
- 0077 - 组合 ｜ [LeetCode 链接](https://leetcode.cn/problems/combinations/) ｜ [题解笔记](../solutions/0001-0100/0077-combinations.md)
- 0216 - 组合总和 III ｜ [LeetCode 链接](https://leetcode.cn/problems/combination-sum-iii/) ｜ [题解笔记](../solutions/0201-0300/0216-combination-sum-iii.md)
### 4.8 组合去重与子序列去重
方法说明：
这类问题的核心是区分“树层去重”和“树枝选择”：
- 树层（横向）去重：同一层不允许重复值展开兄弟分支。
- 树枝（纵向）选择：进入下一层后可按题意继续使用值或仅用后续位置。

常见实现：
- 排序后用 `i > start and nums[i] == nums[i - 1]` 做树层去重（如 `0040`）。
- 不便排序或需要保留原顺序时，用“每层局部集合”记录本层已用值（如 `0491`）。

模板代码：
```python
def dedup_combination(cands, target):
    ans, path = [], []
    cands.sort()

    def dfs(start, remain):
        if remain == 0:
            ans.append(path[:])
            return
        for i in range(start, len(cands)):
            if i > start and cands[i] == cands[i - 1]:
                continue  # 树层去重
            if cands[i] > remain:
                break
            path.append(cands[i])
            dfs(i + 1, remain - cands[i])  # 纵向不可复用同下标
            path.pop()
```

#### 4.8.1 模板题目
- 0040 - 组合总和 II ｜ [LeetCode 链接](https://leetcode.cn/problems/combination-sum-ii/) ｜ [题解笔记](../solutions/0001-0100/0040-combination-sum-ii.md)
- 0491 - 非递减子序列 ｜ [LeetCode 链接](https://leetcode.cn/problems/non-decreasing-subsequences/) ｜ [题解笔记](../solutions/0401-0500/0491-non-decreasing-subsequences.md)
### 4.9 排列与去重回溯
方法说明：
排列问题不能用 `startIndex`，因为每一层都要从完整候选集中挑“还没用过”的元素，需用 `used` 记录纵向占用状态。

去重关键：
- 纵向：`used[i]` 为真表示当前路径已使用该下标，必须跳过。
- 横向：排序后若 `nums[i] == nums[i - 1]` 且前一个相同值在当前层未被使用（`not used[i - 1]`），则跳过当前值。
  这条规则等价于“同层相同值只展开第一个可用分支”，而当相同值在更高层已被选中时，本层允许继续使用后续下标。

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

#### 4.9.1 模板题目
- 0046 - 全排列 ｜ [LeetCode 链接](https://leetcode.cn/problems/permutations/) ｜ [题解笔记](../solutions/0001-0100/0046-permutations.md)
- 0047 - 全排列 II ｜ [LeetCode 链接](https://leetcode.cn/problems/permutations-ii/) ｜ [题解笔记](../solutions/0001-0100/0047-permutations-ii.md)
- 0401 - 二进制手表 ｜ [LeetCode 链接](https://leetcode.cn/problems/binary-watch/) ｜ [题解笔记](../solutions/0401-0500/0401-binary-watch.md)
### 4.10 切分与约束构造回溯
方法说明：
用于“路径含义明确且每步有合法性约束”的搜索，例如回文切分、括号构造、无效括号删减、网格路径搜索。

回文切分类的细节：
- `path` 存放已切出的子串，递归参数表示“下一段起点”。
- 常用左闭右开区间表达子串边界：先校验区间合法（如是否回文），再入栈递归。
- 当起点到达字符串末尾时，说明当前切分完整，加入答案并返回。

模板代码：
```python
def partition_palindrome(s):
    ans, path = [], []

    def is_pal(l, r):  # [l, r]
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
```

#### 4.10.1 模板题目
- 0131 - 分割回文串 ｜ [LeetCode 链接](https://leetcode.cn/problems/palindrome-partitioning/) ｜ [题解笔记](../solutions/0101-0200/0131-palindrome-partitioning.md)
- 0017 - 电话号码的字母组合 ｜ [LeetCode 链接](https://leetcode.cn/problems/letter-combinations-of-a-phone-number/) ｜ [题解笔记](../solutions/0001-0100/0017-letter-combinations-of-a-phone-number.md)
- 0022 - 括号生成 ｜ [LeetCode 链接](https://leetcode.cn/problems/generate-parentheses/) ｜ [题解笔记](../solutions/0001-0100/0022-generate-parentheses.md)
- 0301 - 删除无效的括号 ｜ [LeetCode 链接](https://leetcode.cn/problems/remove-invalid-parentheses/) ｜ [题解笔记](../solutions/0301-0400/0301-remove-invalid-parentheses.md)
- 0079 - Word Search ｜ [LeetCode 链接](https://leetcode.cn/problems/word-search/) ｜ [题解笔记](../solutions/0001-0100/0079-word-search.md)
- 0037 - 解数独 ｜ [LeetCode 链接](https://leetcode.cn/problems/sudoku-solver/) ｜ [题解笔记](../solutions/0001-0100/0037-sudoku-solver.md)
- 0051 - N 皇后 ｜ [LeetCode 链接](https://leetcode.cn/problems/n-queens/) ｜ [题解笔记](../solutions/0001-0100/0051-n-queens.md)
- 0093 - 复原 IP 地址 ｜ [LeetCode 链接](https://leetcode.cn/problems/restore-ip-addresses/) ｜ [题解笔记](../solutions/0001-0100/0093-restore-ip-addresses.md)
## 5 易错点
- 链表丢失后继指针或头结点。
- 树递归返回语义不统一。
- 回溯把“树层去重”和“树枝占用”混为一谈，导致漏解或重复解。
- 剪枝位置错误：该 `continue` 的地方写成 `return`，提前截断整层搜索。

## 6 总结
链表重在指针一致性，树重在递归语义，回溯重在状态恢复；模板先行可显著降低实现风险。
