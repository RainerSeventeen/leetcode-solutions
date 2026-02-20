# LeetCode Solution

个人构建的 leetcode 算法平台知识库

## MCP 配置

本项目集成了 [leetcode-mcp-server](https://github.com/jinzcdev/leetcode-mcp-server)，可让 Claude Code 直接查询题目、提交代码等。

### 前置条件

- [Node.js](https://nodejs.org/)
- Claude Code / Codex / 其他 Agent 等
- 克隆并构建 MCP 服务器：

```bash
git clone https://github.com/jinzcdev/leetcode-mcp-server.git
cd leetcode-mcp-server
npm install && npm run build
```

### Claude Code
```bash
claude mcp add leetcode --scope project -- node /path/to/leetcode-mcp-server/build/index.js --site cn
```

> `--site cn` 对应力扣中文站，国际版改为 `--site global`。

### Codex CLI

```bash
codex mcp add leetcode -- node /path/to/leetcode-mcp-server/build/index.js --site cn
```