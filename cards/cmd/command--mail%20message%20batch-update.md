# dws mail message batch-update

kind: command
completeness: full
usage: dws mail message batch-update
description: 批量修改邮件状态（标记已读/未读/添加标签/移除标签）
example: dws mail message batch-update --email user@company.com --ids <id1>,<id2> --action markRead
source: internal/helpers/mail.go:1697
visible_flags: 4

## Flags
- --email <String>: 邮件所属邮箱地址 (必填)
- --ids <String>: 要修改的邮件 ID 列表，逗号分隔 (必填)
- --action <String>: 操作类型: markRead/markUnread/addTags/removeTags (必填)
- --tags <String>: 标签 ID 列表，逗号分隔 (action 为 addTags/removeTags 时必填)

## Related
- dws mail message batch-delete
- dws mail message batch-get
- dws mail message batch-move
- dws mail message export
- dws mail message forward
- dws mail message get
