# dws calendar attendee delete

kind: command
completeness: full
usage: dws calendar attendee delete
description: 移除参会人
example: dws calendar attendee delete --event EVENT_ID --attendees userId1
source: internal/helpers/calendar.go:772
visible_flags: 1

## Flags
- --attendees <String>: 参会人 userId 列表，逗号分隔 (必填)

## Related
- dws calendar attendee add
- dws calendar attendee list
