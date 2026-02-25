# 图论算法（DFS/BFS/拓扑排序/基环树/最短路/最小生成树/网络流）

## 1 概览
图算法处理节点与边关系，核心任务包括连通性、环检测、拓扑排序、最小生成树与路径可达。

图模型常见分类：

- 有向图 / 无向图
- 无权图 / 带权图
- 稠密图 / 稀疏图

基础概念：

- 度：无向图中表示与该点相连的边数；有向图中细分为入度和出度。
- 连通图：无向图中任意两点可达。
- 强连通图：有向图中任意两点互相可达。
- 连通分量 / 强连通分量：图中彼此可达的极大子图。

## 2 核心思想
- 遍历：BFS/DFS 解决可达性与分层。
- 并查集：维护动态连通性与判环。
- 拓扑排序：在 DAG 中按依赖顺序处理。
- 最小生成树：在连通图中以最小代价连通所有点。

## 3 解题流程
1. 明确图模型：有向/无向，带权/无权，稀疏/稠密。
2. 选择算法：遍历、并查集、拓扑、MST。
3. 设计数据结构：邻接矩阵、邻接表、入度数组、并查集父节点。
4. 明确存储取舍：

   - 邻接矩阵：查询两点是否相连简单，适合稠密图，但空间为 $O(n^2)$。
   - 邻接表：空间随边数增长，适合稀疏图，遍历邻边更自然。
   - 边集：适合 Kruskal 这类“按边处理”的算法。
5. 验证终止条件：是否全访问、是否存在环、是否连通。

## 4 模板与子方法
### 4.1 图建模与存储选择
#### 4.1.1 模板题目
- 1557 - 可以到达所有点的最少点数目 ｜ [LeetCode 链接](https://leetcode.cn/problems/minimum-number-of-vertices-to-reach-all-nodes/) ｜ [题解笔记](../solutions/1501-1600/1557-minimum-number-of-vertices-to-reach-all-nodes.md)

方法说明：

做图题前先定“点是什么、边是什么、边是否带方向与权重”。模型一旦确定，再选存储方式；存储结构会直接决定后续遍历和更新代价。

常见存储方式：

- 边集：实现简单，适合只关心边本身的场景（如 Kruskal）。
- 邻接矩阵：`graph[u][v]` 查询直接，代价是空间固定且高。
- 邻接表：工程与刷题最常用；能自然遍历 `u` 的所有邻边。

一般来说，除了完全图，其他的都是用邻接表就行了

### 4.2 深度优先搜索 DFS
方法说明：

DFS 的核心是“沿一条路走到底，再回溯换路”。当问题是“枚举路径”“判断是否可达”“做连通块涂色”时常用。

DFS 三部曲：

1. 确定函数签名和参数（当前节点、访问状态、路径/答案容器）。
2. 明确终止条件（到终点、越界、重复访问等）；终止条件是正确性核心。
3. 写递归与回溯逻辑（进入、递归、撤销）。

实战要点：

- 有环图必须配合 `visited`，否则会无限递归。
- “先标记再递归”通常更稳妥，避免同层重复进入。
- 在路径枚举题中，`path.append` 与 `path.pop` 必须严格成对。

模板代码：

```python
from collections import defaultdict


def dfs(start, edges):
    g = defaultdict(list)
    for u, v in edges:
        g[u].append(v)

    vis = set()

    def walk(u):
        vis.add(u)
        for v in g[u]:
            if v not in vis:
                walk(v)

    walk(start)
    return vis
```

#### 4.2.1 模板题目
- 0094 - 二叉树的中序遍历 ｜ [LeetCode 链接](https://leetcode.cn/problems/binary-tree-inorder-traversal/) ｜ [题解笔记](../solutions/0001-0100/0094-binary-tree-inorder-traversal.md)
- 0144 - 二叉树的前序遍历 ｜ [LeetCode 链接](https://leetcode.cn/problems/binary-tree-preorder-traversal/) ｜ [题解笔记](../solutions/0101-0200/0144-binary-tree-preorder-traversal.md)
- 0257 - 二叉树的所有路径 ｜ [LeetCode 链接](https://leetcode.cn/problems/binary-tree-paths/) ｜ [题解笔记](../solutions/0201-0300/0257-binary-tree-paths.md)
- 0501 - 二叉搜索树中的众数 ｜ [LeetCode 链接](https://leetcode.cn/problems/find-mode-in-binary-search-tree/) ｜ [题解笔记](../solutions/0501-0600/0501-find-mode-in-binary-search-tree.md)

### 4.3 广度优先搜索 BFS
方法说明：

BFS 按“层”扩散，天然适合最短步数（无权图）与分层遍历。实现上通常使用队列。

层数处理：

- 每轮固定处理当前 `len(queue)` 个节点，即一整层。
- 处理完一层后，层数 `+1`，可直接对应“第几步可达”。

实战要点：

- 入队时就标记 `visited`，避免同一节点被重复入队。
- 网格题可把四方向或八方向移动视作图上的邻接边。

模板代码：

```python
from collections import deque, defaultdict


def bfs(start, edges):
    g = defaultdict(list)
    for u, v in edges:
        g[u].append(v)

    q = deque([start])
    vis = {start}
    level = 0
    while q:
        for _ in range(len(q)):
            u = q.popleft()
            for v in g[u]:
                if v not in vis:
                    vis.add(v)
                    q.append(v)
        level += 1
    return vis, level
```

#### 4.3.1 模板题目
- 0339 - 除法求值 ｜ [LeetCode 链接](https://leetcode.cn/problems/evaluate-division/) ｜ [题解笔记](../solutions/0301-0400/0399-evaluate-division.md)
- 0102 - 二叉树的层序遍历 ｜ [LeetCode 链接](https://leetcode.cn/problems/binary-tree-level-order-traversal/) ｜ [题解笔记](../solutions/0101-0200/0102-binary-tree-level-order-traversal.md)
- 0104 - 二叉树的最大深度 ｜ [LeetCode 链接](https://leetcode.cn/problems/maximum-depth-of-binary-tree/) ｜ [题解笔记](../solutions/0101-0200/0104-maximum-depth-of-binary-tree.md)
- 0112 - 路径总和 ｜ [LeetCode 链接](https://leetcode.cn/problems/path-sum/) ｜ [题解笔记](../solutions/0101-0200/0112-path-sum.md)
- 0116 - 填充每个节点的下一个右侧节点指针 ｜ [LeetCode 链接](https://leetcode.cn/problems/populating-next-right-pointers-in-each-node/) ｜ [题解笔记](../solutions/0101-0200/0116-populating-next-right-pointers-in-each-node.md)
- 0127 - 单词接龙 ｜ [LeetCode 链接](https://leetcode.cn/problems/word-ladder/) ｜ [题解笔记](../solutions/0101-0200/0127-word-ladder.md)
- 0404 - 左叶子之和 ｜ [LeetCode 链接](https://leetcode.cn/problems/sum-of-left-leaves/) ｜ [题解笔记](../solutions/0401-0500/0404-sum-of-left-leaves.md)
- 0433 - 最小基因变化 ｜ [LeetCode 链接](https://leetcode.cn/problems/minimum-genetic-mutation/) ｜ [题解笔记](../solutions/0401-0500/0433-minimum-genetic-mutation.md)
- 0530 - 二叉搜索树的最小绝对差 ｜ [LeetCode 链接](https://leetcode.cn/problems/minimum-absolute-difference-in-bst/) ｜ [题解笔记](../solutions/0501-0600/0530-minimum-absolute-difference-in-bst.md)
- 0813 - 所有可能的路径 ｜ [LeetCode 链接](https://leetcode.cn/problems/all-paths-from-source-to-target/) ｜ [题解笔记](../solutions/0701-0800/0797-all-paths-from-source-to-target.md)
- 1306 - 跳跃游戏 III ｜ [LeetCode 链接](https://leetcode.cn/problems/jump-game-iii/) ｜ [题解笔记](../solutions/1301-1400/1306-jump-game-iii.md)
- 1311 - 获取你好友已观看的视频 ｜ [LeetCode 链接](https://leetcode.cn/problems/get-watched-videos-by-your-friends/) ｜ [题解笔记](../solutions/1301-1400/1311-get-watched-videos-by-your-friends.md)
- 3243 - 新增道路查询后的最短距离 I ｜ [LeetCode 链接](https://leetcode.cn/problems/shortest-distance-after-road-addition-queries-i/) ｜ [题解笔记](../solutions/3201-3300/3243-shortest-distance-after-road-addition-queries-i.md)

### 4.4 并查集
方法说明：

适用于“动态合并集合 + 连通性查询 + 判环”。结构上维护每个节点的父节点，`find` 找根，`union` 合并根。

优化要点：

- 路径压缩：把查询路径上的节点直接挂到根，降低后续查询深度。
- 按秩/按大小合并：让小树挂大树，控制树高增长。
- `union` 前先判同根并提前返回，否则会错误累计大小/秩。

为什么优化有效：

- 仅路径压缩可显著减少重复查询链路。
- 与按秩合并叠加后，树高长期保持很低，均摊复杂度接近常数。

模板代码：

```python
class DSU:
    def __init__(self, n):
        self.fa = list(range(n))
        self.sz = [1] * n

    def find(self, x):
        while self.fa[x] != x:
            self.fa[x] = self.fa[self.fa[x]]
            x = self.fa[x]
        return x

    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return False
        if self.sz[ra] < self.sz[rb]:
            ra, rb = rb, ra
        self.fa[rb] = ra
        self.sz[ra] += self.sz[rb]
        return True
```

#### 4.4.1 模板题目
- 0684 - 冗余连接 ｜ [LeetCode 链接](https://leetcode.cn/problems/redundant-connection/) ｜ [题解笔记](../solutions/0601-0700/0684-redundant-connection.md)
- 0547 - 省份数量 ｜ [LeetCode 链接](https://leetcode.cn/problems/number-of-provinces/) ｜ [题解笔记](../solutions/0501-0600/0547-number-of-provinces.md)
- 0685 - 冗余连接 II ｜ [LeetCode 链接](https://leetcode.cn/problems/redundant-connection-ii/) ｜ [题解笔记](../solutions/0601-0700/0685-redundant-connection-ii.md)
- 1971 - 寻找图中是否存在路径 ｜ [LeetCode 链接](https://leetcode.cn/problems/find-if-path-exists-in-graph/) ｜ [题解笔记](../solutions/1901-2000/1971-find-if-path-exists-in-graph.md)
- 2316 - 统计无向图中无法互相到达点对数 ｜ [LeetCode 链接](https://leetcode.cn/problems/count-unreachable-pairs-of-nodes-in-an-undirected-graph/) ｜ [题解笔记](../solutions/2301-2400/2316-count-unreachable-pairs-of-nodes-in-an-undirected-graph.md)

### 4.5 拓扑排序
方法说明：

适用于先修依赖、任务顺序。Kahn 算法通过入度为 0 的节点逐层剥离。

模板代码：

```python
from collections import deque


def can_finish(num_courses, prerequisites):
    g = [[] for _ in range(num_courses)]
    indeg = [0] * num_courses
    for a, b in prerequisites:
        g[b].append(a)
        indeg[a] += 1
    q = deque([i for i, d in enumerate(indeg) if d == 0])
    cnt = 0
    while q:
        u = q.popleft()
        cnt += 1
        for v in g[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)
    return cnt == num_courses
```

#### 4.5.1 模板题目
- 0207 - 课程表 ｜ [LeetCode 链接](https://leetcode.cn/problems/course-schedule/) ｜ [题解笔记](../solutions/0201-0300/0207-course-schedule.md)
- 0310 - 最小高度树 ｜ [LeetCode 链接](https://leetcode.cn/problems/minimum-height-trees/) ｜ [题解笔记](../solutions/0301-0400/0310-minimum-height-trees.md)
- 0851 - 喧闹和富有 ｜ [LeetCode 链接](https://leetcode.cn/problems/loud-and-rich/) ｜ [题解笔记](../solutions/0801-0900/0851-loud-and-rich.md)
- 2392 - 给定条件下构造矩阵 ｜ [LeetCode 链接](https://leetcode.cn/problems/build-a-matrix-with-conditions/) ｜ [题解笔记](../solutions/2301-2400/2392-build-a-matrix-with-conditions.md)
- 0210 - 课程表 II ｜ [LeetCode 链接](https://leetcode.cn/problems/course-schedule-ii/) ｜ [题解笔记](../solutions/0201-0300/0210-course-schedule-ii.md)
- 3310 - 移除可疑的方法 ｜ [LeetCode 链接](https://leetcode.cn/problems/remove-methods-from-project/) ｜ [题解笔记](../solutions/3301-3400/3310-remove-methods-from-project.md)

### 4.6 最小生成树 MST（Kruskal/Prim）
方法说明：

用于“以最小代价连通全部节点”。

关键理解：

- 目标结构必须是树：包含全部节点、边数为 `n - 1`、且不能有环。
- 这与“判环/去环”问题互补：MST 过程本质是选边且持续避免形成环。
- Prim：从“点集”向外扩展，通常适合稠密图。
- Kruskal：从“边”出发按权排序，通常适合稀疏图。需要并查集判环。

模板代码：

```python
def kruskal(n, edges):
    dsu = DSU(n)
    cost = 0
    used = 0
    for w, u, v in sorted(edges):
        if dsu.union(u, v):
            cost += w
            used += 1
            if used == n - 1:
                break
    return cost if used == n - 1 else -1
```

#### 4.6.1 模板题目
- 1584 - 连接所有点的最小费用 ｜ [LeetCode 链接](https://leetcode.cn/problems/min-cost-to-connect-all-points/) ｜ [题解笔记](../solutions/1501-1600/1584-min-cost-to-connect-all-points.md)

### 4.7 基环树
方法说明：

每个节点最多一条出边的图可视为“若干入树指向若干环”。常见做法是沿出边线性推进并记录访问状态与步数，遇到 `-1` 或已访问节点时停止（有点像拓扑排序）。

如果是找环的题目（一个联通块只有一个环）
1. 对所有的入口遍历一回，记录一个开始时间，然后对所有到达的节点记录访问时间
2. 一旦遇到已经访问的节点就立刻停止，然后判断是否是本轮的循环，是就记录时间，否则已经标记过


#### 4.7.1 模板题目
- 2359 - 找到离给定两个节点最近的节点 ｜ [LeetCode 链接](https://leetcode.cn/problems/find-closest-node-to-given-two-nodes/) ｜ [题解笔记](../solutions/2301-2400/2359-find-closest-node-to-given-two-nodes.md)
- 2360 - 图中的最长环 ｜ [LeetCode 链接](https://leetcode.cn/problems/longest-cycle-in-a-graph/) ｜ [题解笔记](../solutions/2301-2400/2360-longest-cycle-in-a-graph.md)

### 4.8 单源最短路（Dijkstra）
方法说明：

Dijktra 算法用于求从某个点出发，有向有权图最短路径，算法和 prim 算法有一定的相似度，都是逐渐扩展区域

1. 选择距离出发点最近的，同时没有访问过的节点
2. 将该点标记为已经访问
3. 更新所有为访问的节点与出发点之间的距离

模板代码：

```python
def dijkstra(graph, start): # 邻接矩阵 + 数组暴力
    n = len(graph)
    INF = float('inf')
    dist = [INF] * n        # 记录最短距离
    visited = [False] * n  # 是否已经确定
    dist[start] = 0
    
    for _ in range(n):
        # 找当前未访问的最小距离节点，从 start 开始更新相连路径
        u = -1
        for i in range(n):
            if not visited[i] and (u == -1 or dist[i] < dist[u]): 
                u = i # 一个初始条件的设置小技巧, u == -1 短路
        
        if u == -1:
            break # 如果没有可选节点，结束

		# 用 u 更新其他节点
        visited[u] = True
        for v in range(n):
            if not visited[v] and graph[u][v] != INF:
                dist[v] = min(dist[v], dist[u] + graph[u][v])

    return dist    
```

这是优化后的版本：

1. 使用堆，优化了查找下一个最短距离节点
2. 使用邻接表，优化扫描无效边的步骤，跳过了实际不存在的边

```python
import heapq # 最小堆
def dijkstra(n, adj, start): # n 节点数, adj 出度邻接表, start 起始点
    INF = float("inf")
    dist = [INF] * n
    dist[start] = 0

    pq = [(0, start)]  # (最短距离, 节点)

    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]: 	# 旧的记录，直接跳过
            continue

        for v, w in adj[u]:
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                # 注意这里没有删除旧的（代价太大），而是直接 push 一个更小的进去
                heapq.heappush(pq, (nd, v))	

    return dist
```

#### 4.8.1 模板题目
- 0743 - 网络延迟时间 ｜ [LeetCode 链接](https://leetcode.cn/problems/network-delay-time/) ｜ [题解笔记](../solutions/0701-0800/0743-network-delay-time.md)

## 5 易错点

- 遍历未去重导致重复扩展或死循环。
- DFS 递归没有清晰终止条件，导致漏解或爆栈。
- BFS 在出队时才标记访问，导致重复入队。
- 并查集合并前未 `find` 根节点，或同根时没有提前返回。
- 并查集只做路径压缩、不做按秩合并，在极端数据上性能退化。
- 拓扑排序未检查处理节点总数。
- MST 未判断是否真正连通全部点。

## 6 总结
图题先定模型与存储，再在遍历、并查集、拓扑、MST 中选工具；正确性依赖于不变量、边界条件和终止校验。
