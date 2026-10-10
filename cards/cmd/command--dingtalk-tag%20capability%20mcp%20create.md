# dws dingtalk-tag capability mcp create

kind: command
completeness: partial
usage: dws dingtalk-tag capability mcp create
description: —
source: internal/helpers/deap_agent_skill_mcp.go:705
visible_flags: 2
partial_reason: missing_description

## Flags
- --agent-uuid <String> required: 目标数字员工 UUID（MCP 资源 tenant）
- --config-file <String> required: 配置 JSON 对象文件（最大 1 MiB；根节点 name/configString 必填；configString 内 mcpServers.<名称>.type 必填 streamable-http 或 sse；敏感值放 configString/envs）

## Related
- dws dingtalk-tag capability mcp delete
- dws dingtalk-tag capability mcp list
- dws dingtalk-tag capability mcp query
- dws dingtalk-tag capability mcp update
