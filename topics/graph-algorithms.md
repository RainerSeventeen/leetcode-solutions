# 图算法

## 1 概览
图算法处理节点与边关系，核心任务包括连通性、环检测、拓扑排序、最小生成树与路径可达。

## 2 核心思想
- 遍历：BFS/DFS 解决可达性与分层。
- 并查集：维护动态连通性与判环。
- 拓扑排序：在 DAG 中按依赖顺序处理。
- 最小生成树：在连通图中以最小代价连通所有点。

## 3 解题流程
1. 明确图模型：有向/无向，带权/无权，稀疏/稠密。
2. 选择算法：遍历、并查集、拓扑、MST。
3. 设计数据结构：邻接表、入度数组、并查集父节点。
4. 验证终止条件：是否全访问、是否存在环、是否连通。

## 4 模板与子方法
### 4.1 邻接表遍历（BFS/DFS）
方法说明：
适用于可达性与路径关系问题。网格题可抽象成图并交叉到网格专题。

模板代码：
```python
from collections import deque, defaultdict


def bfs(start, edges):
    g = defaultdict(list)
    for u, v in edges:
        g[u].append(v)
    q = deque([start])
    vis = {start}
    while q:
        u = q.popleft()
        for v in g[u]:
            if v not in vis:
                vis.add(v)
                q.append(v)
    return vis
```

#### 4.1.1 模板题目
- 0339 - 除法求值 ｜ [LeetCode 链接](https://leetcode.cn/problems/evaluate-division/) ｜ [题解笔记](../solutions/0301-0400/0339-evaluate-division.md)
- 0200 - 岛屿数量 ｜ [LeetCode 链接](https://leetcode.cn/problems/number-of-islands/) ｜ [题解笔记](../solutions/0201-0300/0200-number-of-islands.md)
### 4.2 并查集
方法说明：
适用于连通分量合并与判环。可与哈希集合类方法交叉，但并查集更偏图连通维护。

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

#### 4.2.1 模板题目
- 0684 - 冗余连接 ｜ [LeetCode 链接](https://leetcode.cn/problems/redundant-connection/) ｜ [题解笔记](../solutions/0601-0700/0684-redundant-connection.md)
- 0128 - 最长连续序列 ｜ [LeetCode 链接](https://leetcode.cn/problems/longest-consecutive-sequence/) ｜ [题解笔记](../solutions/0101-0200/0128-longest-consecutive-sequence.md)
### 4.3 拓扑排序
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

#### 4.3.1 模板题目
- 0207 - Course Schedule ｜ [LeetCode 链接](https://leetcode.cn/problems/course-schedule/) ｜ [题解笔记](../solutions/0201-0300/0207-course-schedule.md)
- 0310 - 最小高度树 ｜ [LeetCode 链接](https://leetcode.cn/problems/minimum-height-trees/) ｜ [题解笔记](../solutions/0301-0400/0310-minimum-height-trees.md)
- 2392 - 给定条件下构造矩阵 ｜ [LeetCode 链接](https://leetcode.cn/problems/build-a-matrix-with-conditions/) ｜ [题解笔记](../solutions/2301-2400/2392-build-a-matrix-with-conditions.md)
### 4.4 最小生成树（Kruskal/Prim）
方法说明：
用于“以最小代价连通全部节点”。`1584` 与 `1631` 都可从 MST 或最短路视角切入。

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

#### 4.4.1 模板题目
- 1584 - 连接所有点的最小费用 ｜ [LeetCode 链接](https://leetcode.cn/problems/min-cost-to-connect-all-points/) ｜ [题解笔记](../solutions/xxxx-xxxx/xxxx-slug.md)
- 1631 - 最小体力消耗路径 ｜ [LeetCode 链接](https://leetcode.cn/problems/path-with-minimum-effort/) ｜ [题解笔记](../solutions/xxxx-xxxx/xxxx-slug.md)
## 5 易错点
- 遍历未去重导致重复扩展或死循环。
- 并查集合并前未 `find` 根节点。
- 拓扑排序未检查处理节点总数。
- MST 未判断是否真正连通全部点。

## 6 总结
图题先定图模型，再在遍历、并查集、拓扑、MST 中选工具；正确性依赖于不变量和终止校验。
