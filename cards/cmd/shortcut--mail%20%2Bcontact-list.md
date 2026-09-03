# dws mail +contact-list

kind: shortcut
completeness: full
usage: dws mail +contact-list
description: 列出指定邮箱的所有邮件联系人
source: internal/shortcut/mail/mail.go:483
visible_flags: 3

## Flags
- --email <String>: 用户邮箱地址
- --limit <String>: 每页返回数量，必须是 1-100 之间的整数
- --cursor <String>: 分页游标，取自响应中的 nextCursor

## Related
- dws mail +draft-create
- dws mail +draft-edit
- dws mail +folder-list
- dws mail +message
- dws mail +messages
- dws mail +tag-list
