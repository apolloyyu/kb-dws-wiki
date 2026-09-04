# dws contract subject delete

kind: command
completeness: full
usage: dws contract subject delete
description: 删除相对方（单个）
example: dws contract subject delete --subject-id 2001 --format json
source: internal/helpers/contract.go:1300
visible_flags: 1

## Flags
- --subject-id <Int64>: 相对方 ID（必填）

## Related
- dws contract subject add
- dws contract subject auto-fill
- dws contract subject base-info
- dws contract subject batch-delete
- dws contract subject detail
- dws contract subject detect-risk
