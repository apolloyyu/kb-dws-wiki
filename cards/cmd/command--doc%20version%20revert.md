# dws doc version revert

kind: command
completeness: full
usage: dws doc version revert
description: 回滚文档到指定版本
example: dws doc version revert --node DOC_ID --version 3 --yes
source: internal/helpers/doc.go:4525
visible_flags: 2

## Flags
- --node <String>: 文档 ID 或 URL (必填)
- --version <Int>: 目标版本号 (必填，从 list 获取)

## Related
- dws doc version list
- dws doc version save
