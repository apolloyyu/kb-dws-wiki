# dws smart +find-mail-user

kind: shortcut
completeness: full
usage: dws smart +find-mail-user
description: 按关键词搜索邮箱联系人并投影列表（姓名/昵称/邮箱/工号等）
source: internal/shortcut/smart/find_mail_user.go:52
visible_flags: 3

## Flags
- --query <String>: 搜索关键词（姓名/花名/邮箱片段，必填且不能为空）
- --limit <Int>: 返回条数上限（可选，1-100）
- --cursor <String>: 分页游标，取自上一页 nextCursor

## Related
- dws smart +access-change
- dws smart +access-grant
- dws smart +access-revoke
- dws smart +action-items
- dws smart +assign
- dws smart +assign-multi
