# dws calendar +invite

kind: shortcut
completeness: full
usage: dws calendar +invite
description: 按姓名把参会人加入已有日程（自动解析 userId 后批量添加）
source: internal/shortcut/smart/invite.go:35
visible_flags: 2

## Flags
- --event <String>: 已有日程的 eventId
- --with <String>: 参会人姓名，逗号分隔

## Related
- dws calendar +agenda
- dws calendar +attendee-list
- dws calendar +book
- dws calendar +book-list
- dws calendar +book-search
- dws calendar +cancel-event
