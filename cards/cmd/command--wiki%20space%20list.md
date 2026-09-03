# dws wiki space list

kind: command
completeness: full
usage: dws wiki space list
description: 列出空间（知识库 / 钉盘空间）
example: dws wiki space list
source: internal/helpers/wiki.go:291
visible_flags: 3

## Flags
- --type <String>: 空间类型: orgWikiSpace(默认) / myWikiSpace / orgSpace(钉盘企业空间) / mySpace(钉盘我的文件)
- --limit <String>: 每页数量 1-50 (默认 20)
- --cursor <String>: 分页游标 (首页留空)

## Related
- dws wiki space create
- dws wiki space delete
- dws wiki space get
- dws wiki space search
