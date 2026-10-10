# dws dingtalk-tag connect

kind: command
completeness: partial
usage: dws dingtalk-tag connect
description: —
source: internal/helpers/deap_agent_channel.go:85
visible_flags: 18
partial_reason: missing_description,too_many_flags:18

## Flags
- --agent-uuid <String> required: 已存在且已发布的数字员工 ID
- --channel <String>: 本地 Agent 类型；省略或 auto 时自动探测
- --client-id <String>: 传给 DEAP 的选应用提示；最终换票始终使用授权响应中的 dwsClientId
- --agent-cmd <String>: custom 命令；问题作为末参，stdout 作为回复
- --agent-model <String>: Agent 模型；同 dev connect
- --agent-workdir <String>: Agent 工作目录；同 dev connect
- --agent-memory <Bool>: 按员工和会话保留 Agent 上下文
- --agent-timeout <Int>: Agent 每轮超时秒数；0 不限制
- --agent-permission-mode <String>: Agent 权限模式；同 dev connect(可选: ask|bypass)
- … 9 more; use dwsdoc cmd/short for full flags

## Related
- dws dingtalk-tag capability
- dws dingtalk-tag channel
- dws dingtalk-tag manage
- dws dingtalk-tag run
