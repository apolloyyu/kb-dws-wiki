# dws drive rename

kind: command
completeness: full
description: 重命名文件/文档
source: internal/helpers/drive.go:2027
visible_flags: 2

## Flags
- --node <String>: 文档/文件 ID 或 URL (必填)
- --name <String>: 新名称 (必填；实际执行时仅去掉与节点当前扩展名完全匹配的一层后缀)

## Related
- dws drive comment
- dws drive commit
- dws drive copy
- dws drive cover
- dws drive delete
- dws drive download
