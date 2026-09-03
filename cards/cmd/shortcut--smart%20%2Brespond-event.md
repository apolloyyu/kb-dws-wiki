# dws smart +respond-event

kind: shortcut
completeness: full
description: 接受 / 拒绝 / 暂定回复一个日程邀请（作为参会人设置自己的响应状态）
source: internal/shortcut/smart/respond_event.go:38
visible_flags: 2

## Flags
- --event <String>: 日程 eventId（用 `dws calendar event list` 查询）
- --response <String>: 响应动作：accept(接受) / decline(拒绝) / tentative(暂定)

## Related
- dws smart +access-change
- dws smart +access-grant
- dws smart +access-revoke
- dws smart +action-items
- dws smart +assign
- dws smart +assign-multi
