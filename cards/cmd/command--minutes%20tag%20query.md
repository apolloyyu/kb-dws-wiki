# dws minutes tag query

kind: command
completeness: full
description: 根据标签ID查询听记列表
source: internal/helpers/minutes.go:2004
visible_flags: 3

## Flags
- --tag-id <String>: 标签/分组 ID，可通过 tag list 获取 (必填)
- --limit <Float64>: 每页数据条数 (默认 10)
- --cursor <String>: 分页 token (首页留空)

## Related
- dws minutes tag list
