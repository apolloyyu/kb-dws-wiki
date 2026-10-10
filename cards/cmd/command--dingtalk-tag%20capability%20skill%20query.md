# dws dingtalk-tag capability skill query

kind: command
completeness: partial
usage: dws dingtalk-tag capability skill query
description: —
source: internal/helpers/deap_agent_skill_mcp.go:685
visible_flags: 3
partial_reason: missing_description

## Flags
- --agent-uuid <String> required: 目标数字员工 UUID（Skill Center V2 tenant）
- --skill-id <String> required: Skill ID
- --snapshot <String>: 配置快照：draft 或 published

## Related
- dws dingtalk-tag capability skill create
- dws dingtalk-tag capability skill delete
- dws dingtalk-tag capability skill list
- dws dingtalk-tag capability skill update
