# dws dev mcp tool get

kind: command
completeness: partial
usage: dws dev mcp tool get
description: 读取 MCP 工具定义
example: dws dev mcp tool get --mcp-id 10487 --tool-id G-ACT-xxx --format json
source: internal/helpers/dev_mcp.go:430
visible_flags: 3
partial_reason: unverified_flags

## Flags
- --version-id <String>: 指定读取的历史版本 ID
- --mcp-id <Int>: MCP 服务 ID
- --tool-id <String>: MCP 工具 ID，G-ACT- 开头

## Related
- dws dev mcp tool create
- dws dev mcp tool create-hsf
- dws dev mcp tool debug
- dws dev mcp tool delete
- dws dev mcp tool list
- dws dev mcp tool publish
