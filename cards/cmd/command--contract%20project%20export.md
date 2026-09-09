# dws contract project export

kind: command
completeness: full
usage: dws contract project export
description: 项目导出到 Excel
example: dws contract project export --project-ids "1001,1002" --format json
source: internal/helpers/contract.go:1024
visible_flags: 2

## Flags
- --project-ids <String>: 项目 ID 列表，逗号分隔（必填）
- --process-code <String>: 审批模板 code（可选）

## Related
- dws contract project add
- dws contract project delete
- dws contract project detail
- dws contract project digests
- dws contract project import
- dws contract project import-result
