# dws dev app disable

kind: command
completeness: full
description: 禁用指定工作流（高危）
source: internal/helpers/aitable.go:5900
visible_flags: 2

## Flags
- --base-id <String>: 目标 Base ID (必填)
- --workflow-id <String>: 目标工作流 ID (必填)

## Related
- dws dev app create
- dws dev app delete
- dws dev app enable
- dws dev app get
- dws dev app list
- dws dev app update
