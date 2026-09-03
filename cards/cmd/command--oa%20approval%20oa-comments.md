# dws oa approval oa-comments

kind: command
completeness: full
description: 对审批实例添加评论
source: internal/helpers/oa.go:1638
visible_flags: 3

## Flags
- --instance-id <String>: 审批实例 ID (必填)
- --content <String>: 评论内容 (必填)
- --text <String>: 评论内容 (必填)

## Related
- dws oa approval approve
- dws oa approval create-instance
- dws oa approval detail
- dws oa approval forecast-process
- dws oa approval form-schema
- dws oa approval list-by-admin
