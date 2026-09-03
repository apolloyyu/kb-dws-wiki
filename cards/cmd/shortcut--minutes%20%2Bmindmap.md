# dws minutes +mindmap

kind: shortcut
completeness: full
usage: dws minutes +mindmap
description: 创建听记思维导图并轮询到明确成功、失败或超时
source: internal/shortcut/minutes/workflows.go:102
visible_flags: 4

## Flags
- --id <String>: 听记 taskUuid
- --timeout <Int>: —
- --interval <Int>: —
- --resume <Bool>: 只继续轮询，不重复创建任务

## Related
- dws minutes +apply-permission
- dws minutes +download
- dws minutes +export-pack
- dws minutes +list-all
- dws minutes +list-mine
- dws minutes +list-shared
