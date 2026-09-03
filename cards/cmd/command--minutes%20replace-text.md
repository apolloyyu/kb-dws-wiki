# dws minutes replace-text

kind: command
completeness: full
usage: dws minutes replace-text
description: Find and replace matching text across a meeting note's transcript paragraphs and summary.
example: dws minutes replace-text --id <taskUuid> --search "旧文字" --replace "新文字"
use_when: When the agent corrects a systemic transcription mistake (e.g. wrong product name) throughout a note.
source: internal/helpers/minutes.go:1407
visible_flags: 3

## Flags
- --id <String>: 听记 taskUuid (必填)
- --search <String>: 要查找的文字 (必填)
- --replace <String>: 替换为的新文字 (必填)

## Related
- dws minutes audio-memo
- dws minutes get
- dws minutes hot-word
- dws minutes list
- dws minutes mind-graph
- dws minutes permission
