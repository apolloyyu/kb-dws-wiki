# dws mail message batch-get

kind: command
completeness: full
usage: dws mail message batch-get
description: 批量获取邮件详情
example: dws mail message batch-get --email user@company.com --ids <id1>,<id2>
source: internal/helpers/mail.go:1747
visible_flags: 2

## Flags
- --email <String>: 邮件所属邮箱地址 (必填)
- --ids <String>: 要获取的邮件 ID 列表，逗号分隔，最多 20 个 (必填)

## Related
- dws mail message batch-delete
- dws mail message batch-move
- dws mail message batch-update
- dws mail message export
- dws mail message forward
- dws mail message get
