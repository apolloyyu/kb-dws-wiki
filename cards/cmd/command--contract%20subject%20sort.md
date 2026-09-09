# dws contract subject sort

kind: command
completeness: full
usage: dws contract subject sort
description: 己方主体排序
example: dws contract subject sort --subject-ids "2001,2003,2002" --format json
source: internal/helpers/contract.go:1345
visible_flags: 1

## Flags
- --subject-ids <String>: 己方主体 ID 列表，逗号分隔，按期望顺序（必填）

## Related
- dws contract subject add
- dws contract subject auto-fill
- dws contract subject base-info
- dws contract subject batch-delete
- dws contract subject delete
- dws contract subject detail
