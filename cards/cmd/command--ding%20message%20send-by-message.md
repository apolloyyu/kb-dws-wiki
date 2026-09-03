# dws ding message send-by-message

kind: command
completeness: full
usage: dws ding message send-by-message
description: 消息转 DING（将聊天消息转为 DING 通知）
example: dws ding message send-by-message --group <openConversationId> --message-id <openMessageId> --users id1,id2
source: internal/helpers/ding.go:369
visible_flags: 5

## Flags
- --group <String> required: 原消息所在会话 openConversationId (必填)
- --message-id <String> required: 原消息 openMessageId (必填)
- --users <String> required: 接收者 openDingTalkId 列表，逗号分隔 (必填)
- --type <String>: 提醒类型: app/sms/call (默认 app)
- --uuid <String>: 幂等唯一标识（可选，不传由服务端生成）

## Related
- dws ding message list
- dws ding message recall
- dws ding message recall-personal
- dws ding message receiver-status
- dws ding message send
- dws ding message send-personal
