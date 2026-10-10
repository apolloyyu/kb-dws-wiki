# dws dingtalk-tag manage login

kind: command
completeness: partial
usage: dws dingtalk-tag manage login
description: —
source: internal/helpers/deap_agent.go:160
visible_flags: 2
partial_reason: missing_description

## Flags
- --agent-uuid <String> required: 数字员工 ID
- --client-id <String>: 用于授权的应用 ID；不传时由服务端选择默认应用

## Related
- dws dingtalk-tag manage create
- dws dingtalk-tag manage delete
- dws dingtalk-tag manage detail
- dws dingtalk-tag manage list
- dws dingtalk-tag manage publish
- dws dingtalk-tag manage save-draft
