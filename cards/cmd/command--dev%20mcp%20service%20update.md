# dws dev mcp service update

kind: command
completeness: partial
usage: dws dev mcp service update
description: 修改 MCP 服务信息
example: dws dev mcp service update --mcp-id 10487 --description "新描述" --dry-run --format json
source: internal/helpers/dev_mcp.go:323
visible_flags: 6
partial_reason: unverified_flags

## Flags
- --name <String>: 新服务名称
- --description <String>: 新服务描述
- --icon-url <String>: 新图标 URL
- --introduction <String>: 新详情介绍
- --server-name <String>: 新服务英文标识，kebab-case
- --mcp-id <Int>: MCP 服务 ID

## Related
- dws dev mcp service create
- dws dev mcp service delete
- dws dev mcp service get
- dws dev mcp service list
