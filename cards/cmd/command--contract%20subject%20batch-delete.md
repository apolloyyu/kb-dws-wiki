# dws contract subject batch-delete

kind: command
completeness: full
usage: dws contract subject batch-delete
description: 批量删除相对方
example: dws contract subject batch-delete --subject-ids "2001,2002,2003" --format json
source: internal/helpers/contract.go:1319
visible_flags: 1

## Flags
- --subject-ids <String>: 相对方 ID 列表，逗号分隔（必填，最多 1000 个）

## Related
- dws contract subject add
- dws contract subject auto-fill
- dws contract subject base-info
- dws contract subject delete
- dws contract subject detail
- dws contract subject detect-risk
