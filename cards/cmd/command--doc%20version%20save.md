# dws doc version save

kind: command
completeness: full
usage: dws doc version save
description: 手动保存文档版本快照
example: dws doc version save --node DOC_ID
source: internal/helpers/doc.go:4424
visible_flags: 1

## Flags
- --node <String>: 文档 ID 或 URL (必填)

## Related
- dws doc version list
- dws doc version revert
