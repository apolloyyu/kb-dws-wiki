# dws minutes update summary

kind: command
completeness: full
usage: dws minutes update summary
description: Overwrite the summary content of a meeting note.
example: dws minutes update summary --id <taskUuid> --content "新的纪要内容"
use_when: When the agent refines or replaces the AI-generated summary with a corrected or customized version.
source: internal/helpers/minutes.go:886
visible_flags: 2

## Flags
- --id <String>: 听记 taskUuid (必填)
- --content <String>: 新的纪要内容 (必填)

## Related
- dws minutes update title
