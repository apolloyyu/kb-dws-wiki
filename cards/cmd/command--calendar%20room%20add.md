# dws calendar room add

kind: command
completeness: full
description: Book a specific meeting room onto an existing calendar event.
use_when: When the agent needs to attach a physical meeting room to an already-scheduled event.
source: internal/helpers/calendar.go:703
visible_flags: 2

## Flags
- --attendees <String>: 参会人 userId 列表，逗号分隔 (必填，最多500人)
- --optional <Bool>: 参会人可选 (默认必选参会人)

## Related
- dws calendar room delete
- dws calendar room list-groups
- dws calendar room search
