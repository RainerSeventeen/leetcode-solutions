# 网格图（DFS/BFS/综合应用）

## 概览
网格图问题把二维坐标视作图节点，常见目标是连通块统计、可达性判断与最短路计算。

## 核心思想
- 用方向数组统一相邻扩展，降低边界与分支错误。
- 连通性优先考虑 DFS/BFS；无权最短路优先 BFS；边权为 0/1 时优先 0-1 BFS。
- 当代价为一般非负权重时使用 Dijkstra；综合题常需多种方法组合。

## 解题流程
1. 明确任务类型：连通块、最短路、状态搜索或混合建模。
2. 定义状态与转移：坐标、方向、额外状态（钥匙、朝向、障碍消耗等）。
3. 选择算法并写模板：DFS/BFS/0-1 BFS/Dijkstra。
4. 校验边界场景：空网格、单行单列、起终点重合、不可达。

## 模板与子方法
### 网格图 DFS
#### 连通块 DFS
模板：

```python
from typing import List


def dfs_grid(grid: List[List[str]]) -> List[int]:
    m, n = len(grid), len(grid[0])
    vis = [[False] * n for _ in range(m)]

    def dfs(i: int, j: int) -> int:
        vis[i][j] = True
        size = 1
        for x, y in ((i, j - 1), (i, j + 1), (i - 1, j), (i + 1, j)):
            if 0 <= x < m and 0 <= y < n and grid[x][y] == '1' and not vis[x][y]:
                size += dfs(x, y)
        return size

    comp_size: List[int] = []
    for i in range(m):
        for j in range(n):
            if grid[i][j] == '1' and not vis[i][j]:
                comp_size.append(dfs(i, j))
    return comp_size
```

模板题目：

- 0200 - 岛屿数量 ｜ [LeetCode 链接](https://leetcode.cn/problems/number-of-islands/) ｜ [题解笔记](../solutions/0101-0200/0200-number-of-islands.md)

### 网格图 BFS
#### 无权最短路 BFS
模板：

```python
from collections import deque
from typing import List


def bfs_grid(grid: List[List[str]], sx: int, sy: int) -> List[List[int]]:
    m, n = len(grid), len(grid[0])
    dist = [[-1] * n for _ in range(m)]
    dist[sx][sy] = 0
    q = deque([(sx, sy)])

    while q:
        i, j = q.popleft()
        for x, y in ((i, j - 1), (i, j + 1), (i - 1, j), (i + 1, j)):
            if 0 <= x < m and 0 <= y < n and grid[x][y] == '.' and dist[x][y] < 0:
                dist[x][y] = dist[i][j] + 1
                q.append((x, y))

    return dist
```

模板题目：

待补充...

### 网格图 0-1 BFS
#### 边权为 0 或 1 的最短路
模板：

```python
from collections import deque
from typing import List


def zero_one_bfs(grid: List[List[int]]) -> int:
    m, n = len(grid), len(grid[0])
    inf = 10**18
    dist = [[inf] * n for _ in range(m)]
    dist[0][0] = 0
    dq = deque([(0, 0)])

    while dq:
        i, j = dq.popleft()
        for x, y in ((i, j - 1), (i, j + 1), (i - 1, j), (i + 1, j)):
            if not (0 <= x < m and 0 <= y < n):
                continue
            w = grid[x][y]  # 题意中的 0/1 边权
            nd = dist[i][j] + w
            if nd < dist[x][y]:
                dist[x][y] = nd
                if w == 0:
                    dq.appendleft((x, y))
                else:
                    dq.append((x, y))

    return dist[m - 1][n - 1]
```

模板题目：

待补充...

### 网格图 Dijkstra
#### 非负权最短路
模板：

```python
import heapq
from typing import List


def dijkstra_grid(cost: List[List[int]]) -> int:
    m, n = len(cost), len(cost[0])
    inf = 10**18
    dist = [[inf] * n for _ in range(m)]
    dist[0][0] = cost[0][0]
    pq = [(cost[0][0], 0, 0)]

    while pq:
        d, i, j = heapq.heappop(pq)
        if d != dist[i][j]:
            continue
        if (i, j) == (m - 1, n - 1):
            return d
        for x, y in ((i, j - 1), (i, j + 1), (i - 1, j), (i + 1, j)):
            if not (0 <= x < m and 0 <= y < n):
                continue
            nd = d + cost[x][y]
            if nd < dist[x][y]:
                dist[x][y] = nd
                heapq.heappush(pq, (nd, x, y))

    return dist[m - 1][n - 1]
```

模板题目：

待补充...

### 综合应用
#### 多状态网格搜索
模板：

```python
from collections import deque
from typing import List, Set, Tuple


def multi_state_bfs(grid: List[List[str]]) -> int:
    m, n = len(grid), len(grid[0])
    start = (0, 0, 0)  # (x, y, state)
    q = deque([(0, 0, 0, 0)])
    vis: Set[Tuple[int, int, int]] = {start}

    while q:
        i, j, st, step = q.popleft()
        # 按题意判断目标态
        for x, y in ((i, j - 1), (i, j + 1), (i - 1, j), (i + 1, j)):
            if not (0 <= x < m and 0 <= y < n):
                continue
            nst = st  # 按题意更新状态（钥匙、机关、朝向等）
            key = (x, y, nst)
            if key not in vis:
                vis.add(key)
                q.append((x, y, nst, step + 1))

    return -1
```

模板题目：

待补充...

## 易错点
- 访问标记时机错误会导致重复入队或重复递归。
- 方向扩展与边界判断不统一，容易出现漏搜和越界。
- 多状态搜索若未把状态纳入 visited，会产生错误剪枝。

## 总结
网格图题目本质是图搜索与最短路建模，优先统一状态与边界，再按权重和目标选择 DFS/BFS/0-1 BFS/Dijkstra 或组合方法。
