# dws sheet write-image

kind: command
completeness: full
description: 上传图片并写入表格单元格
source: internal/helpers/sheet_media.go:330
visible_flags: 8

## Flags
- --node <String>: 目标表格文档的标识，支持传入 URL 或 ID (必填)
- --sheet-id <String>: 工作表 ID 或名称 (必填)
- --range <String>: 目标单元格区域地址，如 A1:B3 (必填)
- --file <String>: 本地图片文件路径 (必填)
- --name <String>: 图片显示名称 (默认使用文件名)
- --mime-type <String>: 文件 MIME 类型 (默认根据扩展名推断)
- --width <Int>: 图片显示宽度 (可选)
- --height <Int>: 图片显示高度 (可选)

## Related
- dws sheet add-dimension
- dws sheet append
- dws sheet batch-set-style
- dws sheet batch-update
- dws sheet changeset-get
- dws sheet comment
