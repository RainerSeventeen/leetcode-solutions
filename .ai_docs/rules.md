# 撰写规则

> 下面所有 python 都在虚拟环境下运行

## `solutions/*.md` 规则
1. solutions 下的文件不允许自行创建, 必须调用 `scripts/fetch_problem.py` 脚本创建

2. 解题思路需要简要介绍代码用到的方法

3. 复杂度内容必须使用 $O(x)$ 这种格式

## `topics/*.md` 格式
1. 所有标题均不写编号和前缀, 使用统一脚本执行格式化

2. 题目条目格式固定为：
   - `- 0000 - 题目名 ｜ [LeetCode 链接](https://leetcode.cn/problems/xxx/) ｜ [题解笔记](../solutions/xxxx-xxxx/xxxx-slug.md)`

## 检验与自动化
1. 必须通过 `scripts/check_solutions.py` 校验

2. 撰写完成后需要通过 `scripts/normalize_topics_title.py` 执行格式化
