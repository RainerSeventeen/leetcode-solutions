# 二叉树

## 1 概览

二叉树是常见的底层数据结构，也是递归的重要应用场景。主要包括满二叉树、完全二叉树、二叉搜索树、平衡二叉树等类型。通过链式存储（左右指针）或线性存储（数组）方式实现。常见的遍历方式分为深度优先搜索（DFS：前中后序）和广度优先搜索（BFS：层序遍历）。

## 2 核心思想

1. **树的类型**：满二叉树（所有节点齐全）、完全二叉树（底层满且从左到右连续）、二叉搜索树（有序排列）、平衡二叉树（高度差小于 1）
2. **递归的要义**：明确返回值、设定终止条件、细化递归逻辑
3. **遍历方式**：
   - DFS（递归/迭代）：前序（中左右-顺序）、中序（左中右-排序）、后序（左右中-回溯）
   - BFS（队列）：层序遍历

## 3 解题流程

1. **分析问题性质**：确定是需要访问、修改还是构造树
2. **选择合适的遍历方式**：
   - 需要改变树结构 → 返回 `TreeNode*`
   - 需要统计整棵树 → 可能需要遍历全树
   - 需要提前终止 → 返回 `bool` 或特定值
3. **确定递归参数和返回值**：根据问题需求设计
4. **实现递归逻辑**：明确终止条件和中间处理

## 4 模板与子方法

### 4.1 子方法 A：树的遍历（DFS）

**方法说明**：使用递归或迭代方式实现前序、中序、后序遍历。前中后指的是父节点相对于左右子树的访问顺序。

**模板代码**：

前序遍历递归：
```C++
void preorderRecursive(TreeNode* root, std::vector<int>& res) {
    if (!root) return;
    res.push_back(root->val);
    preorderRecursive(root->left, res);
    preorderRecursive(root->right, res);
}
```

前序遍历迭代：
```C++
vector<int> preorderTraversal(TreeNode* root) {
    vector<int> ret;
    if (!root) return ret;
    stack<TreeNode*> stk;
    stk.push(root);

    while (!stk.empty()) {
        TreeNode* curr = stk.top();
        stk.pop();
        ret.push_back(curr->val);

        if (curr->right) stk.push(curr->right);
        if (curr->left)  stk.push(curr->left);
    }
    return ret;
}
```

中序遍历迭代：
```C++
std::vector<int> inorderIterative(TreeNode* root) {
    std::vector<int> res;
    std::stack<TreeNode*> st;
    TreeNode* curr = root;

    while (curr || !st.empty()) {
        while (curr) {
            st.push(curr);
            curr = curr->left;
        }
        curr = st.top();
        st.pop();
        res.push_back(curr->val);
        curr = curr->right;
    }
    return res;
}
```

后序遍历：先进行中右左的前序，再将结果翻转得到左右中的顺序。

**模板题目**：

无

### 4.2 子方法 B：树的遍历（BFS）

**方法说明**：使用队列实现层序遍历，记录每一层的元素个数，可用于按层处理节点。

**模板代码**：

```C++
vector<vector<int>> levelOrder(TreeNode* root) {
    queue<TreeNode*> q;
    vector<vector<int>> ret;
    if (!root) return ret;
    q.push(root);
    while(!q.empty()) {
        vector<int> ret_layer;
        int current = q.size();
        for (int i = 0; i < current; i++) {
            TreeNode* cur = q.front();
            q.pop();
            if (cur->left) q.push(cur->left);
            if (cur->right) q.push(cur->right);
            ret_layer.push_back(cur->val);
        }
        ret.push_back(ret_layer);
    }
    return ret;
}
```

**模板题目**：

无

### 4.3 子方法 C：返回值设计 - 返回 void

**方法说明**：当递归只是访问、打印、统计、累积而不改变树结构时使用。通过外部变量（引用）来保存结果。

**模板代码**：

```C++
void dfs(TreeNode* node, int& sum) {
    if (!node) return;
    sum += node->val;
    dfs(node->left, sum);
    dfs(node->right, sum);
}
```

**模板题目**：

- 0101 - 对称二叉树 ｜ [LeetCode 链接](https://leetcode.cn/problems/symmetric-tree/) ｜ [题解笔记](../solutions/0101-0200/0101-symmetric-tree.md)
- 0110 - 平衡二叉树 ｜ [LeetCode 链接](https://leetcode.cn/problems/balanced-binary-tree/) ｜ [题解笔记](../solutions/0101-0200/0110-balanced-binary-tree.md)
- 0114 - 二叉树展开为链表 ｜ [LeetCode 链接](https://leetcode.cn/problems/flatten-binary-tree-to-linked-list/) ｜ [题解笔记](../solutions/0101-0200/0114-flatten-binary-tree-to-linked-list.md)

### 4.4 子方法 D：返回值设计 - 返回 TreeNode*

**方法说明**：当递归会改变树结构（删除、修剪、构造）或需要改变指针指向时，必须返回新的子树根节点。

**模板代码**：

```C++
TreeNode* trimBST(TreeNode* root, int low, int high) {
    if (!root) return nullptr;
    if (root->val < low) return trimBST(root->right, low, high);
    if (root->val > high) return trimBST(root->left, low, high);

    root->left = trimBST(root->left, low, high);
    root->right = trimBST(root->right, low, high);
    return root;
}
```

**模板题目**：

- 0105 - 从前序与中序遍历序列构造二叉树 ｜ [LeetCode 链接](https://leetcode.cn/problems/construct-binary-tree-from-preorder-and-inorder-traversal/) ｜ [题解笔记](../solutions/0101-0200/0105-construct-binary-tree-from-preorder-and-inorder-traversal.md)
- 0106 - 从中序与后序遍历序列构造二叉树 ｜ [LeetCode 链接](https://leetcode.cn/problems/construct-binary-tree-from-inorder-and-postorder-traversal/) ｜ [题解笔记](../solutions/0101-0200/0106-construct-binary-tree-from-inorder-and-postorder-traversal.md)
- 0108 - 将有序数组转换为二叉搜索树 ｜ [LeetCode 链接](https://leetcode.cn/problems/convert-sorted-array-to-binary-search-tree/) ｜ [题解笔记](../solutions/0101-0200/0108-convert-sorted-array-to-binary-search-tree.md)
- 0226 - Invert Binary Tree ｜ [LeetCode 链接](https://leetcode.cn/problems/invert-binary-tree/) ｜ [题解笔记](../solutions/0201-0300/0226-invert-binary-tree.md)
- 0450 - 删除二叉搜索树中的节点 ｜ [LeetCode 链接](https://leetcode.cn/problems/delete-node-in-a-bst/) ｜ [题解笔记](../solutions/0401-0500/0450-delete-node-in-a-bst.md)
- 0538 - 把二叉搜索树转换为累加树 ｜ [LeetCode 链接](https://leetcode.cn/problems/convert-bst-to-greater-tree/) ｜ [题解笔记](../solutions/0501-0600/0538-convert-bst-to-greater-tree.md)
- 0617 - Merge Two Binary Trees ｜ [LeetCode 链接](https://leetcode.cn/problems/merge-two-binary-trees/) ｜ [题解笔记](../solutions/0601-0700/0617-merge-two-binary-trees.md)
- 0669 - 修剪二叉搜索树 ｜ [LeetCode 链接](https://leetcode.cn/problems/trim-a-binary-search-tree/) ｜ [题解笔记](../solutions/0601-0700/0669-trim-a-binary-search-tree.md)

### 4.5 子方法 E：返回值设计 - 返回 bool

**方法说明**：用于存在性判断或条件是否满足。一旦找到满足条件的情况就可以提前终止，避免遍历整棵树。

**模板代码**：

```C++
bool hasPathSum(TreeNode* node, int sum, int target) {
    if (!node) return false;
    sum += node->val;
    if (!node->left && !node->right) return sum == target;
    return hasPathSum(node->left, sum, target) ||
           hasPathSum(node->right, sum, target);
}
```

**模板题目**：

- 0098 - 验证二叉搜索树 ｜ [LeetCode 链接](https://leetcode.cn/problems/validate-binary-search-tree/) ｜ [题解笔记](../solutions/0001-0100/0098-validate-binary-search-tree.md)
- 0236 - 二叉树的最近公共祖先 ｜ [LeetCode 链接](https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-tree/) ｜ [题解笔记](../solutions/0201-0300/0236-lowest-common-ancestor-of-a-binary-tree.md)

### 4.6 子方法 F：返回值设计 - 返回其他类型（int/pair 等）

**方法说明**：用于值的累积或特征汇总，常见于求高度、节点数、直径、最大路径和等问题。

**模板代码**：

```C++
int maxDepth(TreeNode* node) {
    if (!node) return 0;
    int l = maxDepth(node->left);
    int r = maxDepth(node->right);
    return std::max(l, r) + 1;
}
```

**模板题目**：

- 0124 - 二叉树中的最大路径和 ｜ [LeetCode 链接](https://leetcode.cn/problems/binary-tree-maximum-path-sum/) ｜ [题解笔记](../solutions/0101-0200/0124-binary-tree-maximum-path-sum.md)
- 0437 - 路径总和 III ｜ [LeetCode 链接](https://leetcode.cn/problems/path-sum-iii/) ｜ [题解笔记](../solutions/0401-0500/0437-path-sum-iii.md)
- 0543 - 二叉树的直径 ｜ [LeetCode 链接](https://leetcode.cn/problems/diameter-of-binary-tree/) ｜ [题解笔记](../solutions/0501-0600/0543-diameter-of-binary-tree.md)
- 0701 - 二叉搜索树中的插入操作 ｜ [LeetCode 链接](https://leetcode.cn/problems/insert-into-a-binary-search-tree/) ｜ [题解笔记](../solutions/0701-0800/0701-insert-into-a-binary-search-tree.md)

### 4.7 树的序列化相关题目

- 0297 - 二叉树的序列化与反序列化 ｜ [LeetCode 链接](https://leetcode.cn/problems/serialize-and-deserialize-binary-tree/) ｜ [题解笔记](../solutions/0201-0300/0297-serialize-and-deserialize-binary-tree.md)

## 5 易错点

### 5.1 节点指针参数选择

**不需要传递节点指针**：当每次递归都独立创建或遍历子树，父节点仅需接收返回值挂接

```C++
TreeNode* build(const vector<int>& nums, int l, int r) {
    if (l >= r) return nullptr;
    int m = (l + r) / 2;
    TreeNode* root = new TreeNode(nums[m]);
    root->left = build(nums, l, m);
    root->right = build(nums, m + 1, r);
    return root;
}
```

典型用途：构建树、查找并返回新根、改变结构并返回新子树。

**需要传递节点指针**：当函数要在原有节点基础上修改或统计信息，操作依赖父层状态

```C++
void dfs(TreeNode* node, int depth, int& sum) {
    if (!node) return;
    if (!node->left && !node->right) sum += depth;
    dfs(node->left, depth + 1, sum);
    dfs(node->right, depth + 1, sum);
}
```

典型用途：访问/统计整棵树、回溯恢复状态、需要知道父节点信息或方向。

### 5.2 递归搜索策略

**只需搜索一条边**：找到满足条件的第一个则立即返回

```C++
if (递归函数(root->left)) return ;
if (递归函数(root->right)) return ;
```

**搜索整个树**：需要处理左右子树的返回值

```C++
left = 递归函数(root->left);
right = 递归函数(root->right);
// 中间逻辑处理 left 与 right
```

## 6 总结

二叉树问题的核心在于正确选择：
1. **递归返回值类型**：void（统计）、bool（存在性）、TreeNode*（修改结构）、其他（值汇总）
2. **遍历方式**：DFS（递归/迭代）或 BFS（队列）
3. **搜索策略**：搜索一条边（提前返回）vs 搜索整棵树（汇总返回）

掌握这些模板，大多数二叉树问题都可以高效解决。
