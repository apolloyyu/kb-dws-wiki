# dws chat thread reply

kind: command
completeness: partial
usage: dws chat thread reply
description: Append a direct reply to an `openConvThreadId`.
use_when: When the agent needs to reply inside an existing Thread without quoting a message.
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
- dws chat thread add-emoji
- dws chat thread add-text-emotion
- dws chat thread create-group
- dws chat thread forward
- dws chat thread list
- dws chat thread list-emotion-replies
