# dws sheet get-float-image

kind: command
completeness: full
usage: dws sheet get-float-image
description: 获取浮动图片详情
example: dws sheet get-float-image --node NODE_ID --sheet-id SHEET_ID --float-image-id FI_ID
source: internal/helpers/sheet_float_image.go:146
visible_flags: 3

## Flags
- --node <String>: 表格文档 ID 或 URL (必填)
- --sheet-id <String>: 工作表 ID 或名称 (必填)
- --float-image-id <String>: 浮动图片 ID (必填)

## Related
- dws sheet add-dimension
- dws sheet append
- dws sheet batch-update
- dws sheet changeset-get
- dws sheet chart
- dws sheet comment
