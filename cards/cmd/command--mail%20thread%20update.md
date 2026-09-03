# dws mail thread update

kind: command
completeness: full
usage: dws mail thread update
description: 修改邮件会话状态
example: dws mail thread update --email user@company.com --id <conversationId> --action markRead
source: internal/helpers/mail.go:1126
visible_flags: 4

## Flags
- --email <String>: 会话所属邮箱地址 (必填)
- --id <String>: 会话唯一标识 conversationId (必填)
- --action <String>: 操作类型：markRead、markUnread、addTags、removeTags (必填)
- --tag-ids <String>: 标签 ID 列表，多个用英文逗号分隔；addTags/removeTags 时必填 (可选)

## Related
- dws mail thread batch-trash
- dws mail thread batch-update
- dws mail thread get
- dws mail thread list
- dws mail thread trash
