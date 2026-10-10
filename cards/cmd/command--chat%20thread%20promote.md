# dws chat thread promote

kind: command
completeness: partial
usage: dws chat thread promote
description: —
source: internal/helpers/chat_thread.go:94
visible_flags: 2
partial_reason: missing_description

## Flags
- --conversation-id <String> required: 消息所属普通群的 openConversationId (必填)
- --message-id <String> required: 待升级消息的 openMessageId (必填)

## Related
- dws chat thread add-emoji
- dws chat thread add-text-emotion
- dws chat thread create-group
- dws chat thread forward
- dws chat thread list
- dws chat thread list-emotion-replies
