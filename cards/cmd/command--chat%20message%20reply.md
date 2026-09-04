# dws chat message reply

kind: command
completeness: partial
usage: dws chat message reply
description: 引用回复消息（支持单聊/群聊）
example: dws chat message reply --group <openConversationId> --ref-msg-id <openMessageId> --ref-sender <openDingTalkId> --content "收到，马上处理"
source: internal/helpers/chat.go:7778
visible_flags: 6
partial_reason: unverified_flags

## Flags
- --ref-msg-id <String> required: 被引用的消息 openMessageId (必填)
- --ref-sender <String> required: 被引用消息的发送者 openDingTalkId (必填)
- --uuid <String>: 幂等键（可选）
- --ai-tag <Bool>: 消息是否带 AI 发送角标（默认 true）
- --at-all <Bool>: @所有人（仅群聊时生效；正文缺少 <@all> 时自动补齐）
- --at-open-dingtalk-ids <String>: @指定成员的 openDingTalkId 列表，逗号分隔（仅群聊时生效；正文缺少对应 <@id> 时自动补齐，裸 @id 自动规范化）

## Related
- dws chat message add-emoji
- dws chat message add-favorite
- dws chat message add-text-emotion
- dws chat message combine-forward
- dws chat message create-text-emotion
- dws chat message download-media
