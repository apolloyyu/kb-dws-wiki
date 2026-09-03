# dws mail folder create

kind: command
completeness: full
usage: dws mail folder create
description: 创建邮件文件夹
example: dws mail folder create --email user@company.com --name "项目资料"
source: internal/helpers/mail.go:666
visible_flags: 3

## Flags
- --email <String>: 邮件所属邮箱地址 (必填)
- --name <String>: 新建邮件文件夹名称 (必填)
- --folder <String>: 父文件夹 ID，不传则创建顶层文件夹 (可选)

## Related
- dws mail folder delete
- dws mail folder list
- dws mail folder update
