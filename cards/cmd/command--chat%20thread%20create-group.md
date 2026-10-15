# dws chat thread create-group

kind: command
completeness: full
usage: dws chat thread create-group
description: Create a group with Thread mode enabled.
use_when: When the agent needs a new topic-circle container rather than an ordinary group chat.
source: internal/helpers/chat_thread.go:165
visible_flags: 3

## Flags
- --name <String> required: 话题圈名称 (必填)
- --users <String> required: 成员 userId 或 openDingTalkId，逗号分隔 (必填)
- --type <String>: 话题圈类型: INTERNAL/EXTERNAL/NORMAL

## Related
- dws chat thread add-emoji
- dws chat thread add-text-emotion
- dws chat thread forward
- dws chat thread list
- dws chat thread list-emotion-replies
- dws chat thread list-replies
