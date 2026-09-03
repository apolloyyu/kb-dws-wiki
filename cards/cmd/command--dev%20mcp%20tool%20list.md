# dws dev mcp tool list

kind: command
completeness: partial
usage: dws dev mcp tool list
description: 查询 MCP 服务下的工具列表
example: dws dev mcp tool list --mcp-id 10487 --page-size 100 --format json
source: internal/helpers/dev_mcp.go:398
visible_flags: 4
partial_reason: unverified_flags

## Flags
- --keyword <String>: 按工具 name 关键词过滤
- --mcp-id <Int>: MCP 服务 ID
- --cursor <Int>: 分页游标，从 1 开始
- --page-size <Int>: 每页条数，最大 100

## Related
- dws dev mcp tool create
- dws dev mcp tool create-hsf
- dws dev mcp tool debug
- dws dev mcp tool delete
- dws dev mcp tool get
- dws dev mcp tool publish
