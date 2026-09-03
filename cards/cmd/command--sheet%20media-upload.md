# dws sheet media-upload

kind: command
completeness: full
usage: dws sheet media-upload
description: 上传附件到表格
example: dws sheet media-upload --node SHEET_DOC_ID --file ./report.pdf
source: internal/helpers/sheet_media.go:271
visible_flags: 4

## Flags
- --node <String>: 目标表格文档的标识，支持传入 URL 或 ID (必填)
- --file <String>: 本地文件路径 (必填)
- --name <String>: 附件显示名称 (默认使用文件名)
- --mime-type <String>: 文件 MIME 类型 (默认根据扩展名推断)

## Related
- dws sheet add-dimension
- dws sheet append
- dws sheet batch-update
- dws sheet changeset-get
- dws sheet chart
- dws sheet comment
