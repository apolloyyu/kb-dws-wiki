# dws mail message share-to-chat

kind: command
completeness: full
description: [危险] 分享邮件至IM聊天
source: internal/helpers/mail.go:2337
visible_flags: 4

## Flags
- --email <String>: 用户的邮箱地址 (必填)
- --id <String>: 邮件ID (必填)
- --users <String>: 目标用户UID列表，逗号分隔
- --yes <Bool>: 确认执行此危险操作 (必填)

## Related
- dws mail message batch-delete
- dws mail message batch-move
- dws mail message export
- dws mail message forward
- dws mail message get
- dws mail message list
