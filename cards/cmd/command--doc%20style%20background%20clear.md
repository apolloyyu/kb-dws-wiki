# dws doc style background clear

kind: command
completeness: full
usage: dws doc style background clear
description: 清除文档背景
example: dws doc style background clear --node DOC_ID
source: internal/helpers/doc_style.go:152
visible_flags: 1

## Flags
- --node <String>: 目标文档标识，支持 URL 或 ID (必填)

## Related
- dws doc style background set
