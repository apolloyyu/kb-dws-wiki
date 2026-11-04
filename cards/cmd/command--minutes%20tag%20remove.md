# dws minutes tag remove

kind: command
completeness: partial
usage: dws minutes tag remove
description: —
source: internal/helpers/minutes.go:2564
visible_flags: 2
partial_reason: missing_description

## Flags
- --id <String> required: 真实听记taskUuid，不能使用taskId或分享链接
- --tag-ids <String> required: 逗号分隔本人自定义标签ID，原始1-20项，允许重复

## Related
- dws minutes tag add
- dws minutes tag create
- dws minutes tag delete
- dws minutes tag list
- dws minutes tag query
