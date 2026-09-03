# dws calendar room delete

kind: command
completeness: full
usage: dws calendar room delete
description: Release a previously booked meeting room from a calendar event.
example: dws calendar room delete --event EVENT_ID --rooms roomId1
use_when: When the agent cancels or changes the room on an existing event.
source: internal/helpers/calendar.go:1064
visible_flags: 3

## Flags
- --event <String>: 日程 ID (必填)
- --rooms <String>: 会议室 ID 列表 (必填)
- --calendar-id <String>: 日历 ID (可选，默认 primary 主日历；指定其他日历本时填写，可通过 book list 获取)。注意：订阅日历下的日程无会议室

## Related
- dws calendar room add
- dws calendar room list-groups
- dws calendar room search
