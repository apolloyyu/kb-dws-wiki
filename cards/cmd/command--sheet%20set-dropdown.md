# dws sheet set-dropdown

kind: command
completeness: full
description: 设置下拉列表
source: internal/helpers/sheet_dimension.go:795
visible_flags: 7

## Flags
- --node <String>: 表格文档 ID 或 URL (必填)
- --sheet-id <String>: 工作表 ID 或名称 (必填)
- --range <String>: 目标单元格范围，A1 表示法，如 A2:A100 (必填)
- --options <String>: #ff0000
- --source-sheet-id <String>: SourceRange 来源工作表 ID；使用 --source-range 时必填
- --source-range <String>: SourceRange 来源区域，与 --options 二选一；不含工作表前缀，如 T1:T3、T:T 或 1:3
- --multi-select <Bool>: 是否允许多选（默认单选）

## Related
- dws sheet add-dimension
- dws sheet append
- dws sheet batch-set-style
- dws sheet batch-update
- dws sheet changeset-get
- dws sheet comment
