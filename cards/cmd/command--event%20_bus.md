# dws event _bus

kind: command
completeness: full
description: Internal event bus daemon (do not call directly)
source: internal/app/event_command.go:591
visible_flags: 6

## Flags
- --client-id <String>: override clientID resolved from app config / env (used by busctl/Spawn)
- --idle-timeout <Duration>: exit after this long with zero consumers (0 = disabled)
- --source-kind <String>: event source kind: app_stream|personal_stream
- --stream-ticket-mode <String>: 用户 Stream 建联模式：空=SDK app credential；normal/custom=portal 取票
- --stream-source-id <String>: 用户 Stream sourceId；personal_stream 开源版默认 open
- --stream-ticket-url <String>: 用户 Stream 取票 URL；personal_stream 默认由 MCP base URL 派生

## Related
- dws event +listen-im
- dws event consume
- dws event list
- dws event schema
- dws event status
- dws event stop
