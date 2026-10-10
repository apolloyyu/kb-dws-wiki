# dws dev app member remove

kind: command
completeness: partial
usage: dws dev app member remove
description: —
source: internal/helpers/devapp.go:1091
visible_flags: 3
partial_reason: missing_description

## Flags
- --unified-app-id <String> required: 开放平台统一应用 ID（必填）
- --user-ids <String> required: 成员 userId 列表，多个用逗号分隔 (必填)
- --member-type <String> required: 成员类型，如 DEVELOPER (必填)

## Related
- dws dev app member add
- dws dev app member list
