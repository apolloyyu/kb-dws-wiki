# dws wiki space create

kind: command
completeness: full
usage: dws wiki space create
description: 创建知识库
example: dws wiki space create --name "产品文档库"
source: internal/helpers/wiki.go:179
visible_flags: 3

## Flags
- --name <String>: 知识库名称 (必填，不超过 32 字符)
- --desc <String>: 知识库描述 (选填，不超过 500 字符)
- --icon <String>: 知识库图标标识 (选填)

## Related
- dws wiki space delete
- dws wiki space get
- dws wiki space list
- dws wiki space search
