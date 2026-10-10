# dws dev app event list

kind: command
completeness: partial
usage: dws dev app event list
description: —
source: internal/helpers/devapp.go:308
visible_flags: 2
partial_reason: missing_description

## Flags
- --unified-app-id <String> required: 开放平台统一应用 ID（必填）
- --keyword <String>: 事件搜索关键词，支持按事件码或事件名称模糊匹配

## Related
- dws dev app event subscribe
- dws dev app event unsubscribe
