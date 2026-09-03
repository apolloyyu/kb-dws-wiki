# dws doc style background set

kind: command
completeness: full
usage: dws doc style background set
description: 设置文档背景纯色
example: dws doc style background set --node DOC_ID --color "
source: internal/helpers/doc_style.go:118
visible_flags: 2

## Flags
- --node <String>: 目标文档标识，支持 URL 或 ID (必填)
- --color <String>: 背景纯色，如 #E8F2FE (必填)

## Related
- dws doc style background clear
