# dws aicard preview

kind: command
completeness: partial
usage: dws aicard preview
description: Send a real A2UI card to the signed-in user
example: dws aicard preview --file card.a2ui.json --dry-run
source: internal/helpers/aicard.go:110
visible_flags: 3
partial_reason: unverified_flags

## Flags
- --file <String> required: Path to a complete new-card A2UI message-array JSON file
- --summary <String>: Fallback summary shown where the card cannot render
- --support-forward <Bool>: Allow forwarding the preview card (default false)

## Related
- dws aicard explain
- dws aicard lint
- dws aicard template
