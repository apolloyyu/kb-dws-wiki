# dws dev connect stop

kind: command
completeness: full
description: 优雅停止后台连接器守护进程（释放单实例锁与 Stream 连接）
source: internal/helpers/connect_daemon.go:753
visible_flags: 2

## Flags
- --robot-client-id <String>: 机器人 clientId（定位守护进程）
- --unified-app-id <String>: 统一应用 ID（当未用 clientId 起守护进程时定位）

## Related
- dws dev connect list
- dws dev connect restart
- dws dev connect status
