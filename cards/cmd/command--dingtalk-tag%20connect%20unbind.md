# dws dingtalk-tag connect unbind

kind: command
completeness: partial
usage: dws dingtalk-tag connect unbind
description: —
source: internal/helpers/deap_agent_lifecycle.go:284
visible_flags: 2
partial_reason: missing_description

## Flags
- --agent-uuid <String> required: 本地已绑定员工 ID
- --runtime-binding-id <String>: 明确指定服务端绑定 ID；必须与本地记录一致

## Related
- dws dingtalk-tag connect list
- dws dingtalk-tag connect restart
- dws dingtalk-tag connect status
- dws dingtalk-tag connect stop
