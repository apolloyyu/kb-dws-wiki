# dws calendar event respond

kind: command
completeness: full
usage: dws calendar event respond
description: 响应日程（接受/拒绝/暂定）
example: dws calendar event respond --id EVENT_ID --status accepted
source: internal/helpers/calendar.go:569
visible_flags: 3

## Flags
- --id <String>: 日程 ID (必填)
- --status <String>: 响应状态: needsAction(未操作)|accepted(接受)|declined(拒绝)|tentative(暂定) (必填)
- --calendar-id <String>: 日历 ID (可选，默认 primary 主日历；指定其他日历本时填写，可通过 book list 获取)，注意：订阅日历下的日程无参会人，因此不可响应

## Related
- dws calendar event create
- dws calendar event delete
- dws calendar event get
- dws calendar event instances
- dws calendar event list
- dws calendar event share-info
