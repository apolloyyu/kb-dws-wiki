# dws doc delete

kind: command
completeness: full
usage: dws doc delete
description: 删除文档/文件到回收站
example: dws doc delete --node DOC_ID --yes
source: internal/helpers/doc.go:2623
visible_flags: 1

## Flags
- --node <String>: 文档/文件 ID 或 URL (必填)

## Related
- dws doc block
- dws doc comment
- dws doc copy
- dws doc create
- dws doc download
- dws doc export
