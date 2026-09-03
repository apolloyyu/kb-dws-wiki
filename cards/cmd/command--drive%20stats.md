# dws drive stats

kind: command
completeness: full
usage: dws drive stats
description: 获取节点统计信息
example: dws drive stats --node <dentryUuid>
source: internal/helpers/drive.go:2097
visible_flags: 1

## Flags
- --node <String>: 节点 ID 或文档 URL (必填)

## Related
- dws drive comment
- dws drive commit
- dws drive copy
- dws drive cover
- dws drive delete
- dws drive download
