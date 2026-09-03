# dws mcp create

kind: command
completeness: full
description: 新建 MCP 工具草稿
source: internal/helpers/dev_mcp.go:271
visible_flags: 5

## Flags
- --name <String>: 服务名称，组织内唯一
- --description <String>: 服务用途描述
- --icon-url <String>: 服务图标 URL
- --introduction <String>: 服务详情介绍，支持 markdown
- --server-name <String>: 服务英文标识，kebab-case，用于稳定识别已发布 MCP 服务

## Related
- dws mcp create-hsf
- dws mcp debug
- dws mcp delete
- dws mcp get
- dws mcp list
- dws mcp method-list
