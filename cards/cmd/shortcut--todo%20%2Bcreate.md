# dws todo +create

kind: shortcut
completeness: full
usage: dws todo +create
description: 创建待办并读回验证
source: internal/shortcut/todo/lifecycle.go:112
visible_flags: 4

## Flags
- --title <String>: 待办标题
- --executors <StringSlice>: 执行人 userId
- --due <String>: 截止时间（ISO8601）
- --priority <Int>: 优先级；--priority 仅接受 10/20/30/40

## Related
- dws todo +comment
- dws todo +get
- dws todo +get-my-tasks
- dws todo +list-attachment
- dws todo +list-comment
- dws todo +list-sub
