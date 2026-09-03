# dws minutes upload complete

kind: command
completeness: full
description: Complete an upload session and create a meeting note from the uploaded audio/video.
use_when: When the agent finalizes a minutes upload, triggering transcription and AI processing.
source: internal/helpers/minutes.go:1587
visible_flags: 1

## Flags
- --session-id <String>: 上传会话 ID，来自 create 返回的 sessionId (必填)

## Related
- dws minutes upload cancel
- dws minutes upload create
- dws minutes upload create-and-notify
