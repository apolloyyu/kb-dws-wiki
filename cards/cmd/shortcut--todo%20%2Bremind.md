# dws todo +remind

kind: shortcut
completeness: full
usage: dws todo +remind
description: 给自己创建一条带可选截止时间的待办
source: internal/shortcut/smart/remind.go:44
visible_flags: 2

## Flags
- --task <String>: 待办标题/内容
- --at <String>: 截止时间（ISO8601，可选，写入 dueTime，不是提醒时间）

## Related
- dws todo +assign
- dws todo +assign-multi
- dws todo +comment
- dws todo +create
- dws todo +created-todos
- dws todo +due-today
