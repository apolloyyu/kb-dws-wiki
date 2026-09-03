# dws mail message share-to-chat

kind: command
completeness: full
usage: dws mail message share-to-chat
description: [危险] 分享邮件至IM聊天
example: dws mail message share-to-chat --email user@company.com --id <messageId> --users uid1,uid2 --yes
source: internal/helpers/mail.go:2337
visible_flags: 4

## Flags
- --email <String>: 用户的邮箱地址 (必填)
- --id <String>: 邮件ID (必填)
- --users <String>: 目标用户UID列表，逗号分隔
- --yes <Bool>: 确认执行此危险操作 (必填)

## Related
- dws mail message batch-delete
- dws mail message batch-get
- dws mail message batch-move
- dws mail message batch-update
- dws mail message export
- dws mail message forward
