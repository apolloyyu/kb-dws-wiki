# dws oa approval list-cc

kind: command
completeness: partial
usage: dws oa approval list-cc
description: 获取抄送当前用户的审批单列表
example: dws oa approval list-cc --limit 20 --page 1 --query 关键词
source: internal/helpers/oa.go:1536
visible_flags: 0
partial_reason: unverified_flags

## Flags
- none

## Related
- dws oa approval append-task
- dws oa approval approve
- dws oa approval attachment
- dws oa approval create-instance
- dws oa approval detail
- dws oa approval ding-info
