# dws mail template create

kind: command
completeness: full
usage: dws mail template create
description: 创建邮件模板
example: dws mail template create --email user@company.com --from user@company.com --name "周报模板" --subject "周报" --content "本周工作总结..."
source: internal/helpers/mail.go:2718
visible_flags: 8

## Flags
- --email <String>: 用户邮箱地址 (必填)
- --from <String>: 模板发件人邮箱 (可选)
- --subject <String>: 模板邮件标题 (必填)
- --content <String>: 模板邮件正文 (必填)
- --name <String>: 模板名称 (必填)
- --to <String>: 模板收件人列表，逗号分隔 (可选)
- --cc <String>: 模板抄送人列表，逗号分隔 (可选)
- --is-draft <Bool>: 是否为草稿模板 (可选，默认 false；仅草稿模板后续可 template update)

## Related
- dws mail template delete
- dws mail template get
- dws mail template list
- dws mail template update
