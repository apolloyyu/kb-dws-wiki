# dws hrbrain profile query

kind: command
completeness: full
description: 按模块批量查询员工档案数据
source: internal/helpers/hrbrain.go:461
visible_flags: 2

## Flags
- --work-no <String>: 目标员工工号 (必填)
- --data-queries <String>: 按模块查询的条件列表 JSON 数组 (必填)

## Related
- dws hrbrain profile career
- dws hrbrain profile labels
- dws hrbrain profile metadata
- dws hrbrain profile performance
