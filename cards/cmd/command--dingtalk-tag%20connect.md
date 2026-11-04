# dws dingtalk-tag connect

kind: command
completeness: partial
usage: dws dingtalk-tag connect
description: —
source: internal/helpers/deap_agent_channel.go:87
visible_flags: 20
partial_reason: missing_description,too_many_flags:20

## Flags
- --agent-uuid <String> required: 已存在且已发布的数字员工 ID
- --channel <String>: 本地 Agent 类型；省略或 auto 时自动探测
- --client-id <String>: 传给 DEAP 的选应用提示；最终换票始终使用授权响应中的 dwsClientId
- --reply-mode <String>: DWS 直接托管本地 Agent 的回复模式：a2ui 发送占位并更新最终答案，已适配的 Agent 同时显示公开进度，未适配公开进度的 Agent 仍用文本；text 仅发送最终文本。外部宿主接入（--channel dsh）不接受此参数(可选: a2ui|text)
- --reply-card-forward <Bool>: 允许转发新创建的 A2UI 回复卡片，默认关闭；仅对 A2UI 回复生效，不修改已发送卡片
- --agent-cmd <String>: custom 命令；问题作为末参，stdout 作为回复
- --agent-model <String>: Agent 模型；同 dev connect
- --agent-workdir <String>: Agent 工作目录；同 dev connect
- --agent-memory <Bool>: 按员工和会话保留 Agent 上下文
- … 11 more; use dwsdoc cmd/short for full flags

## Related
- dws dingtalk-tag capability
- dws dingtalk-tag channel
- dws dingtalk-tag manage
- dws dingtalk-tag run
