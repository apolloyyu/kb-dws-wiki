# dws event status

kind: command
completeness: full
description: 显示个人事件订阅和本地消费状态
source: internal/app/event_command.go:890
visible_flags: 11

## Flags
- --all <Bool>: 当前 edition 下所有 ClientID
- --all-editions <Bool>: 跨 edition
- --client-id <String>: 指定具体 ClientID
- --format (-f) <String>: 输出格式: text|json
- --fail-on-orphan <Bool>: 检测到 orphan 时退出码 2
- --as <String>: 事件身份: user
- --event <String>: 个人事件 event_key 过滤
- --status <String>: 个人订阅状态过滤: active|paused|error|deleted|all
- --subscribe-id <String>: 个人订阅 ID 过滤
- --personal-event-base-url <String>: 个人事件控制面 base URL；默认由 MCP base 派生 /dws
- --stream-source-id <String>: 个人事件 sourceId；开源版默认 open，可由 edition 覆盖

## Related
- dws event +listen-im
- dws event _bus
- dws event consume
- dws event list
- dws event schema
- dws event stop
