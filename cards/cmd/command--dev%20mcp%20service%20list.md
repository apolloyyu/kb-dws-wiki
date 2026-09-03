# dws dev mcp service list

kind: command
completeness: partial
usage: dws dev mcp service list
description: 查询有开发权限的 MCP 服务列表（含 serverName）
example: dws dev mcp service list --keyword 客户 --page-size 20 --format json
source: internal/helpers/dev_mcp.go:214
visible_flags: 4
partial_reason: unverified_flags

## Flags
- --keyword <String>: 按服务名关键词过滤
- --creator-user-id <String>: 按创建人 staffId 过滤
- --cursor <Int>: 分页游标，从 1 开始
- --page-size <Int>: 每页条数，最大 100

## Related
- dws dev mcp service create
- dws dev mcp service delete
- dws dev mcp service get
- dws dev mcp service update
