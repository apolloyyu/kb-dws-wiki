# dws sheet delete-dropdown

kind: command
completeness: full
description: 删除下拉列表
source: internal/helpers/sheet_dimension.go:1002
visible_flags: 3

## Flags
- --node <String>: 表格文档 ID 或 URL (必填)
- --sheet-id <String>: 工作表 ID 或名称 (必填)
- --range <String>: 要删除下拉列表的范围，A1 表示法，如 A2:A100 (必填)

## Related
- dws sheet add-dimension
- dws sheet append
- dws sheet batch-set-style
- dws sheet batch-update
- dws sheet changeset-get
- dws sheet comment
