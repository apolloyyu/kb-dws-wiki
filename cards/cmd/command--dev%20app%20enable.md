# dws dev app enable

kind: command
completeness: full
description: 启用指定工作流
source: internal/helpers/aitable.go:5857
visible_flags: 2

## Flags
- --base-id <String>: 目标 Base ID (必填)
- --workflow-id <String>: 目标工作流 ID (必填)

## Related
- dws dev app create
- dws dev app delete
- dws dev app disable
- dws dev app get
- dws dev app list
- dws dev app update
