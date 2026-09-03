# dws hrbrain profile metadata

kind: command
completeness: full
usage: dws hrbrain profile metadata
description: 查询员工档案元数据结构
example: dws hrbrain profile metadata --work-no WORK_NO
source: internal/helpers/hrbrain.go:415
visible_flags: 1

## Flags
- --work-no <String>: 员工工号 (必填)

## Related
- dws hrbrain profile career
- dws hrbrain profile labels
- dws hrbrain profile performance
- dws hrbrain profile query
