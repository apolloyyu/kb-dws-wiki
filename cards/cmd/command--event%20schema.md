# dws event schema

kind: command
completeness: partial
usage: dws event schema <event_key>
description: 显示事件 schema
example: dws event schema user_card_action_triggered --flatten -f json
source: internal/app/event_personal_command.go:173
visible_flags: 3
partial_reason: unverified_flags

## Flags
- --as <String>: 事件身份: user
- --format (-f) <String>: 输出格式: json
- --flatten <Bool>: 显示 --flatten 消费模式对应的顶层业务字段 schema

## Related
- dws event _bus
- dws event consume
- dws event list
- dws event status
- dws event stop
