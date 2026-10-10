# dws dingtalk-tag capability mcp update

kind: command
completeness: partial
usage: dws dingtalk-tag capability mcp update
description: —
source: internal/helpers/deap_agent_skill_mcp.go:769
visible_flags: 4
partial_reason: missing_description

## Flags
- --agent-uuid <String> required: 目标数字员工 UUID（MCP 资源 tenant）
- --mcp-id <String> required: MCP ID
- --enabled <Bool>: 启用状态 true|false；不传保持原值（草稿态，不自动发布）
- --config-file <String>: 可选配置 JSON 对象文件（最大 1 MiB；根节点 name/configString 必填；configString 内 mcpServers.<名称>.type 必填 streamable-http 或 sse；敏感值放 configString/envs）；提供时替换配置

## Related
- dws dingtalk-tag capability mcp create
- dws dingtalk-tag capability mcp delete
- dws dingtalk-tag capability mcp list
- dws dingtalk-tag capability mcp query
