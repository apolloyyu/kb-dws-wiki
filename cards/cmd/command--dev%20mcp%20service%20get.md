# dws dev mcp service get

kind: command
completeness: full
usage: dws dev mcp service get
description: 查询 MCP 服务详情
example: dws dev mcp service get --mcp-id 10487 --format json
source: internal/helpers/dev_mcp.go:243
visible_flags: 1

## Flags
- --mcp-id <Int>: MCP 服务 ID

## Related
- dws dev mcp service create
- dws dev mcp service delete
- dws dev mcp service list
- dws dev mcp service update
