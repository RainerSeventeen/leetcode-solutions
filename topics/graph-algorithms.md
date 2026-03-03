# 图论算法（DFS/BFS/拓扑排序/基环树/最短路/最小生成树/网络流）

## 概览
图论专题覆盖图遍历、拓扑排序、最短路、最小生成树、连通分量、二分图与网络流等核心问题。

## 核心思想
- 先建模：明确有向/无向、带权/无权，再确定点与边含义。
- 再选算法：可达性用 DFS/BFS，依赖关系用拓扑排序，路径代价用最短路，连通代价用 MST。
- 最后落地：围绕邻接表、入度数组、并查集、堆与状态压缩实现。

## 解题流程
1. 抽象图模型与状态表示。
2. 选择匹配算法并写出终止条件。
3. 用模板实现并校验边界（重边、自环、不可达、环检测）。

## 模板与子方法
### 图的遍历

#### 深度优先搜索（DFS）
模板：

```python
def solve(n: int, edges: List[List[int]]) -> List[int]:
    # 节点编号从 0 到 n-1
    g = [[] for _ in range(n)]
    for x, y in edges:
        g[x].append(y)
        g[y].append(x)  # 无向图

    vis = [False] * n

    def dfs(x: int) -> int:
        vis[x] = True  # 避免重复访问节点
        size = 1
        for y in g[x]:
            if not vis[y]:
                size += dfs(y)
        return size

    # 计算每个连通块的大小
    ans = []
    for i, b in enumerate(vis):
        if not b:  # i 没有访问过
            size = dfs(i)
            ans.append(size)
    return ans
```

模板题目：

- 0547 - 省份数量 ｜ [LeetCode 链接](https://leetcode.cn/problems/number-of-provinces/) ｜ [题解笔记](../solutions/0501-0600/0547-number-of-provinces.md)
- 1971 - 寻找图中是否存在路径 ｜ [LeetCode 链接](https://leetcode.cn/problems/find-if-path-exists-in-graph/) ｜ [题解笔记](../solutions/1901-2000/1971-find-if-path-exists-in-graph.md)
- 0797 - 所有可能的路径 ｜ [LeetCode 链接](https://leetcode.cn/problems/all-paths-from-source-to-target/) ｜ [题解笔记](../solutions/0701-0800/0797-all-paths-from-source-to-target.md)
- 1306 - 跳跃游戏 III ｜ [LeetCode 链接](https://leetcode.cn/problems/jump-game-iii/) ｜ [题解笔记](../solutions/1301-1400/1306-jump-game-iii.md)
- 2316 - 统计无向图中无法互相到达点对数 ｜ [LeetCode 链接](https://leetcode.cn/problems/count-unreachable-pairs-of-nodes-in-an-undirected-graph/) ｜ [题解笔记](../solutions/2301-2400/2316-count-unreachable-pairs-of-nodes-in-an-undirected-graph.md)
- 3310 - 移除可疑的方法 ｜ [LeetCode 链接](https://leetcode.cn/problems/remove-methods-from-project/) ｜ [题解笔记](../solutions/3301-3400/3310-remove-methods-from-project.md)
- 0207 - 课程表 ｜ [LeetCode 链接](https://leetcode.cn/problems/course-schedule/) ｜ [题解笔记](../solutions/0201-0300/0207-course-schedule.md)

#### 广度优先搜索（BFS）
模板：

```python
# 计算从 start 到各个节点的最短路长度
# 如果节点不可达，则最短路长度为 -1
# 节点编号从 0 到 n-1，边权均为 1
def bfs(n: int, edges: List[List[int]], start: int) -> List[int]:
    g = [[] for _ in range(n)]
    for x, y in edges:
        g[x].append(y)
        g[y].append(x)  # 无向图

    dis = [-1] * n  # -1 表示尚未访问到
    dis[start] = 0
    q = deque([start])
    while q:
        x = q.popleft()
        for y in g[x]:
            if dis[y] < 0:
                dis[y] = dis[x] + 1
                q.append(y)
    return dis
```

模板题目：

- 3243 - 新增道路查询后的最短距离 I ｜ [LeetCode 链接](https://leetcode.cn/problems/shortest-distance-after-road-addition-queries-i/) ｜ [题解笔记](../solutions/3201-3300/3243-shortest-distance-after-road-addition-queries-i.md)
- 1311 - 获取你好友已观看的视频 ｜ [LeetCode 链接](https://leetcode.cn/problems/get-watched-videos-by-your-friends/) ｜ [题解笔记](../solutions/1301-1400/1311-get-watched-videos-by-your-friends.md)

#### 图论建模 + BFS 最短路
模板：

```python
# 待补充
```

模板题目：

- 0433 - 最小基因变化 ｜ [LeetCode 链接](https://leetcode.cn/problems/minimum-genetic-mutation/) ｜ [题解笔记](../solutions/0401-0500/0433-minimum-genetic-mutation.md)
- 0127 - 单词接龙 ｜ [LeetCode 链接](https://leetcode.cn/problems/word-ladder/) ｜ [题解笔记](../solutions/0101-0200/0127-word-ladder.md)

### 拓扑排序

#### 拓扑排序
模板：

```python
# 返回有向无环图（DAG）的其中一个拓扑序
# 如果图中有环，返回空列表
# 节点编号从 0 到 n-1
def topologicalSort(n: int, edges: List[List[int]]) -> List[int]:
    g = [[] for _ in range(n)]
    in_deg = [0] * n
    for x, y in edges:
        g[x].append(y)
        in_deg[y] += 1  # 统计 y 的先修课数量

    topo_order = []
    q = deque(i for i, d in enumerate(in_deg) if d == 0)  # 没有先修课，可以直接上
    while q:
        x = q.popleft()
        topo_order.append(x)
        for y in g[x]:
            in_deg[y] -= 1  # 修完 x 后，y 的先修课数量减一
            if in_deg[y] == 0:  # y 的先修课全部上完
                q.append(y)  # 加入学习队列

    if len(topo_order) < n:  # 图中有环
        return []
    return topo_order
```

模板题目：

- 0210 - 课程表 II ｜ [LeetCode 链接](https://leetcode.cn/problems/course-schedule-ii/) ｜ [题解笔记](../solutions/0201-0300/0210-course-schedule-ii.md)
- 2392 - 给定条件下构造矩阵 ｜ [LeetCode 链接](https://leetcode.cn/problems/build-a-matrix-with-conditions/) ｜ [题解笔记](../solutions/2301-2400/2392-build-a-matrix-with-conditions.md)
- 0310 - 最小高度树 ｜ [LeetCode 链接](https://leetcode.cn/problems/minimum-height-trees/) ｜ [题解笔记](../solutions/0301-0400/0310-minimum-height-trees.md)

#### 在拓扑序上 DP
模板：

```python
# 待补充
```

模板题目：

- 0851 - 喧闹和富有 ｜ [LeetCode 链接](https://leetcode.cn/problems/loud-and-rich/) ｜ [题解笔记](../solutions/0801-0900/0851-loud-and-rich.md)

#### 基环树
模板：

```python
# 待补充
```

模板题目：

- 2359 - 找到离给定两个节点最近的节点 ｜ [LeetCode 链接](https://leetcode.cn/problems/find-closest-node-to-given-two-nodes/) ｜ [题解笔记](../solutions/2301-2400/2359-find-closest-node-to-given-two-nodes.md)
- 2360 - 图中的最长环 ｜ [LeetCode 链接](https://leetcode.cn/problems/longest-cycle-in-a-graph/) ｜ [题解笔记](../solutions/2301-2400/2360-longest-cycle-in-a-graph.md)
- 0684 - 冗余连接 ｜ [LeetCode 链接](https://leetcode.cn/problems/redundant-connection/) ｜ [题解笔记](../solutions/0601-0700/0684-redundant-connection.md)
- 0685 - 冗余连接 II ｜ [LeetCode 链接](https://leetcode.cn/problems/redundant-connection-ii/) ｜ [题解笔记](../solutions/0601-0700/0685-redundant-connection-ii.md)
- 0287 - 寻找重复数 ｜ [LeetCode 链接](https://leetcode.cn/problems/find-the-duplicate-number/) ｜ [题解笔记](../solutions/0201-0300/0287-find-the-duplicate-number.md)

### 最短路

#### 单源最短路：Dijkstra 算法
模板：

```python
# 返回从起点 start 到每个点的最短路长度 dis，如果节点 x 不可达，则 dis[x] = math.inf
# 要求：没有负数边权
# 时间复杂度 O(n + mlogm)，其中 m 是 edges 的长度。注意堆中有 O(m) 个元素
def shortestPathDijkstra(n: int, edges: List[List[int]], start: int) -> List[int]:
    # 注：如果节点编号从 1 开始（而不是从 0 开始），可以把 n 加一
    g = [[] for _ in range(n)]  # 邻接表
    for x, y, wt in edges:
        g[x].append((y, wt))
        # g[y].append((x, wt))  # 无向图加上这行

    dis = [inf] * n
    dis[start] = 0  # 起点到自己的距离是 0
    h = [(0, start)]  # 堆中保存 (起点到节点 x 的最短路长度，节点 x)

    while h:
        dis_x, x = heappop(h)
        if dis_x > dis[x]:  # x 之前出堆过
            continue
        for y, wt in g[x]:
            new_dis_y = dis_x + wt
            if new_dis_y < dis[y]:
                dis[y] = new_dis_y  # 更新 x 的邻居的最短路
                # 懒更新堆：只插入数据，不更新堆中数据
                # 相同节点可能有多个不同的 new_dis_y，除了最小的 new_dis_y，其余值都会触发上面的 continue
                heappush(h, (new_dis_y, y))

    return dis
```

模板题目：

- 0743 - 网络延迟时间 ｜ [LeetCode 链接](https://leetcode.cn/problems/network-delay-time/) ｜ [题解笔记](../solutions/0701-0800/0743-network-delay-time.md)
- 3341 - 到达最后一个房间的最少时间 I ｜ [LeetCode 链接](https://leetcode.cn/problems/find-minimum-time-to-reach-last-room-i/) ｜ [题解笔记](../solutions/3301-3400/3341-find-minimum-time-to-reach-last-room-i.md)
- 3112 - 访问消失节点的最少时间 ｜ [LeetCode 链接](https://leetcode.cn/problems/minimum-time-to-visit-disappearing-nodes/) ｜ [题解笔记](../solutions/3101-3200/3112-minimum-time-to-visit-disappearing-nodes.md)
- 2642 - 设计可以求最短路径的图类 ｜ [LeetCode 链接](https://leetcode.cn/problems/design-graph-with-shortest-path-calculator/) ｜ [题解笔记](../solutions/2601-2700/2642-design-graph-with-shortest-path-calculator.md)

#### 全源最短路：Floyd 算法
模板：

```python
# 返回一个二维列表，其中 (i,j) 这一项表示从 i 到 j 的最短路长度
# 如果无法从 i 到 j，则最短路长度为 math.inf
# 允许负数边权
# 如果计算完毕后，存在 i，使得从 i 到 i 的最短路长度小于 0，说明图中有负环
# 节点编号从 0 到 n-1
# 时间复杂度 O(n^3 + m)，其中 m 是 edges 的长度
def shortestPathFloyd(self, n: int, edges: List[List[int]]) -> List[List[int]]:
    f = [[inf] * n for _ in range(n)]
    for i in range(n):
        f[i][i] = 0

    for x, y, wt in edges:
        f[x][y] = min(f[x][y], wt)  # 如果有重边，取边权最小值
        f[y][x] = min(f[y][x], wt)  # 无向图

    for k in range(n):
        for i in range(n):
            if f[i][k] == inf:  # 针对稀疏图的优化
                continue
            for j in range(n):
                f[i][j] = min(f[i][j], f[i][k] + f[k][j])
    return f
```

模板题目：

待补充...

### 最小生成树

#### 题目清单
模板：

```python
# 待补充
```

模板题目：

- 1584 - 连接所有点的最小费用 ｜ [LeetCode 链接](https://leetcode.cn/problems/min-cost-to-connect-all-points/) ｜ [题解笔记](../solutions/1501-1600/1584-min-cost-to-connect-all-points.md)

### 欧拉路径/欧拉回路

#### 题目清单
模板：

```python
# 待补充
```

模板题目：

待补充...

### 强连通分量/双连通分量

#### 题目清单
模板：

```python
# 待补充
```

模板题目：

待补充...

### 二分图染色

#### 题目清单
模板：

```python
# 待补充
```

模板题目：

待补充...

### 网络流

#### 题目清单
模板：

```python
# 待补充
```

模板题目：

待补充...

### 其他

#### 题目清单
模板：

```python
# 待补充
```

模板题目：

- 3666 - 使二进制字符串全为 1 的最少操作次数 ｜ [LeetCode 链接](https://leetcode.cn/problems/minimum-operations-to-equalize-binary-string/) ｜ [题解笔记](../solutions/3601-3700/3666-minimum-operations-to-equalize-binary-string.md)
- 2612 - 最少翻转操作数 ｜ [LeetCode 链接](https://leetcode.cn/problems/minimum-reverse-operations/) ｜ [题解笔记](../solutions/2601-2700/2612-minimum-reverse-operations.md)

### 树上算法

#### 题目清单
模板：

```python
# 待补充
```

模板题目：

待补充...
