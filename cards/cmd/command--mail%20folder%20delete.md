# dws mail folder delete

kind: command
completeness: full
usage: dws mail folder delete
description: 删除邮件文件夹
example: dws mail folder delete --email user@company.com --id <folderId>
source: internal/helpers/mail.go:724
visible_flags: 2

## Flags
- --email <String>: 邮件所属邮箱地址 (必填)
- --id <String>: 要删除的邮件文件夹 ID (必填)

## Related
- dws mail folder create
- dws mail folder list
- dws mail folder update
