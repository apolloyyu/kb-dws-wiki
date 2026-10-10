# dws chat thread update-text-emotion

kind: command
completeness: full
usage: dws chat thread update-text-emotion
description: Atomically replace a text emotion on a Thread message.
use_when: When the agent needs to change a Thread message status.
source: internal/helpers/chat_thread.go:889
visible_flags: 7

## Flags
- --conversation-id <String> required: 父群 openConversationId；处理回复时也可传 Thread openConvThreadId (必填)
- --message-id <String> required: 消息 openMessageId (必填)
- --old-emotion-id <String> required: 当前文字表情的 emotionId (必填)
- --emotion-id <String> required: 新文字表情的 emotionId (必填)
- --emotion-name <String> required: 新文字表情的名称 (必填)
- --text <String> required: 新文字表情的文字内容 (必填)
- --background-id <String> required: 新文字表情的 backgroundId (必填)

## Related
- dws chat thread add-emoji
- dws chat thread add-text-emotion
- dws chat thread create-group
- dws chat thread forward
- dws chat thread list
- dws chat thread list-emotion-replies
