# dws dev connect

kind: command
completeness: partial
description: 建联：把现成机器人接到当前本地 agent（起 Stream，不建号）
source: internal/helpers/devapp_connect.go:443
visible_flags: 29
partial_reason: too_many_flags:29

## Flags
- --守护进程模式：把连接器放到后台运行（脱离终端），父进程打印 pid/日志路径后退出（Windows 暂不支持） <Bool>: —
- --alwayson <Bool>: 常驻模式：worker 崩溃后自动重启（仅 --daemon 生效）
- --internal: run the daemon supervisor (set automatically by --daemon) <Bool>: —
- --internal: run a single supervised connector worker (set automatically by the supervisor) <Bool>: —
- --channel <String>: 渠道：auto(默认,自动探测)|openclaw|qoder|qoderwork|hermes|workbuddy|claudecode|codebuddy|codex|gemini|opencode|custom(自研/未支持的 AI，配 --agent-cmd)
- --agent-cmd <String>: 自研/未支持的 AI 工具命令（无头/一次性：问题作为最后一个参数追加，答案打到 stdout）；用来接入内置渠道之外的 AI（如网易有道龙虾 LobsterAI）；等价于 --channel custom + 设 DWS_AGENT_CMD；env: DWS_AGENT_CMD
- --robot-client-id <String>: 现成机器人 clientId（AppKey）
- --robot-client-secret <String>: 现成机器人 clientSecret（AppSecret）
- … 21 more; use dwsdoc cmd/short for full flags

## Related
- none
