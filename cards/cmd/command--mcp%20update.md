# dws mcp update

kind: command
completeness: full
description: 编辑 MCP 工具并保存为草稿
source: internal/helpers/dev_mcp.go:323
visible_flags: 5

## Flags
- --name <String>: 新服务名称
- --description <String>: 新服务描述
- --icon-url <String>: 新图标 URL
- --introduction <String>: 新详情介绍
- --server-name <String>: 新服务英文标识，kebab-case

## Related
- dws mcp create
- dws mcp create-hsf
- dws mcp debug
- dws mcp delete
- dws mcp get
- dws mcp list
