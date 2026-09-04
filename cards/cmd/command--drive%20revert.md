# dws drive revert

kind: command
completeness: partial
usage: dws drive revert
description: [危险] 回滚文件到指定历史版本
example: dws drive revert --node <dentryUuid> --version 3 --yes
source: internal/helpers/drive.go:4005
visible_flags: 2
partial_reason: unverified_flags,empty_flag_name

## Flags
- --node <String>: 文件 ID (dentryUuid) 或 URL (必填)
- --version <Int>: 要回滚到的历史版本号 (必填，正整数)

## Related
- dws drive comment
- dws drive commit
- dws drive copy
- dws drive cover
- dws drive delete
- dws drive download
