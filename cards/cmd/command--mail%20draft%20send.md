# dws mail draft send

kind: command
completeness: full
usage: dws mail draft send
description: 发送草稿
example: dws mail draft send --from user@company.com --id <messageId>
source: internal/helpers/mail.go:2550
visible_flags: 2

## Flags
- --from <String>: 发件人邮箱 (必填)，别名: --sender
- --id <String>: 草稿邮件 ID (必填)

## Related
- dws mail draft create
- dws mail draft update
