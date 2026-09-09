# dws contract subject export

kind: command
completeness: full
usage: dws contract subject export
description: 导出相对方到 Excel
example: dws contract subject export --subject-ids "2001,2002" --format json
source: internal/helpers/contract.go:1431
visible_flags: 2

## Flags
- --subject-ids <String>: 相对方 ID 列表，逗号分隔（必填）
- --process-code <String>: 审批模板 code（可选）

## Related
- dws contract subject add
- dws contract subject auto-fill
- dws contract subject base-info
- dws contract subject batch-delete
- dws contract subject delete
- dws contract subject detail
