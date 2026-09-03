# dws todo +upload-attachment

kind: shortcut
completeness: full
description: 上传待办附件（当前请使用原子命令）
source: internal/shortcut/todo/lifecycle.go:500
visible_flags: 2

## Flags
- --task-id <String>: 待办 taskId
- --file-path <String>: 本地文件路径

## Related
- dws todo +comment
- dws todo +create
- dws todo +get
- dws todo +get-my-tasks
- dws todo +list-attachment
- dws todo +list-comment
