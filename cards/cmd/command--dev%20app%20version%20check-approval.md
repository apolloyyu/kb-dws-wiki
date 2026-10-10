# dws dev app version check-approval

kind: command
completeness: partial
usage: dws dev app version check-approval
description: —
source: internal/helpers/devapp.go:1645
visible_flags: 2
partial_reason: missing_description

## Flags
- --unified-app-id <String> required: 开放平台统一应用 ID（必填）
- --version-id <String> required: 版本 ID (必填)

## Related
- dws dev app version create
- dws dev app version get
- dws dev app version list
- dws dev app version publish
- dws dev app version status
