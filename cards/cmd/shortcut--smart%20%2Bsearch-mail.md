# dws smart +search-mail

kind: shortcut
completeness: full
usage: dws smart +search-mail
description: 按 KQL 关键词搜索邮件并投影列表（主题/发件人/时间/messageId）
source: internal/shortcut/smart/search_mail.go:47
visible_flags: 4

## Flags
- --query <String>: KQL 搜索表达式（如 subject:周报、from:alice、folderId:2），不能为空
- --email <String>: 要搜索的邮箱地址（可选，默认取你绑定的第一个邮箱）
- --size <String>: 返回条数上限（可选，默认 20；显式提供时必须是 1-100 之间的整数）
- --cursor <String>: 分页游标，取自上一页 nextCursor

## Related
- dws smart +access-change
- dws smart +access-grant
- dws smart +access-revoke
- dws smart +action-items
- dws smart +assign
- dws smart +assign-multi
