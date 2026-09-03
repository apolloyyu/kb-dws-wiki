# dws mail contact create

kind: command
completeness: full
description: 创建邮件文件夹
source: internal/helpers/mail.go:666
visible_flags: 3

## Flags
- --email <String>: 邮件所属邮箱地址 (必填)
- --name <String>: 新建邮件文件夹名称 (必填)
- --folder <String>: 父文件夹 ID，不传则创建顶层文件夹 (可选)

## Related
- dws mail contact batch-delete
- dws mail contact list
- dws mail contact update
