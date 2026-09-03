# dws calendar event get

kind: command
completeness: full
usage: dws calendar event get
description: Retrieve the full details of a calendar event, including participants, location, and body.
example: dws calendar event get --id EVENT_ID
use_when: When the agent needs to inspect an event before updating or referencing it.
source: internal/helpers/calendar.go:178
visible_flags: 2

## Flags
- --id <String>: 日程 ID (必填)
- --calendar-id <String>: 日历 ID (默认 primary 主日历)

## Related
- dws calendar event create
- dws calendar event delete
- dws calendar event instances
- dws calendar event list
- dws calendar event respond
- dws calendar event share-info
