# dws mail template update

kind: command
completeness: full
description: 更新邮件文件夹
source: internal/helpers/mail.go:779
visible_flags: 3

## Flags
- --email <String>: 邮件所属邮箱地址 (必填)
- --id <String>: 要更新的邮件文件夹 ID (必填)
- --name <String>: 更新后的邮件文件夹名称 (必填)

## Related
- dws mail template create
- dws mail template delete
- dws mail template get
- dws mail template list
