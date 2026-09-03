# dws connect list

kind: command
completeness: full
description: 列出本机所有连接器及健康状态（healthy/degraded/down）；--json 供脚本消费
source: internal/helpers/connect_daemon.go:996
visible_flags: 1

## Flags
- --json <Bool>: 以 JSON 数组输出（供脚本消费）

## Related
- dws connect restart
- dws connect status
- dws connect stop
