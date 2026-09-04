# dws drive cover

kind: command
completeness: partial
usage: dws drive cover
description: 获取节点封面地址
example: dws drive cover --node <dentryUuid>
source: internal/helpers/drive.go:3958
visible_flags: 1
partial_reason: unverified_flags,empty_flag_name

## Flags
- --node <String>: 节点 ID (dentryUuid) 或文档 URL (必填)

## Related
- dws drive comment
- dws drive commit
- dws drive copy
- dws drive delete
- dws drive download
- dws drive download-version
