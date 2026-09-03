# dws minutes +record-wrap-up

kind: shortcut
completeness: full
usage: dws minutes +record-wrap-up
description: 停止实时录音并有界等待听记产物，失败时保留恢复句柄
source: internal/shortcut/minutes/workflows.go:40
visible_flags: 5

## Flags
- --id <String>: 正在录制的听记 taskUuid
- --artifacts <StringSlice>: 停止后等待的产物
- --wait-timeout <Int>: —
- --poll-interval <Int>: —
- --page-limit <Int>: —

## Related
- dws minutes +apply-permission
- dws minutes +download
- dws minutes +export-pack
- dws minutes +list-all
- dws minutes +list-mine
- dws minutes +list-shared
