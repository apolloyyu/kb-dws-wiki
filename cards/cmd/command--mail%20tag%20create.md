# dws mail tag create

kind: command
completeness: full
usage: dws mail tag create
description: 创建邮件标签
example: dws mail tag create --email user@company.com --name "项目资料"
source: internal/helpers/mail.go:905
visible_flags: 3

## Flags
- --email <String>: 用户的邮箱地址 (必填)
- --name <String>: 新建邮件标签名称 (必填)
- --parent-id <String>: 父标签 ID，不传则创建顶层标签 (可选)

## Related
- dws mail tag delete
- dws mail tag list
- dws mail tag update
