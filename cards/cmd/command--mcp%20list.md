# dws mcp list

kind: command
completeness: full
description: 查询 MCP 开发协作者列表
source: internal/helpers/dev_mcp.go:214
visible_flags: 2

## Flags
- --keyword <String>: 按服务名关键词过滤
- --creator-user-id <String>: 按创建人 staffId 过滤

## Related
- dws mcp create
- dws mcp create-hsf
- dws mcp debug
- dws mcp delete
- dws mcp get
- dws mcp method-list
