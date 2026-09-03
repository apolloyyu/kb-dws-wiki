# dws sheet create-float-image

kind: command
completeness: full
usage: dws sheet create-float-image
description: 创建浮动图片
example: dws sheet create-float-image --node NODE_ID --sheet-id SHEET_ID
source: internal/helpers/sheet_float_image.go:11
visible_flags: 9

## Flags
- --node <String>: 表格文档 ID 或 URL (必填)
- --sheet-id <String>: 工作表 ID 或名称 (必填)
- --file <String>: 本地图片文件路径，与 --src 二选一
- --src <String>: 通过 media-upload 获取的 resourceUrl，与 --file 二选一
- --range <String>: 锚点单元格，A1 表示法，如 A1、B3 (必填)
- --width <Int>: 图片宽度，像素 (必填)
- --height <Int>: 图片高度，像素 (必填)
- --offset-x <Int>: 水平偏移量，像素 (默认 0)
- --offset-y <Int>: 垂直偏移量，像素 (默认 0)

## Related
- dws sheet add-dimension
- dws sheet append
- dws sheet batch-update
- dws sheet changeset-get
- dws sheet chart
- dws sheet comment
