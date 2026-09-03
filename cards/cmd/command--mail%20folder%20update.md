# dws mail folder update

kind: command
completeness: full
usage: dws mail folder update
description: 更新邮件文件夹
example: dws mail folder update --email user@company.com --id <folderId> --name "新文件夹名"
source: internal/helpers/mail.go:779
visible_flags: 3

## Flags
- --email <String>: 邮件所属邮箱地址 (必填)
- --id <String>: 要更新的邮件文件夹 ID (必填)
- --name <String>: 更新后的邮件文件夹名称 (必填)

## Related
- dws mail folder create
- dws mail folder delete
- dws mail folder list
