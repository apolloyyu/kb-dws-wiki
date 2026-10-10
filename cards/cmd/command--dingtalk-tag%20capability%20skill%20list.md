# dws dingtalk-tag capability skill list

kind: command
completeness: partial
usage: dws dingtalk-tag capability skill list
description: —
source: internal/helpers/deap_agent_skill_mcp.go:666
visible_flags: 2
partial_reason: missing_description

## Flags
- --agent-uuid <String> required: 目标数字员工 UUID（Skill Center V2 tenant）
- --snapshot <String>: 配置快照：draft 或 published

## Related
- dws dingtalk-tag capability skill create
- dws dingtalk-tag capability skill delete
- dws dingtalk-tag capability skill query
- dws dingtalk-tag capability skill update
