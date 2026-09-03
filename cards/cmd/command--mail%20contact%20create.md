# dws mail contact create

kind: command
completeness: full
usage: dws mail contact create
description: 创建邮件联系人
example: dws mail contact create --email user@company.com --contact-email colleague@company.com --display-name "张三"
source: internal/helpers/mail.go:3068
visible_flags: 6

## Flags
- --email <String>: 用户邮箱地址 (必填)
- --contact-email <String>: 联系人邮箱地址 (必填)
- --first-name <String>: 联系人名 (可选)
- --middle-name <String>: 联系人中间名 (可选)
- --last-name <String>: 联系人姓 (可选)
- --display-name <String>: 联系人显示名称 (可选)

## Related
- dws mail contact batch-delete
- dws mail contact list
- dws mail contact update
