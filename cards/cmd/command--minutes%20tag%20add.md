# dws minutes tag add

kind: command
completeness: partial
usage: dws minutes tag add
description: —
source: internal/helpers/minutes.go:2543
visible_flags: 3
partial_reason: missing_description

## Flags
- --id <String> required: 真实听记taskUuid，不能使用taskId或分享链接
- --tag-ids <String> required: 逗号分隔本人自定义标签ID，原始1-20项，允许重复
- --locale <String>: 可选，知识库同步语言；缺省或空白由服务使用zh

## Related
- dws minutes tag create
- dws minutes tag delete
- dws minutes tag list
- dws minutes tag query
- dws minutes tag remove
