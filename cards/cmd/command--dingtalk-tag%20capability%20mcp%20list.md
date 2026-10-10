# dws dingtalk-tag capability mcp list

kind: command
completeness: partial
usage: dws dingtalk-tag capability mcp list
description: —
source: internal/helpers/deap_agent_skill_mcp.go:729
visible_flags: 4
partial_reason: missing_description

## Flags
- --agent-uuid <String> required: 目标数字员工 UUID（MCP 资源 tenant）
- --keywords <String>: 名称或描述关键词
- --page <Int>: 页码
- --page-size <Int>: 每页数量

## Related
- dws dingtalk-tag capability mcp create
- dws dingtalk-tag capability mcp delete
- dws dingtalk-tag capability mcp query
- dws dingtalk-tag capability mcp update
