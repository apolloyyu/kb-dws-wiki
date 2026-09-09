# dws contract project list

kind: command
completeness: full
usage: dws contract project list
description: 分页查询项目列表
example: dws contract project list --current-page 1 --page-size 20 --scope all --format json
source: internal/helpers/contract.go:896
visible_flags: 11

## Flags
- --current-page <Int64>: 当前页码（必填，正整数）
- --page-size <Int64>: 每页条数（必填，正整数）
- --scope <String>: 查询范围：self(我负责的)/all(所有项目)（必填）
- --name <String>: 项目名称（模糊搜索）
- --code <String>: 项目编码
- --owners <String>: 负责人 staffId 列表，逗号分隔
- --status <String>: 项目状态
- --start-date-left <String>: 开始日期左区间（ISO-8601，如 2026-01-01T00:00:00+08:00）
- --start-date-right <String>: 开始日期右区间（ISO-8601）
- --end-date-left <String>: 结束日期左区间（ISO-8601）
- --end-date-right <String>: 结束日期右区间（ISO-8601）

## Related
- dws contract project add
- dws contract project delete
- dws contract project detail
- dws contract project digests
- dws contract project export
- dws contract project import
