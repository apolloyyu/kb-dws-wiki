# dws chat thread add-emoji

kind: command
completeness: full
usage: dws chat thread add-emoji
description: Add an emoji reaction to a Thread message.
use_when: When the agent needs to react to a Thread root or reply.
source: internal/helpers/chat_thread.go:691
visible_flags: 3

## Flags
- --conversation-id <String> required: 父群 openConversationId；处理回复时也可传 Thread openConvThreadId (必填)
- --message-id <String> required: 消息 openMessageId (必填)
- --emoji <String> required: emoji 表情名称 (必填)

## Related
- dws chat thread add-text-emotion
- dws chat thread create-group
- dws chat thread forward
- dws chat thread list
- dws chat thread list-emotion-replies
- dws chat thread list-replies
