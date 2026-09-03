# dws dev mcp service create

kind: command
completeness: partial
usage: dws dev mcp service create
description: 新建 MCP 服务
example: dws dev mcp service create --name 客户信息查询 --server-name customer-info --description "查询客户基础资料" --dry-run --format json
source: internal/helpers/dev_mcp.go:271
visible_flags: 5
partial_reason: unverified_flags

## Flags
- --name <String>: 服务名称，组织内唯一
- --description <String>: 服务用途描述
- --icon-url <String>: 服务图标 URL
- --introduction <String>: 服务详情介绍，支持 markdown
- --server-name <String>: 服务英文标识，kebab-case，用于稳定识别已发布 MCP 服务

## Related
- dws dev mcp service delete
- dws dev mcp service get
- dws dev mcp service list
- dws dev mcp service update
