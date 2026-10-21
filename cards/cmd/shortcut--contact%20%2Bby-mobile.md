# dws contact +by-mobile

kind: shortcut
completeness: full
usage: dws contact +by-mobile
description: 按手机号查询某人的完整资料（自动解析 userId 后取详情）
source: internal/shortcut/smart/by_mobile.go:34
visible_flags: 1

## Flags
- --mobile <String>: 手机号；--mobile 必须是至少 6 位数字的手机号，可包含国家码、空格、连字符或括号

## Related
- dws contact +dept-members
- dws contact +friend-list
- dws contact +friend-remove
- dws contact +friend-request-accept
- dws contact +friend-request-list
- dws contact +friend-request-reject
