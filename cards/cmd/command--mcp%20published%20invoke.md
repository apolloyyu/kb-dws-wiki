# dws mcp published invoke

kind: command
completeness: full
usage: dws mcp published invoke <mcpId> <tool>
description: 调用当前身份可用的已发布 MCP 工具
example: dws mcp published invoke 2480 search --params '{"query":"example"}' --dry-run --format json
source: internal/app/mcp_published_command.go:156
visible_flags: 1

## Flags
- --params <String>: 工具参数 JSON 对象

## Related
- dws mcp published tools
