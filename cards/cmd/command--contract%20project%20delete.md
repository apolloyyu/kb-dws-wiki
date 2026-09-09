# dws contract project delete

kind: command
completeness: full
usage: dws contract project delete
description: 删除项目（支持批量）
example: dws contract project delete --project-ids "1001,1002" --format json
source: internal/helpers/contract.go:804
visible_flags: 1

## Flags
- --project-ids <String>: 项目 ID 列表，逗号分隔（必填）

## Related
- dws contract project add
- dws contract project detail
- dws contract project digests
- dws contract project export
- dws contract project import
- dws contract project import-result
