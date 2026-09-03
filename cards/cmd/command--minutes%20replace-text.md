# dws minutes replace-text

kind: command
completeness: full
description: Find and replace matching text across a meeting note's transcript paragraphs and summary.
use_when: When the agent corrects a systemic transcription mistake (e.g. wrong product name) throughout a note.
source: internal/helpers/minutes.go:1407
visible_flags: 3

## Flags
- --id <String>: 听记 taskUuid (必填)
- --search <String>: 要查找的文字 (必填)
- --replace <String>: 替换为的新文字 (必填)

## Related
- none
