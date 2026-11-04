# dws minutes template set-default

kind: command
completeness: partial
usage: dws minutes template set-default
description: —
source: internal/helpers/minutes.go:2432
visible_flags: 3
partial_reason: missing_description

## Flags
- --template-id <String>: 官方templateId，与template-key二选一，不能填diy或空串
- --template-key <String>: 本人个人模板templateKey，与template-id二选一
- --locale <String>: 可选，校验系统模板目录时使用

## Related
- dws minutes template create
- dws minutes template delete
- dws minutes template list-custom
- dws minutes template list-system
- dws minutes template update
