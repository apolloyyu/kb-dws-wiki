# dws oa approval oa-comments

kind: command
completeness: full
usage: dws oa approval oa-comments
description: 对审批实例添加评论
example: dws oa approval oa-comments --instance-id <processInstanceId> --content "同意，请尽快处理"
source: internal/helpers/oa.go:1638
visible_flags: 3

## Flags
- --instance-id <String>: 审批实例 ID (必填)
- --content <String>: 评论内容 (必填)
- --text <String>: 评论内容 (必填)

## Related
- dws oa approval append-task
- dws oa approval approve
- dws oa approval attachment
- dws oa approval create-instance
- dws oa approval detail
- dws oa approval ding-info
