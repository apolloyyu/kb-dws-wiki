# dws dev app robot disable

kind: command
completeness: full
description: 禁用指定工作流（高危）
source: internal/helpers/aitable.go:5900
visible_flags: 2

## Flags
- --base-id <String>: 目标 Base ID (必填)
- --workflow-id <String>: 目标工作流 ID (必填)

## Related
- dws dev app robot config
- dws dev app robot enable
- dws dev app robot get
- dws dev app robot result
- dws dev app robot submit
