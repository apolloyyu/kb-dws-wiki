# dws mail contact update

kind: command
completeness: full
usage: dws mail contact update
description: 更新邮件联系人
example: dws mail contact update --email user@company.com --contact-id <contactId> --display-name "李四"
source: internal/helpers/mail.go:3201
visible_flags: 7

## Flags
- --email <String>: 用户邮箱地址 (必填)
- --contact-id <String>: 联系人唯一标识 (必填)
- --contact-email <String>: 联系人邮箱地址 (可选)
- --first-name <String>: 联系人名 (可选)
- --middle-name <String>: 联系人中间名 (可选)
- --last-name <String>: 联系人姓 (可选)
- --display-name <String>: 联系人显示名称 (可选)

## Related
- dws mail contact batch-delete
- dws mail contact create
- dws mail contact list
