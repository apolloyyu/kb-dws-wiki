# dws aicard template get

kind: command
completeness: partial
usage: dws aicard template get
description: —
source: internal/helpers/aicard_template.go:75
visible_flags: 3
partial_reason: unverified_flags,missing_description

## Flags
- --template-id <String> required: Server-issued template ID
- --version <String> required: Requested template version: positive decimal int64 string
- --out <String> required: New destination file; refuses to overwrite an existing path

## Related
- dws aicard template create
- dws aicard template update
