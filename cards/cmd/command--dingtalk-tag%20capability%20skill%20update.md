# dws dingtalk-tag capability skill update

kind: command
completeness: partial
usage: dws dingtalk-tag capability skill update
description: —
source: internal/helpers/deap_agent_skill_mcp.go:574
visible_flags: 4
partial_reason: missing_description

## Flags
- --agent-uuid <String> required: 目标数字员工 UUID（Skill Center V2 tenant）
- --skill-id <String> required: Skill ID
- --enabled <Bool>: 启用状态 true|false；不传保持原值（草稿态，不自动发布）；不能与 --file 同时使用
- --file <String>: 可选本地 Skill ZIP（相对当前目录、最大 50 MiB、必须包含 SKILL.md）；提供时替换 Skill 包；不能与 --enabled 同时使用

## Related
- dws dingtalk-tag capability skill create
- dws dingtalk-tag capability skill delete
- dws dingtalk-tag capability skill list
- dws dingtalk-tag capability skill query
