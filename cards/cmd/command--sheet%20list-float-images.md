# dws sheet list-float-images

kind: command
completeness: full
description: 列出工作表所有浮动图片
source: internal/helpers/sheet_float_image.go:196
visible_flags: 2

## Flags
- --node <String>: 表格文档 ID 或 URL (必填)
- --sheet-id <String>: 工作表 ID 或名称 (必填)

## Related
- dws sheet add-dimension
- dws sheet append
- dws sheet batch-set-style
- dws sheet batch-update
- dws sheet changeset-get
- dws sheet comment
