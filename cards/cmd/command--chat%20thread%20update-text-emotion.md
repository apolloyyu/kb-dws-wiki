# dws chat thread update-text-emotion

kind: command
completeness: partial
usage: dws chat thread update-text-emotion
description: Atomically replace a text emotion on a Thread message.
use_when: When the agent needs to change a Thread message status.
source: internal/helpers/chat_thread.go:908
visible_flags: 0
partial_reason: unverified_usage,unverified_flags

## Flags
- none

## Related
- dws chat thread add-emoji
- dws chat thread add-text-emotion
- dws chat thread create-group
- dws chat thread forward
- dws chat thread list
- dws chat thread list-emotion-replies
