# dws minutes +record-stop

kind: shortcut
completeness: full
usage: dws minutes +record-stop
description: 结束听记录音
source: internal/shortcut/minutes/minutes.go:485
visible_flags: 2

## Flags
- --id <String>: 听记 taskUuid
- --session-id <String>: AI 助理会话 ID (可选)

## Related
- dws minutes +apply-permission
- dws minutes +download
- dws minutes +export-pack
- dws minutes +list-all
- dws minutes +list-mine
- dws minutes +list-shared
