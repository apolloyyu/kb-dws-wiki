# dws minutes upload cancel

kind: command
completeness: full
usage: dws minutes upload cancel
description: Cancel an in-progress meeting-note file upload session.
example: dws minutes upload cancel --session-id <sessionId>
use_when: When the agent aborts a multi-step upload due to user cancellation or upstream error.
source: internal/helpers/minutes.go:1646
visible_flags: 1

## Flags
- --session-id <String>: 要取消的会话 sessionId (必填)

## Related
- dws minutes upload complete
- dws minutes upload create
- dws minutes upload create-and-notify
