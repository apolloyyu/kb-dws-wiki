# dws smart +book

kind: shortcut
completeness: full
description: 创建日程，并可按姓名邀请参会人（自动解析 userId，失败自动回滚删除日程）
source: internal/shortcut/smart/book.go:41
visible_flags: 4

## Flags
- --title <String>: 日程标题
- --start <String>: 开始时间（ISO8601，如 2026-03-10T14:00:00+08:00）
- --end <String>: 结束时间（ISO8601，如 2026-03-10T15:00:00+08:00）
- --with <String>: 参会人姓名，逗号分隔（可选）

## Related
- dws smart +access-change
- dws smart +access-grant
- dws smart +access-revoke
- dws smart +action-items
- dws smart +assign
- dws smart +assign-multi
