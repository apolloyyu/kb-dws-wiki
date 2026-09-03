# dws mail mailbox profile

kind: command
completeness: full
usage: dws mail mailbox profile
description: 获取用户邮箱信息
example: dws mail mailbox profile --email user@company.com
source: internal/helpers/mail.go:174
visible_flags: 1

## Flags
- --email <String>: 用户的邮箱地址 (必填)

## Related
- dws mail mailbox list
- dws mail mailbox shared-with-me
