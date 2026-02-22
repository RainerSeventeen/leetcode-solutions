---
id: 146
title: LRU Cache
difficulty: Medium
tags: [design, hash-table, linked-list, doubly-linked-list]
created: 2026-02-20
---

# 146. LRU 缓存

## 题目链接
https://leetcode.cn/problems/lru-cache/

## 题目描述
<div class="title__3Vvk">请你设计并实现一个满足&nbsp; <a href="https://baike.baidu.com/item/LRU" target="_blank">LRU (最近最少使用) 缓存</a> 约束的数据结构。</div>

<div class="title__3Vvk">实现 <code>LRUCache</code> 类：</div>

<div class="original__bRMd">
<div>
<ul>
	<li><code>LRUCache(int capacity)</code> 以 <strong>正整数</strong> 作为容量&nbsp;<code>capacity</code> 初始化 LRU 缓存</li>
	<li><code>int get(int key)</code> 如果关键字 <code>key</code> 存在于缓存中，则返回关键字的值，否则返回 <code>-1</code> 。</li>
	<li><code>void put(int key, int value)</code>&nbsp;如果关键字&nbsp;<code>key</code> 已经存在，则变更其数据值&nbsp;<code>value</code> ；如果不存在，则向缓存中插入该组&nbsp;<code>key-value</code> 。如果插入操作导致关键字数量超过&nbsp;<code>capacity</code> ，则应该 <strong>逐出</strong> 最久未使用的关键字。</li>
</ul>

<p>函数 <code>get</code> 和 <code>put</code> 必须以 <code>O(1)</code> 的平均时间复杂度运行。</p>
</div>
</div>

<p><strong>示例：</strong></p>

<pre>
<strong>输入</strong>
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
<strong>输出</strong>
[null, null, null, 1, null, -1, null, -1, 3, 4]

<strong>解释</strong>
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // 缓存是 {1=1}
lRUCache.put(2, 2); // 缓存是 {1=1, 2=2}
lRUCache.get(1);    // 返回 1
lRUCache.put(3, 3); // 该操作会使得关键字 2 作废，缓存是 {1=1, 3=3}
lRUCache.get(2);    // 返回 -1 (未找到)
lRUCache.put(4, 4); // 该操作会使得关键字 1 作废，缓存是 {4=4, 3=3}
lRUCache.get(1);    // 返回 -1 (未找到)
lRUCache.get(3);    // 返回 3
lRUCache.get(4);    // 返回 4
</pre>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= capacity &lt;= 3000</code></li>
	<li><code>0 &lt;= key &lt;= 10000</code></li>
	<li><code>0 &lt;= value &lt;= 10<sup>5</sup></code></li>
	<li>最多调用 <code>2 * 10<sup>5</sup></code> 次 <code>get</code> 和 <code>put</code></li>
</ul>


## 解题思路

用 hash 表实现快速查找，另外就是对于 LRU 需要频繁的将某一个值移动到最头处，所以最合适的其实是链表数据，这里使用双端链表，一个头一个尾分别代表最后使用和最先使用

这里用到了 `OrderedDict` 的 API，没有单独写 `hash` 链表，可以放到单独 707, 641 去写

- 时间复杂度: $O(1)$
- 空间复杂度: $O(capacity)$

时间复杂度按单次 `get/put` 计算。
## 相关专题
- [常用数据结构](../../topics/common-data-structures.md)

## 代码
```python
from collections import OrderedDict
class LRUCache:
    def __init__(self, capacity: int):
        self.od = OrderedDict()
        self.max = capacity

    def get(self, key: int) -> int:
        if key in self.od:
            self.od.move_to_end(key)
            return self.od.get(key)
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.od:          # 对于已经存在的情况
            self.od[key] = value
            self.od.move_to_end(key)  # 移动到队伍尾
            return
        elif len(self.od) >= self.max:  # 满了要删除一个
            self.od.popitem(last=False) # 删除队伍头（最近未使用）

        self.od[key] = value    # 新插入，默认在队伍尾部
```
