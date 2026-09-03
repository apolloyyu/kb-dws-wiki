# dws minutes get transcription

kind: command
completeness: full
description: Retrieve the raw speech-to-text transcription of a meeting note.
use_when: When the agent needs the full verbatim transcript for deep analysis or quoting.
source: internal/helpers/minutes.go:326
visible_flags: 3

## Flags
- --id <String>: 听记 taskUuid (必填)
- --direction <String>: 排序方向: 0=正序, 1=倒序 (默认 0)
- --cursor <String>: 分页 token (首页留空)

## Related
- dws minutes get audio
- dws minutes get batch
- dws minutes get info
- dws minutes get keywords
- dws minutes get summary
- dws minutes get todos
