# dws smart +suggest-time

kind: shortcut
completeness: full
description: 按姓名解析多位参与者，推荐大家都有空的可开会时间段（自动解析 userId）
source: internal/shortcut/smart/suggest_time.go:37
visible_flags: 4

## Flags
- --with <StringSlice>: 参与者姓名（逗号分隔的 CSV，如 张三,李四）
- --start <String>: 时间范围开始（ISO8601，如 2026-03-10T09:00:00+08:00）
- --end <String>: 时间范围结束（ISO8601，如 2026-03-10T18:00:00+08:00）
- --duration <String>: 会议时长（分钟，可选）

## Related
- dws smart +access-change
- dws smart +access-grant
- dws smart +access-revoke
- dws smart +action-items
- dws smart +assign
- dws smart +assign-multi
