# dws drive publish unset

kind: command
completeness: full
usage: dws drive publish unset
description: [危险] 关闭文件互联网公开
example: dws drive publish unset --node <fileId> --yes
source: internal/helpers/drive.go:3573
visible_flags: 1

## Flags
- --node <String>: 目标文件 ID (dentryUuid) 或 URL (必填)

## Related
- dws drive publish get
- dws drive publish set
