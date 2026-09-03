# dws mail +folder-list

kind: shortcut
completeness: full
usage: dws mail +folder-list
description: 列出顶层文件夹或指定父文件夹下的子文件夹
source: internal/shortcut/mail/mail.go:154
visible_flags: 2

## Flags
- --email <String>: 邮件所属邮箱地址，不能为空
- --folder <String>: 父文件夹 ID，不传则返回顶层文件夹

## Related
- dws mail +contact-list
- dws mail +draft-create
- dws mail +draft-edit
- dws mail +message
- dws mail +messages
- dws mail +tag-list
