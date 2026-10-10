# dws dingtalk-tag capability mcp delete

kind: command
completeness: partial
usage: dws dingtalk-tag capability mcp delete
description: —
source: internal/helpers/deap_agent_skill_mcp.go:805
visible_flags: 2
partial_reason: missing_description

## Flags
- --agent-uuid <String> required: 目标数字员工 UUID（MCP 资源 tenant）
- --mcp-id <String> required: MCP ID

## Related
- dws dingtalk-tag capability mcp create
- dws dingtalk-tag capability mcp list
- dws dingtalk-tag capability mcp query
- dws dingtalk-tag capability mcp update
