# dws sheet batch-update

kind: command
completeness: full
description: 批量修改邮件会话状态
source: internal/helpers/mail.go:1169
visible_flags: 4

## Flags
- --email <String>: 会话所属邮箱地址 (必填)
- --ids <String>: 会话 ID 列表，多个用英文逗号分隔，最多 100 个 (必填)
- --action <String>: 操作类型：markRead、markUnread、addTags、removeTags (必填)
- --tag-ids <String>: 标签 ID 列表，多个用英文逗号分隔；addTags/removeTags 时必填 (可选)

## Related
- dws sheet add-dimension
- dws sheet append
- dws sheet batch-set-style
- dws sheet changeset-get
- dws sheet comment
- dws sheet copy
