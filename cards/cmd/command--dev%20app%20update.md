# dws dev app update

kind: command
completeness: full
description: 修改 MCP 服务信息
source: internal/helpers/dev_mcp.go:323
visible_flags: 5

## Flags
- --name <String>: 新服务名称
- --description <String>: 新服务描述
- --icon-url <String>: 新图标 URL
- --introduction <String>: 新详情介绍
- --server-name <String>: 新服务英文标识，kebab-case

## Related
- dws dev app create
- dws dev app delete
- dws dev app disable
- dws dev app enable
- dws dev app get
- dws dev app list
