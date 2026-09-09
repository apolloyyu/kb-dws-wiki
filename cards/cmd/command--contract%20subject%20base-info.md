# dws contract subject base-info

kind: command
completeness: full
usage: dws contract subject base-info
description: 查询相对方工商基本信息
example: dws contract subject base-info --subject-name "北京示例科技有限公司" --format json
source: internal/helpers/contract.go:1389
visible_flags: 2

## Flags
- --subject-name <String>: 相对方名称（必填）
- --subject-id <Int64>: 相对方 ID（可选）

## Related
- dws contract subject add
- dws contract subject auto-fill
- dws contract subject batch-delete
- dws contract subject delete
- dws contract subject detail
- dws contract subject detect-risk
