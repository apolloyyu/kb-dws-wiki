# dws mail message verify

kind: command
completeness: full
usage: dws mail message verify
description: 查询邮件发送状态
example: dws mail message verify --email user@company.com --internet-message-id <internetMessageId>
source: internal/helpers/mail.go:1323
visible_flags: 2

## Flags
- --email <String>: 邮件所属邮箱地址 (必填)
- --internet-message-id <String>: 邮件的 internetMessageId (必填)，取自发送类命令返回值

## Related
- dws mail message batch-delete
- dws mail message batch-get
- dws mail message batch-move
- dws mail message batch-update
- dws mail message export
- dws mail message forward
