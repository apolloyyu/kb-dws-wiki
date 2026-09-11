# dws event list

kind: command
completeness: partial
usage: dws event list
description: 列出个人事件目录
example: dws event list --category card --format json
source: internal/app/event_command.go:802
visible_flags: 8
partial_reason: unverified_flags

## Flags
- --all <Bool>: 列出当前 edition 下所有 ClientID 的消费者
- --all-editions <Bool>: 跨 edition 列出（罕用，调试用）
- --client-id <String>: 指定具体 ClientID（覆盖凭证解析）
- --format (-f) <String>: 输出格式: table|json
- --as <String>: 事件身份: user
- --category <String>: 个人事件目录分类：im|oa|voip|todo|card
- --enabled-only <Bool>: 个人事件目录只显示 enabled
- --include-pending <Bool>: 个人事件目录包含 pending 项

## Related
- dws event _bus
- dws event consume
- dws event schema
- dws event status
- dws event stop
