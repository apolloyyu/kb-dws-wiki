# dws mail template list

kind: command
completeness: full
usage: dws mail template list
description: 列举邮件模板
example: dws mail template list --email user@company.com --limit 20
source: internal/helpers/mail.go:2801
visible_flags: 3

## Flags
- --email <String>: 用户邮箱地址 (必填)
- --cursor <String>: 分页游标，取自响应中的 nextCursor 字段 (可选)
- --limit <String>: 每页返回数量 (必填)

## Related
- dws mail template create
- dws mail template delete
- dws mail template get
- dws mail template update
