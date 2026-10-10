# dws dev app event subscribe

kind: command
completeness: partial
usage: dws dev app event subscribe
description: —
source: internal/helpers/devapp.go:344
visible_flags: 2
partial_reason: missing_description

## Flags
- --unified-app-id <String> required: 开放平台统一应用 ID（必填）
- --event-codes <String> required: 事件码，多个用逗号或分号分隔

## Related
- dws dev app event list
- dws dev app event unsubscribe
