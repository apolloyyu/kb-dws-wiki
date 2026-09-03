# dws hrbrain profile career

kind: command
completeness: full
usage: dws hrbrain profile career
description: 查询员工公司内职业历程
example: dws hrbrain profile career --work-no WORK_NO
source: internal/helpers/hrbrain.go:576
visible_flags: 1

## Flags
- --work-no <String>: 员工工号 (必填)

## Related
- dws hrbrain profile labels
- dws hrbrain profile metadata
- dws hrbrain profile performance
- dws hrbrain profile query
