# dws chat thread recall-message

kind: command
completeness: full
usage: dws chat thread recall-message
description: Recall one message from a Thread.
use_when: When the agent needs to retract one Thread reply or root message.
source: internal/helpers/chat_thread.go:652
visible_flags: 2

## Flags
- --conversation-id <String> required: 父群 openConversationId；处理回复时也可传 Thread openConvThreadId (必填)
- --message-id <String> required: 消息 openMessageId (必填)

## Related
- dws chat thread add-emoji
- dws chat thread add-text-emotion
- dws chat thread create-group
- dws chat thread forward
- dws chat thread list
- dws chat thread list-emotion-replies
