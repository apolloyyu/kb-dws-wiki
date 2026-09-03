# dws dev mcp auth get

kind: command
completeness: full
usage: dws dev mcp auth get
description: 查询 MCP 下游鉴权配置
example: dws dev mcp auth get --mcp-id 10520 --format json
source: internal/helpers/dev_mcp.go:648
visible_flags: 1

## Flags
- --mcp-id <Int>: MCP 服务 ID

## Related
- dws dev mcp auth save
