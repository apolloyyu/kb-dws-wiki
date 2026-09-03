# dws mail template update

kind: command
completeness: full
usage: dws mail template update
description: 更新邮件模板
example: dws mail template update --email user@company.com --id <templateId> --subject "新标题" --content "新正文"
source: internal/helpers/mail.go:2919
visible_flags: 8

## Flags
- --email <String>: 用户邮箱地址 (必填)
- --id <String>: 模板唯一标识 (必填)
- --from <String>: 模板发件人邮箱 (可选)
- --subject <String>: 模板邮件标题 (可选)
- --content <String>: 模板邮件正文 (可选)
- --name <String>: 模板名称 (可选)
- --to <String>: 模板收件人列表，逗号分隔 (可选)
- --cc <String>: 模板抄送人列表，逗号分隔 (可选)

## Related
- dws mail template create
- dws mail template delete
- dws mail template get
- dws mail template list
