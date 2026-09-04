# dws drive publish get

kind: command
completeness: full
usage: dws drive publish get
description: 查询文件公开发布状态
example: dws drive publish get --node <fileId>
source: internal/helpers/drive.go:3632
visible_flags: 1

## Flags
- --node <String>: 目标文件 ID (dentryUuid) 或 URL (必填)

## Related
- dws drive publish set
- dws drive publish unset
