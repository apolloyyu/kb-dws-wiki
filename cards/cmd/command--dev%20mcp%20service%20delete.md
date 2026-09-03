# dws dev mcp service delete

kind: command
completeness: full
usage: dws dev mcp service delete
description: 删除 MCP 服务（不可恢复）
example: dws dev mcp service delete --mcp-id 10487 --dry-run --format json
source: internal/helpers/dev_mcp.go:369
visible_flags: 1

## Flags
- --mcp-id <Int>: MCP 服务 ID

## Related
- dws dev mcp service create
- dws dev mcp service get
- dws dev mcp service list
- dws dev mcp service update
