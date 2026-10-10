# dws dev app create

kind: command
completeness: partial
usage: dws dev app create
description: —
source: internal/helpers/devapp.go:512
visible_flags: 3
partial_reason: missing_description

## Flags
- --name <String> required: 应用名称 (必填)
- --desc <String>: 应用描述
- --icon-media-id <String>: 应用图标 mediaId

## Related
- dws dev app credentials
- dws dev app delete
- dws dev app disable
- dws dev app enable
- dws dev app event
- dws dev app get
