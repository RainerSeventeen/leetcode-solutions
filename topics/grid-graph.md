# 网格与图

## 1 概览
网格题可视为隐式图搜索，常见目标是连通块计数、可达性判断、最短步数与网格状态转移。

## 2 核心思想
- 网格 DFS/BFS：把坐标当节点，方向移动当边。
- 层序 BFS：用于无权最短路步数。
- 网格 DP：当转移方向固定时可由搜索转为递推。

## 3 解题流程
1. 判断是连通性、最短路还是固定方向转移。
2. 统一边界检查与访问标记策略。
3. 选 DFS、BFS 或 DP 并写出状态更新。
4. 处理空网格、单行单列、起终点重合等边界。

## 4 模板与子方法
### 4.1 网格 DFS 连通块
方法说明：
用于岛屿数量、封闭区域等连通块问题。与图算法专题可交叉，但这里强调二维坐标递归。

模板代码：
```python
def num_islands(grid):
    m, n = len(grid), len(grid[0])

    def dfs(i, j):
        if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] != '1':
            return
        grid[i][j] = '0'
        dfs(i + 1, j)
        dfs(i - 1, j)
        dfs(i, j + 1)
        dfs(i, j - 1)
```

#### 4.1.1 模板题目
- 0200 - 岛屿数量（DFS 版本） ｜ [LeetCode 链接](https://leetcode.cn/problems/number-of-islands/) ｜ [题解笔记](../solutions/0201-0300/0200-number-of-islands.md)
### 4.2 网格 BFS 连通块
方法说明：
与 DFS 同类问题的队列写法，适合避免递归栈过深。

模板代码：
```python
from collections import deque


def bfs_mark(grid, si, sj):
    m, n = len(grid), len(grid[0])
    q = deque([(si, sj)])
    grid[si][sj] = '0'
    while q:
        i, j = q.popleft()
        for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            ni, nj = i + di, j + dj
            if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == '1':
                grid[ni][nj] = '0'
                q.append((ni, nj))
```

#### 4.2.1 模板题目
- 0200 - 岛屿数量（BFS 版本） ｜ [LeetCode 链接](https://leetcode.cn/problems/number-of-islands/) ｜ [题解笔记](../solutions/0201-0300/0200-number-of-islands.md)
### 4.3 网格搜索与有序剪枝
方法说明：
当矩阵行列有序时，可从角点线性收缩；同题也可按行二分，属于二分专题交叉。

模板代码：
```python
def search_matrix(matrix, target):
    m, n = len(matrix), len(matrix[0])
    i, j = 0, n - 1
    while i < m and j >= 0:
        if matrix[i][j] == target:
            return True
        if matrix[i][j] > target:
            j -= 1
        else:
            i += 1
    return False
```

#### 4.3.1 模板题目
- 0240 - 搜索二维矩阵 II ｜ [LeetCode 链接](https://leetcode.cn/problems/search-a-2d-matrix-ii/) ｜ [题解笔记](../solutions/0201-0300/0240-search-a-2d-matrix-ii.md)
### 4.4 网格 DP 路径转移
方法说明：
当移动方向固定（如仅右/下）时，用 DP 比搜索更直接；题目主归属可在动态规划专题。

模板代码：
```python
def unique_paths(m, n):
    dp = [[1] * n for _ in range(m)]
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    return dp[-1][-1]
```

#### 4.4.1 模板题目
- 0062 - Unique Paths ｜ [LeetCode 链接](https://leetcode.cn/problems/unique-paths/) ｜ [题解笔记](../solutions/0001-0100/0062-unique-paths.md)
- 0064 - Minimum Path Sum ｜ [LeetCode 链接](https://leetcode.cn/problems/minimum-path-sum/) ｜ [题解笔记](../solutions/0001-0100/0064-minimum-path-sum.md)
- 0221 - Maximal Square ｜ [LeetCode 链接](https://leetcode.cn/problems/maximal-square/) ｜ [题解笔记](../solutions/0201-0300/0221-maximal-square.md)
- 0085 - Maximal Rectangle ｜ [LeetCode 链接](https://leetcode.cn/problems/maximal-rectangle/) ｜ [题解笔记](../solutions/0001-0100/0085-maximal-rectangle.md)
### 4.5 网格回溯搜索
方法说明：
用于路径匹配与约束搜索，状态需要“访问标记 + 回撤”；可交叉到回溯专题。

模板代码：
```python
def exist(board, word):
    m, n = len(board), len(board[0])

    def dfs(i, j, k):
        if k == len(word):
            return True
        if i < 0 or i >= m or j < 0 or j >= n or board[i][j] != word[k]:
            return False
        ch = board[i][j]
        board[i][j] = '#'
        ok = dfs(i + 1, j, k + 1) or dfs(i - 1, j, k + 1) or dfs(i, j + 1, k + 1) or dfs(i, j - 1, k + 1)
        board[i][j] = ch
        return ok
```

#### 4.5.1 模板题目
- 0079 - Word Search ｜ [LeetCode 链接](https://leetcode.cn/problems/word-search/) ｜ [题解笔记](../solutions/0001-0100/0079-word-search.md)
- 0048 - 旋转图像 ｜ [LeetCode 链接](https://leetcode.cn/problems/rotate-image/) ｜ [题解笔记](../solutions/0001-0100/0048-rotate-image.md)
## 5 易错点
- 访问标记时机错误导致重复入队/重复递归。
- 越界判断遗漏引发下标错误。
- 搜索题混入 DP 思路时状态定义不一致。

## 6 总结
网格题先抽象为图，再根据目标在 DFS、BFS、DP、回溯间选择；统一坐标边界与访问策略能避免多数 bug。
