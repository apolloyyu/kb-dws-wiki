# dws mail thread batch-update

kind: command
completeness: full
usage: dws mail thread batch-update
description: 批量修改邮件会话状态
example: dws mail thread batch-update --email user@company.com --ids <conversationId1>,<conversationId2> --action markRead
source: internal/helpers/mail.go:1169
visible_flags: 4

## Flags
- --email <String>: 会话所属邮箱地址 (必填)
- --ids <String>: 会话 ID 列表，多个用英文逗号分隔，最多 100 个 (必填)
- --action <String>: 操作类型：markRead、markUnread、addTags、removeTags (必填)
- --tag-ids <String>: 标签 ID 列表，多个用英文逗号分隔；addTags/removeTags 时必填 (可选)

## Related
- dws mail thread batch-trash
- dws mail thread get
- dws mail thread list
- dws mail thread trash
- dws mail thread update
