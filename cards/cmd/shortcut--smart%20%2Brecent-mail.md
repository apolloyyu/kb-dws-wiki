# dws smart +recent-mail

kind: shortcut
completeness: full
usage: dws smart +recent-mail
description: 列出收件箱近期邮件会话并投影列表（主题/发件人/时间/threadId）
source: internal/shortcut/smart/recent_mail.go:54
visible_flags: 4

## Flags
- --limit <Int>: 返回会话条数上限（可选，默认 20，最大 100）
- --email <String>: 要查看的邮箱地址（可选，默认取你绑定的第一个邮箱）
- --folder <String>: 文件夹 ID（可选，默认定位收件箱）
- --cursor <String>: 分页游标，取自上一页 nextCursor

## Related
- dws smart +access-change
- dws smart +access-grant
- dws smart +access-revoke
- dws smart +action-items
- dws smart +assign
- dws smart +assign-multi
