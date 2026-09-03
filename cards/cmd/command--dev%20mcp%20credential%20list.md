# dws dev mcp credential list

kind: command
completeness: partial
usage: dws dev mcp credential list
description: 查询 MCP 凭证账号列表
example: dws dev mcp credential list --mcp-id 10520 --page-size 20 --format json
source: internal/helpers/dev_mcp.go:728
visible_flags: 3
partial_reason: unverified_flags

## Flags
- --mcp-id <Int>: MCP 服务 ID
- --cursor <Int>: 分页游标，从 1 开始
- --page-size <Int>: 每页条数，最大 100

## Related
- dws dev mcp credential save
- dws dev mcp credential unbind
