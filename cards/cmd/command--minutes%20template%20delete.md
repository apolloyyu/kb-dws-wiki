# dws minutes template delete

kind: command
completeness: partial
usage: dws minutes template delete
description: —
source: internal/helpers/minutes.go:2416
visible_flags: 1
partial_reason: missing_description

## Flags
- --template-key <String> required: 待删除的本人个人模板templateKey

## Related
- dws minutes template create
- dws minutes template list-custom
- dws minutes template list-system
- dws minutes template set-default
- dws minutes template update
