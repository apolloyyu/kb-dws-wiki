# dws contract subject list

kind: command
completeness: full
usage: dws contract subject list
description: 查询相对方列表
example: dws contract subject list --current-page 1 --page-size 20 --format json
source: internal/helpers/contract.go:1218
visible_flags: 6

## Flags
- --current-page <Int64>: 当前页码（必填，正整数）
- --page-size <Int64>: 每页条数（必填，正整数）
- --party-type <String>: 相对方类型：other(对方)/our(己方)
- --name <String>: 相对方名称（模糊匹配）
- --code <String>: 主体编号
- --source <String>: 来源：contract/oa

## Related
- dws contract subject add
- dws contract subject auto-fill
- dws contract subject base-info
- dws contract subject batch-delete
- dws contract subject delete
- dws contract subject detail
