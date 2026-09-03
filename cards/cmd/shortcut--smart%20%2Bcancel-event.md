# dws smart +cancel-event

kind: shortcut
completeness: full
description: 取消（删除）一个已有日程（删除前先确认它真实存在）
source: internal/shortcut/smart/cancel_event.go:42
visible_flags: 1

## Flags
- --event <String>: 要取消的日程 eventId（可用 dws calendar event list 查询）

## Related
- dws smart +access-change
- dws smart +access-grant
- dws smart +access-revoke
- dws smart +action-items
- dws smart +assign
- dws smart +assign-multi
