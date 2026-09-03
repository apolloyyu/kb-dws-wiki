# dws chat thread create-group

kind: command
completeness: partial
usage: dws chat thread create-group
description: Create a group with Thread mode enabled.
use_when: When the agent needs a new topic-circle container rather than an ordinary group chat.
source: internal/helpers/chat_thread.go:190
visible_flags: 0
partial_reason: unverified_usage,unverified_flags

## Flags
- none

## Related
- dws chat thread add-emoji
- dws chat thread add-text-emotion
- dws chat thread forward
- dws chat thread list
- dws chat thread list-emotion-replies
- dws chat thread list-replies
