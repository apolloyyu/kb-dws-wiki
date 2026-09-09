# dws drive delete

kind: command
completeness: full
usage: dws drive delete
description: 删除文件/文件夹到回收站
example: dws drive delete --node <dentryUuid> --yes
source: internal/helpers/drive.go:1817
visible_flags: 1

## Flags
- --node <String>: 文件/文件夹 ID (dentryUuid)，即 drive list 返回的 fileId (必填)

## Related
- dws drive comment
- dws drive commit
- dws drive copy
- dws drive cover
- dws drive download
- dws drive download-version
