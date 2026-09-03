# dws mail calendar list

kind: command
completeness: full
usage: dws mail calendar list
description: 列出用户可访问的日历列表
example: dws mail calendar list --email user@company.com
source: internal/helpers/mail.go:3723
visible_flags: 1

## Flags
- --email <String>: 用户的邮箱地址 (必填)

## Related
- none
