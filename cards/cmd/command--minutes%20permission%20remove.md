# dws minutes permission remove

kind: command
completeness: full
description: 批量移除听记成员权限
source: internal/helpers/minutes.go:1817
visible_flags: 2

## Flags
- --ids <String>: 听记 taskUuid 列表，逗号分隔 (必填)
- --member-uids <String>: 成员钉钉 UID 列表，逗号分隔 (必填)

## Related
- dws minutes permission add
- dws minutes permission apply
