# dws dingtalk-tag run trace

kind: command
completeness: partial
usage: dws dingtalk-tag run trace
description: —
source: internal/helpers/deap_agent.go:623
visible_flags: 3
partial_reason: missing_description

## Flags
- --agent-uuid <String> required: 数字员工唯一标识
- --source-id <String> required: 来源侧原始 ID；im_message 传钉钉开放态 openMessageId（不是 DWS openTaskId），trigger_rule 传群感知规则 ID
- --source-type <String> required: 来源类型

## Related
- dws dingtalk-tag run run-status
