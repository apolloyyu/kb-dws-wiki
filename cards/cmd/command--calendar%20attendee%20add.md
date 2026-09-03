# dws calendar attendee add

kind: command
completeness: full
usage: dws calendar attendee add
description: 添加参会人
example: dws calendar attendee add --event EVENT_ID --attendees userId1,userId2
source: internal/helpers/calendar.go:703
visible_flags: 2

## Flags
- --attendees <String>: 参会人 userId 列表，逗号分隔 (必填，最多500人)
- --optional <Bool>: 参会人可选 (默认必选参会人)

## Related
- dws calendar attendee delete
- dws calendar attendee list
