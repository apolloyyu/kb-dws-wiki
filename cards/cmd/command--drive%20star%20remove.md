# dws drive star remove

kind: command
completeness: full
usage: dws drive star remove
description: 取消收藏文档
example: dws drive star remove --node <nodeId_or_URL>
source: internal/helpers/drive.go:3843
visible_flags: 1

## Flags
- --node <String>: 文档 ID 或 URL (必填)

## Related
- dws drive star add
- dws drive star list
