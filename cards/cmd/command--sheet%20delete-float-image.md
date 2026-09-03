# dws sheet delete-float-image

kind: command
completeness: full
description: 删除浮动图片
source: internal/helpers/sheet_float_image.go:396
visible_flags: 3

## Flags
- --node <String>: 表格文档 ID 或 URL (必填)
- --sheet-id <String>: 工作表 ID 或名称 (必填)
- --float-image-id <String>: 浮动图片 ID (必填)

## Related
- dws sheet add-dimension
- dws sheet append
- dws sheet batch-set-style
- dws sheet batch-update
- dws sheet changeset-get
- dws sheet comment
