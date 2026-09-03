# dws dev app robot enable

kind: command
completeness: full
description: 启用指定工作流
source: internal/helpers/aitable.go:5857
visible_flags: 2

## Flags
- --base-id <String>: 目标 Base ID (必填)
- --workflow-id <String>: 目标工作流 ID (必填)

## Related
- dws dev app robot config
- dws dev app robot disable
- dws dev app robot get
- dws dev app robot result
- dws dev app robot submit
