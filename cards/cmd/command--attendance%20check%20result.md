# dws attendance check result

kind: command
completeness: full
description: 查询打卡结果
source: internal/helpers/attendance.go:652
visible_flags: 5

## Flags
- --users <String>: 用户 ID 列表，逗号分隔，最多 100 个 (必填)
- --start <String>: 起始日期，格式 YYYY-MM-DD (必填)
- --end <String>: 结束日期，格式 YYYY-MM-DD，不超过 1 个月 (必填)
- --offset <Int>: 分页偏移量，默认 0（可选）
- --limit <Int>: 分页大小，默认 100，范围 1-1000（可选）

## Related
- dws attendance check record
