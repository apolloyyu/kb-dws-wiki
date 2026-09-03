# dws smart +unread-mail

kind: shortcut
completeness: full
description: 列出未读邮件并投影列表（主题/发件人/时间/messageId）
source: internal/shortcut/smart/unread_mail.go:44
visible_flags: 3

## Flags
- --email <String>: 要查询的邮箱地址（可选，默认取你绑定的第一个邮箱）
- --size <String>: 返回条数上限（可选，默认 20；显式提供时必须是 1-100 之间的整数）
- --cursor <String>: 分页游标，取自上一页 nextCursor

## Related
- dws smart +access-change
- dws smart +access-grant
- dws smart +access-revoke
- dws smart +action-items
- dws smart +assign
- dws smart +assign-multi
