# dws dev mcp tool delete

kind: command
completeness: full
usage: dws dev mcp tool delete
description: 删除 MCP 工具（不可恢复）
example: dws dev mcp tool delete --mcp-id 10487 --tool-id G-ACT-xxx --dry-run --format json
source: internal/helpers/dev_mcp.go:592
visible_flags: 2

## Flags
- --mcp-id <Int>: MCP 服务 ID
- --tool-id <String>: MCP 工具 ID，G-ACT- 开头

## Related
- dws dev mcp tool create
- dws dev mcp tool create-hsf
- dws dev mcp tool debug
- dws dev mcp tool get
- dws dev mcp tool list
- dws dev mcp tool publish
