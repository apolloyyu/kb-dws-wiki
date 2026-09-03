# dws sheet update-float-image

kind: command
completeness: full
description: 更新浮动图片属性
source: internal/helpers/sheet_float_image.go:243
visible_flags: 10

## Flags
- --node <String>: 表格文档 ID 或 URL (必填)
- --sheet-id <String>: 工作表 ID 或名称 (必填)
- --float-image-id <String>: 浮动图片 ID (必填)
- --file <String>: 用于替换浮动图片的本地图片路径，与 --src 不能同时使用
- --src <String>: 新的图片资源路径，通过 media-upload 获取的 resourceUrl
- --range <String>: 新的锚点单元格，A1 表示法
- --width <Int>: 新的图片宽度，像素
- --height <Int>: 新的图片高度，像素
- --offset-x <Int>: 新的水平偏移量，像素
- --offset-y <Int>: 新的垂直偏移量，像素

## Related
- dws sheet add-dimension
- dws sheet append
- dws sheet batch-set-style
- dws sheet batch-update
- dws sheet changeset-get
- dws sheet comment
