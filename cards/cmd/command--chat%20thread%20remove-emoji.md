# dws chat thread remove-emoji

kind: command
completeness: partial
usage: dws chat thread remove-emoji
description: Remove the current user's emoji reaction from a Thread message.
use_when: When the agent needs to undo a Thread reaction.
source: internal/helpers/chat_thread.go:744
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
