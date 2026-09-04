# dws contract project add

kind: command
completeness: full
usage: dws contract project add
description: 新增项目
example: dws contract project add --name "2024采购项目" --format json
source: internal/helpers/contract.go:759
visible_flags: 8

## Flags
- --name <String>: 项目名称（必填）
- --code <String>: 项目编码
- --owners <String>: 负责人 staffId 列表，逗号分隔
- --start-date <String>: 开始日期（ISO-8601，如 2026-03-10T14:00:00+08:00）
- --end-date <String>: 结束日期（ISO-8601，须晚于 --start-date）
- --remark <String>: 备注
- --contract-ids <String>: 关联合同 ID 列表，逗号分隔
- --source <String>: 来源

## Related
- dws contract project delete
- dws contract project detail
- dws contract project digests
- dws contract project export
- dws contract project import
- dws contract project import-result
