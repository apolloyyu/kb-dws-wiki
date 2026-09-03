# dws hrbrain profile labels

kind: command
completeness: full
usage: dws hrbrain profile labels
description: 获取员工标签
example: dws hrbrain profile labels --staff-ids WORK_NO1,WORK_NO2 --all-label
source: internal/helpers/hrbrain.go:523
visible_flags: 2

## Flags
- --staff-ids <String>: 员工工号列表，逗号分隔 (必填)
- --all-label <Bool>: 是否所有标签 (可选)

## Related
- dws hrbrain profile career
- dws hrbrain profile metadata
- dws hrbrain profile performance
- dws hrbrain profile query
