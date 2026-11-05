# dws aicard template update

kind: command
completeness: partial
usage: dws aicard template update
description: —
source: internal/helpers/aicard_template.go:100
visible_flags: 2
partial_reason: unverified_flags,missing_description

## Flags
- --template-id <String> required: Existing server-issued template ID
- --file <String> required: Path to the complete revised A2UI message-array JSON file

## Related
- dws aicard template create
- dws aicard template get
