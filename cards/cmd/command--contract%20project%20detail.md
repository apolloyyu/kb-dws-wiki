# dws contract project detail

kind: command
completeness: full
usage: dws contract project detail
description: 查询项目详情
example: dws contract project detail --project-id 1001 --format json
source: internal/helpers/contract.go:1005
visible_flags: 1

## Flags
- --project-id <Int64>: 项目 ID（必填）

## Related
- dws contract project add
- dws contract project delete
- dws contract project digests
- dws contract project export
- dws contract project import
- dws contract project import-result
