# dws dev app delete

kind: command
completeness: partial
usage: dws dev app delete
description: —
source: internal/helpers/devapp.go:712
visible_flags: 2
partial_reason: missing_description

## Flags
- --unified-app-id <String> required: 开放平台统一应用 ID（必填）
- --confirm-name <String>: 二次确认：必须与被删应用的名称一致（不可逆操作的防误删）

## Related
- dws dev app create
- dws dev app credentials
- dws dev app disable
- dws dev app enable
- dws dev app event
- dws dev app get
