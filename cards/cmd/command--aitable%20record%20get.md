# dws aitable record get

kind: command
completeness: full
description: 获取 AI 表格信息
source: internal/helpers/aitable.go:1812
visible_flags: 1

## Flags
- --base-id <String>: Base 唯一标识。优先使用 base search / base list 返回值 (必填)

## Related
- dws aitable record batch-update
- dws aitable record create
- dws aitable record delete
- dws aitable record group-stats
- dws aitable record history-list
- dws aitable record list
