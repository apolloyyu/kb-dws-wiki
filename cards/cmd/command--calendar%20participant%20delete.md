# dws calendar participant delete

kind: command
completeness: full
description: Remove one or more participants from an existing calendar event.
use_when: When the agent drops attendees who no longer need to join the event.
source: internal/helpers/calendar.go:453
visible_flags: 2

## Flags
- --id <String>: 日程 ID (必填)
- --calendar-id <String>: 日历 ID (可选，默认 primary 主日历；指定其他日历本时填写，可通过 book list 获取)

## Related
- dws calendar participant add
- dws calendar participant list
