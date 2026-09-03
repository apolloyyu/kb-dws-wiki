# dws minutes +speaker-insights

kind: shortcut
completeness: full
usage: dws minutes +speaker-insights
description: 创建发言人段落总结并轮询结果，保留异步任务恢复句柄
source: internal/shortcut/minutes/workflows.go:124
visible_flags: 5

## Flags
- --id <String>: 听记 taskUuid
- --timeout <Int>: —
- --interval <Int>: —
- --resume <Bool>: 只继续轮询，不重复创建任务
- --task-id <String>: 先前 create 返回的异步 taskId，恢复时用于输出追踪

## Related
- dws minutes +apply-permission
- dws minutes +download
- dws minutes +export-pack
- dws minutes +list-all
- dws minutes +list-mine
- dws minutes +list-shared
