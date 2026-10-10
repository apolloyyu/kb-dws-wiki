# dws dev app permission add

kind: command
completeness: partial
usage: dws dev app permission add
description: —
source: internal/helpers/devapp.go:941
visible_flags: 2
partial_reason: missing_description

## Flags
- --unified-app-id <String> required: 开放平台统一应用 ID（必填）
- --scope-values <String> required: 权限点 scopeValue，多个用逗号或分号分隔

## Related
- dws dev app permission list
- dws dev app permission remove
