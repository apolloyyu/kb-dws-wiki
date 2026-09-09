# dws contract subject import-template

kind: command
completeness: full
usage: dws contract subject import-template
description: 获取相对方批量导入模板
example: dws contract subject import-template --format json
source: internal/helpers/contract.go:1456
visible_flags: 1

## Flags
- --type <String>: 相对方类型：other/our（可选）

## Related
- dws contract subject add
- dws contract subject auto-fill
- dws contract subject base-info
- dws contract subject batch-delete
- dws contract subject delete
- dws contract subject detail
