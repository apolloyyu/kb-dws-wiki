# dws todo +get-my-tasks

kind: shortcut
completeness: full
usage: dws todo +get-my-tasks
description: 查询当前组织下我的待办列表
source: internal/shortcut/todo/todo.go:35
visible_flags: 9

## Flags
- --page <String>: —
- --size <String>: —
- --status <String>: —
- --priority <StringSlice>: 优先级过滤；--priority 仅接受 10/20/30/40
- --role-types <StringSlice>: —
- --plan-finish-start <Int>: 截止时间范围开始（Unix 毫秒时间戳）
- --plan-finish-end <Int>: 截止时间范围结束（Unix 毫秒时间戳）
- --all <Bool>: 遍历全部分页；--max-pages 仅用于 --all，且必须在 1-40
- --max-pages <Int>: —

## Related
- dws todo +comment
- dws todo +create
- dws todo +get
- dws todo +list-attachment
- dws todo +list-comment
- dws todo +list-sub
