# dws todo +reminder

kind: shortcut
completeness: full
usage: dws todo +reminder
description: 设置或清除待办提醒（仅终端回执）
source: internal/shortcut/todo/lifecycle.go:413
visible_flags: 5

## Flags
- --task-id <String>: 待办 taskId
- --clear <Bool>: 清除全部提醒规则
- --base-time <String>: —
- --due-date-offset <Int>: 相对截止时间的分钟偏移；
- --at <String>: customTime 的 ISO8601 时间；

## Related
- dws todo +comment
- dws todo +create
- dws todo +get
- dws todo +get-my-tasks
- dws todo +list-attachment
- dws todo +list-comment
