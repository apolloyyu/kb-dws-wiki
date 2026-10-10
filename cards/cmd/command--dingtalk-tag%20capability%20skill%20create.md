# dws dingtalk-tag capability skill create

kind: command
completeness: partial
usage: dws dingtalk-tag capability skill create
description: —
source: internal/helpers/deap_agent_skill_mcp.go:499
visible_flags: 2
partial_reason: missing_description

## Flags
- --agent-uuid <String> required: 目标数字员工 UUID（Skill Center V2 tenant）
- --file <String> required: 本地 Skill ZIP（相对当前目录、最大 50 MiB、必须包含 SKILL.md）

## Related
- dws dingtalk-tag capability skill delete
- dws dingtalk-tag capability skill list
- dws dingtalk-tag capability skill query
- dws dingtalk-tag capability skill update
