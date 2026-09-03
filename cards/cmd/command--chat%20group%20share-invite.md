# dws chat group share-invite

kind: command
completeness: full
usage: dws chat group share-invite
description: 分享群聊链接到会话
example: dws chat group share-invite --source <被分享群openConversationId> --target <目标会话openConversationId>
source: internal/helpers/chat.go:10689
visible_flags: 6

## Flags
- --source <String> required: 被分享群的 openConversationId (必填)
- --target <String>: 接收分享消息的会话 openConversationId（与 --receiver 二选一）
- --receiver <String>: 接收分享消息的单聊用户 openDingTalkId（与 --target 二选一）
- --expires-seconds <Int64>: 链接有效期（秒），0 表示永久有效，不传使用服务端默认值
- --uuid <String>: 消息幂等键（可选）
- --yes (-y) <Bool>: 确认分享群邀请链接

## Related
- dws chat group audit-join-validation
- dws chat group bots
- dws chat group create
- dws chat group dismiss
- dws chat group get-by-group-id
- dws chat group get-mute-config
