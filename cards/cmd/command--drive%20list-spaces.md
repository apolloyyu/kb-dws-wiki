# dws drive list-spaces

kind: command
completeness: full
usage: dws drive list-spaces
description: 获取钉盘空间列表 (deprecated → dws wiki space list --type orgSpace/mySpace)
example: dws drive list-spaces
source: internal/helpers/drive.go:1551
visible_flags: 3

## Flags
- --limit <Int>: 每页返回数量 (默认 20，最大 50)，仅 spaceType 为 orgSpace 时有效
- --space-type <String>: 空间类型: orgSpace=企业空间(默认), mySpace=我的文件 (可选)
- --cursor <String>: 分页游标，仅企业空间支持分页 (可选)

## Related
- dws drive comment
- dws drive commit
- dws drive copy
- dws drive cover
- dws drive delete
- dws drive download
