# dws dingtalk-tag capability skill delete

kind: command
completeness: partial
usage: dws dingtalk-tag capability skill delete
description: —
source: internal/helpers/deap_agent_skill_mcp.go:647
visible_flags: 2
partial_reason: missing_description

## Flags
- --agent-uuid <String> required: 目标数字员工 UUID（Skill Center V2 tenant）
- --skill-id <String> required: Skill ID

## Related
- dws dingtalk-tag capability skill create
- dws dingtalk-tag capability skill list
- dws dingtalk-tag capability skill query
- dws dingtalk-tag capability skill update
