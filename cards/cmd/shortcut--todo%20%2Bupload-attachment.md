# dws todo +upload-attachment

kind: shortcut
completeness: full
usage: dws todo +upload-attachment
description: 上传待办附件（当前请使用原子命令）
source: internal/shortcut/todo/lifecycle.go:500
visible_flags: 2

## Flags
- --task-id <String>: 待办 taskId
- --file-path <String>: 本地文件路径

## Related
- dws todo +assign
- dws todo +assign-multi
- dws todo +comment
- dws todo +create
- dws todo +created-todos
- dws todo +due-today
