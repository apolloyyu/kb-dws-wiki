# dws minutes +action-items

kind: shortcut
completeness: full
usage: dws minutes +action-items
description: 读取指定或我最新一条听记中已抽取的行动项
source: internal/shortcut/smart/action_items.go:39
visible_flags: 1

## Flags
- --id <String>: 听记 taskUuid；不传时选择我最新的一条

## Related
- dws minutes +apply-permission
- dws minutes +detail
- dws minutes +download
- dws minutes +export-pack
- dws minutes +latest
- dws minutes +list-all
