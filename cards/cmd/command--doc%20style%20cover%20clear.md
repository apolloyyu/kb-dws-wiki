# dws doc style cover clear

kind: command
completeness: full
usage: dws doc style cover clear
description: 移除文档封面
example: dws doc style cover clear --node DOC_ID
source: internal/helpers/doc_style.go:79
visible_flags: 1

## Flags
- --node <String>: 目标文档标识，支持 URL 或 ID (必填)

## Related
- dws doc style cover set
