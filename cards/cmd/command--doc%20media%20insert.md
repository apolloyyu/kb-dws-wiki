# dws doc media insert

kind: command
completeness: full
usage: dws doc media insert
description: 上传附件并插入文档
example: dws doc media insert --node DOC_ID --file ./report.pdf
source: internal/helpers/doc.go:2991
visible_flags: 7

## Flags
- --node <String>: 目标文档的标识，支持传入 URL 或 ID (必填)
- --file <String>: 本地文件路径 (必填)
- --name <String>: 附件显示名称 (默认使用文件名)
- --mime-type <String>: 文件 MIME 类型 (默认根据扩展名推断)
- --index <Int>: 插入位置索引
- --where <String>: 相对位置: before / after (配合 --ref-block)
- --ref-block <String>: 参考块 ID (配合 --where)

## Related
- dws doc media download
- dws doc media upload
