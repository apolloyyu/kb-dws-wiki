# dws calendar room delete

kind: command
completeness: full
description: Release a previously booked meeting room from a calendar event.
use_when: When the agent cancels or changes the room on an existing event.
source: internal/helpers/calendar.go:453
visible_flags: 2

## Flags
- --id <String>: 日程 ID (必填)
- --calendar-id <String>: 日历 ID (可选，默认 primary 主日历；指定其他日历本时填写，可通过 book list 获取)

## Related
- dws calendar room add
- dws calendar room list-groups
- dws calendar room search
