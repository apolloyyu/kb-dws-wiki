# dws wiki space search

kind: command
completeness: full
usage: dws wiki space search
description: 搜索知识库
example: dws wiki space search --query "产品文档"
source: internal/helpers/wiki.go:376
visible_flags: 3

## Flags
- --query <String>: 搜索关键词 (搜索组织知识库时必填)
- --type <String>: 知识库类型: myWikiSpace 时直接返回「我的文档」，省略则搜索组织知识库
- --limit <String>: 返回数量 1-20 (默认 10)

## Related
- dws wiki space create
- dws wiki space delete
- dws wiki space get
- dws wiki space list
