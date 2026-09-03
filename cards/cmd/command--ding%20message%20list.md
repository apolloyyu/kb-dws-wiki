# dws ding message list

kind: command
completeness: full
usage: dws ding message list
description: 查询 DING 消息历史
example: dws ding message list
source: internal/helpers/ding.go:293
visible_flags: 2

## Flags
- --cursor <Int64>: 分页游标（首次传 0，翻页传返回的 nextCursor）
- --type <String>: 消息类型: ALL / UNREAD / SEND / NEW_COMMENT / DELETED（必填，服务端不接受空值；默认 ALL 全部）

## Related
- dws ding message recall
- dws ding message recall-personal
- dws ding message receiver-status
- dws ding message send
- dws ding message send-by-message
- dws ding message send-personal
