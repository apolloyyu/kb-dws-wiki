# dws smart +by-mobile

kind: shortcut
completeness: full
usage: dws smart +by-mobile
description: 按手机号查询某人的完整资料（自动解析 userId 后取详情）
source: internal/shortcut/smart/by_mobile.go:34
visible_flags: 1

## Flags
- --mobile <String>: 手机号；--mobile 必须是至少 6 位数字的手机号，可包含国家码、空格、连字符或括号

## Related
- dws smart +access-change
- dws smart +access-grant
- dws smart +access-revoke
- dws smart +action-items
- dws smart +assign
- dws smart +assign-multi
