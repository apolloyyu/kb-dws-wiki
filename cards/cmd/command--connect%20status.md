# dws connect status

kind: command
completeness: full
description: 查看连接器健康状态（healthy/degraded/down，pid、收发活动、日志路径；--json 供外部托管消费）
source: internal/helpers/connect_daemon.go:694
visible_flags: 3

## Flags
- --robot-client-id <String>: 机器人 clientId（定位守护进程）
- --unified-app-id <String>: 统一应用 ID（当未用 clientId 起守护进程时定位）
- --json <Bool>: 以 JSON 输出健康报告（供 launchd/systemd/pm2/cron 判断是否重启）

## Related
- dws connect list
- dws connect restart
- dws connect stop
