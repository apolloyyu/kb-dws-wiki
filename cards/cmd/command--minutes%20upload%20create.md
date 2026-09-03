# dws minutes upload create

kind: command
completeness: full
description: Create a file upload session for producing a meeting note from a local audio/video file.
use_when: When the agent begins uploading a recording to be turned into a meeting note.
source: internal/helpers/minutes.go:953
visible_flags: 1

## Flags
- --id <String>: 听记 taskUuid (必填)

## Related
- dws minutes upload cancel
- dws minutes upload complete
- dws minutes upload create-and-notify
