# dws minutes update title

kind: command
completeness: full
usage: dws minutes update title
description: Update the title of a meeting note.
example: dws minutes update title --id <taskUuid> --title "Q2 复盘会议"
use_when: When the agent renames a meeting note for clarity before sharing or archiving.
source: internal/helpers/minutes.go:555
visible_flags: 2

## Flags
- --id <String>: 听记 taskUuid (必填)
- --title <String>: 新标题 (必填)

## Related
- dws minutes update summary
