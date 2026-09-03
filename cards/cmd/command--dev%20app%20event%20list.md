# dws dev app event list

kind: command
completeness: full
description: 查询有开发权限的 MCP 服务列表（含 serverName）
source: internal/helpers/dev_mcp.go:214
visible_flags: 2

## Flags
- --keyword <String>: 按服务名关键词过滤
- --creator-user-id <String>: 按创建人 staffId 过滤

## Related
- dws dev app event subscribe
- dws dev app event unsubscribe
