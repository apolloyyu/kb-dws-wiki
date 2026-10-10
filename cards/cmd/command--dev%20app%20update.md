# dws dev app update

kind: command
completeness: partial
usage: dws dev app update
description: —
source: internal/helpers/devapp.go:549
visible_flags: 4
partial_reason: missing_description

## Flags
- --unified-app-id <String> required: 开放平台统一应用 ID（必填）
- --name <String>: 新的应用名称
- --desc <String>: 新的应用描述
- --icon-media-id <String>: 新的应用图标 mediaId

## Related
- dws dev app create
- dws dev app credentials
- dws dev app delete
- dws dev app disable
- dws dev app enable
- dws dev app event
