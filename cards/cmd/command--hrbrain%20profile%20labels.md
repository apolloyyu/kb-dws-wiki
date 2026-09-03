# dws hrbrain profile labels

kind: command
completeness: full
description: 获取员工标签
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
