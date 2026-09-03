# dws calendar event delete

kind: command
completeness: full
usage: dws calendar event delete
description: Delete an existing calendar event by event ID.
example: dws calendar event delete --id EVENT_ID
use_when: When the agent cancels a previously scheduled event.
source: internal/helpers/calendar.go:453
visible_flags: 2

## Flags
- --id <String>: 日程 ID (必填)
- --calendar-id <String>: 日历 ID (可选，默认 primary 主日历；指定其他日历本时填写，可通过 book list 获取)

## Related
- dws calendar event create
- dws calendar event get
- dws calendar event instances
- dws calendar event list
- dws calendar event respond
- dws calendar event share-info
