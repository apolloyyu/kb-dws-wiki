# dws event stop

kind: command
completeness: full
description: 取消个人事件订阅并停止本地消费
source: internal/app/event_command.go:1205
visible_flags: 4

## Flags
- --as <String>: 事件身份: user
- --personal-event-base-url <String>: 个人事件控制面 base URL；默认由 MCP base 派生 /dws
- --stream-source-id <String>: 个人事件 sourceId；开源版默认 open，可由 edition 覆盖
- --all <Bool>: 取消当前身份下本地记录的所有个人订阅

## Related
- dws event +listen-im
- dws event _bus
- dws event consume
- dws event list
- dws event schema
- dws event status
