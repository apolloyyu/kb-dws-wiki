# dws chat thread list-emotion-replies

kind: command
completeness: full
description: List emoji and text-emotion replies for Thread messages.
use_when: When the agent needs reaction users or statistics for Thread messages.
source: internal/helpers/chat.go:10890
visible_flags: 1

## Flags
- --msg-ids <String> required: 消息 ID 列表，逗号分隔 (必填)

## Related
- dws chat thread add-emoji
- dws chat thread add-text-emotion
- dws chat thread create-group
- dws chat thread forward
- dws chat thread list
- dws chat thread list-replies
