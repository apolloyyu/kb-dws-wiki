# dws connect restart

kind: command
completeness: full
description: 重启连接器守护进程（通过持久化的 unifiedAppId 重新拉取密钥，无需本地存密钥）
source: internal/helpers/connect_daemon.go:881
visible_flags: 2

## Flags
- --robot-client-id <String>: 机器人 clientId（定位守护进程）
- --unified-app-id <String>: 统一应用 ID（当未用 clientId 起守护进程时定位）

## Related
- dws connect list
- dws connect status
- dws connect stop
