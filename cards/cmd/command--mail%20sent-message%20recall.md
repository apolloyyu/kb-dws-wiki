# dws mail sent-message recall

kind: command
completeness: full
usage: dws mail sent-message recall
description: [危险] 撤回已发送的邮件
example: dws mail sent-message recall --email user@company.com --id <mailId> --subject "邮件主题" --yes
source: internal/helpers/mail.go:2454
visible_flags: 4

## Flags
- --email <String>: 发件人邮箱地址 (必填)
- --id <String>: 要撤回的邮件 ID (必填)
- --subject <String>: 邮件主题 (必填)
- --yes <Bool>: 跳过确认提示，直接执行

## Related
- dws mail sent-message recall-detail
