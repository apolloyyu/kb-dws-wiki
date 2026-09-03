# dws sheet group-dimension

kind: command
completeness: full
description: 对指定连续行/列创建分组
source: internal/helpers/sheet_dimension.go:663
visible_flags: 4

## Flags
- --node <String>: 表格文档 ID 或 URL (必填)
- --sheet-id <String>: 工作表 ID 或名称 (必填)
- --range <String>: C:F
- --group-state <String>: 创建后的分组状态: expand 或 fold

## Related
- dws sheet add-dimension
- dws sheet append
- dws sheet batch-set-style
- dws sheet batch-update
- dws sheet changeset-get
- dws sheet comment
