# dws contract project update

kind: command
completeness: full
usage: dws contract project update
description: 更新项目信息
example: dws contract project update --project-id 1001 --name "更新后的名称" --format json
source: internal/helpers/contract.go:827
visible_flags: 8

## Flags
- --project-id <Int64>: 项目 ID（必填）
- --name <String>: 项目名称（必填）
- --code <String>: 项目编码
- --owners <String>: 负责人 staffId 列表，逗号分隔
- --start-date <String>: 开始日期（ISO-8601，如 2026-03-10T14:00:00+08:00）
- --end-date <String>: 结束日期（ISO-8601，须晚于 --start-date）
- --remark <String>: 备注
- --contract-ids <String>: 关联合同 ID 列表，逗号分隔

## Related
- dws contract project add
- dws contract project delete
- dws contract project detail
- dws contract project digests
- dws contract project export
- dws contract project import
