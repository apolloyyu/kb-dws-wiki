# dws chat thread add-text-emotion

kind: command
completeness: full
usage: dws chat thread add-text-emotion
description: Add a text emotion to a Thread message.
use_when: When the agent needs to attach a known text status such as processing or resolved.
source: internal/helpers/chat_thread.go:799
visible_flags: 6

## Flags
- --conversation-id <String> required: 父群 openConversationId；处理回复时也可传 Thread openConvThreadId (必填)
- --message-id <String> required: 消息 openMessageId (必填)
- --emotion-id <String> required: create-text-emotion 返回的 emotionId (必填)
- --emotion-name <String> required: create-text-emotion 返回的表情名称 (必填)
- --text <String> required: create-text-emotion 返回的文字内容 (必填)
- --background-id <String> required: create-text-emotion 返回的 backgroundId (必填)

## Related
- dws chat thread add-emoji
- dws chat thread create-group
- dws chat thread forward
- dws chat thread list
- dws chat thread list-emotion-replies
- dws chat thread list-replies
