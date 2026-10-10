# dws chat thread remove-emoji

kind: command
completeness: full
usage: dws chat thread remove-emoji
description: Remove the current user's emoji reaction from a Thread message.
use_when: When the agent needs to undo a Thread reaction.
source: internal/helpers/chat_thread.go:729
visible_flags: 3

## Flags
- --conversation-id <String> required: 父群 openConversationId；处理回复时也可传 Thread openConvThreadId (必填)
- --message-id <String> required: 消息 openMessageId (必填)
- --emoji <String> required: emoji 表情名称 (必填)

## Related
- dws chat thread add-emoji
- dws chat thread add-text-emotion
- dws chat thread create-group
- dws chat thread forward
- dws chat thread list
- dws chat thread list-emotion-replies
