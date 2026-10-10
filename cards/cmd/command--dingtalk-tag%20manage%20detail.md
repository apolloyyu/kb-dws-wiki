# dws dingtalk-tag manage detail

kind: command
completeness: partial
usage: dws dingtalk-tag manage detail
description: —
source: internal/helpers/deap_agent.go:299
visible_flags: 2
partial_reason: missing_description

## Flags
- --agent-uuid <String> required: 数字员工 ID
- --snapshot <String>: 详情快照：draft（未发布草稿）或 published（已发布配置）(可选: draft|published)

## Related
- dws dingtalk-tag manage create
- dws dingtalk-tag manage delete
- dws dingtalk-tag manage list
- dws dingtalk-tag manage login
- dws dingtalk-tag manage publish
- dws dingtalk-tag manage save-draft
