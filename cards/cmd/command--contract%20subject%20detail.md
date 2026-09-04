# dws contract subject detail

kind: command
completeness: full
usage: dws contract subject detail
description: 查询相对方详情
example: dws contract subject detail --subject-id 2001 --format json
source: internal/helpers/contract.go:1256
visible_flags: 1

## Flags
- --subject-id <Int64>: 相对方 ID（必填）

## Related
- dws contract subject add
- dws contract subject auto-fill
- dws contract subject base-info
- dws contract subject batch-delete
- dws contract subject delete
- dws contract subject detect-risk
