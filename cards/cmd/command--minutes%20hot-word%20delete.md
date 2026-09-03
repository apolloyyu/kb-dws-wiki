# dws minutes hot-word delete

kind: command
completeness: full
usage: dws minutes hot-word delete
description: 批量删除个人热词
example: dws minutes hot-word delete --words "天气"
source: internal/helpers/minutes.go:1350
visible_flags: 1

## Flags
- --words <String>: 要删除的热词，多个用逗号分隔 (必填)

## Related
- dws minutes hot-word add
- dws minutes hot-word list
