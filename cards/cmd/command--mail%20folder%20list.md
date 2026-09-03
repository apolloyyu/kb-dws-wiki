# dws mail folder list

kind: command
completeness: full
usage: dws mail folder list
description: 列举邮件文件夹
example: dws mail folder list --email user@company.com
source: internal/helpers/mail.go:599
visible_flags: 2

## Flags
- --email <String>: 邮件所属邮箱地址 (必填)
- --folder <String>: 父文件夹唯一标识，不传则返回顶层文件夹 (可选)

## Related
- dws mail folder create
- dws mail folder delete
- dws mail folder update
