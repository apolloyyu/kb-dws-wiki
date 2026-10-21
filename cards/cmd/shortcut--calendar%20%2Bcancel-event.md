# dws calendar +cancel-event

kind: shortcut
completeness: full
usage: dws calendar +cancel-event
description: 取消（删除）一个已有日程（删除前先确认它真实存在）
source: internal/shortcut/smart/cancel_event.go:42
visible_flags: 1

## Flags
- --event <String>: 要取消的日程 eventId（可用 dws calendar event list 查询）

## Related
- dws calendar +agenda
- dws calendar +attendee-list
- dws calendar +book
- dws calendar +book-list
- dws calendar +book-search
- dws calendar +conflicts
