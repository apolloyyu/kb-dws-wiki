# dws chat thread forward

kind: command
completeness: partial
usage: dws chat thread forward
description: Forward a complete Thread with its context.
example: dws chat thread forward --src-msg-id <messageId> --src-conversation-id <openConversationId> --src-thread-id <openConvThreadId> --dest-conversation-id <openConversationId>
use_when: When the agent needs to copy a Thread into another conversation.
source: internal/helpers/chat_thread.go:1021
visible_flags: 0
partial_reason: unverified_flags,empty_flag_name

## Flags
- none

## Related
- dws chat thread add-emoji
- dws chat thread add-text-emotion
- dws chat thread create-group
- dws chat thread list
- dws chat thread list-emotion-replies
- dws chat thread list-replies
