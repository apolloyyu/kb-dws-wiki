# dws dev mcp tool versions

kind: command
completeness: partial
usage: dws dev mcp tool versions
description: 查询 MCP 工具版本历史
example: dws dev mcp tool versions --mcp-id 10487 --tool-id G-ACT-xxx --format json
source: internal/helpers/dev_mcp.go:619
visible_flags: 4
partial_reason: unverified_flags

## Flags
- --mcp-id <Int>: MCP 服务 ID
- --tool-id <String>: MCP 工具 ID，G-ACT- 开头
- --cursor <Int>: 分页游标，从 1 开始
- --page-size <Int>: 每页条数，最大 100

## Related
- dws dev mcp tool create
- dws dev mcp tool create-hsf
- dws dev mcp tool debug
- dws dev mcp tool delete
- dws dev mcp tool get
- dws dev mcp tool list
