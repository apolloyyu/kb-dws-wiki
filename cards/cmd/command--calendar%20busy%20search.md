# dws calendar busy search

kind: command
completeness: full
usage: dws calendar busy search
description: Query the busy/free time windows of one or more users over a given range.
example: dws calendar busy search --users userId1,userId2 --start "2026-03-10T14:00:00+08:00" --end "2026-03-10T18:00:00+08:00"
use_when: When the agent is scheduling a meeting and needs to find a slot where all attendees are free.
source: internal/helpers/calendar.go:1182
visible_flags: 4

## Flags
- --users <String>: 用户 ID 列表，逗号分隔 (与 --rooms 至少指定其一)
- --rooms <String>: 会议室 ID 列表，逗号分隔 (与 --users 至少指定其一，用于查询会议室闲忙)
- --start <String>: 开始时间 ISO-8601 (必填，例如 2026-03-10T14:00:00+08:00)
- --end <String>: 结束时间 ISO-8601 (必填，例如 2026-03-10T18:00:00+08:00)

## Related
- none
