# dws smart +action-items

kind: shortcut
completeness: full
usage: dws smart +action-items
description: 读取指定或我最新一条听记中已抽取的行动项
source: internal/shortcut/smart/action_items.go:37
visible_flags: 1

## Flags
- --id <String>: 听记 taskUuid；不传时选择我最新的一条

## Related
- dws smart +access-change
- dws smart +access-grant
- dws smart +access-revoke
- dws smart +assign
- dws smart +assign-multi
- dws smart +at-me
