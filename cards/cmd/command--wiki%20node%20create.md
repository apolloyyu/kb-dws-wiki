# dws wiki node create

kind: command
completeness: full
description: 创建知识库
source: internal/helpers/wiki.go:179
visible_flags: 3

## Flags
- --name <String>: 知识库名称 (必填，不超过 32 字符)
- --desc <String>: 知识库描述 (选填，不超过 500 字符)
- --icon <String>: 知识库图标标识 (选填)

## Related
- dws wiki node copy
- dws wiki node delete
- dws wiki node list
- dws wiki node move
- dws wiki node search
