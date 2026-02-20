# 二叉树

二叉树是常见的底层数据结构，也是递归的重要应用场景

## 1 种类

- 满二叉树：所有节点都齐全的一个二叉树
- 完全二叉树：除了底层全部都满，并且 **从左到右** 连续有节点，满二叉树一定是完全二叉树
 ![搜索二叉树与满二叉树](http://oss.rainerseventeen.cn/blog/2025/20251018223257.png)
- 二叉搜索树：搜索效率是 O(log n)，节点元素有顺序，可以是左小右大
- 平衡二叉树：左子树高度和右子树高度差绝对值 **小于 1**

在 C++ 中 `std::set` / `std::multiset` / `std::map` / `std::multimap` 都由红黑树（自平衡二叉搜索树）

下方演示了如何判断平衡二叉搜索树



![](http://oss.rainerseventeen.cn/blog/2025/20251018223558.png)



## 2 存储方式

### 2.1 链式

使用左右指针即可，如果没有孩子则为 `nullptr`

代码实现如下：

```C++
struct TreeNode {
    int val;                // 节点值
    TreeNode* left;         // 左子节点
    TreeNode* right;        // 右子节点

    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}  // 构造函数
};
```



### 2.2 线性

线性存储唯一要注意的就是如何计算左右孩子，（实际上不太会用这种方式存储）

假设根节点是编号 `i` ，左孩子的 `2i + 1`， 右孩子 `2i + 2`

![](http://oss.rainerseventeen.cn/blog/2025/20251018224318.png)



## 3 遍历方式

### 3.1 深度优先搜索（DFS）

一般使用的 前中后序遍历都属于 DFS，可以使用递归或者迭代的方式实现，本质是栈 FILO

前中后指的是父节点的访问顺序

1. 前序遍历： 中左右，前序遍历是按照数据结构来**顺序**处理节点，迭代逻辑最简单
2. 中序遍历：左中右，中序遍历对二叉搜索树有**排序**的作用
3. 后序遍历：左右中，后序遍历有**回溯**的功能，能够实现类似从下向上遍历的功能

下面是两种方式实现中序遍历，注意中序遍历能够获得二叉搜索树排序后的结果

```C++
#include <vector>
void inorderRecursive(TreeNode* root, std::vector<int>& res) {
    if (!root) return;
    inorderRecursive(root->left, res);
    res.push_back(root->val);
    inorderRecursive(root->right, res);
}
```
前序遍历的 DFS （迭代）要更加简单一点，因为访问和处理的节点都是同一个

```C++
#include <vector>
#include <stack>
using namespace std;

class Solution {
public:
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
};
```
后序遍历有两步：

1. 将前序左右子树访问顺序交换： 中左右 -> 中右左
2. 将结果翻转（双指针）： 左右中


中序遍历要复杂一点，需要借助指针深度访问到底，再进行对应处理
```C++
// 迭代法中序遍历
#include <stack>
#include <vector>
std::vector<int> inorderIterative(TreeNode* root) {
    std::vector<int> res;
    std::stack<TreeNode*> st;
    TreeNode* curr = root;

    while (curr || !st.empty()) {
        // 一直向左走
        while (curr) {
            st.push(curr);
            curr = curr->left;
        }
        // 访问栈顶节点
        curr = st.top();
        st.pop();
        res.push_back(curr->val);
        // 转向右子树
        curr = curr->right;
    }
    return res;
}
```

也有一种使用标记法的方式，可以使用同一个代码结构完成 3 种遍历，稍微难理解一点

### 3.2 广度优先搜索 （BFS）

层序遍历，就是使用迭代法进行，本质是使用队列的 LIFO

注意的是需要记住每一层的队列中的元素个数

```C++
#include <vector>
#include <queue>
class Solution {
public:
    vector<vector<int>> levelOrder(TreeNode* root) {
        queue<TreeNode*> q;
        vector<vector<int>> ret;
        if (!root) return ret;
        q.push(root);
        while(!q.empty()) {
            // 取出所有的子节点
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
};
```



## 4 题目选取

> 挑选一些初见不是很顺利的题记录一下

递归的要义：

1. 返回值和输入参数
2. 终止条件
3. 递归细化逻辑

### 4.1 二叉树递归相关题目

- 0110 - 平衡二叉树 ｜ [LeetCode 链接](https://leetcode.cn/problems/balanced-binary-tree/) ｜ [题解笔记](../solutions/0101-0200/0110-balanced-binary-tree.md)
- 0106 - 从中序与后序遍历序列构造二叉树 ｜ [LeetCode 链接](https://leetcode.cn/problems/construct-binary-tree-from-inorder-and-postorder-traversal/) ｜ [题解笔记](../solutions/0101-0200/0106-construct-binary-tree-from-inorder-and-postorder-traversal.md)
- 0236 - 二叉树的最近公共祖先 ｜ [LeetCode 链接](https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-tree/) ｜ [题解笔记](../solutions/0201-0300/0236-lowest-common-ancestor-of-a-binary-tree.md)

### 4.2 二叉搜索树相关题目

- 0098 - 验证二叉搜索树 ｜ [LeetCode 链接](https://leetcode.cn/problems/validate-binary-search-tree/) ｜ [题解笔记](../solutions/0001-0100/0098-validate-binary-search-tree.md)
- 0701 - 二叉搜索树中的插入操作 ｜ [LeetCode 链接](https://leetcode.cn/problems/insert-into-a-binary-search-tree/) ｜ [题解笔记](../solutions/0701-0800/0701-insert-into-a-binary-search-tree.md)
- 0450 - 删除二叉搜索树中的节点 ｜ [LeetCode 链接](https://leetcode.cn/problems/delete-node-in-a-bst/) ｜ [题解笔记](../solutions/0401-0500/0450-delete-node-in-a-bst.md)
- 0669 - 修剪二叉搜索树 ｜ [LeetCode 链接](https://leetcode.cn/problems/trim-a-binary-search-tree/) ｜ [题解笔记](../solutions/0601-0700/0669-trim-a-binary-search-tree.md)
- 0108 - 将有序数组转换为二叉搜索树 ｜ [LeetCode 链接](https://leetcode.cn/problems/convert-sorted-array-to-binary-search-tree/) ｜ [题解笔记](../solutions/0101-0200/0108-convert-sorted-array-to-binary-search-tree.md)



## 5 易混淆点

### 5.1 节点指针参数

#### 5.1.1 不需要传递节点指针

当每次递归都**独立创建或遍历子树**，父节点仅需**接收返回值**挂接：

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

每一层都独立产生节点，不依赖外层状态，**不传当前节点指针**。
这种结构用于：

- 构建树（如 `sortedArrayToBST`）
- 查找并返回新根（如 `trimBST`、`invertTree`）
- 需要改变结构并返回新子树时

#### 5.1.2 需要传递节点指针

当函数要**在原有节点基础上修改或统计信息**，且操作依赖父层状态：

```C++
void dfs(TreeNode* node, int depth, int& sum) {
    if (!node) return;
    if (!node->left && !node->right) sum += depth;
    dfs(node->left, depth + 1, sum);
    dfs(node->right, depth + 1, sum);
}
```

典型用途：

- 访问或**统计整棵树**（遍历）
- **回溯**时要恢复状态
- 需要知道父节点信息或方向（左/右）

### 5.2 递归返回值

- 不要返回值：搜索整棵⼆叉树且不用处理递归返回值
- 需要返回值：搜索整棵⼆叉树且需要处理递归返回值
- 必须有返回：遇到符合条件的路径了就要及时返回，例如搜索其中⼀条符合条件的路径

只需要搜索⼀条边

```C++
if (递归函数(root->left)) return ;
if (递归函数(root->right)) return ;
```

搜索整个树

```C++
left = 递归函数(root->left);  // 左
right = 递归函数(root->right); // 右
left与right的逻辑处理;         // 中 
```
#### 5.2.1 返回 `void`

当递归只是**访问、打印、统计、累积**而不改变结构，这种函数只是向外输出或修改外部变量，不需要返回子树。

```C++
void preorder(TreeNode* node) { ... }
void dfs(TreeNode* node, int& sum) { ... }
```

#### 5.2.2 返回 `TreeNode*`

父节点要拿到新的子树根进行挂接，递归**会改变树结构**（删除、修剪、构造）：

```C++
TreeNode* trimBST(TreeNode* root, int low, int high);
TreeNode* invertTree(TreeNode* root);
TreeNode* deleteNode(TreeNode* root, int key);
```



#### 5.2.3 返回 `bool`

用于**存在性判断 / 条件是否满足**，当子树满足条件时应提前终止或者向上报告

- 一旦有一个分支返回 `true`，整棵递归可结束。
- 常用于“是否存在路径”、“是否对称”、“是否平衡”等问题。

```C++
bool hasPathSum(TreeNode* node, int sum, int target) {
    if (!node) return false;
    sum += node->val;
    if (!node->left && !node->right) return sum == target;
    return hasPathSum(node->left, sum, target) || 
           hasPathSum(node->right, sum, target);
}
```



#### 5.2.4 返回其他类型

常用于**值的累积 / 特征汇总**，常用于求**高度、节点数、直径、最大路径和**等。

```C++
int maxDepth(TreeNode* node) {
    if (!node) return 0;
    int l = maxDepth(node->left);
    int r = maxDepth(node->right);
    return std::max(l, r) + 1;
}
```
