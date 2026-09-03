# dws calendar room add

kind: command
completeness: full
usage: dws calendar room add
description: Book a specific meeting room onto an existing calendar event.
example: dws calendar room add --event EVENT_ID --rooms roomId1,roomId2
use_when: When the agent needs to attach a physical meeting room to an already-scheduled event.
source: internal/helpers/calendar.go:1000
visible_flags: 3

## Flags
- --event <String>: 日程 ID (必填)
- --rooms <String>: 会议室 ID 列表 (必填)
- --calendar-id <String>: 日历 ID (可选，默认 primary 主日历；指定其他日历本时填写，可通过 book list 获取)，注意：订阅日历下的日程不支持添加会议室

## Related
- dws calendar room delete
- dws calendar room list-groups
- dws calendar room search
