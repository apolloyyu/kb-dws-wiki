# dws mcp method-list

kind: command
completeness: full
description: 查询 HSF 接口的方法清单（建 hsf 工具前的方法发现，含每方法出入参 schema）
source: internal/helpers/dev_mcp_hsf.go:30
visible_flags: 2

## Flags
- --interface-name <String>: 必填。HSF 接口全限定名（不能只传简名），如 com.dingtalk.open.connect.workbench.api.service.hsf.MCPHsfService
- --version <String>: 可选。HSF 服务版本号，缺省 1.0.0

## Related
- dws mcp create
- dws mcp create-hsf
- dws mcp debug
- dws mcp delete
- dws mcp get
- dws mcp list
