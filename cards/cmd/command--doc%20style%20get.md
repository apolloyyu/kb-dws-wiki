# dws doc style get

kind: command
completeness: full
usage: dws doc style get
description: 读取文档封面/背景 (只读)
example: dws doc style get --node DOC_ID
source: internal/helpers/doc_style.go:185
visible_flags: 1

## Flags
- --node <String>: 目标文档标识，支持 URL 或 ID (必填)

## Related
- dws doc style background
- dws doc style cover
