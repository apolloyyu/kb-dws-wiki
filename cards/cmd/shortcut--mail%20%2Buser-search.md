# dws mail +user-search

kind: shortcut
completeness: full
description: 按关键词或工号搜索邮箱用户（仅企业邮箱）
source: internal/shortcut/mail/mail.go:286
visible_flags: 5

## Flags
- --keyword <String>: 搜索关键词；显式提供时不能为空（未提供 --employee-no 时为必填）
- --employee-no <String>: 按工号精确搜索；显式提供时不能为空
- --email <String>: 搜索目标邮箱地址
- --cursor <String>: 分页游标，取自响应中的 nextCursor
- --limit <String>: 每页返回数量，必须是 1-100 之间的整数

## Related
- dws mail +contact-list
- dws mail +draft-create
- dws mail +draft-edit
- dws mail +folder-list
- dws mail +message
- dws mail +messages
