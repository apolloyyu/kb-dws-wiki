# dws aicard preview

kind: command
completeness: partial
usage: dws aicard preview
description: Send a real A2UI card to the signed-in user
example: dws aicard preview --file card.a2ui.json --dry-run
source: internal/helpers/aicard.go:107
visible_flags: 2
partial_reason: unverified_flags

## Flags
- --file <String> required: Path to a complete new-card A2UI message-array JSON file
- --summary <String>: Conversation-list summary

## Related
- dws aicard explain
- dws aicard lint
