# dws mail contact list

kind: command
completeness: full
usage: dws mail contact list
description: 列举邮件联系人
example: dws mail contact list --email user@company.com --limit 20
source: internal/helpers/mail.go:3135
visible_flags: 3

## Flags
- --email <String>: 用户邮箱地址 (必填)
- --cursor <String>: 分页游标，取自响应中的 nextCursor 字段 (可选)
- --limit <String>: 每页返回数量 (必填)

## Related
- dws mail contact batch-delete
- dws mail contact create
- dws mail contact update
